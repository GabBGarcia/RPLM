# Trabalho Prático 3 - Detetive


#### Trabalho desenvolvido por:
- Gabrielle Batista Garcia

O jogo foi desenvolvido com intuito de ser resolvido através de regras de inferência a partir das pistas apresentadas.

O jogo pode ser executado através do executável que se encontra em:
```
build/Executável/mainloop.exe
```
ou pela IDE, para isso será necessario a instalação da biblioteca pygame através do comando:
```
pip install pygame
```

#### Informações

A nave contém 10 tripulantes fantasiados, sendo essas fantasias: Tobi, Spider-Man, Inosuk, Darth Vader, Sem Rosto, Iron-Man, Venom, Chewbacca, Sonic e Totoro.

Locais: 12 locais diferentes dentro da nave com diferentes tarefas a serem realizadas:
1.	Sala do café: limpar as mesas, comprar bebidas
2.	Administração: passar cartão, transferir dados
3.	Salão principal: dispensar lixo, inserir chaves
4.	Enfermaria: fazer checagem de saúde, 
5.	Sala de controle: observar câmeras, estabilizar a direção, moderar clima, mapear rota
6.	Elétrica: concertar fiação, calibrar o distribuidor 
7.	Laboratório: verificar amostras, limpar filtro de 02
8.	Reator: desbloquear coletores, ligar reator 
9.	Cozinha: preparar o café, substituir galão d’água
10.	Comunicação: resetar wi-fi, transferir dados
11.	Armazenamento: esvaziar escotilha, regar plantas
12.	Motor: ajustar potência, encher os motores

#### Cenário:

Você está em uma nave espacial com uma tripulação de 10 integrantes fantasiados rumo ao planeta NOME DO PLANETA para o evento NOME DO EVENTO que ocorrerá no planeta, 
quando a nave começa a apresentar problemas e a tripulação se vê obrigada a pousar no planeta Terra e realizar o reparo, no meio da confusão ninguém notou o desaparecimento repentino de dois tripulantes. Ao término do reparo todos voltam para a nave para dar continuidade a viagem, durante o embarque dois humanos se infiltram na nave o que faz com que ninguém perceba que dois de seus companheiros desapareceram. Todos dão continuidade em suas tarefas na nave, quando você, ao entrar LOCAL NA NAVE, se depara com o corpo de um de seus companheiros, então você aciona o botão de emergência para relatar o ocorrido, os tripulantes tentam se justificar dizendo onde estavam e o que estavam fazendo.

- Objetivo: Descobrir quem são os dois humanos infiltrados que assassinaram Chewbacca. 

#### Pistas

-	Chewbacca foi encontrado morto na elétrica.
-	Tobi estava na administração comprando bebidas ou Darth Vader é cúmplice;
-	Se Tobi não estava na administração comprando bebidas, então Venom não é um dos assassinos de Chewbacca;
-	Inosuk estava na sala do café limpando mesa ou Iron-man estava na administração fazendo checagem de exame;
-	Se Spider-Man estava na sala de controle observando as câmeras, então Sonic estava na sala do café limpando mesa;
-	Se Iron-Man estava na administração passando o cartão, então Sonic encontrou o corpo no salão principal;
-	Se Inosuk estava na sala do café limpando mesa, então Totoro é o assasino do Chewbacca;
-	Se Iron-Man estava na administração passando o cartão, então Venom é um dos assassinos de Chewbacca;
-	Se Inosuk estava na sala do café limpando mesa, então Sem Rosto matou Chewbacca;
-	Se Spider-Man estava na sala de controle observando as câmeras, então Inosuk estava na sala do café limpando mesa;
-	Inosuk não estava na sala do café limpando mesa ou Sonic estava na sala do café limpando mesa.


