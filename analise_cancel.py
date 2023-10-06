# Importando a base de dados
import pandas as pd
import plotly.express as px

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop("CustomerID", axis=1)
display(tabela)

# Identificando e removendo valores vazios
display(tabela.info())
tabela = tabela.dropna()
display(tabela.info())

# Quantas pessoas cancelaram e não cancelaram
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

display(tabela["duracao_contrato"].value_counts(normalize=True))
display(tabela["duracao_contrato"].value_counts())

# Analisando o contrato mensal
display(tabela.groupby("duracao_contrato").mean(numeric_only=True))

# Descobrimos que contrato mensal é ruim, vamos tirar ele e continuar analisando
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
display(tabela)
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# Chegamos agora em menos da metade de pessoas que cancelaram
display(tabela["assinatura"].value_counts(normalize=True))
display(tabela.groupby("assinatura").mean(numeric_only=True))

# Vamos criar gráfico, porque só com número tá dificil de visualizar
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou", width=600)
    grafico.show()
