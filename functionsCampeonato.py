import time
from random import randint

jogos = []


def montaTabela():
    return ["Atlético-MG", "Bahia", "Corinthians", "Flamengo", "Fluminense", "Grêmio", "Internacional", "Palmeiras",
            "Santos", "São Paulo"]


def dadosPartidas():
    for c in range(0, len(montaTabela())):
        montaJogos = montaTabela()
        jogos.append([montaJogos[c], 0, 0, 0, 0, 0, 0, 0])
    for c in range(0, montaJogos.__len__()):
        for j in range(0, montaJogos.__len__()):
            if c != j:
                time1 = randint(0, 4)
                time2 = randint(0, 4)
                if time1 == time2:
                    jogos[c][4] += 1
                    jogos[j][4] += 1
                    jogos[c][5] += time1
                    jogos[j][5] += time2
                    jogos[c][6] += time1
                    jogos[j][6] += time2
                    jogos[c][1] += 1
                    jogos[j][1] += 1

                    print("{} {}x{} {}".format(jogos[c][0], time1, time2, jogos[j][0]))

                if time1 > time2:
                    jogos[c][2] += 1
                    jogos[c][5] += time1
                    jogos[c][6] += time2
                    jogos[c][1] += 3
                    jogos[j][3] += 1
                    jogos[j][5] += time2
                    jogos[j][6] += time1

                    print("{} {}x{} {}".format(jogos[c][0], time1, time2, jogos[j][0]))
                if time1 < time2:
                    jogos[j][2] += 1
                    jogos[j][5] += time2
                    jogos[j][6] += time1
                    jogos[j][1] += 3
                    jogos[c][3] += 1
                    jogos[c][5] += time1
                    jogos[c][6] += time2

                    print("{} {}x{} {}".format(jogos[j][0], time2, time1, jogos[c][0]))


def jogoCampeonato(times=[]):
    maior = 0
    maiorValor = 0
    for i in range(0, jogos.__len__()):
        for j in range(0, jogos.__len__()):
            if jogos[j][1] == maior:
                if jogos[j][5] == jogos[maiorValor][5]:
                    if jogos[j][2] > jogos[maiorValor][2]:
                        maior = jogos[j][1]
                        maiorValor = j
                if jogos[j][5] > jogos[maiorValor][5]:
                    maior = jogos[j][1]
                    maiorValor = j

            if maior < jogos[j][1]:
                maior = jogos[j][1]
                maiorValor = j

            if j == (len(jogos) - 1):
                times.append([jogos[maiorValor][0],
                              jogos[maiorValor][1],
                              jogos[maiorValor][2],
                              jogos[maiorValor][3],
                              jogos[maiorValor][4],
                              jogos[maiorValor][5],
                              jogos[maiorValor][6]])
                jogos.remove(jogos[maiorValor])
                maior = 0
                maiorValor = 0
    return times


def pontuacaotabela():
    for i in range(0, jogoCampeonato().__len__()):
        time.sleep(0.1)
        print("{} - Pontos:{} Vitórias:{} Empates:{} Derrotas:{} Gols Feitos:{} Gols Sofridos:{}".format(
            jogoCampeonato()[i][0], jogoCampeonato()[i][1], jogoCampeonato()[i][2],
            jogoCampeonato()[i][4], jogoCampeonato()[i][3],
            jogoCampeonato()[i][5], jogoCampeonato()[i][6]))


def tabela():
    print("1° {}".format(jogoCampeonato()[0][0]))
    print("2° {}".format(jogoCampeonato()[1][0]))
    print("3° {}".format(jogoCampeonato()[2][0]))
    print("4° {}".format(jogoCampeonato()[3][0]))
    print("5° {}".format(jogoCampeonato()[4][0]))
    print("6° {}".format(jogoCampeonato()[5][0]))
    print("7° {}".format(jogoCampeonato()[6][0]))
    print("8° {}".format(jogoCampeonato()[7][0]))
    print("9° {}".format(jogoCampeonato()[8][0]))
    print("10° {}".format(jogoCampeonato()[9][0]))

def campeaoEVice():
    print("1° lugar - {} Campeão Brasileiro".format(jogoCampeonato()[0][0]))
    print("2° lugar - {} Vice-Campeão Brasileiro".format(jogoCampeonato()[1][0]))


def rebaixados():
    print("REBAIXADOS")
    print(jogoCampeonato()[8][0])
    print(jogoCampeonato()[9][0])
