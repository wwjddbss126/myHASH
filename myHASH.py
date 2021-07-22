# -*- coding : utf-8 -*-
import os, hashlib, sqlite3
from tkinter import *
from tkinter import messagebox as msg
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import *

def hashFile(file_path):
    f = open(file_path, 'rb')
    data = f.read()
    f.close()
    return hashlib.md5(data).hexdigest(), hashlib.sha1(data).hexdigest(), hashlib.sha256(data).hexdigest()

def selectFile(btn_select, label_select, label_hash):
    global file_path
    file_path = filedialog.askopenfilename(initialdir = "/",title = "choose your file")
    btn_select.configure(text='Selected')
    label_select.configure(text='File Path: %s'%file_path)
    label_hash.configure(text='MD5: %s\nSHA-1: %s\nSHA-256: %s'%(hashFile(file_path)[0], hashFile(file_path)[1], hashFile(file_path)[2]))
    return file_path

def findFile(hashType, hashValue, hashScope):
    
    if(hashType=='MD5'):
        return connDB(0, hashValue, hashScope)
    elif(hashType=='SHA-1'):
        return connDB(1, hashValue, hashScope)
    elif(hashType=='SHA-256'):
        return connDB(2, hashValue, hashScope)

def connDB(hashType, hashValue, hashScope):
    conn = sqlite3.connect('hash.db')
    cur = conn.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS hashTB
                (path text, value text)''')
    q = "INSERT INTO hashTB(path, value) VALUES (?, ?)"

    data = []

    for r, d, f in os.walk(hashScope):
        for file in f:
            target = os.path.join(r, file)
            data.append((target, hashFile(target)[hashType]))

    cur.executemany(q,data)
    cur.execute("SELECT * FROM hashTB WHERE value = ?", (hashValue, ))
    
    # 2eb7b66bd1d8005d746332575401ac5a
    # C:\Users\82107\Documents\카카오톡 받은 파일

    res = cur.fetchall()
    conn.close()
    
    if(hashType == 0):
        foundType = 'MD5'
    elif(hashType == 1):
        foundType = 'SHA-1'
    else:
        foundType = 'SHA-256'

    if(len(res) != 0):
        info = 'File Path: '+str(res[0][0])+'\nFile Hash: '+str(res[0][1])+foundType+'\n\nOpen Directory?'
        if(msg.askquestion("File Found!", info) == 'yes'):
            os.startfile(os.path.dirname(res[0][0]))
    else:
        msg.showwarning("File Not Found!", "Not Found with %s :("%foundType)
        
def gui():
    window = Tk()
    window.title("myHASH")
    window.iconbitmap('C:\\Users\82107\OneDrive - 서울여자대학교\BoB 10th\\01. BOB BI\\bob_bi_solid.ico')

    label_n1 = Label(window, text = '=========HASHING FILE=========')
    label_n1.grid(row=0, column=0, columnspan=2)

    btn_select = Button(window, text = "Select file to hash", command=lambda: selectFile(btn_select, label_select, label_hash))
    btn_select.grid(row=1, column =0, columnspan=2)
    
    label_select = Label(window, text = 'File: Not Selected!')
    label_select.grid(row=2, column=0, columnspan=2)

    label_hash = Label(window, text='Hash Value: Not Selected!')
    label_hash.grid(row=3, column=0, columnspan=2)

    label_n2 = Label(window, text = '=====FINDING FILE WITH HASH=====')
    label_n2.grid(row=4, column=0, columnspan=2)

    label_n3 = Label(window, text='Hash Type: ')
    label_n3.grid(row=5, column=0)

    typeCombo = ttk.Combobox(window, values=['MD5', 'SHA-1', 'SHA-256'], width = 15)
    typeCombo.current(0)
    typeCombo.grid(row=5, column=1)
    
    label_n4 = Label(window, text='Hash Value: ')
    label_n4.grid(row=6, column=0)

    hashValue = ttk.Entry(window, width = 25)
    hashValue.grid(row=6, column=1)

    label_n5 = Label(window, text='Dir. Scope (Recursively): ')
    label_n5.grid(row=7, column=0)

    hashScope = ttk.Entry(window, width = 25)
    hashScope.grid(row=7, column=1)

    btn_find = Button(window, text = "Find file with hash", command=lambda: findFile(typeCombo.get(), hashValue.get(), hashScope.get()))
    btn_find.grid(row=8, column =0, columnspan=2)

    window.mainloop()

def main():
    gui()

if __name__ == "__main__":
    main()