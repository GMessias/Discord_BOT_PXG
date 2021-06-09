# Discord_BOT_PXG
Este é um BOT de discord para saber média de pokeball que precisa gastar na captura de um pokemon.

O BOT é focado no jogo PokeXGames ou conhecido também por PXG.
Dentro do jogo a captura de pokemons é especulado que tenha uma fórmula, ou é puramente sorte.
No site http://pokexgames-tutoriais.blogspot.com/p/media-de-balls.html#axzz6x1tSndEM você pode informar o nome de um pokemon que retornará a média de balls dele.
Perguntando pra alguns jogadores todos entram em concorrdância que o site é ruim, lento, poluído e queria algo melhor.
Perguntei pra equipe do PXG se tinha alguma API pra conseguir essas informações, não têm.
Não sei de onde que esse site da média recebe as informações então comecei a fazer testes e pensar numa fórmula.
Cheguei na mais aproximada que é (Preço_Pokemon_NPC / 65) * 1,09
A margem de erro é baixa e pouquissímos pokemons fogem dessa margem. Ex: Tentacruel, Pidgeotto, provavelmente tem mais.
