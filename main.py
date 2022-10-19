from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem

import sys
from PyQt5.uic import loadUi


listas = ["Email", "Estudar", "Web"]
class Janela(QWidget):
    def __init__(self):
        super(Janela, self).__init__()
        loadUi("main.ui", self)
        self.calendarWidget.selectionChanged.connect(self.datacalendario)
        # self.listWidget
        self.updateTarefas()


    def datacalendario(self):
        print("Data selecionada")
        # dataselecionada = self.calendarWidget.selectedDate().toPyDate().strftime("%m-%d")
        dataselecionada = self.calendarWidget.selectedDate().toPyDate()
        print("Data escolhida", dataselecionada)

    def updateTarefas(self):
        for lista in listas:
            item = QListWidgetItem(lista)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)




if __name__ == "__main__":
   app = QApplication(sys.argv)
   janela = Janela()
   janela.show()
   sys.exit(app.exec())


