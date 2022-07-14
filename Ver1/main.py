from asyncio import sleep
from turtle import down
from cv2 import imshow
from sqlalchemy import false
import win32gui, win32ui, win32con
from PIL import Image, ImageGrab
import numpy as np
import cv2
import win32api
import time
import pytesseract
import threading

import opencv_hong as oh
import winapi_hong as wh
import GetFarmName as gf

import defineMonster as monster

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
config = ('-l kor+eng --oem 3 --psm 4') #

def CropImage(img):
    # crop=img[271:550,585:782]

    # crop=img[451:496,600:775]

    crop=img[460:505,600:775]
    return crop

def Capture():
    im,windowcor=wh.WindowCapture('MapleStory')
    mat = np.array(im)
    mat=cv2.cvtColor(mat,cv2.COLOR_RGB2GRAY)
    return mat

def ClickMatImage(WhatToClick):
    mat= Capture()
    ByeByecoor=oh.coorTemplateMatch(mat,WhatToClick,0.9)
    wh.mouse_click(ByeByecoor[0],ByeByecoor[1]+25)

def ScreenshotMain():
    wh.mouse_move(1000,500)
    MainImage,b =wh.WindowCapture("MapleStory")
    matMainImage=np.array(MainImage)
    matMainImage=cv2.cvtColor(matMainImage,cv2.COLOR_RGB2GRAY)
    return matMainImage

def RightClickLatestMonseter():
    wh.mouse_Rclick(520,720)

def RightClickMonster():
    for i in range(7):
        wh.mouse_Rclick(520-67*i,720)
        time.sleep(0.1)

        # ClickCapture(ByeBye)
        wh.mouse_click(500-67*i,553)

        # ClickCapture(OKButton)
        time.sleep(0.1)
        wh.key_input_enter()




def InitSequence():
    wh.mouse_click(45, 673)
    im,windowcor=wh.WindowCapture('MapleStory')
    wh.mouse_Wheeel(245,727,'down',30)

def MixNextPage():
    im,windowcor=wh.WindowCapture('MapleStory')
    wh.mouse_Wheeel(245,727,'down',7)

def ClickOKButton():
    wh.mouse_click(485,450)

def ClickFirstMon():
    time.sleep(0.05)
    wh.mouse_click(254, 573)

def ClickSecondMon():
    time.sleep(0.1)
    wh.mouse_click(333, 558)

def ClickThirdMon():
    time.sleep(0.1)
    wh.mouse_click(412, 558)

def ClickMix():
    time.sleep(0.1)
    wh.mouse_click(478, 479)


def ClickMix_OK():
    time.sleep(0.1)
    wh.mouse_click(479, 526)
    time.sleep(0.1)
    wh.mouse_click(479, 526)

def ClickByeBye():
    
    
    x,y,_=oh.coorTemplateMatch(ScreenshotMain(),cv2.cvtColor(cv2.imread('./image/ByeBye.jpg',1),cv2.COLOR_RGB2GRAY),0.8)

    time.sleep(0.1)
    wh.mouse_click(x, y)
    time.sleep(0.1)
    wh.mouse_click(x, y)

def ClickByeBye_OK():
    x,y,_=oh.coorTemplateMatch(ScreenshotMain(),cv2.cvtColor(cv2.imread('./image/ByeByeOK.png',1),cv2.COLOR_RGB2GRAY),0.8)

    time.sleep(0.1)
    wh.mouse_click(x, y)
    time.sleep(0.1)
    wh.mouse_click(x, y)

def ClickImageSearch(main,template):
    x,y,_=oh.coorTemplateMatch(main,template,0.8)
    wh.mouse_click(x,y)

def GoAwayMonster():
    im,windowcor=wh.WindowCapture('MapleStory')
    mat = np.array(im)
    mat=cv2.cvtColor(mat,cv2.COLOR_RGB2GRAY)
    lock=cv2.imread('./image/Lock.jpg',0)


    w, h = lock.shape[::-1]

    # wh.mouse_click(245,727)
    # time.sleep(0.5)

    croprect=(500,690,70,80)
    crop=oh.subMat(mat,croprect)
    
    # cv2.imshow('123',crop)
    # cv2.waitKey(0)
    Template_Result=oh.bTemplateMatch(crop,lock,0.8)
    if Template_Result:
        print('Monster Locked')
        wh.mouse_Wheeel(245,727,'up',1)
        return False
    else :
        print('Monster Not locked')

    RightClickLatestMonseter()

    time.sleep(0.1)

    # ClickCapture(ByeBye)
    wh.mouse_click(500,583)

    # ClickCapture(OKButton)
    time.sleep(0.1)

    ClickOKButton()

    wh.key_input_enter()
    wh.mouse_Wheeel(245,727,'up',1)
    return True

