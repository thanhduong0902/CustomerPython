from tkinter import Toplevel, messagebox, filedialog
import time
import pymysql
import pandas
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import *
import random


def addcustomer():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()

        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into customerdata1 values(%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel(
                'Notificatrions', 'Id {} Name {} Added sucessfully.. and want to clean the form'.format(id, name), parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')

        except:
            messagebox.showerror(
                'Notifications', 'Id Already Exist try another id...', parent=addroot)
        strr = 'select * from customerdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        customertable.delete(*customertable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            customertable.insert('', END, values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Customer Management System')
    addroot.config(bg='#FCF3CF')
    addroot.iconbitmap('mana.ico')
    addroot.resizable(False, False)
    # --------------------------------------------------- Add Customer Labels
    idlabel = Label(addroot, text='Enter Id : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Enter Name : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    # ----------------------------------------------------------- Add Customer Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()

    identry = Entry(addroot, font=('times', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('times', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('times', 15, 'bold'),
                        bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    # ------------------------- add button
    submitbtn = Button(addroot, text='Submit', font=('times', 15, 'bold'), width=20, bd=5, activebackground='#D1F2EB',
                       bg='#F5EEF8', command=submitadd)
    submitbtn.place(x=150, y=420)

    addroot.mainloop()


def searchcustomer():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()

        addeddate = time.strftime("%d/%m/%Y")
        if (id != ''):
            strr = 'select *from customerdata1 where id=%s'
            mycursor.execute(strr, (id))
            datas = mycursor.fetchall()
            customertable.delete(*customertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                customertable.insert('', END, values=vv)
        elif (name != ''):
            strr = 'select *from customerdata1 where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            customertable.delete(*customertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                customertable.insert('', END, values=vv)
        elif (mobile != ''):
            strr = 'select *from customerdata1 where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            customertable.delete(*customertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                customertable.insert('', END, values=vv)

            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                customertable.insert('', END, values=vv)

        elif (addeddate != ''):
            strr = 'select *from customerdata1 where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            customertable.delete(*customertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                customertable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Customer Management System')
    searchroot.config(bg='#FCF3CF')
    searchroot.iconbitmap('mana.ico')
    searchroot.resizable(False, False)
    # --------------------------------------------------- Add studenmt Labels
    idlabel = Label(searchroot, text='Enter Id : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    datelabel = Label(searchroot, text='Enter Date : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=190)

    # ----------------------------------------------------------- Add Customer Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('times', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('times', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=(
        'times', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    dateentry = Entry(searchroot, font=('times', 15, 'bold'),
                      bd=5, textvariable=dateval)
    dateentry.place(x=250, y=190)
    # ------------------------- add button
    submitbtn = Button(searchroot, text='Submit', font=('times', 15, 'bold'), width=20, bd=5, activebackground='#D1F2EB',
                       bg='#F5EEF8', command=search)
    submitbtn.place(x=150, y=480)

    searchroot.mainloop()


def deletecustomer():
    cc = customertable.focus()
    content = customertable.item(cc)
    pp = content['values'][0]
    strr = 'delete from customerdata1 where id=%s'
    mycursor.execute(strr, (pp))
    con.commit()
    messagebox.showinfo(
        'Notifications', 'Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from customerdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    customertable.delete(*customertable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4]]
        customertable.insert('', END, values=vv)


def updatecustomer():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()

        time = timeval.get()
        date = dateval.get()
        strr = 'update customerdata1 set name=%s,mobile=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr, (name, mobile, date,  time, id))
        con.commit()
        messagebox.showinfo(
            'Notifications', 'Id {} Modified sucessfully...'.format(id), parent=updateroot)
        strr = 'select *from customerdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        customertable.delete(*customertable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            customertable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Customer Management System')
    updateroot.config(bg='#FCF3CF')
    updateroot.iconbitmap('mana.ico')
    updateroot.resizable(False, False)
    # --------------------------------------------------- Add Customer Labels
    idlabel = Label(updateroot, text='Enter Id : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    datelabel = Label(updateroot, text='Enter Date : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=190)

    timelabel = Label(updateroot, text='Enter Time : ', bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=250)

    # ----------------------------------------------------------- Add Customer Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()

    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('times', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('times', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=(
        'times', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    dateentry = Entry(updateroot, font=('times', 15, 'bold'),
                      bd=5, textvariable=dateval)
    dateentry.place(x=250, y=190)

    timeentry = Entry(updateroot, font=('times', 15, 'bold'),
                      bd=5, textvariable=timeval)
    timeentry.place(x=250, y=250)
    # ------------------------- add button
    submitbtn = Button(updateroot, text='Submit', font=('times', 15, 'bold'), width=20, bd=5, activebackground='#D1F2EB',
                       bg='#F5EEF8', command=update)
    submitbtn.place(x=150, y=540)
    cc = customertable.focus()
    content = customertable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        dateval.set(pp[3])
        timeval.set(pp[4])

    updateroot.mainloop()


def showcustomer():
    strr = 'select *from customerdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    customertable.delete(*customertable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4]]
        customertable.insert('', END, values=vv)


def exportcustomer():
    ff = filedialog.asksaveasfilename()
    gg = customertable.get_children()
    id, name, mobile,  addeddate, addedtime = [
    ], [], [], [], []
    for i in gg:
        content = customertable.item(i)
        pp = content['values']
        id.append(pp[0]), name.append(pp[1]), mobile.append(
            pp[2]),  addeddate.append(pp[3]), addedtime.append(pp[4])
    dd = ['Id', 'Name', 'Mobile',  'Added Date', 'Added Time']
    df = pandas.DataFrame(
        list(zip(id, name, mobile, addeddate, addedtime)), columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo(
        'Notifications', 'Customer data is Saved {}'.format(paths))


def exitcustomer():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if (res == True):
        root.destroy()


# Connecttion of Database---------------------------------------------------------------------------------------------------------------------------------
def Connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror(
                'Notifications', 'Data is incorrect please try again', parent=dbroot)
            return
        try:
            strr = 'create database Customermanagementsystem1'
            mycursor.execute(strr)
            strr = 'use Customermanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table customerdata1(id int,name varchar(20),mobile varchar(12),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table customerdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table customerdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo(
                'Notification', 'database created and now you are connected connected to the database ....', parent=dbroot)

        except:
            strr = 'use Customermanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo(
                'Notification', 'Now you are connected to the database ....', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('mana.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='#FCF3CF')
    # -------------------------------Connectdb Labels
    hostlabel = Label(dbroot, text="Enter Host : ", bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text="Enter User : ", bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password : ", bg='#F5EEF8', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    # -------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('times', 15, 'bold'),
                      bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('times', 15, 'bold'),
                      bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('times', 15, 'bold'),
                          bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    # -------------------------------- Connectdb button
    submitbutton = Button(dbroot, text='Submit', font=('times', 15, 'bold'), bg='#F5EEF8', bd=5, width=20, activebackground='#D1F2EB',
                          command=submitdb)
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()
# ---------------------------------------------------------------------------


def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200, tick)


##########################################################################################################
root = Tk()
root.title('Customer Management System')
root.config(bg='#FCF3CF')
root.geometry('1430x700+200+50')
root.iconbitmap('mana.ico')
root.resizable(False, False)
# Frames
# ---------------------------------------------------------------------------- dataentry frame

DataEntryFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=600)

addbtn = Button(DataEntryFrame, text='Add Customer', width=25, font=('times', 15, 'bold'), bd=6, bg='#F5EEF8', activebackground='#E8F6F3', relief=RIDGE,
                command=addcustomer)
addbtn.pack(side=TOP, expand=True)

searchbtn = Button(DataEntryFrame, text='Search Customer', width=25, font=('times', 15, 'bold'), bd=6, bg='#F5EEF8', activebackground='#E8F6F3', relief=RIDGE,
                   command=searchcustomer)
searchbtn.pack(side=TOP, expand=True)

deletebtn = Button(DataEntryFrame, text='Delete Customer', width=25, font=('times', 15, 'bold'), bd=6, bg='#F5EEF8', activebackground='#E8F6F3', relief=RIDGE,
                   command=deletecustomer)
deletebtn.pack(side=TOP, expand=True)

updatebtn = Button(DataEntryFrame, text='Update Customer', width=25, font=('times', 15, 'bold'), bd=6, bg='#F5EEF8', activebackground='#E8F6F3', relief=RIDGE,
                   command=updatecustomer)
updatebtn.pack(side=TOP, expand=True)

showallbtn = Button(DataEntryFrame, text='Show All', width=25, font=('times', 15, 'bold'), bd=6, bg='#F5EEF8', activebackground='#E8F6F3', relief=RIDGE,
                    command=showcustomer)
showallbtn.pack(side=TOP, expand=True)

exportbtn = Button(DataEntryFrame, text='Export data', width=25, font=('times', 15, 'bold'), bd=6, bg='#F5EEF8', activebackground='#E8F6F3', relief=RIDGE,
                   command=exportcustomer)
exportbtn.pack(side=TOP, expand=True)

exitbtn = Button(DataEntryFrame, text='Exit', width=25, font=('times', 15, 'bold'), bd=6, bg='#F5EEF8', activebackground='#E8F6F3', relief=RIDGE,
                 command=exitcustomer)
exitbtn.pack(side=TOP, expand=True)

# -----------------------------------------------------------Show data frame
ShowDataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=550, y=80, width=870, height=600)

##-------------------------------------------------  Showdataframe
style = ttk.Style()
style.configure('Treeview.Heading', font=(
    'times', 15, 'bold'), foreground='#283747')
style.configure('Treeview', font=('times', 15, 'bold'),
                background='cyan', foreground='black')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
customertable = Treeview(ShowDataFrame, columns=('Id', 'Name', 'Mobile No', 'Added Date', 'Added Time'),
                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=customertable.xview)
scroll_y.config(command=customertable.yview)
customertable.heading('Id', text='Id')
customertable.heading('Name', text='Name')
customertable.heading('Mobile No', text='Mobile No')

customertable.heading('Added Date', text='Added Date')
customertable.heading('Added Time', text='Added Time')
customertable['show'] = 'headings'
customertable.column('Id', width=100)
customertable.column('Name', width=200)
customertable.column('Mobile No', width=200)

customertable.column('Added Date', width=150)
customertable.column('Added Time', width=150)
customertable.pack(fill=BOTH, expand=1)


# clock
clock = Label(root, font=('times', 14, 'bold'),
              relief=RIDGE, borderwidth=4, bg='#FADBD8')
clock.place(x=10, y=0)
tick()
# ConnectDatabaseButton
connectbutton = Button(root, text='Connect To Database', width=23, font=('times', 13, 'italic bold'), relief=RIDGE, borderwidth=4, bg='#FADBD8',
                       activebackground='#A3E4D7', command=Connectdb)
connectbutton.place(x=1170, y=0)
root.mainloop()
