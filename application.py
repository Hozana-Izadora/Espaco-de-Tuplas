from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import linsimpy

import Espaco_Tuplas as ts
lista_nuvens = []

nuvens = []
hosts = []
vms = []
processos = []


tse = linsimpy.TupleSpaceEnvironment()
tse.out(("NUVENS", tuple(nuvens)))
tse.out(("HOSTS", tuple(hosts)))
tse.out(("VMS", tuple(vms)))
tse.out(("PROCESSOS", tuple(processos)))


def atualizaTela():
    lista_nuvens = ts.listNuvens()
    lista_hosts = ts.listHosts()
    lista_vms = ts.listVMs()
    lista_processos = ts.listProcessos()
    openSegundaTela(lista_nuvens,lista_hosts,lista_vms,lista_processos)
    primeira_tela.lineEdit.clear()
    primeira_tela.lineEdit_2.clear()
    primeira_tela.lineEdit_3.clear()
    primeira_tela.lineEdit_4.clear()

def cadastraContainer():
    nuvem    = primeira_tela.lineEdit.text()
    host     = primeira_tela.lineEdit_2.text()
    vm       = primeira_tela.lineEdit_3.text()
    processo = primeira_tela.lineEdit_4.text()
    
    data = [nuvem, host,vm, processo]
    if(data[0]!= ''):
        nomeNuvem = data[0]             
        if(ts.existe("NUVEM",nomeNuvem) == 0):
            ts.criaNuvem(nomeNuvem)
        else:
            QMessageBox.about(primeira_tela,"ALERTA", "NUVEM JÁ EXISTE")            
    if(data[1]!= ''):
        nomeHost = data[1]
        if(ts.existe("HOST",nomeHost) == 0):
            ts.criaHost(nomeHost)
        else:
            QMessageBox.about(primeira_tela,"ALERTA", "HOST JÁ EXISTE")  
    if(data[2]!= ''):
        nomeVM = data[2]
        if(ts.existe("VM",nomeVM) == 0):
            ts.criaVM(nomeVM)
        else:
            QMessageBox.about(primeira_tela,"ALERTA", "VM JÁ EXISTE")  

    if(data[3]!= ''):
        nomeProcesso = data[3]
        if(ts.existe("PROCESSO",nomeProcesso) == 0):
            ts.criaProcesso(nomeProcesso)
        else:
            QMessageBox.about(primeira_tela,"ALERTA", "PROCESSO JÁ EXISTE")  

    atualizaTela()

def openSegundaTela(nuvens,hosts,vms,processos):
    segunda_tela.show()
    segunda_tela.listWidget.clear()
    segunda_tela.listWidget_2.clear()
    segunda_tela.listWidget_3.clear()
    segunda_tela.listWidget_4.clear()

    if(len(nuvens)>0):
        for n in nuvens:
            segunda_tela.listWidget.addItem(n)
            segunda_tela.label_6.setText(str(len(nuvens)))
    if(len(hosts)>0):            
        for h in hosts:
            segunda_tela.listWidget_2.addItem(h)
            segunda_tela.label_8.setText(str(len(hosts)))
    if(len(vms)>0):
        for v in vms:
            segunda_tela.listWidget_3.addItem(v)
            segunda_tela.label_7.setText(str(len(vms)))
    if(len(processos)>0):
        for p in processos:
            segunda_tela.listWidget_4.addItem(p)
            segunda_tela.label_9.setText(str(len(processos)))

def excluiItem():
    nuvem    = primeira_tela.lineEdit.text()
    host     = primeira_tela.lineEdit_2.text()
    vm       = primeira_tela.lineEdit_3.text()
    processo = primeira_tela.lineEdit_4.text() 
    if(nuvem != ''):
        ts.deleteItem("NUVEM",nuvem)
        response =ts.deleteTuple("NUVENS",nuvem)        
        QMessageBox.about(primeira_tela,"ALERTA", response) 
        atualizaTela()     
    if(host != ''):
        ts.deleteItem("HOST",host)
        response =ts.deleteTuple("HOSTS",host)        
        QMessageBox.about(primeira_tela,"ALERTA", response) 
        atualizaTela()     
    if(vm != ''):
        ts.deleteItem("VM",vm)
        response =ts.deleteTuple("VMS",vm)        
        QMessageBox.about(primeira_tela,"ALERTA", response) 
        atualizaTela()     
    if(processo != ''):
        ts.deleteItem("PROCESSO",processo)
        response =ts.deleteTuple("PROCESSOS",processo)        
        QMessageBox.about(primeira_tela,"ALERTA", response) 
        atualizaTela()     

app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
primeira_tela.show()
segunda_tela=uic.loadUi("segunda_tela.ui")
primeira_tela.pushButton.clicked.connect(cadastraContainer)
primeira_tela.pushButton_2.clicked.connect(excluiItem)

app.exec()
