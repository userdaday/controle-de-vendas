#codigo para proucurar e importar as informações
import os
import pandas as pd
patch = r"C:\Users\luis gustavo\Desktop\meus projetos em python\curso basico\Vendas" #localizei e definir a pasta dos arquivos em uma variavel
l1 = os.listdir(patch) #serve para lista nomes
tabela_vazia = pd.DataFrame() #serve para criar uma tabela vazia
for arquivo in l1:# codigo de repetição
   if "Vendas" in arquivo:
        tabela = pd.read_csv(f"C:/Users/luis gustavo/Desktop/meus projetos em python/curso basico/Vendas/{arquivo}")#listei e abrir os arquivos do banco de dados com o pandas
        tabela_vazia = tabela_vazia.append(tabela)#setei todos os arquivos da tabela para tabela vazia assim sempre adicionando arquivos novos
#calculo de indicadores.
tabela_produtos = tabela_vazia.groupby('Produto').sum()
# definir qual linha da tabela eu queria visualizar
#tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by="Quantidade Vendida", ascending=False) # setei quais colunas eu quero mostrar, e ordenei em ordem decresente
#print(tabela_produtos)
#calculo do produto que mais faturou
l2 = tabela_produtos['Faturamento'] = tabela_produtos['Quantidade Vendida']*tabela_produtos['Preco Unitario']#adicionei na tabela uma nova couna chamada faturamento somando duas outras
l2 = tabela_produtos[['Faturamento']].sort_values(by='Faturamento', ascending=False) #setei como eu quis mostrar a mesma de forma individual
l3 = tabela_produtos[['Quantidade Vendida']].sort_values(by="Quantidade Vendida", ascending=False) # setei quais colunas eu quero mostrar, e ordenei em ordem decresente
l4 = tabela_vazia.groupby('Loja').sum()
l5 = l4['faturamento'] = l4['Quantidade Vendida']*l4['Preco Unitario']
l6 = l4[['faturamento']].sort_values(by='faturamento', ascending=False)
print(l2)
print(l3)
print(l6)