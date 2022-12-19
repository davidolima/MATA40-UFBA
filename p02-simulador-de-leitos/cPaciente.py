#!/usr/bin/env python3

from funcAux import faixaEtaria

cor_reset = "\033[00m"
cor_sem_prioridade = "\033[92m"
cor_baixa_prioridade = "\033[93m"
cor_media_prioridade = "\033[33m"
cor_alta_prioridade = "\033[91m"

class Paciente:
    def __init__(self, idade, gravidade):
        self.idade = int(idade)
        self.gravidade = gravidade
        self.f_etaria = faixaEtaria(idade)

    def __str__(self):
        if self.gravidade == 5:
            out =  f"%s{str(id(self))}"% cor_alta_prioridade
        elif self.gravidade == 4:
            out = f"%s{str(id(self))}"%cor_media_prioridade
        elif self.gravidade == 3:
            out = f"%s{str(id(self))}"%cor_baixa_prioridade
        else:
            out = f"%s{str(id(self))}"%cor_sem_prioridade

        return out + cor_reset

    def info(self):
        out  = "\nID: " + str(id(self))
        out += "\nIdade: " + str(self.idade)
        out += "\nFaixa Etária: " + str(self.f_etaria)
        out += "\nEstado: " + str(self.gravidade)
        return out

if __name__ == '__main__':
    p1 = Paciente(10  , 5)
    p2 = Paciente(0.11, 4)
    p3 = Paciente(16  , 3)
    p4 = Paciente(90  , 2)
    p5 = Paciente(35  , 1)

    print(p1,p2,p3,p4,p5)
