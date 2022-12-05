import linsimpy
from tkinter import *

tse = linsimpy.TupleSpaceEnvironment()

#inp = Lê e remove atomicamente – consome – uma tupla, gerando KeyError se não for encontrado
#out = Retorna um evento simple que escreve uma tupla
#rdp = Lê uma tupla de forma não destrutiva, gerando KeyError se não for encontrado.
def criaNuvem(nomeNuvem): 
    print(f"Nuvem: {nomeNuvem} criada")
    tse.out((nomeNuvem))

    nuvens = tse.inp(("NUVENS", object))
    tsNuvens = list(nuvens[1])
    tsNuvens.append(nomeNuvem)
    tse.out(("NUVENS", tuple(tsNuvens)))

#end criaNuvem

def criaHost(nomeHost): 
    print(f"Host: {nomeHost} criada")
    tse.out((nomeHost))

    hosts = tse.inp(("HOSTS", object))
    tsHosts = list(hosts[1])
    tsHosts.append(nomeHost)
    tse.out(("HOSTS", tuple(tsHosts)))
    
#end criaHost

def criaVM(nomeVM): 
    print(f"VM: {nomeVM} criada")
    tse.out((nomeVM))

    vms = tse.inp(("VMS", object))
    tsVms = list(vms[1])
    tsVms.append(nomeVM)
    tse.out(("VMS", tuple(tsVms)))
#end criaVM

def criaProcesso(nomeProcesso):
    print(f"Processo: {nomeProcesso} criada")
    tse.out((nomeProcesso))

    processos = tse.inp(("VMS", object))
    tsProcessos = list(processos[1])
    tsProcessos.append(nomeProcesso)
    tse.out(("PROCESSOS", tuple(tsProcessos)))

def getTuple(nome):
    tse.timeout(1)
    tupla = tse.rdp((nome))
    print(tupla)
#end getNuvem

def listNuvens():
    nuvens = tse.rdp(("NUVENS",object))    
    print(nuvens)
    return list(nuvens[1])


nuvens = tse.inp(("NUVENS", object))
print(nuvens)

