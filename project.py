from tkinter import *
from tkinter import messagebox
from math import *
import sqlite3
conn = sqlite3.connect('mca.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS credits1 (
usno varchar(10) not null,
subcode varchar(10) not null,
fullname varchar(30),
q1 int(20),
q2 int(20),
q3 int(20),
q4 int(20),
t1 int(20),
t2 int(20),
assignment int(20)
)""")
#c.execute("DELETE FROM credits1");
#conn.commit()

    
usn=''
name=''
sub=''
q1credits=0
q2credits=0
q3credits=0
q4credits=0
t1credits=0
t2credits=0
assignmentcredits=0
fields = ('USN','SUBJECT CODE','NAME', 'QUIZ1','QUIZ2','QUIZ3','QUIZ4','TEST1','TEST2','ASSIGNMENT')
def convert(entries):
   
   usn = str(entries['USN'].get()).strip().upper()
   name= str(entries['NAME'].get()).strip().upper()
   sub= str(entries['SUBJECT CODE'].get()).strip().upper()
   q1= int(entries['QUIZ1'].get())
   q2= int(entries['QUIZ2'].get())
   q3= int(entries['QUIZ3'].get())
   q4= int(entries['QUIZ4'].get())
   t1= int(entries['TEST1'].get())
   t2= int(entries['TEST2'].get())
   assignmentcredits= int(entries['ASSIGNMENT'].get())

   q1credits=ceil((q1/15)*3)
   q2credits=ceil((q2/15)*3)
   q3credits=ceil((q3/15)*3)
   q4credits=ceil((q4/15)*3)
   t1credits=ceil((t1/50)*17)
   t2credits=ceil((t2/50)*17)
   total=q1credits+q2credits+q3credits+q4credits+t1credits+t2credits+assignmentcredits
   
   print("USN:",usn,"\nNAME:",name,"\nSUBJECT CODE:",sub,"\nQUIZ1 CREDITS",q1credits,"\nQUIZ2 CREDITS",q2credits,"\nQUIZ3 CREDITS",q3credits,"\nQUIZ4 CREDITS",q4credits,"\nTEST1 CREDITS",t1credits,"\nTEST2 CREDITS",t2credits,"\nASSIGNMENT CREDITS",assignmentcredits,"\n")
   print("TOTAL CREDITS=",total)
   c.execute("INSERT INTO credits1 values(?,?,?,?,?,?,?,?,?,?)",(usn,sub,name,q1credits,q2credits,q3credits,q4credits,t1credits,t2credits,assignmentcredits))
   conn.commit()
   
   
  
   

def search(entries):
 
   usn = str(entries['USN'].get()).strip().upper()
   name= str(entries['NAME'].get()).strip().upper()
   sub= str(entries['SUBJECT CODE'].get()).strip().upper()
   q1= int(entries['QUIZ1'].get())
   q2= int(entries['QUIZ2'].get())
   q3= int(entries['QUIZ3'].get())
   q4= int(entries['QUIZ4'].get())
   t1= int(entries['TEST1'].get())
   t2= int(entries['TEST2'].get())
   assignmentcredits= int(entries['ASSIGNMENT'].get())
   val=c.execute("select * from credits1 where usno=? AND subcode=?",(usn,sub)).fetchall()
   for j in val:
         print("\n\nUSN:",j[0])
         print("NAME:",j[2])
         print("SUBJECT CODE:",j[1])
         if(j[1]=="1NMCA01"):
            sub="FOUNDATION OF MATHEMATICS"
         elif(j[1]=="1NMCA02"):
            sub="SOFTWARE ENGINEERING"
         elif(j[1]=="1NMCA03"):
            sub="OPERATING SYSTEM AND UNIX"
         elif(j[2]=="1NMCA04"):
            sub="WEB APPLICATION PROGRAMMING"
         elif(j[1]=="1NMCA05"):
            sub="PROGRAMMING WITH PYTHON"
         elif(j[1]=="1NMCA06"):
            sub="PROGRAMMING WITH JAVA"
         elif(j[1]=="1NMCANC"):
            sub="BASIC PROGRAMMING"
         elif(j[1]=="HSS08"):
            sub="SOFT SKILLS"
         elif(j[1]=="1NMCACC"):
            sub="MOOC COURSE"
         else:
            sub=""
         print("SUBJECT:",sub)
         print("QUIZ1 CREDITS:",j[3])
         print("QUIZ2 CREDITS:",j[4])
         print("QUIZ3 CREDITS:",j[5])
         print("QUIZ4 CREDITS:",j[6])
         print("TEST1 CREDITS:",j[7])
         print("TEST2 CREDITS:",j[8])
         print("ASSIGNMENT CREDITS:",j[9])
         print()
         tc=j[3]+j[4]+j[5]+j[6]+j[7]+j[8]+j[9]
         print("TOTAL CREDITS=",tc)
         if(tc<25):
            messagebox.showwarning("Low credits warning","you are not eligible for the exam since your credits is less tha 25")
            messagebox.showwarning("credits",tc)
            

         print()
         print()
         print()
         print()
         
      
def showdata():
   val=c.execute("select * from credits1").fetchall()
   for j in val:
         print("\n\nUSN:",j[0])
         print("NAME:",j[2])
         print("SUBJECT CODE:",j[1])
         if(j[1]=="1NMCA01"):
            sub="FOUNDATION OF MATHEMATICS"
         elif(j[1]=="1NMCA02"):
            sub="SOFTWARE ENGINEERING"
         elif(j[1]=="1NMCA03"):
            sub="OPERATING SYSTEM AND UNIX"
         elif(j[2]=="1NMCA04"):
            sub="WEB APPLICATION PROGRAMMING"
         elif(j[1]=="1NMCA05"):
            sub="PROGRAMMING WITH PYTHON"
         elif(j[1]=="1NMCA06"):
            sub="PROGRAMMING WITH JAVA"
         elif(j[1]=="1NMCANC"):
            sub="BASIC PROGRAMMING"
         elif(j[1]=="HSS08"):
            sub="SOFT SKILLS"
         elif(j[1]=="1NMCACC"):
            sub="MOOC COURSE"
         else:
            sub=""
         print("SUBJECT:",sub)
         print("QUIZ1 CREDITS:",j[3])
         print("QUIZ2 CREDITS:",j[4])
         print("QUIZ3 CREDITS:",j[5])
         print("QUIZ4 CREDITS:",j[6])
         print("TEST1 CREDITS:",j[7])
         print("TEST2 CREDITS:",j[8])
         print("ASSIGNMENT CREDITS:",j[9])
         print()
         tc=j[3]+j[4]+j[5]+j[6]+j[7]+j[8]+j[9]
         print("TOTAL CREDITS=",tc)
        
   
   
   
def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent
   return entries
if __name__ == '__main__':
   root = Tk()
   root.title("SIT MCA CREDITS MANAGEMENT SYSTEM")
   l=Label(root,text="SIT MCA CREDITS MANAGEMENT SYSTEM",fg="black",bg="yellow",width=50,height=2,font=('arial',10))
   l.pack()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e = ents: fetch(e)))
   b1 = Button(root, text = 'SEARCH',
      command=(lambda e = ents: search(e)),bg="black",fg="yellow")
   b1.pack(side = LEFT, padx = 5, pady = 10)
   b2 = Button(root, text='ADD CREDITS',
   command=(lambda e = ents: convert(e)),bg="black",fg="yellow")
   b2.pack(side = LEFT, padx = 5, pady = 10)
   b4 = Button(root, text = 'SHOW DATABASE', command = showdata,bg="black",fg="yellow")
   b4.pack(side = LEFT, padx = 5, pady = 10)
   b3 = Button(root, text = 'EXIT', command = root.destroy,bg="black",fg="yellow")
   b3.pack(side = LEFT, padx = 5, pady = 10)
   root.mainloop()
   c.close()
