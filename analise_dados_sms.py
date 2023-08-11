import pandas as pd
from twilio.rest import Client
account_sid = 'ACb8fa41c190bce1df9505f452257bb5d9'
auth_token = '4861652241057c51a9f9cb725ab5bf03'
client = Client(account_sid, auth_token)


lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']
valor_da_meta = 55000

for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > valor_da_meta).any():
        condicao  = tabela_vendas['Vendas'] > valor_da_meta

        vendedor = tabela_vendas.loc[condicao,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[condicao, 'Vendas'].values[0]

        print(f'No mês de {mes} a meta foi batida')

        print(f'Nome : {vendedor}\nNúmero de vendas: {vendas}')





message = client.messages \
.create(
body="Você bateu a meta e ganhou a viagem!",
from_='+13135137552',
 to='+5521979856850'
)

print(message.sid)