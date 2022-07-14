import win32api,win32con,win32gui,win32process,win32clipboard,win32com,win32com.client,win32timezone
from PIL import Image, ImageGrab
import time
from pynput.keyboard import Key, Controller
import hgtk
from ctypes import windll

import ctypes


def hangul_compose(text):
    return hgtk.text.compose(text)

def hangul_decompose(text):
    return hgtk.text.decompose(text,compose_code='')

def Set_Keyboard_Language():
    time.sleep(0.1)
    win32api.keybd_event(15,0,0,0)     # enter
    win32api.keybd_event(15,0,win32con.KEYEVENTF_KEYUP,0)  # Release the button 

def get_keyboard_language():
    languages = {'0x409' : "English - United States", '0x809' : "English - United Kingdom", '0x0c09' : "English - Australia", '0x2809' : "English - Belize",
                 '0x1009' : "English - Canada", '0x2409' : "English - Caribbean", '0x3c09' : "English - Hong Kong SAR", '0x4009' : "English - India", '0x3809' : "English - Indonesia",
                 '0x1809' : "English - Ireland", '0x2009' : "English - Jamaica", '0x4409' : "English - Malaysia", '0x1409' : "English - New Zealand", '0x3409' : "English - Philippines",
                 '0x4809' : "English - Singapore", '0x1c09' : "English - South Africa", '0x2c09' : "English - Trinidad", '0x3009' : "English - Zimbabwe", '0x425' : "Estonian",
                 '0x412' : "Korean", '0x440' : "Kyrgyz (Cyrillic)", '0x454' : "Lao", '0x476' : "Latin", '0x426' : "Latvian", '0x427' : "Lithuanian", '0x043e' : "Malay - Malaysia",
                 '0x083e' : "Malay - Brunei Darussalam", '0x044c' : "Malayalam", '0x043a' : "Maltese", '0x458' : "Manipuri", '0x481' : "Maori - New Zealand", '0x044e' : "Marathi",
                 '0x450' : "Mongolian (Cyrillic)", '0x850' : "Mongolian (Mongolian)", '0x461' : "Nepali", '0x861' : "Nepali - India", '0x414' : "Norwegian (Bokmål)", 
                 '0x814' : "Norwegian (Nynorsk)", '0x448' : "Oriya", '0x472' : "Oromo", '0x479' : "Papiamentu", '0x463' : "Pashto", '0x415' : "Polish", '0x416' : "Portuguese - Brazil",
                 '0x816' : "Portuguese - Portugal", '0x446' : "Punjabi", '0x846' : "Punjabi (Pakistan)", '0x046B' : "Quecha - Bolivia", '0x086B' : "Quecha - Ecuador", 
                 '0x0C6B' : "Quecha - Peru", '0x417' : "Rhaeto-Romanic", '0x418' : "Romanian", '0x818' : "Romanian - Moldava", '0x419' : "Russian", '0x819' : "Russian - Moldava",
                 '0x043b' : "Sami (Lappish)", '0x044f' : "Sanskrit", '0x046c' : "Sepedi", '0x0c1a' : "Serbian (Cyrillic)", '0x081a' : "Serbian (Latin)", '0x459' : "Sindhi - India",
                 '0x859' : "Sindhi - Pakistan", '0x045b' : "Sinhalese - Sri Lanka", '0x041b' : "Slovak", '0x424' : "Slovenian", '0x477' : "Somali", '0x042e' : "Sorbian", 
                 '0x0c0a' : "Spanish - Spain (Modern Sort)", '0x040a' : "Spanish - Spain (Traditional Sort)", '0x2c0a' : "Spanish - Argentina", '0x400a' : "Spanish - Bolivia",
                 '0x340a' : "Spanish - Chile", '0x240a' : "Spanish - Colombia", '0x140a' : "Spanish - Costa Rica", '0x1c0a' : "Spanish - Dominican Republic", 
                 '0x300a' : "Spanish - Ecuador", '0x440a' : "Spanish - El Salvador", '0x100a' : "Spanish - Guatemala", '0x480a' : "Spanish - Honduras", '0xe40a' : "Spanish - Latin America",
                 '0x080a' : "Spanish - Mexico", '0x4c0a' : "Spanish - Nicaragua", '0x180a' : "Spanish - Panama", '0x3c0a' : "Spanish - Paraguay", '0x280a' : "Spanish - Peru",
                 '0x500a' : "Spanish - Puerto Rico", '0x540a' : "Spanish - United States", '0x380a' : "Spanish - Uruguay", '0x200a' : "Spanish - Venezuela", '0x430' : "Sutu",
                 '0x441' : "Swahili", '0x041d' : "Swedish", '0x081d' : "Swedish - Finland", '0x045a' : "Syriac", '0x428' : "Tajik", '0x045f' : "Tamazight (Arabic)", 
                 '0x085f' : "Tamazight (Latin)", '0x449' : "Tamil", '0x444' : "Tatar", '0x044a' : "Telugu", '0x041e' : "Thai", '0x851' : "Tibetan - Bhutan", 
                 '0x451' : "Tibetan - People's Republic of China", '0x873' : "Tigrigna - Eritrea", '0x473' : "Tigrigna - Ethiopia", '0x431' : "Tsonga", '0x432' : "Tswana",
                 '0x041f' : "Turkish", '0x442' : "Turkmen", '0x480' : "Uighur - China", '0x422' : "Ukrainian", '0x420' : "Urdu", '0x820' : "Urdu - India", '0x843' : "Uzbek (Cyrillic)",
                 '0x443' : "Uzbek (Latin)", '0x433' : "Venda", '0x042a' : "Vietnamese", '0x452' : "Welsh", '0x434' : "Xhosa", '0x478' : "Yi", '0x043d' : "Yiddish", '0x046a' : "Yoruba",
                 '0x435' : "Zulu", '0x04ff' : "HID (Human Interface Device)"
                 }

    user32 = ctypes.WinDLL('user32', use_last_error=True)

    # Get the current active window handle
    handle =  win32gui.FindWindow(None, 'MapleStory')

    # Get the thread id from that window handle
    threadid = user32.GetWindowThreadProcessId(handle, 0)

    # Get the keyboard layout id from the threadid
    layout_id = user32.GetKeyboardLayout(threadid)

    # Extract the keyboard language id from the keyboard layout id
    language_id = layout_id & (2 ** 16 - 1)

    # Convert the keyboard language id from decimal to hexadecimal
    language_id_hex = hex(language_id)

    # Check if the hex value is in the dictionary.
    if language_id_hex in languages.keys():
        return languages[language_id_hex]

