from tkinter import *
from tkinter import ttk
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import datetime
from main import answer

x = datetime.datetime.now()
x=str(x.strftime("%c"))
x1=x.split()
date=x1[0]+" "+x1[1]+" "+x1[2]+" "+x1[4]

root=Tk()
root.title("Covid 19 India Tracker")
root.config(bg='white')
#root.geometry("900x600+200+80")


ui_frame = Frame(root, width= 600, height=200, bg='white')
ui_frame.grid(row=0, column=0, padx=10, pady=5)

global ans
ans=[]
temp=StringVar()
def CheckData():
    global ans
    temp=locality_entry.get()
    ans=answer(temp)
    addresslabel=Label(root, text=ans[0],bg='DarkSeaGreen4', width=50,bd=5).grid(row=4,column=0)

    datelabel=Label(root,text=date,bg='DarkSeaGreen4', width=10,bd=5).grid(row=4,column=1)

    districtlabel=Label(root,text="District: "+ str(ans[1]),bg='DarkSeaGreen4', width=50,bd=5).grid(row=6,column=0)


    totallabel=Label(root,text="Total Cases: "+str(ans[2]),bg='lightblue', width=50,bd=5).grid(row=7,column=0)


    activelabel=Label(root,text="Active Cases: "+str(ans[3]),bg='red', width=50,bd=5).grid(row=8,column=0)


    recoverlabel=Label(root,text="Recovered : "+str(ans[4]),bg='lightgreen', width=50,bd=5).grid(row=9,column=0)


    deathlabel=Label(root,text="Death : "+str(ans[5]),bg='grey', width=50,bd=5).grid(row=10,column=0)



localitylabel=Label(ui_frame, text="Enter Locality :",bg='White', width=10,bd=5,pady=5,padx=5).grid(row=0,column=0)
#localitylabel.grid(row=0 , column=0,columnspan=2)
locality_entry=Entry(ui_frame,width=20)
locality_entry.grid(row=0,column=2,padx=5)
check =Button(ui_frame,text="Check",bg="white",width=10,command=CheckData)
check.grid(row=1,column=0)

# addresslabel=Label(root, text=full_name,bg='DarkSeaGreen4', width=20,bd=5).grid(row=4,column=0)

# datelabel=Label(root,text=date,bg='DarkSeaGreen4', width=10,bd=5).grid(row=4,column=1)

# districtlabel=Label(root,text=district_name,bg='DarkSeaGreen4', width=20,bd=5).grid(row=6,column=0)


# totallabel=Label(root,text=total_cases_district,bg='DarkSeaGreen4', width=20,bd=5).grid(row=7,column=0)


# activelabel=Label(root,text=active_cases_district,bg='DarkSeaGreen4', width=20,bd=5).grid(row=8,column=0)


# recoverlabel=Label(root,text=recovered_cases_district,bg='DarkSeaGreen4', width=20,bd=5).grid(row=9,column=0)


# deathlabel=Label(root,text=death_cases_district,bg='DarkSeaGreen4', width=20,bd=5).grid(row=10,column=0)





root.mainloop()