def PlayWithMonster():
    im,windowcor=wh.WindowCapture('MapleStory')
    mat = np.array(im)
    mat=cv2.cvtColor(mat,cv2.COLOR_RGB2GRAY)
    lock=cv2.imread('Lock.jpg',0)


    w, h = lock.shape[::-1]

    # wh.mouse_click(245,727)
    # time.sleep(0.5)

    croprect=(500,690,70,60)
    crop=oh.subMat(mat,croprect)


    # Template_Result=oh.bTemplateMatch(crop,lock,0.8)
    # if Template_Result:
    #     print('Monster Locked')
    #     wh.mouse_Wheeel(245,727,'up',1)
    #     return False
    # else :
    #     print('Monster Not locked')


    wh.mouse_Rclick(520,720)
    time.sleep(0.1)

    # ClickCapture(ByeBye)
    wh.mouse_click(500,553)

    # ClickCapture(OKButton)
    time.sleep(0.1)
    wh.key_input_enter()
    time.sleep(0.1)
    wh.key_input_enter()
    wh.mouse_Wheeel(245,727,'up',1)
    return True

def MixSpecialMonster(monster):
    global isMonFull
    MonsterImage=cv2.cvtColor(monster,cv2.COLOR_RGB2GRAY)
    try:
        wh.mouse_move(1000,1000)
        x,y,_=oh.coorTemplateMatch(ScreenshotMain(),MonsterImage,0.8)
        wh.mouse_Rclick(x,y)
        time.sleep(0.3)
        wh.mouse_click(x,y-70)
        wh.key_input_enter()
        checkimage=cv2.cvtColor(cv2.imread('./image/Check_Exist.PNG',1),cv2.COLOR_RGB2GRAY)
        warning=cv2.cvtColor(cv2.imread('./image/warning.PNG',1),cv2.COLOR_RGB2GRAY)
        success=cv2.cvtColor(cv2.imread('./image/Check_Success.PNG',1),cv2.COLOR_RGB2GRAY)
        ScreenshotMain()
        if oh.bTemplateMatch(ScreenshotMain(),checkimage,0.8):
            ClickFirstMon()
            time.sleep(0.05)
            ClickMix()
            time.sleep(0.05)
            ScreenshotMain()
            if oh.bTemplateMatch(ScreenshotMain(),warning,0.8):
                isMonFull=True
                print('Full')
                return "FULL"

          
            wh.key_input_enter()
            wh.key_input_enter()

            time.sleep(3.5)
            ScreenshotMain()
            if oh.bTemplateMatch(ScreenshotMain(),success,0.8):
                wh.key_input_enter()
                ClickMix_OK()
                ClickByeBye()
                ClickByeBye_OK()
                wh.key_input_enter()
            else:
                wh.key_input_enter()
                ClickMix_OK()
                wh.key_input_enter()
                wh.key_input_enter()
    except:
        return False

