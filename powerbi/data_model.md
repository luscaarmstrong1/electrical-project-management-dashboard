# Modelo de Dados

| Origem | Destino | Cardinalidade | Filtro |
| --- | --- | --- | --- |
| Dim_Cliente[ID_Cliente] | Fato_Projetos[ID_Cliente] | 1:* | Único |
| Dim_Responsavel[ID_Responsavel] | Fato_Projetos[ID_Responsavel] | 1:* | Único |
| Dim_Concessionaria[ID_Concessionaria] | Fato_Projetos[ID_Concessionaria] | 1:* | Único |
| Dim_TipoProjeto[ID_TipoProjeto] | Fato_Projetos[ID_TipoProjeto] | 1:* | Único |
| Dim_Status[ID_Status] | Fato_Projetos[ID_Status] | 1:* | Único |
| Dim_Etapa[ID_Etapa] | Fato_Projetos[ID_Etapa] | 1:* | Único |
| Dim_Localidade[ID_Localidade] | Fato_Projetos[ID_Localidade] | 1:* | Único |
| Dim_Calendario[Data] | Fato_Projetos[Data_Entrada] | 1:* | Único |
| Fato_Projetos[ID_Projeto] | Fato_Pendencias[ID_Projeto] | 1:* | Único |
| Fato_Projetos[ID_Projeto] | Fato_Horas[ID_Projeto] | 1:* | Único |
| Fato_Projetos[ID_Projeto] | Fato_Faturamento[ID_Projeto] | 1:* | Único |