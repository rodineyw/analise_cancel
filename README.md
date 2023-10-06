# Análise de Cancelamentos de Assinaturas 📉📊

Este é um projeto de análise de dados que visa entender melhor o comportamento dos clientes em relação às assinaturas de serviços. Utilizamos Python, Pandas e Plotly Express para realizar essa análise. Vamos dar uma olhada em como este código funciona e os insights que podemos obter a partir dele. 👀

## Importação de Dados 📥

Começamos importando a nossa base de dados a partir do arquivo "cancelamentos.csv" e carregando-a em um DataFrame do Pandas. Em seguida, removemos a coluna "CustomerID" que não será utilizada na análise. Aqui está um vislumbre da tabela de dados: 📊

```python
import pandas as pd
import plotly.express as px

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop("CustomerID", axis=1)
display(tabela)
```

## Tratamento de Valores Vazios 🚿

Em seguida, identificamos e removemos valores vazios (NaN) da tabela, garantindo que nossos cálculos sejam precisos. Aqui está um resumo das informações sobre os dados ausentes: 📋

```python
display(tabela.info())
tabela = tabela.dropna()
display(tabela.info())
```

## Quantidade de Cancelamentos e Não Cancelamentos 📈

Vamos dar uma olhada em quantos clientes cancelaram e quantos não cancelaram suas assinaturas. Isso nos ajudará a entender a distribuição dos cancelamentos na nossa base de dados: 📊

```python
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
```

## Análise da Duração dos Contratos ⌛

Agora, vamos analisar a duração dos contratos dos clientes. Queremos entender se a duração do contrato tem alguma influência nos cancelamentos. Aqui estão algumas estatísticas interessantes: 📊

```python
display(tabela["duracao_contrato"].value_counts(normalize=True))
display(tabela["duracao_contrato"].value_counts())
display(tabela.groupby("duracao_contrato").mean(numeric_only=True))
```

## Exclusão dos Contratos Mensais 🗓️

Após a análise da duração do contrato, identificamos que os contratos mensais parecem ter um alto índice de cancelamento. Decidimos remover esses contratos e continuar nossa análise. Aqui estão os resultados após essa exclusão: 📈

```python
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
display(tabela)
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
```

## Análise das Assinaturas 📋

Agora que temos uma base de dados mais limpa, podemos analisar as diferentes assinaturas dos clientes e suas características. Vamos dar uma olhada nas estatísticas e criar gráficos para visualizar melhor os dados: 📊

```python
display(tabela["assinatura"].value_counts(normalize=True))
display(tabela.groupby("assinatura").mean(numeric_only=True))

# Vamos criar gráfico, porque só com número tá difícil de visualizar
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou", width=600)
    grafico.show()
```

## Conclusão 📝

Este código fornece uma análise inicial de cancelamentos de assinaturas e nos ajuda a identificar tendências e insights valiosos. Com essas informações, podemos tomar decisões mais informadas para reter clientes e melhorar nossos serviços.

Fique à vontade para explorar ainda mais os dados ou expandir essa análise para obter informações adicionais. Esperamos que este readme tenha despertado seu interesse e o inspire a investigar mais a fundo! 🔍💡

Divirta-se explorando os dados e descobrindo novos insights! Se tiver alguma dúvida ou sugestão, não hesite em entrar em contato. 📧👍