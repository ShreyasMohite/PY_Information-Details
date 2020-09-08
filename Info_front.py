from tkinter import *
import tkinter
from PIL import ImageTk
from PIL import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.messagebox
import datetime
import time
from Info_back import *
import os

from tkinter.filedialog import askopenfile

todaydate=datetime.datetime.now().date()





class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x690+0+0") #"C:\\Users\\SHREYAS\\Desktop\\shreyas python\\Info-Store\\icon\\lista.ico"
        self.root.iconbitmap("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\Info-Store\\icon\\lista.ico")
        self.root.title("Personal_Information")

        fullname=StringVar()
        address=StringVar()
        email=StringVar()
        gender=StringVar()
        contact=StringVar()
        dob=StringVar()
        sid=StringVar()
        

        #======================Buttons_Defination/Hower==============================================
        def on_enter(e):
            Insert_image_button['background']="black"
            Insert_image_button['foreground']="cyan"
               
               

        def on_leave(e):
            Insert_image_button['background']="SystemButtonFace"
            Insert_image_button['foreground']="SystemButtonText"

        def on_enters(e):
            but_Del['background']="black"
            but_Del['foreground']="cyan"
               
               

        def on_leaves(e):
            but_Del['background']="SystemButtonFace"
            but_Del['foreground']="SystemButtonText"
        
        def on_enterss(e):
            but_View['background']="black"
            but_View['foreground']="cyan"
               
               

        def on_leavess(e):
            but_View['background']="SystemButtonFace"
            but_View['foreground']="SystemButtonText"


        def on_entersss(e):
            but_Upd['background']="black"
            but_Upd['foreground']="cyan"
               
               

        def on_leavesss(e):
            but_Upd['background']="SystemButtonFace"
            but_Upd['foreground']="SystemButtonText"

        def on_enterssss(e):
            but_Clear['background']="black"
            but_Clear['foreground']="cyan"
               
               

        def on_leavessss(e):
            but_Clear['background']="SystemButtonFace"
            but_Clear['foreground']="SystemButtonText"

        def on_entersssss(e):
            but_Exit['background']="black"
            but_Exit['foreground']="cyan"
               
               

        def on_leavesssss(e):
            but_Exit['background']="SystemButtonFace"
            but_Exit['foreground']="SystemButtonText"


        def on_enterssssss(e):
            But_Add['background']="black"
            But_Add['foreground']="cyan"
               
               

        def on_leavessssss(e):
            But_Add['background']="SystemButtonFace"
            But_Add['foreground']="SystemButtonText"
        
        def on_entersssssss(e):
            But_Search['background']="black"
            But_Search['foreground']="cyan"
               
               

        def on_leavesssssss(e):
            But_Search['background']="SystemButtonFace"
            But_Search['foreground']="SystemButtonText"

        def on_entersp(e):
            But_Dis['background']="black"
            But_Dis['foreground']="cyan"
               
               

        def on_leavesp(e):
            But_Dis['background']="SystemButtonFace"
            But_Dis['foreground']="SystemButtonText"


        #================================================================================================
        #button ===================defination============================================================
        def Exit():
            iExit=tkinter.messagebox.askyesnocancel("Information System","you want to exit system")
            if iExit ==True:
                 root.destroy()
                 return

        def Reset():
            fullname.set("")
            address.set("")
            email.set("")
            gender.set("")
            contact.set("")
            dob.set("")
            sid.set("")
            
        
        
        def Add_Data():
            if(len(fullname.get( ) ) !=0):
                add_personal_information(fullname.get(),address.get(),email.get(),dob.get(),gender.get(),contact.get())
                Reset()
                View_Data()

        def View_Data():
            emplist.delete(*emplist.get_children())
            for rows in view_personal_information():
                emplist.insert('',END,values=rows)
        
        
        
        def Delete_Data():
            
            delete_by_id_personal_information(sid.get())
            View_Data()
            
        def Update_Data():
            if(len(fullname.get())!=0):
                delete_by_id_personal_information(sid.get())
            if(len(fullname.get())!=0):
                add_personal_information(fullname.get(),address.get(),email.get(),dob.get(),gender.get(),contact.get())
                
                Reset()
                View_Data()

        def Display_Data():
            if(len(fullname.get())!=0):
                Lab_name_on_profile=Label(Lab_Profile,text=fullname.get(),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_name_on_profile.place(x=300,y=10)

                Lab_address_on_profile=Label(Lab_Profile,text=address.get(),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_address_on_profile.place(x=300,y=60)  

                Lab_email_on_profile=Label(Lab_Profile,text=email.get(),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_email_on_profile.place(x=300,y=110)

                Lab_gender_on_profile=Label(Lab_Profile,text=gender.get(),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_gender_on_profile.place(x=300,y=160)

                Lab_contact_on_profile=Label(Lab_Profile,text=contact.get(),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_contact_on_profile.place(x=300,y=210) 

                Lab_dob_on_profile=Label(Lab_Profile,text=dob.get(),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_dob_on_profile.place(x=300,y=260)

            else:
                Lab_name_on_profile=Label(Lab_Profile,text=fullname.set(""),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_name_on_profile.place(x=300,y=10)

                Lab_address_on_profile=Label(Lab_Profile,text=address.set(""),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_address_on_profile.place(x=300,y=60)  

                Lab_email_on_profile=Label(Lab_Profile,text=email.set(""),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_email_on_profile.place(x=300,y=110)

                Lab_gender_on_profile=Label(Lab_Profile,text=gender.set(""),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_gender_on_profile.place(x=300,y=160)

                Lab_contact_on_profile=Label(Lab_Profile,text=contact.set(""),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_contact_on_profile.place(x=300,y=210) 

                Lab_dob_on_profile=Label(Lab_Profile,text=dob.set(""),font=('times new roman',11,"bold"),fg="red",bg="peachpuff")
                Lab_dob_on_profile.place(x=300,y=260)


        def Search_Data():
            emplist.delete(*emplist.get_children())
            for rows in search_all_data(fullname.get(),address.get(),email.get(),dob.get(),gender.get(),contact.get()):
                emplist.insert('',END,values=rows)






        
        
        

        #==================================Frame============================================================
                     #Frame

        Frame_root=Frame(root,bg="cyan2",width=1360,height=695).pack() #Frame on top main Frame
        Frame_Top=Frame(Frame_root,relief=RIDGE,width=1360,height=300,bg="gray",bd=4)
        Frame_Top.place(x=3,y=0) #first frame on top

        Frame_Down_Left=Frame(Frame_root,relief=RIDGE,width=650,height=380,bg="green",bd=4)
        Frame_Down_Left.place(x=3,y=310) #frame on left

        Frame_Down_Right=Frame(Frame_root,relief=RIDGE,width=703,height=380,bg="gray",bd=4)
        Frame_Down_Right.place(x=660,y=310) #frame on right
        
        Frame_photo_Label_Left=Frame(Frame_Top,bg="gray",width=250,height=290,bd=4,relief=RIDGE)
        Frame_photo_Label_Left.place(x=0,y=0)

        Frame_Top_Information_Right=Frame(Frame_Top,bg="gray75",width=773,height=290,bd=4,relief=RIDGE)
        Frame_Top_Information_Right.place(x=250,y=0)

        Frame_Top_Button=Frame(Frame_Top,bg="red",width=330,height=290,bd=4,relief=RIDGE)
        Frame_Top_Button.place(x=1023,y=0)

        Frame_Down_Right_Down=Frame(Frame_Down_Right,width=695,height=290,bd=4,relief=RIDGE,bg="yellow")
        Frame_Down_Right_Down.place(x=0,y=80)

        Frame_Top_Button_Date=Frame(Frame_Top_Button,width=323,height=140,bd=4,bg="snow",relief=RIDGE)
        Frame_Top_Button_Date.place(x=0,y=143)

        #==============================================================================
        #inserting lable on photo_label_left
        say_label=Label(Frame_photo_Label_Left,text="Set The Photo Image",font=("times new roman",13,"bold"),bg="gray",fg="cyan")
        say_label.place(x=40,y=6) 
        #"C:\\Users\\SHREYAS\\Desktop\\shreyas python\\Students\\Images\\user.png"

        self.original = Image.open("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\Info-Store\\Images\\default4.jpg")
        resized = self.original.resize((155,165),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        #bglab=Label(F1,image=self.image,bd=2).place(x=0,y=0)
        photo_image=Label(Frame_photo_Label_Left,image=self.image,bd=2)
        photo_image.place(x=40,y=35)

        def open_file():
            files=askopenfile(title="choose file",mode="rb",filetypes=[('Jpg File','.jpg'),('png File','.png'),('Jpeg File','.jpeg')])
            self.original = Image.open(files)
            resized = self.original.resize((155,165),Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized)
            #imges=tkinter.PhotoImage(file=files)
            photo_image=Label(Frame_photo_Label_Left,image=self.image,bd=2)
            photo_image.place(x=40,y=35)
            #print(file.name)



        #Adding button on Frame_photo_Label
        Insert_image_button=Button(Frame_photo_Label_Left,width=15,height=1,text="Add Image",font=("arial",10,"bold"),bd=5,cursor="hand2",command=lambda:open_file())
        Insert_image_button.place(x=53,y=220)
        Insert_image_button.bind("<Enter>",on_enter)
        Insert_image_button.bind("<Leave>",on_leave)
        
    #=========================Frame/Label/Entrys=========================================================
        Lab_Information=Label(Frame_Top_Information_Right,text="Fill All The Information",font=("times new roman",14,"bold"),fg="red",bg="gray75")
        Lab_Information.place(x=254,y=6)
        

        Lab_Fullname=Label(Frame_Top_Information_Right,text="FullName  :",font=("times new roman",11,"bold"),fg="Steelblue",bg="gray75")
        Lab_Fullname.place(x=12,y=55)
        Ent_Fullname=Entry(Frame_Top_Information_Right,width=30,font=("times new roman",11,"bold"),bd=3,textvariable=fullname)
        Ent_Fullname.place(x=100,y=55)

        Lab_Address=Label(Frame_Top_Information_Right,text="Address    :",font=("times new roman",11,"bold"),fg="Steelblue",bg="gray75")
        Lab_Address.place(x=12,y=135)
        Ent_Address=Entry(Frame_Top_Information_Right,width=30,font=("times new roman",11,"bold"),bd=3,textvariable=address)
        Ent_Address.place(x=100,y=135)

        Lab_Email=Label(Frame_Top_Information_Right,text="Email        :",font=("times new roman",11,"bold"),fg="Steelblue",bg="gray75")
        Lab_Email.place(x=12,y=210)
        Ent_Email=Entry(Frame_Top_Information_Right,width=30,font=("times new roman",11,"bold"),bd=3,textvariable=email)
        Ent_Email.place(x=100,y=215)

        Lab_Gender=Label(Frame_Top_Information_Right,text="Gender  :",font=("times new roman",11,"bold"),fg="Steelblue",bg="gray75")
        Lab_Gender.place(x=400,y=55)
        v=["Male","Female"]
        txtGender=Combobox(Frame_Top_Information_Right,values=v,font=('arial',10),width=32,state="readonly",textvariable=gender)
        txtGender.place(x=480,y=55)
        txtGender.set("select Gender")
        

        Lab_Contact=Label(Frame_Top_Information_Right,text="Contact  :",font=("times new roman",11,"bold"),fg="Steelblue",bg="gray75")
        Lab_Contact.place(x=400,y=135)
        Ent_Contact=Entry(Frame_Top_Information_Right,width=30,font=("times new roman",11,"bold"),bd=3,textvariable=contact)
        Ent_Contact.place(x=480,y=135)

        Lab_DOB=Label(Frame_Top_Information_Right,text="Birth       :",font=("times new roman",11,"bold"),fg="Steelblue",bg="gray75")
        Lab_DOB.place(x=400,y=215)
        Ent_DOB=Entry(Frame_Top_Information_Right,width=30,font=("times new roman",11,"bold"),bd=3,textvariable=dob)
        Ent_DOB.place(x=480,y=215)


        


    

    #======================================================================================================
    #frame/Top/Right/button/Bottom/Date/Time
        Lab_Top=Label(Frame_Top_Button_Date,text="Today's Date  And Time :",font=('times new roman',13,"bold"),bg="snow",fg="cyan3")
        Lab_Top.place(x=68,y=0)

        Lab_Date=Label(Frame_Top_Button_Date,text="Today's Date   :",font=('times new roman',11,"bold"),bg="snow",fg="cyan3")
        Lab_Date.place(x=0,y=40)

        Lab_Date_now=Label(Frame_Top_Button_Date,text=todaydate,font=('times new roman',11,"bold"),bg="snow",fg="cyan3")
        Lab_Date_now.place(x=130,y=40)

        Lab_Time=Label(Frame_Top_Button_Date,text="Time                :",font=('times new roman',11,"bold"),bg="snow",fg="cyan3")
        Lab_Time.place(x=0,y=80)

        
        def times():
            Lab_Time_now=Label(Frame_Top_Button_Date,font=('times new roman',11,"bold"),bg="snow",fg="cyan3")
            time_strf=time.strftime("%H:%M:%S %p")
            Lab_Time_now.config(text=time_strf)
            Lab_Time_now.after(1000,times)
            Lab_Time_now.place(x=130,y=80)
        times()
        #Lab_Time_now=Label(Frame_Top_Button_Date,font=('times new roman',11,"bold"),bg="snow",fg="cyan3")
        
        
        #Lab_Time_now.place(x=130,y=80)

    #==============================Frame/Top/ringt=========================================================
        But_Add=Button(Frame_Top_Button,text="Insert Data",font=('times new roman',11,"bold"),bd=2,width=11,height=2,cursor="hand2",command=Add_Data)
        But_Add.place(x=12,y=10)
        But_Add.bind("<Enter>",on_enterssssss)
        But_Add.bind("<Leave>",on_leavessssss)

        But_Dis=Button(Frame_Top_Button,text="Display Profile",font=('times new roman',11,"bold"),bd=2,width=11,height=2,cursor="hand2",command=Display_Data)
        But_Dis.place(x=12,y=70)
        But_Dis.bind("<Enter>",on_entersp)
        But_Dis.bind("<Leave>",on_leavesp)

        But_Search=Button(Frame_Top_Button,text="Search Data",font=('times new roman',11,"bold"),bd=2,width=11,height=2,cursor="hand2",command=Search_Data)
        But_Search.place(x=192,y=10)
        But_Search.bind("<Enter>",on_entersssssss)
        But_Search.bind("<Leave>",on_leavesssssss)

        Lab_SID=Label(Frame_Top_Button,text="ID :",font=('times new roman',11,"bold"),bg="red")
        Lab_SID.place(x=192,y=70)

        Ent_SID=Entry(Frame_Top_Button,font=('times new roman',11,"bold"),width=5,relief=RIDGE,bd=3,bg="darkblue",fg="red",textvariable=sid)
        Ent_SID.place(x=240,y=70)
    #=====================Frame/bottom/Left==================================================================
        Lab_Profile=LabelFrame(Frame_Down_Left,text="Profile Information",fg="Red",height=370,width=643,bg="peachpuff")
        Lab_Profile.place(x=0,y=0)

        self.original1 = Image.open("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\Info-Store\\Images\\default2.jpg")
        resized1 = self.original1.resize((155,165),Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(resized1)
        #bglab=Label(F1,image=self.image,bd=2).place(x=0,y=0)
        photo_image1=Label(Lab_Profile,image=self.image1,bd=2)
        photo_image1.place(x=10,y=10)

        Lab_name=Label(Lab_Profile,text="FullName    :-",fg="black",font=('times new roman',12,"bold"),bg="peachpuff")
        Lab_name.place(x=180,y=10)

        Lab_address=Label(Lab_Profile,text="Address      :-",fg="black",font=('times new roman',12,"bold"),bg="peachpuff")
        Lab_address.place(x=180,y=60)

        Lab_email=Label(Lab_Profile,text="Email          :-",fg="black",font=('times new roman',12,"bold"),bg="peachpuff")
        Lab_email.place(x=180,y=110)

        Lab_gender=Label(Lab_Profile,text="Gender       :-",fg="black",font=('times new roman',12,"bold"),bg="peachpuff")
        Lab_gender.place(x=180,y=160)

        Lab_contact=Label(Lab_Profile,text="Contact      :-",fg="black",font=('times new roman',12,"bold"),bg="peachpuff")
        Lab_contact.place(x=180,y=210)

        Lab_dob=Label(Lab_Profile,text="Birth Date :-",fg="black",font=('times new roman',12,"bold"),bg="peachpuff")
        Lab_dob.place(x=180,y=260)




    #=================Frame/bottom/right======================================================================
        #button
        but_Del=Button(Frame_Down_Right,text="Delete",font=('times new roman',11,"bold"),bd=2,width=11,height=2,cursor="hand2",command=Delete_Data)
        but_Del.place(x=35,y=10)
        but_Del.bind("<Enter>",on_enters)
        but_Del.bind("<Leave>",on_leaves)

        but_View=Button(Frame_Down_Right,text="View",font=('times new roman',11,"bold"),bd=2,width=11,height=2,cursor="hand2",command=View_Data)
        but_View.place(x=165,y=10)
        but_View.bind("<Enter>",on_enterss)
        but_View.bind("<Leave>",on_leavess)

        but_Upd=Button(Frame_Down_Right,text="Update",font=('times new roman',11,"bold"),bd=2,width=11,height=2,cursor="hand2",command=Update_Data)
        but_Upd.place(x=295,y=10)
        but_Upd.bind("<Enter>",on_entersss)
        but_Upd.bind("<Leave>",on_leavesss)

        but_Clear=Button(Frame_Down_Right,text="Clear",font=('times new roman',11,"bold"),bd=2,width=11,height=2,cursor="hand2",command=Reset)
        but_Clear.place(x=425,y=10)
        but_Clear.bind("<Enter>",on_enterssss)
        but_Clear.bind("<Leave>",on_leavessss)

        but_Exit=Button(Frame_Down_Right,text="Exit",font=('times new roman',11,"bold"),bd=2,width=11,height=2,cursor="hand2",command=Exit)
        but_Exit.place(x=555,y=10)
        but_Exit.bind("<Enter>",on_entersssss)
        but_Exit.bind("<Leave>",on_leavesssss)



       #Scrollbar and Treeview
        
        
        
        global emplist
        global scrollbar
        global sor
        def  game(event):
            crow=emplist.focus()
            contents=emplist.item(crow)
            row=contents['values']
            sid.set(row[0])
            fullname.set(row[1])
            address.set(row[2])
            email.set(row[3])
            dob.set(row[4])
            gender.set(row[5])
            contact.set(row[6])
            

        scrollbar=Scrollbar(Frame_Down_Right_Down,orient=VERTICAL)
        
        sor=Scrollbar(Frame_Down_Right_Down,orient=HORIZONTAL)
        emplist=tkinter.ttk.Treeview(Frame_Down_Right_Down,columns=("ID","fullname","address","email","DOB","gender","Contact"),height=12)
        
        
        scrollbar.config(command=emplist.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        sor.config(command=emplist.xview)
        sor.pack(side=BOTTOM,fill=BOTH)
        emplist.heading("ID",text="ID")
        emplist.heading("fullname",text="fullname")
        emplist.heading("address",text="address")
        emplist.heading("email",text="email")
        emplist.heading("gender",text="gender")
        emplist.heading("DOB",text="DOB")
        emplist.heading("Contact",text="Contact")
        #emplist.heading("Image",text="Image")
        
        emplist['show']="headings"
        emplist.column("ID",width=35,minwidth=10)
        emplist.column("fullname",width=120,minwidth=40)
        emplist.column("address",width=80,minwidth=50)
        emplist.column("email",width=150,minwidth=50)
        
        emplist.column("gender",width=70,minwidth=30)
        emplist.column("DOB",width=100,minwidth=40)
        emplist.column("Contact",width=110,minwidth=60)
        #emplist.column("Image",width=115,minwidth=50)
        
        emplist.bind('<ButtonRelease-1>',game)
        
        emplist.pack(side=TOP,fill=X)
    #=================================================================================


    



if __name__=="__main__":
    root=Tk()
    app=Student(root)
    root.mainloop()
