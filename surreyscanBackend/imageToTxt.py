from PIL import Image
import pytesseract
import time
import cv2
global imageToConvert
import sqlite3
from sqlite3 import Error
from PIL import Image
# URN = int()
# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()

def KeyVerify(filename):
    URN = int()
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    text = pytesseract.image_to_string(Image.open(filename))

    listNum = []
    listURN = []
    strURN = ''

    for char in text:
        if char.isdigit():
            listNum.append(char) #if is an integer then appends to listNum

    for i in range(0, 7):
        listURN.append(listNum[i]) #First 7 numbers on card

    for i in listURN:
        strURN = str(strURN) +str(i) #adds the numbers to a string

    URN = int(strURN) #converts the string to an int

    key = URN
    cursor.execute("SELECT rowid FROM keys WHERE key = ?", (key,))
    data=cursor.fetchall()
    if len(data)==0:
        print('There is no ID number named %s' %key)
        return False
    else:
        print('ID Number %s is verified' %key)
        return True
