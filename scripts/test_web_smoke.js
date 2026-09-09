const { chromium } = require("playwright");

async function main() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  const errors = [];
  page.on("console", (msg) => {
    if (msg.type() === "error") errors.push(msg.text());
  });
  page.on("pageerror", (error) => errors.push(error.message));

  await page.goto("http://127.0.0.1:8765", { waitUntil: "networkidle" });
  const buttons = await page.locator("nav button").count();
  const filters = await page.locator("select[data-filter]").count();
  const cards = await page.locator(".card").count();

  for (const key of ["executiva", "prazos", "operacoes", "engenharia", "financeiro", "pendencias", "detalhe"]) {
    await page.locator(`button[data-page="${key}"]`).click();
    await page.waitForTimeout(100);
    const panels = await page.locator(".panel").count();
    if (panels < 1) throw new Error(`Página sem painel: ${key}`);
  }

  await page.locator('select[data-filter="status"]').selectOption({ label: "ATRASADO" });
  await page.waitForTimeout(200);
  const filteredContext = await page.locator("#contexto").innerText();
  await page.screenshot({ path: "assets/screenshots/web_desktop.png", fullPage: true });

  const mobile = await browser.newPage({ viewport: { width: 390, height: 900 }, isMobile: true });
  await mobile.goto("http://127.0.0.1:8765", { waitUntil: "networkidle" });
  await mobile.screenshot({ path: "assets/screenshots/web_mobile.png", fullPage: true });
  await browser.close();

  if (errors.length) throw new Error(errors.join(" | "));
  console.log(JSON.stringify({ buttons, filters, cards, filteredContext }, null, 2));
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
