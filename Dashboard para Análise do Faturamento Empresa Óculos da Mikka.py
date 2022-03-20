from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("C:\\Users\\miche\OneDrive\\Área de Trabalho\\Projeto análise de Dados\\Vendas.xlsx")

# criando o gráfico
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")


app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com o Faturamento de Todos os Produtos separados por Loja'),
    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),

    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),

    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig

)
])
#Input meu dropdow, Output mudar div texto
@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == "Todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja']==value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)



#Conclusão Após análise dos dados para tomada de decisão - Regras de Negócios

#1) A loja com menor Faturamento foi: Óculos e Acessórios da Mikka Alagoinhas
#2) A Loja com maior faturamento foi: Óculos e Acessórios da Mikka FSA

#Ao analisar os produtos no "Gráfico com o Faturamento de Todos os Produtos separados por Loja", podemos notar que o Item "bermuda lisa" foi o de maior venda na loja Óculos e Acessórios da Mikka FSA.
#Podemos analisar tamém que o Item "bermuda lisa" não estava disponível nas lojas com menor faturamento.

#Sugestões para aplicação às regras de Negócios:

#Avaliar os itens menos vendidos:
#Avaliar atendimento aos clientes, nessa loja
#Testar a venda da "bermuda lisa", nas demais lojas, devido ao grande número de vendas, na loja com maior faturamento Óculos e Acessórios da Mikka FSA

