# print("hello ")
from tkinter import *
import pandas as pd 
file =Tk()#file 
file.geometry("500x500")#create page geometry  


def getvals():
    result = [namevalue.get(),phonevalue.get(),gendervalue.get(),payment_modeentry.get()]
    data = pd.DataFrame({'Name':[result[0]], 'Phone Number': [result[1]], 'Gender': [result[2]],'Payment Mode': [result[2]]})
    data.to_excel('amit.xlsx', index=False)


#  HEADING USING LABLE AND GRID FUNCTION 
Label(file ,text="Python Registration Form",font="ar 15 bold").grid(row=0,column=3)# we use it for writing hadding in root file 

#  FEILD NAME 

name =Label(file,text="Name",font="ar 15 bold")
phone =Label(file,text="Phone",font="ar 15 bold")
gender =Label(file,text="Gender",font="ar 15 bold")
payment_mode =Label(file,text="Payment_mode",font="ar 15 bold")

# PACKING FEILD  FROM DATA 
name.grid(row=1, column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
payment_mode.grid(row=4,column=2)

#  storing values in field 

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
payment_modevalue=StringVar()
checkvalue=IntVar()

# for entering  the values 


nameentry = Entry(file, textvariable=namevalue)
phoneentry = Entry(file, textvariable=phonevalue)
genderentry = Entry(file, textvariable=gendervalue)
payment_modeentry = Entry(file, textvariable=payment_modevalue)


# PAKING ENTRY FEILD 

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
payment_modeentry.grid(row=4,column=3)


#  CREATING CHELK BOX 
Checkbtn= Checkbutton(text ="remember me ?" )
Checkbtn.grid(row=8,column=3)

# submit button 

submit=Button(text="Submit ",command=getvals)
submit.grid(row=9,column=2)

# reset button
reset=Button(text="Reset  ")
reset.grid(row=9,column=5)

list1 = Listbox(file,height=6,width=35)
list1.grid(row=10,column=3,rowspan=6,columnspan=2)

file.mainloop()