import cv2
import numpy as np

def imRead(loc,mode):
    type=''
    if(mode=='Gray'):
        type=cv2.IMREAD_GRAYSCALE
    elif(mode=='Color'):
        type=cv2.IMREAD_ANYCOLOR
    else:
        type=cv2.IMREAD_ANYCOLOR

    return cv2.imread(loc,type)

def subMat(img, rect):
    x=rect[0]
    y=rect[1]
    width=rect[2]
    height=rect[3]
    crop=img[y:y+height,x:x+width]
    return crop

def coorTemplateMatch(img,tmp,threshold):
    res = cv2.matchTemplate(img,tmp,cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
    loc = np.where(res >= threshold) #좌표값 따기
    w, h = tmp.shape[::-1]
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2) #박스표시하기
        result_X=pt[0]
        result_Y=pt[1]
        return result_X,result_Y,img



def bTemplateMatch(img,tmp,threshold):
    try:
        res = cv2.matchTemplate(img,tmp,cv2.TM_CCOEFF_NORMED)
    except:
        tmp=cv2.cvtColor(tmp,cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(img,tmp,cv2.TM_CCOEFF_NORMED)


    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
    threshold = 0.8
    #loc = np.where(res >= threshold) #좌표값 따기
    #for pt in zip(*loc[::-1]):
    #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2) #박스표시하기
    return True if maxVal>threshold else False

def Resize(img,mul):
    resize=cv2.resize(img, dsize=(0, 0), fx=mul, fy=mul, interpolation=cv2.INTER_LINEAR)
    return resize
    
def Sharpening(img,mode,arg):
    sharpening_mask1 = np.array([[-1, -1, -1], [-1, arg, -1], [-1, -1, -1]]) 
    sharpening_mask2 = np.array([[0, -1, 0], [-1, arg, -1], [0, -1, 0]])
    sharpening_out1 = cv2.filter2D(img, -1, sharpening_mask1) 
    sharpening_out2 = cv2.filter2D(img, -1, sharpening_mask2)
    if mode==1:
        return sharpening_out1
    else:
        return sharpening_out2