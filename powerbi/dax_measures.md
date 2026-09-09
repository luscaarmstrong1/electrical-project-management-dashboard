# Medidas DAX

Use `Parametros[DataReferencia]` como data fixa da demonstração.

```DAX
Data Referencia = SELECTEDVALUE(Parametros[DataReferencia], DATE(2026, 9, 8))
Total Projetos = DISTINCTCOUNT(Fato_Projetos[ID_Projeto])
Projetos Ativos = CALCULATE([Total Projetos], FILTER(Fato_Projetos, NOT (Fato_Projetos[Status_Simplificado] IN {"CONCLUÍDO", "SUSPENSO", "CANCELADO"})))
Projetos Concluidos = CALCULATE([Total Projetos], Fato_Projetos[Status_Simplificado] = "CONCLUÍDO")
Projetos Atrasados = CALCULATE([Total Projetos], Fato_Projetos[Status_Simplificado] = "ATRASADO")
Projetos Suspensos = CALCULATE([Total Projetos], Fato_Projetos[Status_Simplificado] = "SUSPENSO")
Projetos Cancelados = CALCULATE([Total Projetos], Fato_Projetos[Status_Simplificado] = "CANCELADO")
Potencia Total kW = SUM(Fato_Projetos[Potencia_kW])
Potencia Total MW = DIVIDE([Potencia Total kW], 1000)
Valor da Carteira = SUM(Fato_Projetos[Valor_Projeto])
Valor Projetos Ativos = CALCULATE([Valor da Carteira], FILTER(Fato_Projetos, NOT (Fato_Projetos[Status_Simplificado] IN {"CONCLUÍDO", "SUSPENSO", "CANCELADO"})))
Ticket Medio = AVERAGE(Fato_Projetos[Valor_Projeto])
Prazo Medio = AVERAGEX(Fato_Projetos, DATEDIFF(Fato_Projetos[Data_Entrada], Fato_Projetos[Data_Prazo], DAY))
% Projetos Concluidos = DIVIDE([Projetos Concluidos], [Total Projetos])
% Concluido no Prazo = DIVIDE(CALCULATE([Total Projetos], FILTER(Fato_Projetos, Fato_Projetos[Status_Simplificado] = "CONCLUÍDO" && Fato_Projetos[Data_Conclusao] <= Fato_Projetos[Data_Prazo])), [Projetos Concluidos])
% Projetos Atrasados = DIVIDE([Projetos Atrasados], [Total Projetos])
Total Pendencias = COUNTROWS(Fato_Pendencias)
Projetos com Pendencia = CALCULATE([Total Projetos], Fato_Projetos[Possui_Pendencia] = TRUE())
Tempo Medio Parado = AVERAGE(Fato_Projetos[Dias_Parado])
Horas Estimadas = SUM(Fato_Projetos[Horas_Estimadas])
Horas Realizadas = SUM(Fato_Projetos[Horas_Realizadas])
Desvio de Horas = [Horas Realizadas] - [Horas Estimadas]
Eficiencia de Horas = DIVIDE([Horas Estimadas], [Horas Realizadas])
Margem Estimada = SUM(Fato_Projetos[Margem_Estimada])
% Margem Estimada = DIVIDE([Margem Estimada], [Valor da Carteira])
```
