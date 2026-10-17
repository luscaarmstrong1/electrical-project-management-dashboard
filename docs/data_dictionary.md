# Dicionário de Dados

| Tabela | Campo | Tipo | Descrição | Exemplo |
| --- | --- | --- | --- | --- |
| Dim_Calendario | Data | str | Data | 2024-01-01 |
| Dim_Calendario | Ano | int64 | Ano | 2024 |
| Dim_Calendario | Mes | str | Mes | Jan |
| Dim_Calendario | Numero_Mes | int64 | Numero mes | 1 |
| Dim_Calendario | Mes_Ano | str | Mes ano | Jan/2024 |
| Dim_Calendario | Trimestre | str | Trimestre | T1 |
| Dim_Calendario | Semana | int64 | Semana | 1 |
| Dim_Calendario | Dia | int64 | Dia | 1 |
| Dim_Calendario | Dia_Semana | str | Dia semana | Monday |
| Dim_Calendario | Ano_Mes | str | Ano mes | 2024-01 |
| Dim_Calendario | Inicio_Mes | str | Inicio mes | 2024-01-01 |
| Dim_Calendario | Fim_Mes | str | Fim mes | 2024-01-31 |
| Dim_Cliente | ID_Cliente | str | Id cliente | CLI001 |
| Dim_Cliente | Cliente | str | Cliente | Indústria Alfa |
| Dim_Cliente | Segmento | str | Segmento | Industrial |
| Dim_Concessionaria | ID_Concessionaria | str | Id concessionaria | CONC01 |
| Dim_Concessionaria | Concessionaria | str | Concessionaria | CEMIG |
| Dim_Etapa | ID_Etapa | str | Id etapa | ETAPA01 |
| Dim_Etapa | Ordem_Etapa | int64 | Ordem etapa | 1 |
| Dim_Etapa | Etapa | str | Etapa | Levantamento inicial |
| Dim_Etapa | Macro_Etapa | str | Macro etapa | Entrada |
| Dim_Localidade | ID_Localidade | str | Id localidade | LOC01 |
| Dim_Localidade | Estado | str | Estado | SP |
| Dim_Localidade | Municipio | str | Município de referência sintético. | São Paulo |
| Dim_Localidade | Regiao | str | Regiao | Sudeste |
| Dim_Localidade | Peso_Carteira | float64 | Peso carteira | 0.34 |
| Dim_Responsavel | ID_Responsavel | str | Id responsavel | RESP01 |
| Dim_Responsavel | Responsavel | str | Responsavel | Lucas Silva Santos |
| Dim_Responsavel | Cargo | str | Cargo | Engenheiro de Projetos |
| Dim_Responsavel | Squad | str | Squad | Projetos |
| Dim_Status | ID_Status | str | Id status | STAT01 |
| Dim_Status | Status | str | Status | Não iniciado |
| Dim_Status | Status_Simplificado_Base | str | Status simplificado base | ABERTO |
| Dim_TipoProjeto | ID_TipoProjeto | str | Id tipoprojeto | TIPO01 |
| Dim_TipoProjeto | Tipo_Projeto | str | Tipo projeto | Sistema Fotovoltaico |
| Dim_TipoProjeto | Categoria_Engenharia | str | Categoria engenharia | Geração distribuída |
| Dim_TipoProjeto | Nivel_Tensao_Padrao | str | Nivel tensao padrao | BT |
| Fato_Faturamento | ID_Faturamento | str | Id faturamento | FAT00001 |
| Fato_Faturamento | ID_Projeto | str | Identificador único do projeto. | PROJ0001 |
| Fato_Faturamento | Marco | str | Marco | Entrada |
| Fato_Faturamento | Data_Faturamento | str | Data faturamento | 2026-07-16 |
| Fato_Faturamento | Valor_Faturado | float64 | Valor faturado | 672237.02 |
| Fato_HistoricoStatus | ID_Historico | str | Id historico | HIST00001 |
| Fato_HistoricoStatus | ID_Projeto | str | Identificador único do projeto. | PROJ0001 |
| Fato_HistoricoStatus | Status | str | Status | Não iniciado |
| Fato_HistoricoStatus | Data_Status | str | Data status | 2026-07-09 |
| Fato_HistoricoStatus | Ordem_Status | int64 | Ordem status | 1 |
| Fato_Horas | ID_Horas | str | Id horas | HORA00001 |
| Fato_Horas | ID_Projeto | str | Identificador único do projeto. | PROJ0001 |
| Fato_Horas | ID_Responsavel | str | Id responsavel | RESP05 |
| Fato_Horas | Mes_Referencia | str | Mes referencia | 2026-07-01 |
| Fato_Horas | Horas | int64 | Horas | 26 |
| Fato_Horas | Atividade | str | Atividade | Campo |
| Fato_Pendencias | ID_Pendencia | str | Id pendencia | PEND0001 |
| Fato_Pendencias | ID_Projeto | str | Identificador único do projeto. | PROJ0003 |
| Fato_Pendencias | Categoria_Pendencia | str | Categoria pendencia | Documento do cliente |
| Fato_Pendencias | Descricao_Pendencia | str | Descricao pendencia | Pendência sintética para demonstração de gestão operacional |
| Fato_Pendencias | Data_Abertura | str | Data abertura | 2026-10-23 |
| Fato_Pendencias | Data_Resolucao | str | Data resolucao | nan |
| Fato_Pendencias | Status_Pendencia | str | Status pendencia | Aberta |
| Fato_Pendencias | Dias_Em_Aberto | int64 | Dias em aberto | 0 |
| Fato_Pendencias | Impacta_Prazo | bool | Impacta prazo | True |
| Fato_Projetos | ID_Projeto | str | Identificador único do projeto. | PROJ0001 |
| Fato_Projetos | Nome_Projeto | str | Nome fictício do projeto. | Projeto Volt 001 |
| Fato_Projetos | ID_Cliente | str | Id cliente | CLI014 |
| Fato_Projetos | ID_Responsavel | str | Id responsavel | RESP05 |
| Fato_Projetos | ID_Concessionaria | str | Id concessionaria | CONC04 |
| Fato_Projetos | ID_TipoProjeto | str | Id tipoprojeto | TIPO03 |
| Fato_Projetos | ID_Status | str | Id status | STAT03 |
| Fato_Projetos | ID_Etapa | str | Id etapa | ETAPA04 |
| Fato_Projetos | ID_Localidade | str | Id localidade | LOC01 |
| Fato_Projetos | Data_Entrada | str | Data entrada | 2026-07-09 |
| Fato_Projetos | Data_Inicio | str | Data inicio | 2026-07-13 |
| Fato_Projetos | Data_Prazo | str | Data prazo | 2026-10-13 |
| Fato_Projetos | Data_Conclusao | str | Data conclusao | nan |
| Fato_Projetos | Potencia_kW | float64 | Potência elétrica associada ao projeto. | 755.8 |
| Fato_Projetos | Valor_Projeto | float64 | Valor comercial estimado. | 2688948.06 |
| Fato_Projetos | Custo_Estimado | float64 | Custo estimado | 1840925.96 |
| Fato_Projetos | Margem_Estimada | float64 | Margem estimada | 848022.1 |
| Fato_Projetos | Horas_Estimadas | int64 | Horas estimadas | 120 |
| Fato_Projetos | Horas_Realizadas | int64 | Horas realizadas | 44 |
| Fato_Projetos | Percentual_Conclusao | int64 | Percentual conclusao | 30 |
| Fato_Projetos | Prioridade | str | Prioridade | Média |
| Fato_Projetos | Complexidade | str | Complexidade | Baixa |
| Fato_Projetos | Nivel_Tensao | str | Nivel tensao | MT |
| Fato_Projetos | Tipo_Conexao | str | Tipo conexao | Grupo A |
| Fato_Projetos | Tipo_Sistema | str | Tipo sistema | Geração distribuída |
| Fato_Projetos | Possui_Pendencia | bool | Possui pendencia | False |
| Fato_Projetos | Quantidade_Pendencias | int64 | Quantidade pendencias | 0 |
| Fato_Projetos | Dias_Parado | int64 | Dias parado | 0 |
| Fato_Projetos | Status_Simplificado | str | Status executivo calculado. | ABERTO |
| Fato_Projetos | Dias_Ate_Prazo | float64 | Dias ate prazo | 35.0 |
| Fato_Projetos | Dias_Atraso | int64 | Dias de atraso na data de referência. | 0 |
| Fato_Projetos | Faixa_Prazo | str | Faixa prazo | Mais de 30 dias |
| Fato_Projetos | Criticidade | str | Criticidade | Baixa |
| Fato_Projetos | Observacao_Status | str | Observacao status | Fluxo regular |