def MixNormalMonster(MainMonster,index):
    MonsterImage=cv2.cvtColor(MainMonster,cv2.COLOR_RGB2GRAY)
    try:
        wh.mouse_move(1000,1000)
        x,y,_=oh.coorTemplateMatch(ScreenshotMain(),MonsterImage,0.8)
        wh.mouse_Rclick(x,y)
        time.sleep(0.3)
        wh.mouse_click(x,y-70)
        wh.key_input_enter()
        checkimage=cv2.cvtColor(cv2.imread('./image/Check_Exist.PNG',1),cv2.COLOR_RGB2GRAY)
        warning=cv2.cvtColor(cv2.imread('./image/warning.PNG',1),cv2.COLOR_RGB2GRAY)
        success=cv2.cvtColor(cv2.imread('./image/Check_Success.PNG',1),cv2.COLOR_RGB2GRAY)
        ScreenshotMain()
        if oh.bTemplateMatch(ScreenshotMain(),checkimage,0.8):
            if index ==1:
                ClickFirstMon()
                time.sleep(0.05)
            elif index ==2:
                ClickSecondMon()
                time.sleep(0.05)
            elif index==3:
                ClickThirdMon()
                time.sleep(0.05)
            else:
                return 
            ClickMix()
            time.sleep(0.05)
            ScreenshotMain()
            if oh.bTemplateMatch(ScreenshotMain(),warning,0.8):
                isMonFull=True
                print('Full')
                return "FULL"
            wh.key_input_enter()
            wh.key_input_enter()

            time.sleep(4.5)
            ScreenshotMain()
            if oh.bTemplateMatch(ScreenshotMain(),success,0.8):
                wh.key_input_enter()
                ClickMix_OK()
                ClickByeBye()
                ClickByeBye_OK()
                wh.key_input_enter()
            else:
                wh.key_input_enter()
                ClickMix_OK()
                wh.key_input_enter()
                wh.key_input_enter()
    except:
        return False

def OpenBox(ran):

    time.sleep(0.1)
    wh.mouse_click(158, 663)
    for i in range(ran):
        time.sleep(0.1)
        wh.mouse_click(190, 722)
        time.sleep(0.1)
        wh.key_input_enter()
        time.sleep(0.1)
        wh.key_input_enter()
        time.sleep(0.1)
        wh.key_input_enter()

def CheckSpecial(Monster):
    inv_key = {v: k for k, v in monster.monlist.items()}
    if inv_key[Monster] in monster.isSpecial:
        return True
    else:
        return False

monfilter=''

def MixMonsterSequence():
    existMon=CheckMonsterExist(monfilter.split(','))
    inv_key = {v: k for k, v in monster.monlist.items()}
    for i in existMon:
        for mon in monfilter.split(','):
            try:
                if mon=='':
                    break                
                if(monster.monlist[mon]==i):
                    # if CheckSpecial(i):
                    MixSpecialMonster(cv2.imread(i,1))
                    # else:
                        # MixNormalMonster(cv2.imread(i,1),monster.NormalMonster[inv_key[i]])
                else:
                    print('no'+ monfilter)
            except:
                print('No Monster')
    MixNextPage()

def GetMonsterList(monster):
    list=[]
    if wh.FileExist('./list/'+monster+'.txt'):
        return ReadMonsterFromFile(monster)
    else:
        for farmname in gf.GetFarmList(monster):
            if not CheckSSang(farmname):
                list.append(farmname)
        
        wh.FileWrite('./list/'+monster+'.txt',list)
        return list

def RemoveFinishedMonsterFromList(monster):
    list=ReadMonsterFromFile(monster)
    print(list[0]+' Removed')
    del list[0]
    wh.FileWrite('./list/'+monster+'.txt',list)
    return list

def RemoveFarmFromList(monster,FarmName):
    list=ReadMonsterFromFile(monster)
    print(FarmName+' Removed')
    del list[list.index(FarmName)]
    wh.FileWrite('./list/'+monster+'.txt',list)
    return list

def ReadMonsterFromFile(monster):
    return wh.FileRead('./list/'+monster+'.txt')

def CheckMonsterExist(monlist):
    list=[]
    wh.mouse_move(1000,500)
    im,windowcor=wh.WindowCapture('MapleStory')
    mat = np.array(im)
    mat=cv2.cvtColor(mat,cv2.COLOR_RGB2GRAY)
    croprect=(20, 697,600,120)
    crop=oh.subMat(mat,croprect)
    for i in monlist:
        if i=='':
            break
        mon=cv2.imread(monster.monlist[i],1)
        MonsterImage=cv2.cvtColor(mon,cv2.COLOR_RGB2GRAY)
        if oh.bTemplateMatch(crop,MonsterImage,0.8):
            list.append(monster.monlist[i])
    return list
        


def MoveToFarm(FarmName):
    wh.mouse_click(994,242)
    time.sleep(0.05)
    wh.mouse_click(780,760)
    time.sleep(0.05)
    wh.mouse_click(931, 588)
    time.sleep(0.1)
    text=wh.hangul_decompose(FarmName)
    wh.key_input_Type(wh.convertToEnglish(text))
    time.sleep(0.05)
    wh.key_input_enter()
    return True


