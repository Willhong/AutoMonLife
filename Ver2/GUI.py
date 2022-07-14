import threading
import tkinter
from tkinter import messagebox
from UI import Ui_MainWindow as ui
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import main
import os
import opencv_hong as oh
import winapi_hong as wh
import GetFarmName as gf
import defineRecipe as dr
class MainClass(QMainWindow):
    def __init__(self) :
        QMainWindow.__init__(self)
        # UI 선언
        self.main_ui = ui()
        # UI 준비
        self.main_ui.setupUi(self)
        #self.main_ui.pushButton.clicked.connect(self.asdf)
        self.main_ui.leMonSearch.textChanged.connect(self.leMonSearch_TextChanged)
        self.main_ui.lwAutoFill.clicked.connect(self.lwAutoFill_Clicked)
        self.main_ui.btnSearch.clicked.connect(self.btnSearch_Clicked)
        
        # 화면을 보여준다.
        self.show()
        wh.CheckDirectory('./list')
        wh.CheckDirectory('./image')

    def leMonSearch_TextChanged(self):
        word=self.main_ui.leMonSearch.text()
        if word!="":
            Allmon=[]
            self.ClearListAutoFill()
            Recipe=dr.Recipe

            for i in Recipe:
                Allmon.append(i)
                Allmon.append(Recipe[i][0])
                Allmon.append(Recipe[i][1])

            Allmon = list(set(Allmon)) #중복제거
            Allmon.sort()
            for i in Allmon:
                if self.CheckWord(i,word):
                    self.main_ui.lwAutoFill.addItem(i)

    def lwAutoFill_Clicked(self):
        word=self.main_ui.lwAutoFill.currentItem().text()
        self.main_ui.leMonSearch.setText(word)
        #self.main_ui.lwAutoFill.clear()
        # prev_list= []
        # for i in self.main_ui.lwAutoFill.items():
        #     prev_list.append(i)
        # self.main_ui.lwAutoFill.addItems(prev_list)

    def btnSearch_Clicked(self):
        self.ClearListFarmList()
        if self.main_ui.rbLoadNew.isChecked():
            if wh.FileExist('./list/'+self.main_ui.leMonSearch.text()+'.txt'):
                os.remove('./list/'+self.main_ui.leMonSearch.text()+'.txt')
        monsterlist=main.GetMonsterList(self.main_ui.leMonSearch.text())
        if monsterlist.count!=0:
            for i in monsterlist:
                self.main_ui.lwFarmList.addItem(str(i))
            if wh.FileExist('./image/'+self.main_ui.leMonSearch.text()+'.png'):
                self.main_ui.lbMonIMG.setPixmap(QPixmap('./image/'+self.main_ui.leMonSearch.text()+'.png'))
            else:
                QMessageBox.information(self, "경고", "미등록 몬스터 입니다.")
                self.main_ui.lbMonIMG.setText("미등록 몬스터 입니다.")
                wh.SetClipboard(self.main_ui.leMonSearch.text())
                openSnippingToolThread=threading.Thread(target=wh.openSnippingTool)
                openSnippingToolThread.start()

            

        

    def ClearListAutoFill(self):
        self.main_ui.lwAutoFill.clear()

    def ClearListFarmList(self):
        self.main_ui.lwFarmList.clear()

    def CheckWord(self,SearchWord,word):
        a=SearchWord.find(word)
        if a!=-1:
            return True
        return False

        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()