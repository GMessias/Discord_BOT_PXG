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
        await message.channel.send('Comando: \n1- $media "nomePokemon" = informa a média de Ultraball pra capturar o Pokemon, ex.: $media Charizard. \n2- $sistema = explica o que é Sistema de Catch. \n3- $ball "nomePokemon" = informa a média geral de todas as pokebolas possíveis, ex.: $ballCharizard')
    #------- Script de Busca de Pokemon -------#   
    
    if message.content.startswith('$media'):
        var_input = message.content[7:]

        df = pd.read_csv("pxg.csv")
        if var_input in df.values :
            search = df[df.pokemon==var_input]
            number_npc = search[search['pokemon'] == var_input]

            for row in number_npc.index:
                price = float(number_npc['preco'][row])
                sistema = str(number_npc['sistemaCatch'][row])

            ultraball = (price / 65)*1.09
            ultraball = trunc(ultraball)
            #print(ultraball)
            await message.channel.send('Média Aproximada de '+var_input+' são: '+str(ultraball)+' ultraballs.')
            
            if sistema=='1':
                await message.channel.send('Este Pokemon NÃO está no Sistema de Catch do PXG ou ele não é CAPTURÁVEL.\n Para saber o que é Sistema de Catch digite: $sistema.\n')
                #print("Este Pokemon NÃO está no Sistema de Catch do PXG ou ele não é CAPTURÁVEL.\n")
                #print("Para saber o que é Sistema de Catch digite: $sistema.\n")
        else:
            await message.channel.send('Não existe esse Pokemon OU ele não está registrado na base de dados.\n')
            #print("Não existe esse Pokemon OU ele não está registrado na base de dados.\n")
            #--------------- FIM SCRIPT ---------------
    if message.content.startswith('$ball Bulbassaur'):
        await message.channel.send('A média de catch do Bulbassaur é: 450 Pokeballs, 300 Great Balls, 108 Super ball, 50 Ultra Balls e 35 Janguruball')
    if message.content.startswith('$ball Ivysaur'):
        await message.channel.send('A média de catch do Ivysaur é: 800 Great Balls, 290 Super ball, 140 Ultra Balls e 100 Janguruball')
    if message.content.startswith('$ball Venusaur'):
        await message.channel.send('A média de catch do Venusaur é: 300 Ultra Balls, 210 Janguruball e 210 Heavy Balls')    
    if message.content.startswith('$ball Charmander'):
        await message.channel.send('A média de catch do Charmander é: 450 Pokeballs, 300 Great Balls, 108 Super ball, 50 Ultra Balls e 35 Maguball')
    if message.content.startswith('$ball Charmeleon'):
        await message.channel.send('A média de catch do Charmeleon é: 800 Great Balls, 290 Super ball, 140 Ultra Balls e 100 Maguball')
    if message.content.startswith('$ball Charizard'):
        await message.channel.send('A média de catch do Charizard é: 300 Ultra Balls, 210 Maguball e 210 Sora Balls')
    if message.content.startswith('$ball Squirtle'):
        await message.channel.send('A média de catch do Squirtle é: 450 Pokeballs, 300 Great Balls, 108 Super ball, 50 Ultra Balls e 35 Netball')
    if message.content.startswith('$ball Wartortle'):
        await message.channel.send('A média de catch do Wartortle é: 800 Great Balls, 290 Super ball, 140 Ultra Balls e 100 Netball')
    if message.content.startswith('$ball Blastoise'):
        await message.channel.send('A média de catch do Blastoise é: 300 Ultra Balls e 210 Netballs')
    if message.content.startswith('$ball Caterpie'):
        await message.channel.send('A média de catch do Caterpie é: 1 Pokeball, 1 Great Ball, 1 Super ball, 1 Ultra Ball e 1 Netball')
    if message.content.startswith('$ball Metapod'):
        await message.channel.send('A média de catch do Metapod é: 38 Pokeball, 25 Great Balls, 9 Super ball, 5 Ultra Balls e 3 Netballs')
    if message.content.startswith('$ball Butterfree'):
        await message.channel.send('A média de catch do Butterfree é: 300 Pokeballs, 200 Great Balls, 72 Super ball, 34 Ultra Balls, 24 Netball, 24 Soraball e 24 Fastball')
    if message.content.startswith('$ball Weedle'):
        await message.channel.send('A média de catch do Weedle é: 1 Pokeball, 1 Great Ball, 1 Super ball, 1 Ultra Ball, 1 Netball e 1 Janguruball')
    if message.content.startswith('$ball Kakuna'):
        await message.channel.send('A média de catch do Kakuna é: 38 Pokeball, 25 Great Balls, 9 Super ball, 5 Ultra Balls, 3 Netballs e 3 Janguruball')
    if message.content.startswith('$ball Beedrill'):
        await message.channel.send('A média de catch da Beedrill é: 300 Pokeballs, 200 Great Balls, 72 Super ball, 34 Ultra Balls, 24 Netball, 24 Soraball e 24 Fastball')
    if message.content.startswith('$ball Pidgey'):
        await message.channel.send('A média de catch do Pidgey é: 1 Pokeball, 1 Great Ball, 1 Super ball, 1 Ultra Ball, 1 Soraball, 1 Yumeball e 1 Fastball')
    if message.content.startswith('$ball Pidgeotto'):
        await message.channel.send('A média de catch do Pidgeotto é: 450 Pokeballs, 300 Great Balls, 108 Super ball, 50 Ultra Balls, 35 Soraball, 35 Yumeball e 35 Fastball')
    if message.content.startswith('$ball Pidgeot'):
        await message.channel.send('A média de catch do Pidgeot é: 200 Ultra Balls, 140 Soraball, 140 Yumeball e 140 Fastball')
    if message.content.startswith('$ball Raticate'):
        await message.channel.send('A média de catch do Pidgeot é: 300 Poke Balls, 200 Great Balls, 72 Super Balls, 34 Ultra Balls e 24 Yumeball')
    if message.content.startswith('$ball Fearow'):
        await message.channel.send('A média de catch do Fearow é: 510 Great Balls, 190 Super Balls, 90 Ultra Balls, 60 Soraball, 60 Yumeball e 60 Fastball')
    if message.content.startswith('$ball Arbok'):
        await message.channel.send('A média de catch do Arbok é: 300 Great Balls, 108 Super Balls, 50 Ultra Balls e 35 Janguruball')
    if message.content.startswith('$ball Pikachu'):
        await message.channel.send('A média de catch do Pikachu é: 800 Great Balls, 290 Super Balls, 140 Ultra Balls, 100 Tinker Balls e 100 Fast Balls')
    if message.content.startswith('$ball Raichu'):
        await message.channel.send('A média de catch do Raichu é: 300 Ultra Balls, 210 Tinker Balls e 210 Fast Balls')
    if message.content.startswith('$ball Sandslash'):
        await message.channel.send('A média de catch do Sandslash é: 400 Super Balls, 190 Ultra Balls e 130 Maguball')
    if message.content.startswith('$ball Nidoqueen'):
        await message.channel.send('A média de catch da Nidoqueen é: 600 Safari Balls')
    if message.content.startswith('$ball Nidoking'):
        await message.channel.send('A média de catch do Nidoking é: 600 Safari Balls')
    if message.content.startswith('$ball Clefairy'):
        await message.channel.send('A média de catch do Clefairy é: 800 Great Balls, 290 Super Balls, 140 Ultra Balls, 100 Taleball')
    if message.content.startswith('$ball Clefable'):
        await message.channel.send('A média de catch do Clefable é: 300 Ultra Balls e 210 Tale Balls')
    if message.content.startswith('$ball Ninetales'):
        await message.channel.send('A média de catch do Ninetales é: 190 Ultra Balls, 130 Maguballs e 130 Fast Balls')
    if message.content.startswith('$ball Wigglytuff'):
        await message.channel.send('A média de catch do Wigglytuff é: 300 Ultra Balls, 210 Taleball e 210 Yumeballs')
    if message.content.startswith('$ball Golbat'):
        await message.channel.send('A média de catch do Golbat é: 300 Great Balls, 108 Super Balls, 50 Ultra Balls, 35 Janguruball, 35 Soraball e 35 Fastballs')
    if message.content.startswith('$ball Vileplume'):
        await message.channel.send('A média de catch do Vileplume é: 430 Super Balls, 200 Ultra Balls, 140 Janguruball')
    if message.content.startswith('$ball Parasect'):
        await message.channel.send('A média de catch do Parasect é: 730 GreatBalls, 260 Super Balls, 130 Ultra Balls, 90 Janguruball e 90 Netballs')
    if message.content.startswith('$ball Venomoth'):
        await message.channel.send('A média de catch do Venomoth é: 730 GreatBalls, 260 Super Balls, 130 Ultra Balls, 90 Janguruball e 90 Netballs')
    if message.content.startswith('$ball Dugtrio'):
        await message.channel.send('A média de catch do Dugtrio é: 300 GreatBalls, 108 Super Balls, 50 Ultra Balls, 35 Maguball e 35 Fastballs')
    if message.content.startswith('$ball Persian'):
        await message.channel.send('A média de catch do Persian é: 300 GreatBalls, 108 Super Balls, 50 Ultra Balls, 35 Yumeball e 35 Fastballs')
    if message.content.startswith('$ball Golduck'):
        await message.channel.send('A média de catch do Golduck é: 420 Super Balls, 200 Ultra Balls, 140 Netball')
    if message.content.startswith('$ball Primeape'):
        await message.channel.send('A média de catch do Primeape é: 730 Great Balls, 260 Super Balls, 130 Ultra Balls e 90 Duskballs')
    if message.content.startswith('$ball Arcanine'):
        await message.channel.send('A média de catch do Arcanine é: 980 Ultra Balls, 690 Maguball, 690 Heavyball e 690 Fastball')
    if message.content.startswith('$ball Poliwrath'):
        await message.channel.send('A média de catch do Poliwrath é: 470 Super Balls, 220 Ultra Balls, 160 Netballs e 160 Duskballs')
    if message.content.startswith('$ball Kadabra'):
        await message.channel.send('A média de catch do Kadabra é: 580 GreatBalls, 210 Super Balls, 100 Ultra Balls e 70 Yumeballs')
    if message.content.startswith('$ball Alakazam'):
        await message.channel.send('A média de catch do Alakazam é: 270 Ultra Balls e 190 Yumeballs')
    if message.content.startswith('$ball Machamp'):
        await message.channel.send('A média de catch do Machamp é: 350 Ultra Balls, 250 Duskball e 250 Heavyballs')
    if message.content.startswith('$ball Victreebel'):
        await message.channel.send('A média de catch do Victreebel é: 430 Super Balls, 200 Ultra Balls, 140 Janguruball')
    if message.content.startswith('$ball Tentacruel'):
        await message.channel.send('A média de catch do Tentacruel é: 250 Ultra Balls, 180 Netballs e 180 Janguruball')
    if message.content.startswith('$ball Golem'):
        await message.channel.send('A média de catch do Golem é: 250 Ultra Balls, 180 Duskball, 180 Heavyball e 180 Maguball')
    if message.content.startswith('$ball Rapidash'):
        await message.channel.send('A média de catch do Rapidash é: 210 Ultra Balls, 150 Maguball e 150 Fastball')
    if message.content.startswith('$ball Slowbro'):
        await message.channel.send('A média de catch do Slowbro é: 800 Great Balls, 290 Super Balls, 140 Ultra Balls, 100 Netball')
    if message.content.startswith('$ball Magneton'):
        await message.channel.send('A média de catch do Magneton é: 90 Ultra Balls e 70 Tinkerballs')
    if message.content.startswith('$ball Farfetchd'):
        await message.channel.send('A média de catch do Farfetchd é: 800 Great Balls, 290 Super Balls, 140 Ultra Balls, 100 Soraball, 100 Yumeball e 100 Fastballs')
    if message.content.startswith('$ball Dodrio'):
        await message.channel.send('A média de catch do Dodrio é: 560 Great Balls, 200 Super Balls, 100 Ultra Balls, 70 Soraball, 70 Yumeball e 70 Fastballs')
    if message.content.startswith('$ball Muk'):
        await message.channel.send('A média de catch do Muk é: 190 Ultra Balls e 130 Janguruballs')
    if message.content.startswith('$ball Cloyster'):
        await message.channel.send('A média de catch do Cloyster é: 370 Super Balls, 170 Ultra Balls, 120 Netballs e 120 Soraballs')
    if message.content.startswith('$ball Gengar'):
        await message.channel.send('A média de catch do Gengar é: 300 Ultra Balls, 210 Moonballs e 210 Janguruballs')
    if message.content.startswith('$ball Onix'):
        await message.channel.send('A média de catch do Onix é: 600 Great Balls, 220 Super Balls, 100 Ultra Balls, 70 Duskball, 70 Maguball e 70 Heavyball')
    if message.content.startswith('$ball Hypno'):
        await message.channel.send('A média de catch do Hypno é: 600 Great Balls, 220 Super Balls, 100 Ultra Balls, 70 Yumeballs')
    if message.content.startswith('$ball Kingler'):
        await message.channel.send('A média de catch do Kingler é: 520 Great Balls, 190 Super Balls, 90 Ultra Balls e 70 Netballs')
    if message.content.startswith('$ball Electrode'):
        await message.channel.send('A média de catch do Kingler é: 300 Great Balls, 108 Super Balls, 50 Ultra Balls e 35 Tinkerballs')
    if message.content.startswith('$ball Exeggutor'):
        await message.channel.send('A média de catch do Exeggutor é: 250 Ultra Balls, 180 Yumeballs, 180 Heavyballs e 180 Janguruballs')
    if message.content.startswith('$ball Rhydon'):
        await message.channel.send('A média de catch do Rhydon é: 220 Ultra Balls, 160 Maguballs, 160 Heavyballs e 180 Duskballs')
    if message.content.startswith('$ball Starmie'):
        await message.channel.send('A média de catch do Starmie é: 50 Ultra Balls, 35 Netballs, 35 Yumeballs e 35 Fastballs')
    if message.content.startswith('$ball Jynx'):
        await message.channel.send('A média de catch do Jynx é: 2000 Ultra Balls, 1400 Soraballs e 1400 Yumeballs')
    if message.content.startswith('$ball Electabruzz'):
        await message.channel.send('A média de catch do Electabuzz é: 2000 Ultra Balls e 1400 Tinkerballs')
    if message.content.startswith('$ball Magmar'):
        await message.channel.send('A média de catch do Magmar é: 2000 Ultra Balls e 1400 Maguballs')
    if message.content.startswith('$ball Pinsir'):
        await message.channel.send('A média de catch do Pinsir é: 2000 Ultra Balls, 1400 Netballs e 1400 Fastballs')
    if message.content.startswith('$ball Taurus'):
        await message.channel.send('A média de catch do Taurus é: 500 Great Balls, 180 Super Balls, 90 Ultra Balls e 60 Yumeballs')
    if message.content.startswith('$ball Gyarados'):
        await message.channel.send('A média de catch do Gyarados é: 920 Ultra Balls, 650 Netballs e 650 Soraballs')
    if message.content.startswith('$ball Lapras'):
        await message.channel.send('A média de catch do Lapras é: 2000 Ultra Balls, 1400 Netballs, 1400 Soraballs e 1400 Heavyballs')
    if message.content.startswith('$ball Snorlax'):
        await message.channel.send('A média de catch do Snorlax é: 3340 Ultra Balls, 2340 Yumeballs e 2340 Heavyballs')
    if message.content.startswith('$ball Dragonite'):
        await message.channel.send('A média de catch do Dragonite é: 2090 Ultra Balls, 1460 Taleballs e 1460 Heavyballs')
    if message.content.startswith('$ball Meganium'):
        await message.channel.send('A média de catch do Meganium é: 300 Ultra Balls, 210 Janguruballs e 210 Heavyballs')
    if message.content.startswith('$ball Typhlosion'):
        await message.channel.send('A média de catch do Typhlosion é: 300 Ultra Balls e 210 Maguballs')
    if message.content.startswith('$ball Feraligatr'):
        await message.channel.send('A média de catch do Feraligatr é: 300 Ultra Balls e 210 Netballs')
    if message.content.startswith('$ball Xatu'):
        await message.channel.send('A média de catch do Xatu é: 220 Ultra Balls e 160 Yumeballs')
    if message.content.startswith('$ball Lanturn'):
        await message.channel.send('A média de catch do Lanturn é: 200 Ultra Ball, 140 Netball e 140 Tinkerball')
    if message.content.startswith('$ball Ampharos'):
        await message.channel.send('A média de catch do Ampharos é: 300 Ultra Ball e 210 Tinkerball')
    if message.content.startswith('$ball Steelix'):
        await message.channel.send('A média de catch do Steelix é: 1840 Ultra Balls, 1290 Tinkerballs e 1290 Heavyballs')  
    if message.content.startswith('$ball Azumarill'):
        await message.channel.send('A média de catch do Azumarill é: 470 Super ball, 220 Ultra Ball, 160 Netball e 160 Taleball')
    if message.content.startswith('$ball Politoed'):
        await message.channel.send('A média de catch do Politoed é: 290 Super ball, 140 Ultra Ball e 100 Netballs')
    if message.content.startswith('$ball Girafarig'):
        await message.channel.send('A média de catch do Girafarig é: 2000 Ultra Balls, 1400 Yumeballs e 1400 Fastballs')
    if message.content.startswith('$ball Heracross'):
        await message.channel.send('A média de catch do Heracross é: 2000 Ultra Balls, 1400 Netballs e 1400 Duskballs')
    if message.content.startswith('$ball Sneasel'):
        await message.channel.send('A média de catch do Steelix é: 1000 Great Balls, 360 Super Balls, 170 Ultra Balls, 120 Moonballs e 120 Soraballs')
    if message.content.startswith('$ball Mantine'):
        await message.channel.send('A média de catch do Mantine é: 2000 Ultra Balls, 1400 Netballs, 1400 Soraballs, 1400 Heavyballs e 1400 Duskballs')
    if message.content.startswith('$ball Skarmory'):
        await message.channel.send('A média de catch do Skarmory é: 2000 Ultra Balls, 1400 Tinkerballs, 1400 Soraballs e 1400 Duskballs')
    if message.content.startswith('$ball Houndoom'):
        await message.channel.send('A média de catch do Houndoom é: 230 Ultra Balls, 160 Maguballs, 160 Moonballs e 160 Fastballs')
    if message.content.startswith('$ball Kingdra'):
        await message.channel.send('A média de catch do Kingdra é: 1000 Ultra Balls, 700 Netballs, 700 Taleballs e 700 Heavyballs')
    if message.content.startswith('$ball Donphan'):
        await message.channel.send('A média de catch do Donphan é: 220 Ultra Balls, 160 Maguball e 160 Heavyballs')
    if message.content.startswith('$ball Elekid'):
        await message.channel.send('A média de catch do Elekid é: 1290 Poke Balls, 860 Great Balls, 310 Super Balls, 150 Ultra Balls e 100 Tinkerballs')
    if message.content.startswith('$ball Forretres'):
        await message.channel.send('A média de catch do Forretres é: 170 Ultra Balls, 120 Netballs e 120 Tinkerballs')
    if message.content.startswith('$ball Shuckle'):
        await message.channel.send('A média de catch do Shuckle é: 350 Great Balls, 130 Super Balls, 60 Ultra Balls, 50 Netballs e 50 Duskballs')    


client.run(os.getenv('TOKEN'))
my_secret = os.environ['TOKEN']   