# Power Query

Importe todos os CSVs da pasta `data` com UTF-8, promova cabeçalhos e tipifique datas, moedas, potência, horas e campos booleanos.

```powerquery
let
    Fonte = Csv.Document(File.Contents("data/Fato_Projetos.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Cabecalhos = Table.PromoteHeaders(Fonte, [PromoteAllScalars=true]),
    Tipos = Table.TransformColumnTypes(Cabecalhos, {{"ID_Projeto", type text}, {"Data_Entrada", type date}, {"Data_Prazo", type date}, {"Potencia_kW", type number}, {"Valor_Projeto", Currency.Type}})
in
    Tipos
```
