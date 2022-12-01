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
    addroot.config(bg='blue')
    addroot.iconbitmap('mana.ico')
    addroot.resizable(False, False)
    # --------------------------------------------------- Add Customer Labels
    idlabel = Label(addroot, text='Enter Id : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Enter Name : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    # ----------------------------------------------------------- Add Customer Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()

    identry = Entry(addroot, font=('roman', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'),
                        bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    # ------------------------- add button
    submitbtn = Button(addroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue', activeforeground='white',
                       bg='red', command=submitadd)
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
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customertable.insert('', END, values=vv)
        elif (mobile != ''):
            strr = 'select *from customerdata1 where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            customertable.delete(*customertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customertable.insert('', END, values=vv)

            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customertable.insert('', END, values=vv)

        elif (addeddate != ''):
            strr = 'select *from customerdata1 where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            customertable.delete(*customertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customertable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Customer Management System')
    searchroot.config(bg='firebrick1')
    searchroot.iconbitmap('mana.ico')
    searchroot.resizable(False, False)
    # --------------------------------------------------- Add studenmt Labels
    idlabel = Label(searchroot, text='Enter Id : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    datelabel = Label(searchroot, text='Enter Date : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    # ----------------------------------------------------------- Add Customer Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('roman', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=(
        'roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)
    # ------------------------- add button
    submitbtn = Button(searchroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue', activeforeground='white',
                       bg='red', command=search)
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

        strr = 'update customerdata1 set name=%s,mobile=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr, (name, mobile,  time, id))
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
    updateroot.config(bg='firebrick1')
    updateroot.iconbitmap('mana.ico')
    updateroot.resizable(False, False)
    # --------------------------------------------------- Add Customer Labels
    idlabel = Label(updateroot, text='Enter Id : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    datelabel = Label(updateroot, text='Enter Date : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time : ', bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=490)

    # ----------------------------------------------------------- Add Customer Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()

    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'),
                    bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=(
        'roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=dateval)
    timeentry.place(x=250, y=490)
    # ------------------------- add button
    submitbtn = Button(updateroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue', activeforeground='white',
                       bg='red', command=update)
    submitbtn.place(x=150, y=540)
    cc = customertable.focus()
    content = customertable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])

        dateval.set(pp[7])
        timeval.set(pp[8])

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


# Connecttion of Database
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
    dbroot.config(bg='blue')
    # -------------------------------Connectdb Labels
    hostlabel = Label(dbroot, text="Enter Host : ", bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text="Enter User : ", bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password : ", bg='gold2', font=(
        'times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    # -------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'),
                      bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'),
                          bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    # -------------------------------- Connectdb button
    submitbutton = Button(dbroot, text='Submit', font=('roman', 15, 'bold'), bg='red', bd=5, width=20, activebackground='blue',
                          activeforeground='white', command=submitdb)
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()
###########################################


def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200, tick)


# INTRO SLIDER
colors = ['red', 'green', 'blue', 'yellow', 'pink', 'red2', 'gold2']


def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelColorTick)


def IntroLabelTick():
    global count, text
    if (count >= len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, IntroLabelTick)


##########################################################################################################
root = Tk()
root.title('Customer Management System')
root.config(bg='gold2')
root.geometry('1174x700+200+50')
root.iconbitmap('mana.ico')
root.resizable(False, False)
# Frames
# ---------------------------------------------------------------------------- dataentry frame

DataEntryFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=600)
frontlabel = Label(DataEntryFrame, text='--------------Welcome--------------',
                   width=30, font=('arial', 22, 'italic bold'), bg='gold2')
frontlabel.pack(side=TOP, expand=True)
addbtn = Button(DataEntryFrame, text='1. Add Customer', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3', activebackground='blue', relief=RIDGE,
                activeforeground='white', command=addcustomer)
addbtn.pack(side=TOP, expand=True)

searchbtn = Button(DataEntryFrame, text='2. Search Customer', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3', activebackground='blue', relief=RIDGE,
                   activeforeground='white', command=searchcustomer)
searchbtn.pack(side=TOP, expand=True)

deletebtn = Button(DataEntryFrame, text='3. Delete Customer', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3', activebackground='blue', relief=RIDGE,
                   activeforeground='white', command=deletecustomer)
deletebtn.pack(side=TOP, expand=True)

updatebtn = Button(DataEntryFrame, text='4. Update Customer', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3', activebackground='blue', relief=RIDGE,
                   activeforeground='white', command=updatecustomer)
updatebtn.pack(side=TOP, expand=True)

showallbtn = Button(DataEntryFrame, text='5. Show All', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3', activebackground='blue', relief=RIDGE,
                    activeforeground='white', command=showcustomer)
showallbtn.pack(side=TOP, expand=True)

exportbtn = Button(DataEntryFrame, text='6. Export data', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3', activebackground='blue', relief=RIDGE,
                   activeforeground='white', command=exportcustomer)
exportbtn.pack(side=TOP, expand=True)

exitbtn = Button(DataEntryFrame, text='7.  Exit', width=25, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3', activebackground='blue', relief=RIDGE,
                 activeforeground='white', command=exitcustomer)
exitbtn.pack(side=TOP, expand=True)

# -----------------------------------------------------------Show data frame
ShowDataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=550, y=80, width=620, height=600)

##-------------------------------------------------  Showdataframe
style = ttk.Style()
style.configure('Treeview.Heading', font=(
    'chiller', 20, 'bold'), foreground='blue')
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

# Slider
ss = 'Welcome To Customer Management System'
count = 0
text = ''
##################################
SliderLabel = Label(root, text=ss, font=(
    'chiller', 30, 'italic bold'), relief=RIDGE, borderwidth=4, width=35, bg='cyan')
SliderLabel.place(x=260, y=0)
IntroLabelTick()
IntroLabelColorTick()
# clock
clock = Label(root, font=('times', 14, 'bold'),
              relief=RIDGE, borderwidth=4, bg='lawn green')
clock.place(x=0, y=0)
tick()
# ConnectDatabaseButton
connectbutton = Button(root, text='Connect To Database', width=23, font=('chiller', 19, 'italic bold'), relief=RIDGE, borderwidth=4, bg='green2',
                       activebackground='blue', activeforeground='white', command=Connectdb)
connectbutton.place(x=930, y=0)
root.mainloop()
