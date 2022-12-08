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

def openTerceiraTela():
    terceira_tela.show()

def openQuartaTela():
    quarta_tela.show()
    lista_p= ts.listProcessos()
    quarta_tela.comboBox_2.addItems(lista_p)
    quarta_tela.comboBox_3.addItems(lista_p)
   
def chat():    
    p1 = quarta_tela.comboBox_2.currentText()
    p2 = quarta_tela.comboBox_3.currentText()
    msg = quarta_tela.lineEdit.text()
    ts.enviamsg(p1,p2,msg)
    resp = ts.recebeMsg(p1,p2,msg)
    quarta_tela.listWidget.addItem(f"{str(resp[1])} recebendo msg de {str(resp[0])}: {str(resp[2])}")
    quarta_tela.lineEdit.clear()

def insertHost():       
    path_host = terceira_tela.lineEdit.text()
    path_host = path_host.split("-")
    existeNuvem = ts.existe("NUVEM",path_host[1]) #VERIFICA SE A NUVEM EXISTE
    existeHost = ts.existe("HOST",path_host[2]) #VERIFICA SE O HOST EXISTE
    if(existeNuvem == 1 and existeHost == 1):
        id = path_host[0]
        path_host.remove(id)
        response = ts.criaContainer(id,path_host)
        if(response == 1):
            QMessageBox.about(terceira_tela,"ALERTA", "TUPLA JÁ EXISTE")  
        else:
            terceira_tela.label_5.setText("PATH: " +  str(response))
    else:
        QMessageBox.about(terceira_tela,"ALERTA", "ITEM NÃO FOI LOCALIZADO")  

    terceira_tela.lineEdit.clear()
def insertVM():   
    path_vm = terceira_tela.lineEdit_2.text()
    path_vm = path_vm.split("-")
    existeNuvem = ts.existe("NUVEM",path_vm[1]) #VERIFICA SE A NUVEM EXISTE
    existeHost = ts.existe("HOST",path_vm[2]) #VERIFICA SE O HOST EXISTE
    existeVm = ts.existe("VM",path_vm[3]) #VERIFICA SE O HOST EXISTE
    id = path_vm[0]
    path_vm.remove(id)

    if(existeNuvem == 1 and existeHost == 1 and existeVm == 1):
        response = ts.criaContainer(id,path_vm)
        if(response == 1):
            QMessageBox.about(terceira_tela,"ALERTA", "TUPLA JÁ EXISTE")  
        else:
            terceira_tela.label_5.setText("PATH: " +  str(response))
    else:
        QMessageBox.about(terceira_tela,"ALERTA", "ITEM NÃO FOI LOCALIZADO")  

    terceira_tela.lineEdit_2.clear()
def insertProcesso():   
    path_processo = terceira_tela.lineEdit_3.text()
    path_processo = path_processo.split("-")  
    
    existeNuvem = ts.existe("NUVEM",path_processo[1]) #VERIFICA SE A NUVEM EXISTE
    existeHost = ts.existe("HOST",path_processo[2]) #VERIFICA SE O HOST EXISTE
    existeVm = ts.existe("VM",path_processo[3]) #VERIFICA SE O HOST EXISTE
    processos = path_processo[4]
    proc = processos.split(",")
    id = path_processo[0]
    path_processo.remove(id)
    path_processo.remove(processos)
    x = False
    for p in proc:
        existeProcesso = ts.existe("PROCESSO",p) #VERIFICA SE O PROCESSO EXISTE
        if(existeProcesso == 1):
            path_processo.append(p)
            
            x=True

    if(x == True):
        if(existeNuvem == 1 and existeHost == 1 and existeVm == 1):
            response = ts.criaContainer(id,path_processo) 
            if(response == 1):
                QMessageBox.about(terceira_tela,"ALERTA", "TUPLA JÁ EXISTE")          
            else:
                terceira_tela.label_5.setText("PATH: " + str(response))
    else:
        QMessageBox.about(terceira_tela,"ALERTA", "ITEM NÃO FOI LOCALIZADO")  
    terceira_tela.lineEdit_3.clear()
def migracaoContainer():
    old_ts = terceira_tela.lineEdit_6.text()
    new_ts = terceira_tela.lineEdit_7.text()
    old_ts = old_ts.split("-")
    new_ts = new_ts.split("-")
    id = old_ts[0]
    old_ts.remove(id)
    id_new = new_ts[0]
    new_ts.remove(id_new)
    response = ts.migraContainer(id,old_ts,id_new,new_ts)
    if(response == 0):
        QMessageBox.about(terceira_tela,"ERRO", "ERRO AO CADASTRAR TUPLA")  
    else:
        terceira_tela.label_13.setText("NOVO PATH: "+ str(response))
    terceira_tela.lineEdit_6.clear()
    terceira_tela.lineEdit_7.clear()

def renomear():
    antigo = terceira_tela.lineEdit_4.text()
    novo = terceira_tela.lineEdit_5.text()
    tupla = terceira_tela.comboBox.currentText()
    response = ts.rename(tupla,antigo,novo)
    print(tupla)
    if(response == 1):
        QMessageBox.about(terceira_tela,"ERRO", "ERRO AO RENOMEAR TUPLA")  
    else:
        terceira_tela.label_9.setText(response)
        atualizaTela()
    terceira_tela.lineEdit_4.clear()
    terceira_tela.lineEdit_5.clear()

  

###########    MAIN   ###############
app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
primeira_tela.show()
segunda_tela=uic.loadUi("segunda_tela.ui")
terceira_tela=uic.loadUi("terceira_tela.ui")
quarta_tela=uic.loadUi("quarta_tela.ui")
primeira_tela.pushButton.clicked.connect(cadastraContainer)
primeira_tela.pushButton_2.clicked.connect(excluiItem)
segunda_tela.pushButton.clicked.connect(openTerceiraTela)
terceira_tela.pushButton_2.clicked.connect(renomear)
terceira_tela.pushButton.clicked.connect(insertHost)
terceira_tela.pushButton_3.clicked.connect(insertVM)
terceira_tela.pushButton_4.clicked.connect(insertProcesso)
terceira_tela.pushButton_5.clicked.connect(migracaoContainer)
terceira_tela.pushButton_6.clicked.connect(openQuartaTela)
quarta_tela.pushButton.clicked.connect(chat)

# quarta_tela.pushButton_2.clicked.connect(iniciaChat)

app.exec()
