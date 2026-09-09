from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
REFERENCE_DATE = pd.Timestamp("2026-09-08")


def load(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / f"{name}.csv", encoding="utf-8-sig")


def assert_true(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    tables = {
        name: load(name)
        for name in [
            "Fato_Projetos",
            "Dim_Cliente",
            "Dim_Responsavel",
            "Dim_Concessionaria",
            "Dim_TipoProjeto",
            "Dim_Status",
            "Dim_Etapa",
            "Dim_Localidade",
            "Dim_Calendario",
            "Fato_Pendencias",
            "Fato_HistoricoStatus",
            "Fato_Horas",
            "Fato_Faturamento",
        ]
    }
    fato = tables["Fato_Projetos"]

    assert_true(len(fato) == 200, "Fato_Projetos deve conter exatamente 200 projetos.", failures)
    assert_true(fato["ID_Projeto"].is_unique, "IDs dos projetos devem ser únicos.", failures)
    assert_true(not fato["Nome_Projeto"].duplicated().any(), "Nomes dos projetos devem ser únicos.", failures)

    relationships = {
        "ID_Cliente": "Dim_Cliente",
        "ID_Responsavel": "Dim_Responsavel",
        "ID_Concessionaria": "Dim_Concessionaria",
        "ID_TipoProjeto": "Dim_TipoProjeto",
        "ID_Status": "Dim_Status",
        "ID_Etapa": "Dim_Etapa",
        "ID_Localidade": "Dim_Localidade",
    }
    for key, dim in relationships.items():
        assert_true(set(fato[key]).issubset(set(tables[dim][key])), f"{key} possui valores ausentes em {dim}.", failures)

    for date_col in ["Data_Entrada", "Data_Inicio", "Data_Prazo", "Data_Conclusao"]:
        fato[date_col] = pd.to_datetime(fato[date_col], errors="coerce")

    concluded = fato["Status_Simplificado"].eq("CONCLUÍDO")
    open_projects = ~fato["Status_Simplificado"].isin(["CONCLUÍDO", "CANCELADO", "SUSPENSO"])
    overdue_expected = open_projects & (fato["Data_Prazo"] < REFERENCE_DATE)

    assert_true(fato.loc[concluded, "Data_Conclusao"].notna().all(), "Projetos concluídos devem ter data de conclusão.", failures)
    assert_true(fato.loc[~concluded, "Data_Conclusao"].isna().all(), "Somente projetos concluídos podem ter data de conclusão.", failures)
    assert_true(fato.loc[concluded, "Percentual_Conclusao"].eq(100).all(), "Projetos concluídos devem estar 100% completos.", failures)
    assert_true(fato["Percentual_Conclusao"].between(0, 100).all(), "Percentual de conclusão deve ficar entre 0 e 100.", failures)
    assert_true((fato["Potencia_kW"] > 0).all(), "Potência deve ser positiva.", failures)
    assert_true((fato["Valor_Projeto"] > 0).all(), "Valor do projeto deve ser positivo.", failures)
    assert_true((fato["Custo_Estimado"] > 0).all(), "Custo estimado deve ser positivo.", failures)
    assert_true((fato["Horas_Estimadas"] > 0).all(), "Horas estimadas devem ser positivas.", failures)
    assert_true((fato["Horas_Realizadas"] >= 0).all(), "Horas realizadas não podem ser negativas.", failures)
    assert_true((fato["Quantidade_Pendencias"] >= 0).all(), "Quantidade de pendências não pode ser negativa.", failures)
    assert_true((fato["Dias_Parado"] >= 0).all(), "Dias parados não podem ser negativos.", failures)
    assert_true(fato.loc[overdue_expected, "Status_Simplificado"].eq("ATRASADO").all(), "Projetos abertos fora do prazo devem estar como ATRASADO.", failures)
    assert_true((fato.loc[fato["Status_Simplificado"].eq("ATRASADO"), "Dias_Atraso"] > 0).all(), "Projetos atrasados devem ter Dias_Atraso positivo.", failures)
    assert_true(fato.loc[fato["Quantidade_Pendencias"].gt(0), "Possui_Pendencia"].eq(True).all(), "Quantidade e indicador de pendência devem estar coerentes.", failures)

    pend = tables["Fato_Pendencias"]
    assert_true(set(pend["ID_Projeto"]).issubset(set(fato["ID_Projeto"])), "IDs de projetos em pendências devem existir.", failures)
    counts = pend.groupby("ID_Projeto").size()
    for project_id, count in counts.items():
        expected = int(fato.loc[fato["ID_Projeto"].eq(project_id), "Quantidade_Pendencias"].iloc[0])
        assert_true(count == expected, f"Divergência na contagem de pendências para {project_id}.", failures)

    for child_name in ["Fato_HistoricoStatus", "Fato_Horas", "Fato_Faturamento"]:
        child = tables[child_name]
        assert_true(set(child["ID_Projeto"]).issubset(set(fato["ID_Projeto"])), f"{child_name} referencia projetos desconhecidos.", failures)

    report_lines = [
        "# Relatório de Validação dos Dados",
        "",
        f"Data de referência: {REFERENCE_DATE.date().isoformat()}",
        f"Projetos: {len(fato)}",
        f"Pendências: {len(pend)}",
        f"Projetos atrasados: {int(fato['Status_Simplificado'].eq('ATRASADO').sum())}",
        f"Projetos concluídos: {int(concluded.sum())}",
        "",
    ]
    if failures:
        report_lines.append("## Falhas")
        report_lines.extend(f"- {failure}" for failure in failures)
    else:
        report_lines.append("Todas as validações passaram.")

    report_path = ROOT / "docs" / "validation_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print("\n".join(report_lines))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
