import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit,QLabel,QGridLayout,QLineEdit,QListWidget,QCheckBox
from PyQt5.QtCore import Qt
import main
import os
import opencv_hong as oh
import winapi_hong as wh
import GetFarmName as gf

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.CreateUI()
        self.initUI()
        

    def CreateUI(self):
        self.btn=QPushButton('검색')
        self.btn2=QPushButton('방출')
        self.btn3=QPushButton('조합')
        self.btn4=QPushButton('TestButton')
        self.tbox1=QLineEdit()
        self.listbox=QListWidget()
        self.AutoCheck=QCheckBox('자동모드')
        self.RenewFarmList=QCheckBox('신규 리스트')
        self.tbox2=QTextEdit()
        self.tbox3=QTextEdit()
        self.tbox4=QTextEdit()
        self.tbox5=QTextEdit()
        self.qlabel=QLabel('목록:')
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('몬스터 검색'), 0, 0)
        grid.addWidget(self.qlabel, 1, 0)
        grid.addWidget(QLabel('반복횟수:'), 2, 0)
        grid.addWidget(QLabel('몬스터 필터링: \',\'로 구분'), 3, 0)
        
        grid.addWidget(self.tbox1, 0, 1)
        grid.addWidget(self.listbox, 1, 1)
        grid.addWidget(self.tbox2, 2, 1)
        grid.addWidget(self.tbox3, 3, 1)

        grid.addWidget(self.btn, 0, 2)
        grid.addWidget(self.btn2, 1, 2)
        grid.addWidget(self.btn3, 2, 2)
        grid.addWidget(self.AutoCheck)
        grid.addWidget(self.RenewFarmList)
        grid.addWidget(self.btn4)
        grid.addWidget(self.tbox4)
        grid.addWidget(self.tbox5)
        
        # # self.te1 = QTextEdit()
        # # self.te2 = QTextEdit()
        # # self.te3 = QTextEdit()
        # # btn2 = QPushButton(self)
        # vbox.addWidget(self.te1)
        # # vbox.addWidget(self.te2)
        # # vbox.addWidget(self.te3)
        # # vbox.addWidget(btn2)
        # # self.te1.setPlainText('200')
        # # self.te2.setPlainText('12000')
        # # self.te3.setPlainText('30000')
        self.btn.clicked.connect(self.btnRun_clicked)
        self.btn2.clicked.connect(self.ReleaseMonster)
        self.btn3.clicked.connect(self.MixMonster)
        self.btn4.clicked.connect(self.TestButtonClick)
        self.listbox.itemClicked.connect(self.ListClicked)
        
        # btn2.clicked.connect(self.btnRun_clicked)

        self.setLayout(grid)
        self.setWindowTitle('AutoMon')
        self.setGeometry(300, 300, 800, 400)
        self.show()

    
    def TestButtonClick(self):
        main.clicktest=True
        main.clickEvent.set()
        
        main.testx=int(self.tbox4.toPlainText())
        main.testy=int(self.tbox5.toPlainText())

    def ReleaseMonster(self):
        main.GoAwayFlag=True
        main.GoAwayEvent.set()

    def MixMonster(self):
        self.setFliter()
        main.MixMonsterFlag=True
        main.MixMonsterEvent.set()
    
    def MixMonsterRepeat(self):
        self.setFliter()
        main.MixMonsterRepeatFlag=True
        main.MixMonsterRepeatEvent.set()

    def setFliter(self):
        main.monfilter=self.tbox1.text()+','+self.tbox3.toPlainText()

    def btnRun_clicked(self):
        global MixFlag
        MixFlag= True
        self.setFliter()
        self.ClearList()
        if self.RenewFarmList.isChecked():
            if wh.FileExist('./list/'+self.tbox1.text()+'.txt'):
                os.remove('./list/'+self.tbox1.text()+'.txt')
        monsterlist=main.GetMonsterList(self.tbox1.text())
        listcount=0
        for i in monsterlist:
            listcount=listcount+1
            self.listbox.addItem(str(i))
        self.qlabel.setText('목록: '+str(listcount)+'개')
        

    def ListClickedFunc(self):
        global MixFlag
        MixFlag=False
        listcount=0

        self.setFliter()
        if not self.AutoCheck.isChecked():
            SelectedItem=self.listbox.currentItem().text()
            main.RemoveFarmFromList(self.tbox1.text(),SelectedItem)
            main.MoveToFarm(SelectedItem)
            self.ClearList()
            monsterlist=main.GetMonsterList(self.tbox1.text())
            for i in monsterlist:
                listcount=listcount+1
                self.listbox.addItem(str(i))
            self.qlabel.setText('목록: '+str(listcount)+'개')
        else:
            self.setFliter()
            main.RemoveFinishedMonsterFromList(self.tbox1.text())
            SelectedItem=self.listbox.currentItem().text()
            main.MoveToFarm(SelectedItem)
            self.ClearList()
            monsterlist=main.GetMonsterList(self.tbox1.text())
            for i in monsterlist:
                listcount=listcount+1
                self.listbox.addItem(str(i))
            self.qlabel.setText('목록: '+str(listcount)+'개')
            

            try:
                count=int(self.tbox2.toPlainText())
            except:
                count=999
            
            for i in range(count):
                if MixFlag:
                    break
                if not main.isMonFull:
                    self.MixMonster()
                    while True:
                        if main.MixFinished:
                            main.RemoveFinishedMonsterFromList(self.tbox1.text())
                            SelectedItem=self.listbox.item(0).text()
                            main.MoveToFarm(SelectedItem)
                            main.time.sleep(6)
                            self.ClearList()
                            monsterlist=main.GetMonsterList(self.tbox1.text())
                            listcount=0
                            for j in monsterlist:
                                listcount=listcount+1
                                self.listbox.addItem(str(j))
                            self.qlabel.setText('목록: '+str(listcount)+'개')
                            
                            main.MixFinished=False
                            break

                else:
                    main.isMonFull=False
                    break

    def ListClicked(self):
        global ListClickedThread
        ListClickedThread=threading.Thread(target=self.ListClickedFunc)
        ListClickedThread.start()
                    
    def ClearList(self):
        self.listbox.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())