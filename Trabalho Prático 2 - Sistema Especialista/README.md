# Sistema Especialista

#### Trabalho desenvolvido por:
- Gabrielle Batista Garcia
- Thiago Aoyama

### Sistema Especialista em Recomendações de lugares para ir em Curitiba-PR

O sistema especialista proposto consiste em ajudar o usuário a decidir um lugar para passear em Curitiba. Podendo ser usado tanto por pessoas que não conhecem Curitiba e estão na cidade a turismo, como por pessoas indecisas que apresentam dificuldades na hora de decidir um lugar para ir. 

A indicação será feita através de informações como:
- dia
- objetivo
- categoria
- ambiente
- custo

O sistema dará como resposta os seguintes destinos: 
-	Jardim Botânico
-	Museu Oscar Niemeyer
-	Torre Panorâmica 
-	Parque Tanguá
-	Bosque Zaninelli
-	Linha Turismo
-	Museu do Holocausto 
-	Passeio de Trem
-	Strike 7
-	Impulso Park
-	Puzzle Room: Escape Game
-	RA Kart Curitiba
-	Curitiba Paintball e Airsoft 
-	Campo Base Ginásio de Escalada 

## Regras

- Dia do passeio
  - segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira, sábado, domingo

- Objetivo do passeio
  - Se divertir com a família, Se divertir com os amigos, Passeio individual, Conhecer a cidade, Encontro, Sair da rotina

- Categoria
  - Atrativo Turístico, Museu, Parque, Bosque, Viagem local, Diversão

- Tipo de ambiente
  - Aberto, Fechado

- Custo
  - Pago, Gratuito

>> SE segunda OU terça OU quarta OU quinta OU sexta OU sábado OU domingo E gratuito E atrativo turístico E aberto E se divertir com a família OU encontro OU conhecer a cidade, ENTÃO sugerir ir ao Jardim Botânico.

>> SE terça OU quarta OU quinta OU sexta OU sábado OU domingo E pago E museu E fechado E passeio individual, ENTÃO sugerir ir ao Museu Oscar Niemeyer.

>> SE terça OU quarta OU quinta OU sexta OU sábado OU domingo E pago E atrativo turístico E fechado E passeio individual OU se divertir com a família, ENTÃO sugerir ir a Torre Panorâmica. 

>> SE segunda OU terça OU quarta OU quinta OU sexta OU sábado OU domingo E gratuito E parque E aberto E se divertir com a família OU encontro, ENTÃO sugerir ir ao Parque Tanguá.

>> SE segunda OU terça OU quarta OU quinta OU sexta OU sábado OU domingo E gratuito E bosque E aberto E se divertir com a família, ENTÃO sugerir ir ao Bosque Zaninelli.

>> SE terça OU quarta OU quinta OU sexta OU sábado OU domingo E pago E atrativo turístico E aberto E se divertir com a família, ENTÃO sugerir ir a Linha Turismo.

>> SE segunda OU terça OU quarta OU sexta OU domingo E gratuito E museu E fechado E passeio individual, ENTÃO sugerir ir ao Museu do Holocausto.

>> SE sexta OU sábado OU domingo E pago E viagem local E aberto E passeio individual OU conhecer a cidade, ENTÃO sugerir fazer um Passeio de Trem.

>> SE terça OU quarta OU quinta OU sexta OU sábado OU domingo E pago E diversão E fechado E encontro, ENTÃO sugerir ir ao Strike 7.

>> SE terça OU quarta OU quinta OU sexta OU sábado OU domingo E pago E diversão E fechado E se divertir com a família, ENTÃO sugerir ir ao Impulso Park.

>> SE segunda OU terça OU quarta OU quinta OU sexta OU sábado OU domingo E pago E diversão E fechado E se divertir com os amigos, ENTÃO sugerir ir ao Puzzle Room Escape Game.

>> SE terça OU quarta OU quinta OU sexta OU sábado OU domingo E pago E diversão E aberto E se divertir com os amigos, ENTÃO sugerir ir ao RA Kart Curitiba.

>> SE terça OU quarta OU quinta OU sexta OU sábado OU domingo E pago E diversão E aberto E sair da rotina OU se divertir com a família, ENTÃO sugerir ir ao Curitiba Paintball e Airsoft.

>> SE segunda OU terça OU quarta OU quinta OU sexta OU sábado E pago E diversão E fechado E sair da rotina OU passeio individual, ENTÃO sugerir ir ao Campo Base Ginásio de Escalada.


