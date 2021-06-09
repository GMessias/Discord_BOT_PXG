# Discord_BOT_PXG
Este é um BOT de discord para saber média de pokeball que precisa gastar na captura de um pokemon.

<img src ="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src ="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white"/>

Tabela de conteúdos
=================
<!--ts-->
   * [Introdução](#Introdução)
   * [Explicação](#Explicação)
   * [Funcionamento](#Funcionamento)
   * [Updates](#Updates)
<!--te-->
## Introdução
O BOT é focado no jogo PokeXGames ou conhecido também por PXG. O BOT está em https://replit.com/</br>
Dentro do jogo a captura de pokemons é especulado que tenha uma fórmula, ou é puramente sorte.</br>
No site http://pokexgames-tutoriais.blogspot.com/p/media-de-balls.html#axzz6x1tSndEM você pode informar o nome de um pokemon que retornará a média de balls dele.</br>
Perguntando pra alguns jogadores todos entram em concorrdância que o site é ruim, lento, poluído e queria algo melhor.</br>
Perguntei pra equipe do PXG se tinha alguma API pra conseguir essas informações, não têm.</br>
Não sei de onde que esse site da média recebe as informações então comecei a fazer testes e pensar numa fórmula.</br>
Cheguei aproximadamente nisso: 
```
(Preço_Pokemon_NPC / 65) * 1,09
```
A margem de erro é baixa e pouquissímos pokemons fogem dessa margem. Ex: Tentacruel, Pidgeotto, provavelmente tem mais.</br>

## Explicação
Essa fórmula foi baseada em algumas informações que achei.
1- No site do média de ball que coloquei o link ali encima, tem no final da página isto: "O sistema de médias faz um cálculo automático, com base no valor do pokemon no NPC e da ball que está sendo usada".
2- PXG tem uma função que nomearam como Sistema de Catch, que consiste em aumentar as chances de captura em pokemons cujo valor gasto em pokeball compradas num NPC seja maior que o preço do pokemon vendido num outro NPC.
Levando em conta isso, peguei o preço do pokemon e dividi por 65 que é 130 o valor de uma ultraball porém dividida por 2. Depois encima desse valor acrescento 9%, que seria x1,09.
O número resultante é a média de ultraballs pra capturar o pokemon.
O BOT lê um arquivo CSV e procura o preço do pokemon no NPC. Eu tirei essa tabela desse site: https://wiki.pokexgames.com/index.php/NPC_Heather_(Pok%C3%A9mon).
O arquivo CSV tem uma coluna que quando valor é 1, o pokemon não está no Sistema de Catch. Se está ou não o BOT te informa na pesquisa de um pokemon que não esteja. Exemplo: Jolteon.

## Funcionamento
O BOT tem 4 comandos, por enquanto.
1- $media Nome_Pokemon  
2- $help
3- $ballNome_Pokemon
4- $sistema

1- Vê a média de ultraball na minha fórmula.
2- Mostrar os comandos que o BOT possui.
3- Caso tenha o pokemon mencionado irá informar as balls que são médias. Tem alguns pokemons registrados, isso porque a informação é manualmente.
4- Explica o que é o Sistema de Catch.
## Updates
Gostaria de implementar mais funções para identifcar outras informações como: onde tem mais desse pokemon, suas fraquezas, seu level etc.
