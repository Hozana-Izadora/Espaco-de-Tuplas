import linsimpy
from tkinter import *

tse = linsimpy.TupleSpaceEnvironment()

#inp = Lê e remove atomicamente – consome – uma tupla, gerando KeyError se não for encontrado
#out = Retorna um evento simple que escreve uma tupla
#rdp = Lê uma tupla de forma não destrutiva, gerando KeyError se não for encontrado.
def criaNuvem(nomeNuvem): 
    tse.out(("NUVEM", nomeNuvem))
    print(f"Nuvem: {nomeNuvem} criada")
    tsNuvens = []
    try:
        nuvens = tse.inp(("NUVENS", object))
        tsNuvens = list(nuvens[1])
        tsNuvens.append(nomeNuvem)
        tse.out(("NUVENS", tuple(tsNuvens)))
    except:
        tsNuvens = [nomeNuvem]
        tse.out(("NUVENS", tuple(tsNuvens)))
#end criaNuvem

def criaHost(nomeHost): 
    print(f"Host: {nomeHost} criada")
    tse.out((nomeHost))
    tsHosts = []
    try:
        hosts = tse.inp(("HOSTS", object))
        tsHosts = list(hosts[1])
        tsHosts.append(nomeHost)
        tse.out(("HOSTS", tuple(tsHosts)))
    except:
        tsHosts = [nomeHost]
        tse.out(("HOSTS", tuple(tsHosts)))    
#end criaHost

def criaVM(nomeVM): 
    print(f"VM: {nomeVM} criada")
    tse.out((nomeVM))
    tsVms = []
    try:
        vms = tse.inp(("VMS", object))
        tsVms = list(vms[1])
        tsVms.append(nomeVM)
        tse.out(("VMS", tuple(tsVms)))
    except:
        tsVms = [nomeVM]
        tse.out(("VMS", tuple(tsVms)))
#end criaVM

def criaProcesso(nomeProcesso):
    print(f"Processo: {nomeProcesso} criada")
    tse.out((nomeProcesso))
    tsProcessos = []
    try:
        processos = tse.inp(("PROCESSOS", object))
        tsProcessos = list(processos[1])
        tsProcessos.append(nomeProcesso)
        tse.out(("PROCESSOS", tuple(tsProcessos)))
    except:
        tsProcessos = [nomeProcesso]
        tse.out(("PROCESSOS", tuple(tsProcessos)))


def deleteItem(tipo_tupla,nome):
    try:
        tupla = tse.inp((tipo_tupla,nome))
        return 1
    except:
        return 0
def deleteTuple(tipo_tupla, nome):
    try:
        tupla = tse.inp((tipo_tupla,object))
        nova_tupla = list(tupla[1])
        nova_tupla.remove(nome)
        tse.out((tipo_tupla,tuple(nova_tupla)))
        return(f"Tupla {nome} excluida")
    except:
        return(f"Tupla {nome} não encontrada")

def existe(tipo_tupla, nome):
    try:
        tupla = tse.rdp((tipo_tupla,nome))
        print(f"TUPLA {tupla[1]} JÁ EXISTE")
        return 1
    except:
        return 0
        

#listagem - read
def listNuvens():
    try:
        nuvens = tse.rdp(("NUVENS",object))    
        print(nuvens)
        return list(nuvens[1])
    except: 
        print(f"Tuple matching not found")
def listHosts():
    try:
        hosts = tse.rdp(("HOSTS",object))    
        print(hosts)
        return list(hosts[1])
    except: 
        print(f"Tuple matching not found")
def listVMs():
    try:
        vms = tse.rdp(("VMS",object))    
        print(vms)
        return list(vms[1])
    except: 
        print(f"Tuple matching not found")
def listProcessos():
    try:
        processos = tse.rdp(("PROCESSOS",object))    
        print(processos)
        return list(processos[1])
    except: 
        print(f"Tuple matching not found")

