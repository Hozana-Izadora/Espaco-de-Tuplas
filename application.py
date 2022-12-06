from PyQt5 import QtWidgets, uic
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

def cadastraContainer():
    nuvem    = primeira_tela.lineEdit.text()
    host     = primeira_tela.lineEdit_2.text()
    vm       = primeira_tela.lineEdit_3.text()
    processo = primeira_tela.lineEdit_4.text()

    data = [nuvem, host,vm, processo]
    
    if(data[0]!= ''):
        nomeNuvem = data[0]
        ts.criaNuvem(nomeNuvem)
    if(data[1]!= ''):
        nomeHost = data[1]
        ts.criaHost(nomeHost)
    if(data[2]!= ''):
        nomeVM = data[2]
        ts.criaVM(nomeVM)
    if(data[3]!= ''):
        nomeProcesso = data[3]
        ts.criaProcesso(nomeProcesso)
    lista_nuvens = ts.listNuvens()
    openSegundaTela(lista_nuvens)

def openSegundaTela(itens):
    segunda_tela.show()
    for i in itens:
        segunda_tela.listView.addItem(i)

    
    

app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("primeira_tela.ui")
primeira_tela.show()
segunda_tela=uic.loadUi("segunda_tela.ui")
primeira_tela.pushButton.clicked.connect(cadastraContainer)
# primeira_tela.pushButton.clicked.connect(openSegundaTela)

app.exec()
