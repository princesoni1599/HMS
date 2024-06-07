# This section will contain photos of IIITB-Hostel's and a Navigation/Menu bar in it for [ Admin , Mess , Sports , Direction , Events ]
# This section will contain a NOTICE container also 

#----- LIBRARIES -----------

from tkinter import *
from PIL import Image, ImageTk 

#---------------------------


class Home_Page:
    #Functions:-
    def __init__(self,root):
        self.root = root
        self.root.title("IIITB Hostlers")
        self.root.geometry("1280x650+0+0")
    
        #================= Home Page ICON ==================================      
       
        #================= Home Page Background Image ======================
        img_home_page_main = Image.open(r"C:\Users\BHANU\Desktop\Hostel Management System (MP)\Experiments\Images\HostelMain.jpg")
        img_home_page_main = img_home_page_main.resize((1280,650),Image.ANTIALIAS)

        self.varHPI = ImageTk.PhotoImage(img_home_page_main)

        labelHPI = Label(self.root, image=self.varHPI)
        labelHPI.place(x=0, y=0, width=1280, height=650)

        #================= Home Page LOGO Label ==================================  
        logo_hpm = Label(self.root, text="IIIT BHOPAL HOSTELER",font=("times new roman",14,"bold"),bg="#fff",fg="white")
        logo_hpm.place(x=5,y=5,width=250,height=50)



if __name__ =="__main__":
    root = Tk()
    obj = Home_Page(root)
    root.mainloop()

