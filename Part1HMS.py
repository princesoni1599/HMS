from tkinter import *
from typing import Mapping #Tkinter is changed to tkinter in newer version of python
from PIL import Image,ImageTk #pip install pillow
from Part2HMS import Cust_win

class HMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Hostel Management System")
        self.root.iconbitmap(r"C:\Users\STARNET\OneDrive\Desktop\desktop\Hostel Management System (MP)/Images/Logo.ico")              # self.root.iconbitmap('path') add icon instead of feather 
        self.root.geometry("1550x800+0+0") #do not use spaces in between [ERROR]


        #==================== F I R S T   I M A G E =====================================================
        img1 = Image.open(r"C:\Users\STARNET\OneDrive\Desktop\desktop\Hostel Management System (MP)/Images/HostelMain.jpg")
        img1 = img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        #Another way to do above step is:
        # my_img = ImageTk.PhotoImage(Image.open("Path"))

        lblimg = Label(self.root,image = self.photoimg1,bd=4,relief=RIDGE) # Image= -> image= [ERROR]
        lblimg.place(x=0,y=0,width=1550,height=140)


        #==================== L O G O =====================================================

        logoImg = Image.open(r"C:\Users\STARNET\OneDrive\Desktop\desktop\Hostel Management System (MP)/Images/Logo.png")
        logoImg = logoImg.resize((140,140), Image.ANTIALIAS)
        self.logoImage = ImageTk.PhotoImage(logoImg)

        lblLogo = Label(self.root, image = self.logoImage,bd=2,relief=RIDGE)
        lblLogo.place(x=0,y=0,width=140,height=140)

        #==================== T I T L E =====================================================

        lblTitle = Label(self.root, text="HOSTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold") # OR ->  lblTitle = Label(self.root, text="Hostel Management System",font=("times new roamn",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lblTitle.place(x=0,y=140,width=1550,height=60)

        #======================copyright information ========================================

        copyright = Label(self.root, text="Copyright © 2017 IIIT Bhopal", font=("times new roman",15,"bold"))
        copyright.place(x=0,y=680,width=1550, height=27)
        #==================== F R A M E =====================================================

        mainFrame = Frame(self.root) #OR -> mainFrame = Frame(self.root,bd=4,relief=RIDGE) <--{styling}
        mainFrame.place(x=0,y=190,width=1550,height=490) # y=140+50

        #==================== M E N U =====================================================

        # lblMenu = Label(mainFrame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        # lblMenu.place(x=0,y=0,width=230)

        #==================== M E N U  - O P T I O N S (AKA Buttons)=====================================================

        btn_frame = Frame(mainFrame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=0,width=1550,height=40)

        #Buttons-
        cust_btn =Button(btn_frame,text="HOME",width=24, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2") #Cursor pointer type / Width added to fill
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame,text="DETAILS",command=self.cust_details,width=24,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=0,column=1,pady=1)

        det_btn =Button(btn_frame,text="ROOM",width=24, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2") #Cursor pointer type / Width added to fill
        det_btn.grid(row=0,column=2,pady=1)

        rep_btn = Button(btn_frame,text="QUERY",width=24,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        rep_btn.grid(row=0,column=3,pady=1)

        log_btn =Button(btn_frame,text="HELP",width=24, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2") #Cursor pointer type / Width added to fill
        log_btn.grid(row=0,column=4,pady=1)


        #==================== R I G H T - S I D E  I M A G E =====================================================

        rgt_img = Image.open(r"C:\Users\STARNET\OneDrive\Desktop\desktop\Hostel Management System (MP)/Images/HostelGallery.jpg")
        rgt_img = rgt_img.resize((1535,590),Image.ANTIALIAS)
        self.rgtImage = ImageTk.PhotoImage(rgt_img)

        lblRgtImg = Label(mainFrame,image=self.rgtImage,bd=4,relief=RIDGE)
        lblRgtImg.place(x=0,y=40,width=1550,height=463)


        #==================== L E F T - S I D E - D O W N  I M A G E =====================================================

        # lib_img = Image.open(r"C:\Users\prince soni\Desktop\Hostel Management System (MP)/Images/LibraryMini2.jpg")
        # lib_img = lib_img.resize((230,210),Image.ANTIALIAS)
        # self.libImage = ImageTk.PhotoImage(lib_img)

        # lblLibImage = Label(mainFrame,image=self.libImage,bd=4,relief=RIDGE)
        # lblLibImage.place(x=0,y=225,width=230,height=150)

        # lib_img2 = Image.open(r"C:\Users\prince soni\Desktop\Hostel Management System (MP)/Images/LibraryMini.jpg")
        # lib_img2 = lib_img2.resize((230,190),Image.ANTIALIAS)
        # self.libImage2 = ImageTk.PhotoImage(lib_img2)

        # lblLibImage2 = Label(mainFrame,image=self.libImage2,bd=4,relief=RIDGE)
        # lblLibImage2.place(x=0,y=340,width=230,height=150)



    #========================== Part2HMS ====================================
    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_win(self.new_window) # LINE 57 [ cust_btn =Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22, font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2") ]
    #========================================================================



if __name__ == "__main__":
    root = Tk()
    obj = HMS(root)
    root.mainloop()