def convertToEnglish(word):
    result=[]
    key={'a':'ㅁ','q':'ㅂ','w':'ㅈ','e':'ㄷ','r':'ㄱ','t':'ㅅ','y':'ㅛ','u':'ㅕ','i':'ㅑ','o':'ㅐ',
    'p':'ㅔ','a':'ㅁ','s':'ㄴ','d':'ㅇ','f':'ㄹ','g':'ㅎ','h':'ㅗ','j':'ㅓ','k':'ㅏ'
    ,'l':'ㅣ','z':'ㅋ','x':'ㅌ','c':'ㅊ','v':'ㅍ','b':'ㅠ','n':'ㅜ','m':'ㅡ',
    'hk':'ㅘ','fr':'ㄺ','nj':'ㅝ','ml':'ㅢ','hl':'ㅚ','nl':'ㅟ','ho':'ㅙ',
    'np':'ㅞ','sh':'ㄶ','qt':'ㅄ','fa':'ㄻ','fh':'ㅀ','rt':'ㄳ'}
    inv_key = {v: k for k, v in key.items()}
    for i in list(word):
        result.append(inv_key[i])
    return "".join(result)


user32 = windll.user32
user32.SetProcessDPIAware()
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('%')

def SetClipboard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.SetClipboardText(text,win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

    
def FileExist(filename):
    return win32api.FindFiles(filename)


def FileWrite(filename,data):
    f = open(filename, 'w',encoding='utf8')
    for i in data:
        sData = i
        f.write(sData+'\n')
    f.close()
    
def FileRead(filename):
    f = open(filename, 'r',encoding='utf8')
    list=[]
    for i in f:
        list.append(i[:-1])
    f.close()
    return list

def SetFocus(handle):

    win32gui.SetFocus(handle)

def mouse_move(x,y):
    pos = (x, y)
    win32api.SetCursorPos(pos)

def mouse_click(x, y):

    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def mouse_Rclick(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

def mouse_Wheeel(x,y,up,count):
    win32api.SetCursorPos((x, y))
    for i in range(count):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, win32con.WHEEL_DELTA if up=="up" else -win32con.WHEEL_DELTA , 0)
        time.sleep(0.02)

def key_input_enter():
    time.sleep(0.1)
    win32api.keybd_event(13,0,0,0)     # enter
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)  # Release the button 

def key_input_Type(FarmName):
    time.sleep(0.1)
    a= Controller()
    a.type(FarmName)

    # win32api.keybd_event(0x11, 0, 0, 0)
    # win32api.keybd_event(0x56, 0, 0, 0)
    # win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    # win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    #paste



def print_mouse_position():
    pos = win32api.GetCursorPos()
    print(pos)

def SetForeground(handle):
    win32gui.SetForegroundWindow(handle)

def WindowCapture(window_name):
    global globalx
    global globaly
    win_name=window_name # 창이름
    hWnd = win32gui.FindWindow(None, win_name)
    remote_thread, _ = win32process.GetWindowThreadProcessId(hWnd)
    win32process.AttachThreadInput(win32api.GetCurrentThreadId(), remote_thread, True)
    prev_handle = SetFocus(hWnd)
    SetForeground(hWnd)
    SetFocus(hWnd)
    windowcor = win32gui.GetWindowRect(hWnd)
    # im = ImageGrab.grab() # 전체화면 캡쳐
    #windowcor=(int(windowcor[0]*1.5),int(windowcor[1]*1.5),int(windowcor[2]*1.5),int(windowcor[3]*1.5))

    im = ImageGrab.grab(windowcor) # 창 캡쳐
    globalx=windowcor[1]
    globaly=windowcor[0]
    im.save('test.jpg','JPEG')
    return im,windowcor

def SetFocusNew(window_name):
    win_name=window_name # 창이름
    hWnd = win32gui.FindWindow(None, win_name)
    remote_thread, _ = win32process.GetWindowThreadProcessId(hWnd)
    win32process.AttachThreadInput(win32api.GetCurrentThreadId(), remote_thread, True)
    prev_handle = SetFocus(hWnd)
    SetForeground(hWnd)
    SetFocus(hWnd)
    windowcor = win32gui.GetWindowRect(hWnd)
    globalx=windowcor[0]
    globaly=windowcor[1]