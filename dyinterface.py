from tkinter import *
import sqlite3
#connect to table insid database
con = sqlite3.connect('warehouse.db')
cursor = con.cursor()
cursor.execute("SELECT * FROM sheet1;") 
rows = cursor.fetchall()
root = Tk()
#test the connection
#for row in rows:
#    print (row)
# count then number of columns
numbercolumns = (len(rows[0]))
numberows = (len(rows))
height = numberows
width = numbercolumns

#the main formm: main interface for log in onhter windows
class Welcome():
    def __init__(self,master):
        self.master = master
        #defind shap and position of windows
        self.master.geometry('500x500+500+100')
        self.master.title('warehouse!')
        self.label1=Label(self.master,text='Test Database Main Menu',fg='red').grid(row=0,column=1)
        self.button1=Button(self.master,text="Enter Data",fg='green',command=self.gotodataentry).grid(row=1,column=1)
        self.button2=Button(self.master,text="Exit",fg='red',command=self.exit).grid(row=3,column=1)       
    def exit(self):
        self.master.destroy()
    def gotodataentry(self):    
        myGUI=DataEntry(root)

#the record form: showing the table in tkinter#
class DataEntry():
    def __init__(self,master):
        self.master = master
        self.master.geometry('250x200+100+200')
        self.master.title('Data Entry')
        for i in range(height): #Rows
            for j in range(width): #Columns
                text_var = StringVar()
                        # here we are setting cell text value
                text_var.set('%s%s' % (i, j)) 
                b = Entry(root, text="")
                b.grid(row=i, column=j)
    #first name of columns equal name of table columns

    #the field of each row in plance in coumns
    #select_table()
    #mainloop()
# to start main window
def main():
     myGUIWelcome=Welcome(root)
     root.mainloop()

if __name__ == '__main__':
     main()