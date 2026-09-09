from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run_script(filename: str) -> None:
    print(f"Executando {filename}...")
    subprocess.run([sys.executable, str(SCRIPTS / filename)], cwd=ROOT, check=True)


def main() -> None:
    run_script("generate_data.py")
    run_script("validate_data.py")
    run_script("build_project_assets.py")
    print("Projeto finalizado com sucesso.")


if __name__ == "__main__":
    main()
