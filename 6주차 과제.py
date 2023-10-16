def insertdata():
    con,cur = None,None
    data1,data2,data3,data4 = "","","",""
    sql = ""
    con = sqlite3.connect("C:/Users/sam03/OneDrive/바탕 화면/2학기 프로그래밍/splite/sqlite-tools-win32-x86-3430100/naverDB")
    cur = con.cursor()

    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get(); data4 = edt4.get()
    try :
        sql = "INSERT INTO userTable VALUES('"+ data1 +"','"+ data2 +"','"+ data3 +"',"+ data4 +")"
        cur.execute(sql)
    except:
        messagebox.showerror('오류','데이터 입력 오류가 발생함')
    else :
        messagebox.showinfo('성공','데이터 입력 성공')
    con.commit()
    con.close()

def showdata():
    list_data1.delete(0, END)
    list_data2.delete(0, END)
    list_data3.delete(0, END)
    list_data4.delete(0, END)

    con = sqlite3.connect("C:/Users/sam03/OneDrive/바탕 화면/2학기 프로그래밍/splite/sqlite-tools-win32-x86-3430100/naverDB")
    cur = con.cursor()
    cur.execute("SELECT * FROM userTable")

    str_data1, str_data2, str_data3, str_data4 = [], [], [], []

    for row in cur.fetchall():
        str_data1.append(row[0])
        str_data2.append(row[1])
        str_data3.append(row[2])
        str_data4.append(row[3])

    for item1, item2, item3, item4 in zip(str_data1, str_data2, str_data3, str_data4):
        list_data1.insert(END, item1)
        list_data2.insert(END, item2)
        list_data3.insert(END, item3)
        list_data4.insert(END, item4)

    con.close()

import sqlite3

con = sqlite3.connect("C:\\Users\\sam03\\OneDrive\\바탕 화면\\2학기 프로그래밍\\splite\\sqlite-tools-win32-x86-3430100\\naverDB")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS userTable(id char(4), userName char(15), email char(15), birthyear int)")

while (True):
    data1 = input("사용자ID:")
    if data1=="":
        break
    data2 = input("사용자이름:")
    data3= input("이메일:")
    data4 = input("출생연도:")
    sql = "INSERT INTO userTable VALUES('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)

con.commit()
con.close()

import sqlite3
con,cur = None,None
data1,data2,data3,data4 = "","","",""
row = None

con = sqlite3.connect("C:/Users/sam03/OneDrive/바탕 화면/2학기 프로그래밍/splite/sqlite-tools-win32-x86-3430100/naverDB")
cur = con.cursor()
cur.execute("SELECT * FROM userTable")
print("사용자ID    사용자이름        이메일       출생연도")
print("----------------------------------------------------")

while True:
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s   %15s   %15s   %5s" % (data1,data2,data3,data4))
con.close()


import sqlite3
from tkinter import * 
from tkinter import messagebox
    
window = Tk()
window.title("GUI 데이터 입력")
edt_Frame = Frame(window)
edt_Frame.pack()
list_Frame = Frame(window)
list_Frame.pack(side = BOTTOM,fill = BOTH, expand=1)
edt1 = Entry(edt_Frame,width=10); edt1.pack(side=LEFT,padx=10,pady=10)
edt2 = Entry(edt_Frame,width=10); edt2.pack(side=LEFT,padx=10,pady=10)
edt3 = Entry(edt_Frame,width=10); edt3.pack(side=LEFT,padx=10,pady=10)
edt4 = Entry(edt_Frame,width=10); edt4.pack(side=LEFT,padx=10,pady=10)

button1 = Button(edt_Frame, text="입력",command= insertdata)
button1.pack(side=LEFT,padx=10,pady=10)
button2 = Button(edt_Frame,text="조회",command=showdata)
button2.pack(side=LEFT,padx=10,pady=10)

list_data1 = Listbox(list_Frame, bg = 'yellow')
list_data1.pack(side=LEFT, fill = BOTH, expand=1)
list_data2 = Listbox(list_Frame,bg = 'yellow')
list_data2.pack(side=LEFT, fill = BOTH, expand=1)
list_data3 = Listbox(list_Frame,bg = 'yellow')
list_data3.pack(side=LEFT, fill = BOTH, expand=1)
list_data4 = Listbox(list_Frame,bg = 'yellow')
list_data4.pack(side=LEFT, fill = BOTH, expand=1)

window.mainloop()