def CheckSSang(FarmName):
    ssang=['ㅃ','ㅉ','ㄸ','ㄲ','ㅆ','ㅖ','ㅒ','ㄶ','ㄼ']
    text=wh.hangul_decompose(FarmName)
    for i in ssang:
        a=text.find(i)
        if a!=-1:
            return True
    return False



    

def main_play():
    InitSequence()
    count=0
    while count<10:
        PlayWithMonster()
        count+=1
    #RightClickMonster()
    print("Finish")
    
def GoAwayMain():
    im,windowcor=wh.WindowCapture('MapleStory')
    wh.mouse_click(45, 673)
    wh.mouse_Wheeel(245,727,'down',30)
    count=0
    while count<3:
        if not GoAwayMonster():
            count+=1
            print("Finish")

GoAwayFlag=False
MixMonsterFlag=False
MixFinished=False
GoAwayEvent=threading.Event()
MixMonsterEvent=threading.Event()
isMonFull=False

clicktest=False
clickEvent=threading.Event()
testx=0
testy=0
def ClickTest():
    try:
        global clicktest
        global clickEvent
        while(True):
            clickEvent=threading.Event()
            clickEvent.wait()
            if clicktest:
                wh.mouse_click(testx,testy)
                time.sleep(0.05)
                wh.mouse_click(testx,testy)
                clicktest=False
    except:
        ClickTest()

def GoAwayWhile():
    try:
        global GoAwayFlag
        global GoAwayEvent
        while(True):
            GoAwayEvent=threading.Event()
            GoAwayEvent.wait()
            if GoAwayFlag:
                GoAwayMain()
                GoAwayFlag=False
    except:
        GoAwayWhile()

def MixMonsterWhile():
    try:
        global MixMonsterFlag
        global MixMonsterEvent
        global MixFinished
        while(True):
            MixMonsterEvent=threading.Event()
            MixMonsterEvent.wait()
            if MixMonsterFlag:
                for i in range(4):
                    MixMonsterSequence()
                MixMonsterFlag=False
                MixFinished=True
    except:
        MixMonsterWhile()

GoAwayThread=threading.Thread(target=GoAwayWhile)
MixMonsterThread=threading.Thread(target=MixMonsterWhile)
test=threading.Thread(target=ClickTest)
GoAwayThread.start()
MixMonsterThread.start()
test.start()
# wh.mouse_click(245,727)   
# wh.mouse_Wheeel(245,727,'down',30)

#MixMonsterSequence()
#ScreenshotMain()
# MixMonsterSequence()


# if CheckSSang(ReadMonsterFromFile('월묘')[0]):
#     RemoveFinishedMonsterFromList('월묘')
# else :
#     MoveToFarm(ReadMonsterFromFile('월묘')[0])
#     RemoveFinishedMonsterFromList('월묘')

# wh.mouse_click(780,760)
# wh.key_input_Type('asd f')
# time.sleep(0.05)
# wh.mouse_click(931, 588)
# wh.SetClipboard('왓음왓업')
# time.sleep(1)
# wh.key_input_paste()
# wh.key_input_Type('Ehd')
# for i in range(3):
#     OpenBox(10)
#     main_play()
#     main()

#MixMonsterSequence()

# a,b =wh.WindowCapture("MapleStory")
# yetti = cv2.imread('mon_timer.PNG',1)
# mat=cv2.cvtColor(yetti,cv2.COLOR_RGB2GRAY)
# mmm=np.array(a)
# mmm=cv2.cvtColor(mmm,cv2.COLOR_RGB2GRAY)
# x,y,_=oh.coorTemplateMatch(mmm,mat,0.8)
# wh.mouse_Rclick(x,y)
# time.sleep(0.1)
# wh.mouse_click(x,y-70)
# wh.key_input_enter()
# ClickFirstMon()
# ClickMix()
# wh.key_input_enter()
# wh.key_input_enter()
# time.sleep(5)
# wh.key_input_enter()
# ClickMix_OK()
# wh.key_input_enter()
# wh.key_input_enter()

# wh.mouse_move(500,583)


# Image.fromarray(crop).save('OK.jpg')

# while True:
#     wh.print_mouse_position()

# #