import csv
import pandas as pd
from math import trunc
from keep_alive import keep_alive
keep_alive()
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$sistema'):
        await message.channel.send('Quando a quantidade, em dinheiro, de Balls arremessadas num Pokemon for SUPERIOR ao preço de venda num NPC, entrará no Sistema que aumentará a chance de capturar o Pokemon. Obs: Apenas se o seu level for IGUAL ou MAIOR do Pokemon')    
    
    if message.content.startswith('$help'):
        await message.channel.send('Comando: 1- $media "nomePokemon" = informa a média de Ultraball pra capturar o Pokemon. \n2- $sistema = explica o que é Sistema de Catch.')
    #------- Script de Busca de Pokemon -------#   
    var_input = message

    df = pd.read_csv("c:/Users/gmess/OneDrive/Área de Trabalho/pxg.csv")
    if var_input in df.values :
        search = df[df.pokemon==var_input]
        number_npc = search[search['pokemon'] == var_input]

        for row in number_npc.index:
            price = float(number_npc['preco'][row])
            sistema = str(number_npc['sistemaCatch'][row])

        ultraball = (price / 65)*1.09
        ultraball = trunc(ultraball)
        print(ultraball)
        
        if sistema=='1':
            print("Este Pokemon NÃO está no Sistema de Catch do PXG ou ele não é CAPTURÁVEL.\n")
            print("Para saber o que é Sistema de Catch digite: $sistema.\n")
    else:
        print("Não existe esse Pokemon OU ele não está registrado na base de dados.\n")
        #--------------- FIM SCRIPT ---------------#
        await message.channel.send('Média Aproximada de '+var_input+' são: '+ultraball+' ultraballs.')
 
client.run(os.getenv('TOKEN'))
my_secret = os.environ['TOKEN']   