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
    tse.out(("HOST", nomeHost))
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
    tse.out(("VM", nomeVM))
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
    tse.out(("PROCESSO", nomeProcesso))

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

def criaContainer(id,ts):
    tuplas = []
    try:
        tupla = tse.inp(("TS",id,tuple(ts)))
        print(f"Tupla já existe: {tupla}")
        return 1
    except:        
        tse.out(("TS",id,tuple(ts)))
        x = [id,tuple(ts)]
        tuplas.append(x)
        tupla = tse.rdp(("TS",id,tuple(ts)))
        return tupla


def migraContainer(id, oldTs, idNew,newTs):
    try:
        tuplas = tse.inp(("TS",id,tuple(oldTs)))
        tse.out(("TS",idNew, tuple(newTs)))
        tupla = tse.rdp(("TS",idNew,tuple(newTs)))
        return tupla
    except:        
        return 0
            

def rename(ts,oldName,newName):
    try:
        if(ts == "NUVEM"):
            tse.inp((ts,oldName))
            tse.out((ts,newName))
            
            tupla = tse.inp(("NUVENS",object))
            nova_tupla = list(tupla[1])
            nova_tupla.remove(oldName)
            nova_tupla.append(newName)
            tse.out(("NUVENS",tuple(nova_tupla)))
            print("NOVO NOME: "+ str(newName))
            return "NOVO NOME: "+ str(newName)
        
        elif(ts == "HOST"):
            tse.inp((ts,oldName))
            tse.out((ts,newName))
            
            tupla = tse.inp(("HOSTS",object))
            nova_tupla = list(tupla[1])
            nova_tupla.remove(oldName)
            nova_tupla.append(newName)
            tse.out(("HOSTS",tuple(nova_tupla)))
            print("NOVO NOME: "+ str(newName))
            return "NOVO NOME: "+ str(newName)
        
        elif(ts == "VM"):
            tse.inp((ts,oldName))
            tse.out((ts,newName))
            
            tupla = tse.inp(("VMS",object))
            nova_tupla = list(tupla[1])
            nova_tupla.remove(oldName)
            nova_tupla.append(newName)
            tse.out(("VMS",tuple(nova_tupla)))
            return "NOVO NOME: "+ str(newName)
        
        elif(ts == "PROCESSO"):
            tse.inp((ts,oldName))
            tse.out((ts,newName))
            
            tupla = tse.inp(("PROCESSOS",object))
            nova_tupla = list(tupla[1])
            nova_tupla.remove(oldName)
            nova_tupla.append(newName)
            tse.out(("PROCESSOS",tuple(nova_tupla)))
            return "NOVO NOME: "+ newName    
    except:
        return 1
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

def enviamsg(p1,p2,msg):
    tse.out((p1,p2,msg))

def recebeMsg(p1,p2,msg):
    mensagem = tse.inp((p1,p2,msg))
    return (mensagem)

