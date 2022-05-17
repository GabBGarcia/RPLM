var answers = {};

var question_one = document.getElementById('question-1');
var question_two = document.getElementById('question-2');
var question_three = document.getElementById('question-3');
var question_four = document.getElementById('question-4');
var question_five = document.getElementById('question-5');

function storeAnswer(question_number, event){
    if(event.target.type === 'radio'){
        console.log(event.target.value);
        answers['question'+question_number] = parseInt(event.target.value);
        console.log(answers);
    }
}

question_one.addEventListener('click', function(event){
    storeAnswer(1, event)
})
question_two.addEventListener('click', function(event){
    storeAnswer(2, event)
})
question_three.addEventListener('click', function(event){
    storeAnswer(3, event)
})
question_four.addEventListener('click', function(event){
    storeAnswer(4, event)
})
question_five.addEventListener('click', function(event){
    storeAnswer(5, event)
})

function totalScore(){
    var total_score =
    answers.question1+
    answers.question2+
    answers.question3+
    answers.question4+
    answers.question5;

    return total_score;
}

function getInfoBasedOnScore(){
    if(answers.question1 == 1 || 2 || 3 || 4 || 5 || 6 || 7){
        if(answers.question2 == 1 || 2 || 4 || 5){
            if(answers.question3 == 1){
                if(answers.question4 == 1){
                    if(answers.question5 == 2){
                        var choice = "JARDIM BOTÂNICO: A atração mais visitada de Curitiba! É ocupado por lagos, trilhas, a estufa de vidro, o Jardim das sensações, o Jardim frânces e um bosque. Localização: Rua Eng°. Ostoja Roguski, 690 - Jardim Botânico. Horário de funcionamento: De Segunda-feira a Domingo - Das 06h às 19h30";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 2 || 4 || 5 || 6 || 7){
        if(answers.question2 == 3){
            if(answers.question3 == 2){
                if(answers.question4 == 2){
                    if(answers.question5 == 1){
                        var choice = "MUSEU OSCAR NIEMEYER: Considerado o maior museu de arte da América Latina abriga referenciais importantes da produção artística nacional e internacional, com mais de 9 mil obras nas áreas de artes visuais, arquitetura e design. Localização: Rua Mal. Hermes, 999 - Centro Cívico. Horário de funcionamento: De Terça à Domingo - Das 10h às 17h30. Ingresso: R$ 30,00 (inteira).";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 3){
        if(answers.question2 == 3){
            if(answers.question3 == 2){
                if(answers.question4 == 2){
                    if(answers.question5 == 2){
                        var choice = "MUSEU OSCAR NIEMEYER: Considerado o maior museu de arte da América Latina abriga referenciais importantes da produção artística nacional e internacional, com mais de 9 mil obras nas áreas de artes visuais, arquitetura e design. Localização: Rua Mal. Hermes, 999 - Centro Cívico. Horário de funcionamento: De Terça à Domingo - Das 10h às 17h30. Ingresso: quarta-feira Entrada gratuita.";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 2 || 3 || 4 || 5 || 6 || 7){
        if(answers.question2 == 1 || 3){
            if(answers.question3 == 1){
                if(answers.question4 == 2){
                    if(answers.question5 == 1){
                        var choice = "TORRE PANORÂMICA: Localização: Rua Prof. Lycio Grein de Castro Vellozo, 191 - Mercês. Horário de funcionamento: De Terça à Domingo - Das 10h às 18h. Ingresso: R$ 6,00 (inteira).";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 1 || 2 || 3 || 4 || 5 || 6 || 7){
        if(answers.question2 == 1 || 2 || 5){
            if(answers.question3 == 3){
                if(answers.question4 == 1){
                    if(answers.question5 == 2){
                        var choice = "PARQUE TANGUA: A torre de telefonia que fica a mais de 100 m de altura e de onde se tem uma vista em 360º da cidade, onde é possível observar o planejamento urbano de Curitiba e seu zoneamento. Localização: Rua Oswaldo Maciel, 97 - Taboão. Horário de funcionemnto: Todos os dias - Das 6h às 20h.";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 1 || 2 || 3 || 4 || 5 || 6 || 7){
        if(answers.question2 == 1){
            if(answers.question3 == 4){
                if(answers.question4 == 1){
                    if(answers.question5 == 2){
                        var choice = "BOSQUE ZANINELLI: Localização: Rua Victor Benato, 210 - Pilarzinho. Horário de funcionamento: Todos os dias - Das 6h às 19h.";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 2 || 3 || 4 || 5 || 6 || 7){
        if(answers.question2 == 4){
            if(answers.question3 == 1){
                if(answers.question4 == 1){
                    if(answers.question5 == 1){
                        var choice = "LINHA TURISMO: O projeto arquitetônico, executado com materiais rústicos, repete na forma e nas cores os quatro elementos da natureza: terra, fogo, água e ar. Localização: Ponto inicial na Rua 24 Horas (portal de entrada da Rua Visconde de Nácar). Horário de funcionamento: De Terça à Domingo - Das 8h30 às 17h00, a cada 30 minutos";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 1 || 2 || 3 || 5 || 7){
        if(answers.question2 == 3){
            if(answers.question3 == 2){
                if(answers.question4 == 2){
                    if(answers.question5 == 2){
                        var choice = "MUSEU DO HOLOCAUSTO: O Museu do Holocausto de Curitiba é uma proposta pioneira que uniu os eixos de educação, memória e pesquisa com um projeto museológico permanente sobre este tema. Localização: Rua Cel. Agostinho Macedo, 248 - Bom Retiro. Horário de funcionamento: Segunda, terça e quarta: 8h30 às 11h30 e 14h30 às 17h30 - Sexta: 8h30 às 11h30 - Domingo: 9h às 12h. OBSERVAÇÃO: NÃO É PERMITIDA a entrada de menores de 12 anos. ";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 5 || 6 || 7){
        if(answers.question2 == 3 || 4){
            if(answers.question3 == 5){
                if(answers.question4 == 1){
                    if(answers.question5 == 1){
                        var choice = "PASSEIO DE TREM: Descubra a história da Ferrovia Paranaguá-Curitiba, com suas mais de 41 pontes e 13 túneis. Aprecie o impressionante visual da maior área contínua de Mata Atlântica preservada do país com montanhas e vales, rios, cascatas, penhascos e desfiladeiros.  Partida: Saída da Rodoferroviária de Curitiba. Horário: Sexta, Sabado e Domingo - saída às 8h30. Bilhete: apróximadamente R$ 150, 00 (apenas ida). OBSERVAÇÃO: O retorno NÃO é incluso.";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 2 || 3 || 4 || 5 || 6 || 7){
        if(answers.question2 == 5){
            if(answers.question3 == 6){
                if(answers.question4 == 2){
                    if(answers.question5 == 1){
                        var choice = "STRIKE 7: boliche com 13 pistas, cada uma com limite de 10 pessoas,  local ainda tem karaokê, 14 mesas de sinuca, fliperama e playground. Localização: Rua Via Veneto, 1979 - Santa Felicidade. Horário de funcionamento: De Terça à Sexta - Das 18h às 00h. Sábado e Domingo - Das 17h às 2h. Valor: a partir de R$ 60,00 por hora de pista.";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 2 || 3 || 4 || 5 || 6 || 7){
        if(answers.question2 == 1){
            if(answers.question3 == 6){
                if(answers.question4 == 2){
                    if(answers.question5 == 1){
                        var choice = "IMPULSO PARK: Com um único ingresso é possível aproveitar todas as atividades, como Free Jump, Basket, Ninja, Half Pipe, Parkour, Piscina de Espuma, Escalada, Batalha de Cotonete, Batak e Arena Imp. Localização: Rua Francisco Nunes, 1467 – Curitiba. Horóario de funcionamento: De Terça à Sexta - Das 13h às 22h. Sábado - Das 10h às 22h. Domingo - Das 13h às 22h. Ingresso: comum R$120,00 por pessoa. ";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 1 || 2 || 3 || 4 || 5 || 6 || 7){
        if(answers.question2 == 2){
            if(answers.question3 == 6){
                if(answers.question4 == 2){
                    if(answers.question5 == 1){
                        var choice = "PUZZLE ROOM - ESCAPE GAME: Escape Game é uma experiência real e interativa. Você e seu time de 2 a 10 jogadores serão trancados em uma sala e terão que cooperar em equipe, utilizando várias pistas para resolver enigmas e escapar da sala, antes que os 60 minutos acabe. Localização: Rua Visconde de Nacar 743, Curitiba-Centro. Horário de funcionamento: De Domingo à Quinta - Das 14h às 20h30. Sexta e Sábado - Das 14h às 22h. Ingresso: R$ 84,00 por pessoa.";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 2 || 3 || 4 || 5 || 6 || 7){
        if(answers.question2 == 2){
            if(answers.question3 == 6){
                if(answers.question4 == 1){
                    if(answers.question5 == 1){
                        var choice = "RA KART CURITIBA: A RA Kart oferece tanto pista coberta como descoberta, ainda mais, o kartódromo possui uma estrutura completa com sala de briefing e equipamentos, lanchonete e até torre de controle! Além disso, para quem não quiser correr de kart, o kartódromo tem uma sala de jogos com mesas de sinuca, fliperama e pebolim. Localização: Rodovia, BR-116, 15560 - Novo Mundo. Horário de funcionamento: De Terça à Sexta - Das 17h às 22h. Sábado e Domingo - Das 14h às 22h.";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 2 || 3 || 4 || 5 || 6 || 7){
        if(answers.question2 == 1 || 6){
            if(answers.question3 == 6){
                if(answers.question4 == 1){
                    if(answers.question5 == 1){
                        var choice = "CURITIBA PAINTBALL E AIRSOFT: Grupo mínimo de pessoas 6 e máximo de 18 pessoas em cada campo, podendo reservar equipamentos com 100 ou 200 bolas. Localização: Av. Cândido Hartmann, 5055 - Santa Felicidade. Horário de funcionamento: De Terça à Domingo - Das 14h às 22h. Ingresso: a partir de R$ 35,00 por pessoa por 1 hora.";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
    if(answers.question1 == 1 || 2 || 3 || 4 || 5 || 6){
        if(answers.question2 == 3 || 6){
            if(answers.question3 == 6){
                if(answers.question4 == 2){
                    if(answers.question5 == 1){
                        var choice = "CAMPO BASE GINÁSIO DE ESCALADA: Com uma estrutura de aproximadamente 700 m², sendo 500 m² de paredes escaláveis, as modalidades de escalada vão desde caminhos fáceis para quem nunca escalou até vias mais difíceis para escaladores mais experientes. Localização: Ginásio - Av. Pres. Kennedy, 35 - Rebouças. Horário de funcionamento: De Segunda à Sexta - Das 7h às 22h. Sábado - Das 10h às 19h. Diária: R$ 40,00.";
                    }
                }
            }
        }  
    } else {
        var choice = "Não foi possível encontrar um lugar que adeque-se a suas seleções. Tente outras opções!";
    }
        
    return choice;
}

var submit1 = document.getElementById('submit1');
var submit2 = document.getElementById('submit2');
var submit3 = document.getElementById('submit3');
var submit4 = document.getElementById('submit4');
var submit5 = document.getElementById('submit5');

function nextQuestion(question_number){
    var current_question_number = question_number - 1;
    var question_number = question_number.toString();
    var current_question_number = current_question_number.toString();

    var el = document.getElementById('question-'+question_number);
    var el2 = document.getElementById('question-'+current_question_number);

    el.style.display = "block";
    el2.style.display = "none";
}

submit1.addEventListener('click', function(){
    nextQuestion(2);
    growProgressBar('40%');
})
submit2.addEventListener('click', function(){
    nextQuestion(3);
    growProgressBar('60%');
})
submit3.addEventListener('click', function(){
    nextQuestion(4);
    growProgressBar('80%');
})
submit4.addEventListener('click', function(){
    nextQuestion(5);
    growProgressBar('100%');
})
submit5.addEventListener('click', function(){
    nextQuestion(6);
})

submit5.addEventListener('click', function(){
    document.getElementById("printscoreinfo").innerHTML = getInfoBasedOnScore();
})

function growProgressBar(percentage_width){
    var bar = document.getElementById("progress_bar");
    bar.style.width = percentage_width;
}

function mudaPaginaIn(){
    window.location.href = "index.html";
}