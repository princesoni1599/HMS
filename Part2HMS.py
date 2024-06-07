
from io import TextIOBase
from tkinter import *
import tkinter

from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox



class Cust_win:
    def __init__(self,root):
        self.root =root
        self.root.title("CUSTOMER WINDOW")
        self.root.geometry("1050x450+230+225")
        ################################################################################################################################################################################################################################### 
        ####################################################################  P A R T 3     H M S   #######################################################################################################################################
        ###################################################################################################################################################################################################################################


        #--------------- G E N E R A T I N G   R A N D O M   N U M B E R S   AS  ID ---------------------
        #import random
        self.var_cust_id = StringVar()
        x = random.randint(1000,10000)
        self.var_cust_id.set(str(x))

        #------------------ O T H E R   V A R I A B L E S -----------------------------------------------
        self.var_cust_name = StringVar()
        self.var_cust_mother = StringVar()
        self.var_cust_gender = StringVar()
        self.var_cust_pin = StringVar()
        self.var_cust_mobile = StringVar()
        self.var_cust_email = StringVar()
        self.var_cust_nationality = StringVar()
        self.var_cust_address = StringVar()
        self.var_cust_id_proof = StringVar()
        self.var_cust_id_number = StringVar()

        ###################################################################################################################################################################################################################################
        ###################################################################################################################################################################################################################################
        ###################################################################################################################################################################################################################################
        


        #=========================== T I T L E ==========================
        cust_title = Label(self.root, text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        cust_title.place(x=0 , y=0 , width=1205, height=50) #<-- Root is changed from 'mainFrame' to 'Cust_Win'


        #=========================== L O G O ============================
        cust_win_logo = Image.open(r"C:\Users\STARNET\OneDrive\Desktop\desktop\Hostel Management System (MP)\Images\Logo.png")
        cust_win_logo = cust_win_logo.resize((60,50),Image.ANTIALIAS)
        self.LogoImage = ImageTk.PhotoImage(cust_win_logo)

        lblCust_win_logo = Label(self.root, image=self.LogoImage, bd=4, relief=RIDGE)
        lblCust_win_logo.place(x=2 ,y=0 , width=60, height=50)

        #============================= L A B E L   F R A M E ============
        lblFrame = LabelFrame(self.root, text="Customer Details", font=("times new roman",12,"bold"),relief=RIDGE,bd=2)
        lblFrame.place(x=5,y=50,width=425,height=490)

        #============================  E N T R Y    F E I L D S ========
        #customer Reference -------
        # Lable
        cust_ref= Label(lblFrame,text="Customer ID :- ",font=("arial",13,"bold"),padx=2,pady=6)
        cust_ref.grid(row=0,column=0,sticky=W)
        # Entry Field
        cust_ref_ent = ttk.Entry(lblFrame,width=29,font=("arial",13,"italic"),textvariable=self.var_cust_id,state="readonly")
        cust_ref_ent.grid(row=0, column=1)

        #customer Name -----------
        #label
        cust_name = Label(lblFrame,text="Customer Name :-",font=("arial",13,"bold"),padx=2,pady=6)
        cust_name.grid(row=1,column=0,sticky=W)
        #Entry Field
        cust_name_entry = ttk.Entry(lblFrame,font=("arial",13,"bold"),width=29,textvariable=self.var_cust_name)
        cust_name_entry.grid(row=1,column=1)

        #customer Mother Name -----------
        #label
        cust_moth = Label(lblFrame,text="Mother Name :-",font=("arial",13,"bold"),padx=2,pady=6)
        cust_moth.grid(row=2,column=0,sticky=W)
        #Enrty Field
        cust_moth_entry = ttk.Entry(lblFrame,font=("arial",13,"italic"),width=29,textvariable=self.var_cust_mother)
        cust_moth_entry.grid(row=2,column=1)

        #customer Gender ------------------------------DIFF-----
        #label
        cust_gend = Label(lblFrame,text="Gender :-",font=("arial",13,"bold"),padx=2,pady=6)
        cust_gend.grid(row=3,column=0,sticky=W)
        #Enrty Field
        cust_gend_combo = ttk.Combobox(lblFrame,font=("arial",13,"italic"),width=27,state="readonly",textvariable=self.var_cust_gender)
        cust_gend_combo["values"]=("Male","Female","Other")
        cust_gend_combo.current(0)
        cust_gend_combo.grid(row=3,column=1)

        #customer Post Code -----------
        #label
        cust_pc = Label(lblFrame,text="PinCode :-",font=("arial",13,"bold"),padx=2,pady=6)
        cust_pc.grid(row=4,column=0,sticky=W)
        #Enrty Field
        cust_pc_entry = ttk.Entry(lblFrame,font=("arial",13,"italic"),width=29,textvariable=self.var_cust_pin)
        cust_pc_entry.grid(row=4,column=1)



        #customer Email -----------
        #label
        cust_email = Label(lblFrame,text="Email :-",font=("arial",13,"bold"),padx=2,pady=6)
        cust_email.grid(row=5,column=0,sticky=W)
        #Enrty Field
        cust_email_entry = ttk.Entry(lblFrame,font=("arial",13,"italic"),width=29,textvariable=self.var_cust_email)
        cust_email_entry.grid(row=5,column=1)

        #customer Nationality --------------------------------DIFF
        #label
        cust_nation = Label(lblFrame,text="Nationality :-",font=("arial",13,"bold"),padx=2,pady=6)
        cust_nation.grid(row=6,column=0,sticky=W)
        #Enrty Field
        cust_nation_combo = ttk.Combobox(lblFrame,font=("arial",13,"italic"),width=27,state="readonly",textvariable=self.var_cust_nationality)
        cust_nation_combo["values"]=("Indian","American","British","Other")
        cust_nation_combo.current(3)
        cust_nation_combo.grid(row=6,column=1)

        #customer ID proof -----------------------------------DIFF
        #label
        cust_ID = Label(lblFrame,text="ID Proof :-",font=("arial",13,"bold"),padx=2,pady=6)
        cust_ID.grid(row=7,column=0,sticky=W)
        #Enrty Field
        cust_ID_type = ttk.Combobox(lblFrame,font=("arial",13,"italic"),width=27,state="readonly",textvariable=self.var_cust_id_proof)
        cust_ID_type["values"]=("Adhar Card","Driving License","Passport")
        cust_ID_type.current(0)
        cust_ID_type.grid(row=7,column=1)

        #customer ID NUMBER -----------
        #label
        cust_IDnum = Label(lblFrame,text="ID Number :-",font=("arial",13,"bold"),padx=2,pady=6,textvariable=self.var_cust_id_number)
        cust_IDnum.grid(row=8,column=0,sticky=W)
        #Enrty Field
        cust_IDnum_entry = ttk.Entry(lblFrame,font=("arial",13,"italic"),width=29)
        cust_IDnum_entry.grid(row=8,column=1)

        #customer Address -----------
        #label
        cust_addrs = Label(lblFrame,text="Address :-",font=("arial",13,"bold"),padx=2,pady=6)
        cust_addrs.grid(row=9,column=0,sticky=W)
        #Enrty Field
        cust_addrs_entry = ttk.Entry(lblFrame,font=("arial",13,"italic"),width=29,textvariable=self.var_cust_address)
        cust_addrs_entry.grid(row=9,column=1)

        #customer Mobile  -----------
        #label
        cust_mob = Label(lblFrame,text="Mobile No. :-",font=("arial",13,"bold"),padx=2,pady=6)
        cust_mob.grid(row=10,column=0,sticky=W)
        #Enrty Field
        cust_mob_entry = ttk.Entry(lblFrame,font=("arial",13,"italic"),width=29,textvariable=self.var_cust_mobile)
        cust_mob_entry.grid(row=10,column=1)

        # =========================== ADD / UPDATE / DELET / RESET ===============
        #Create Frame for Buttons
        button_Frame = Frame(lblFrame,bd=2, relief=RIDGE)
        button_Frame.place(x=0,y=400,width=412,height=40)

        add_btn = Button(button_Frame,text="ADD", font=("times new roman",13,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,padx=15,cursor="hand2",command=self.add_data)
        add_btn.grid(row=11,column=0)

        upd_btn = Button(button_Frame,text="UPDATE", font=("times new roman",13,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,padx=15,cursor="hand2",command=self.update_data)
        upd_btn.grid(row=11,column=1)

        del_btn = Button(button_Frame,text="DELETE", font=("times new roman",13,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,padx=15,cursor="hand2",command=self.delete_data)
        del_btn.grid(row=11,column=2)

        res_btn = Button(button_Frame,text="RESET", font=("times new roman",13,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,padx=15,cursor="hand2",command=self.reset_data)
        res_btn.grid(row=11,column=3)

        #========================= D A T A B A S E   F R A M E ====================
        database_frame = LabelFrame(self.root,text="DATABASE DETAILS",font=("times new roman",13,"bold"),bd=2,fg="green",relief=RIDGE)
        database_frame.place(x=435, y=60,width=725,height=490)

        search_by_label = Label(database_frame,text="Search By - ",font=("arial",13,"bold"),bg="red",fg="white")
        search_by_label.grid(row=0,column=0,sticky=W,padx=3)

        #..............FROM search_data()...........................
        self.varSearch =StringVar()  # insert this variable in  search's combobox
        #...........................................................

        #Search Options ----
        search_opt1 = ttk.Combobox(database_frame,font=("italic",13),width=15,state="readonly",textvariable=self.varSearch)
        search_opt1["values"]=("Name","ID","Mobile No.","Nationality")
        search_opt1.current(1)
        search_opt1.grid(row=0,column=1,padx=3)

        
        #..............FROM search_data()...........................
        self.textSearch =StringVar()  # insert this variable in  search's combobox
        #...........................................................
        #entry field for search option---
        entry_op1= ttk.Entry(database_frame,font=("arial",13),width=15,textvariable=self.textSearch)
        entry_op1.grid(row=0,column=2,padx=3)

        #Create Button to Show Current Entry & Show All Entries
        show_current = Button(database_frame,text="Search",font=("arial",13),bg="black",fg="gold",bd=2,relief=RIDGE,cursor="hand2",command=self.search_data)
        show_current.grid(row=0,column=3,padx=3)

        show_all = Button(database_frame,text="Show All",font=("arial",13),bg="black",fg="gold",bd=2,relief=RIDGE,cursor="hand2",command=self.fetch_data)
        show_all.grid(row=0,column=4,padx=3)

        # ===================================== S H O W   D A T A   T A B L E ==================================
        data_table = Frame(database_frame,bd=2,relief=RIDGE)
        data_table.place(x=0,y=60,width=500,height=350)

        #Scroll Bar
        scroll_x = ttk.Scrollbar(data_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_table,orient=VERTICAL)

        self.data_table_details = ttk.Treeview(data_table,columns=("ID","NAME","MOTHER","GENDER","PIN","MOBILE","EMAIL","NATION","IDPROOF","IDNUMBER","ADDRESS"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)

        scroll_x.config(command=self.data_table_details.xview)
        scroll_y.config(command=self.data_table_details.yview)

        #Showing Columns
        self.data_table_details.heading("ID", text="ID")
        self.data_table_details.heading("NAME", text="NAME")
        self.data_table_details.heading("MOTHER", text="MOTHER")
        self.data_table_details.heading("GENDER", text="GENDER")
        self.data_table_details.heading("PIN", text="PIN CODE")
        self.data_table_details.heading("MOBILE", text="MOBILE NO")
        self.data_table_details.heading("EMAIL", text="EMAIL")
        self.data_table_details.heading("NATION", text="NATIONALITY")
        self.data_table_details.heading("IDPROOF", text="ID PROOF")
        self.data_table_details.heading("IDNUMBER", text="ID NUMBER")
        self.data_table_details.heading("ADDRESS", text="ADDRESS")

        self.data_table_details["show"]="headings"

        self.data_table_details.column("ID",width=100)
        self.data_table_details.column("NAME",width=100)
        self.data_table_details.column("MOTHER",width=100)
        self.data_table_details.column("GENDER",width=100)
        self.data_table_details.column("PIN",width=100)
        self.data_table_details.column("MOBILE",width=100)
        self.data_table_details.column("EMAIL",width=100)
        self.data_table_details.column("NATION",width=100)
        self.data_table_details.column("IDPROOF",width=100)
        self.data_table_details.column("IDNUMBER",width=100)
        self.data_table_details.column("ADDRESS",width=100) 


        self.data_table_details.pack(fill=BOTH,expand=1)
        self.data_table_details.bind("<ButtonRelease-1>",self.get_focus)
        self.fetch_data()
###################################################################################################################################################################################################################################
####################################################################  P A R T 3     H M S   #######################################################################################################################################
###################################################################################################################################################################################################################################

    #Add data in database -----------------------------------------------------------------------------------
    def add_data(self):
        if self.var_cust_mobile.get()=="" or self.var_cust_mother.get()=="":
            messagebox.showerror("Form Filling Error","Mobile & Mother Field are Required ",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="college")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                                                     (self.var_cust_id.get(),
                                                                                                      self.var_cust_name.get(),
                                                                                                      self.var_cust_mother.get(),
                                                                                                      self.var_cust_gender.get(),
                                                                                                      self.var_cust_pin.get(),
                                                                                                      self.var_cust_mobile.get(),
                                                                                                      self.var_cust_email.get(),
                                                                                                      self.var_cust_nationality.get(),
                                                                                                      self.var_cust_id_proof.get(),
                                                                                                      self.var_cust_id_number.get(),
                                                                                                      self.var_cust_address.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning !!! ", f"Something went wrong : {str(es)}",parent=self.root)
    

    # SHOW DATA IN RIGHT <window> 
    # self.fetch_data()  <-this function should be added in add_data()'s  .commit() line & at the end of the Cust_win class -----------------------
    def fetch_data(self):
        conn_fetch = mysql.connector.connect(host="localhost", username="root", password="123456789", database="college")
        conn_fetch2= conn_fetch.cursor()
        conn_fetch2.execute("select * from customer")

        #creating variable to store fetched data
        var_rows =conn_fetch2.fetchall()
        
        #if table is showing already filled in our <window> 
        if len(var_rows)!=0:
            self.data_table_details.delete(*self.data_table_details.get_children())
            for i in var_rows:
                self.data_table_details.insert("",END,values=i)
            conn_fetch.commit()
        conn_fetch.close()
    

    #CLICK on any row AND GET DETAILS TO     U P D A T E - PART 1 (SELECT DATA)  ------------------------------------------------------------------------------------------

    def get_focus(self,event=""):                       #<--- bind this function in Cust_win class just before self.fetch_data()
        var_focus = self.data_table_details.focus()

        #store focused data in variable
        var_store = self.data_table_details.item(var_focus) #this will be of string type

        #to store individual data of string in an array type variable we create a variable
        var_rows = var_store["values"]

        #by using indices we get datas
        self.var_cust_id.set(var_rows[0]),
        self.var_cust_name.set(var_rows[1]),
        self.var_cust_mother.set(var_rows[2]),
        self.var_cust_gender.set(var_rows[3]),
        self.var_cust_pin.set(var_rows[4]),
        self.var_cust_mobile.set(var_rows[5]),
        self.var_cust_email.set(var_rows[6]),
        self.var_cust_nationality.set(var_rows[7]),
        self.var_cust_id_proof.set(var_rows[8]),
        self.var_cust_id_number.set(var_rows[9]),
        self.var_cust_address.set(var_rows[10])

    #-------------------------------- U P D A T E - PART 2   (UPDATE SELECTED DATA) ------------------------------------------------------------------------------------------
    def update_data(self):          #<--- add this function in UPDATE button LINE- 171

        #conditions before updation
        # (1): if any feild is empty
        if(self.var_cust_mobile.get()==""):
            messagebox.showerror("Error","Enter Mobile Number",parent=self.root)
        else:
            var_upd = mysql.connector.connect(host="localhost", username="root", password="123456789", database="college" )
            var_curs = var_upd.cursor()
            var_curs.execute("update customer set NAME=%s, MOTHER=%s, GENDER=%s, PIN=%s, MOBILE=%s, EMAIL=%s, NATION=%s, IDPROOF=%s, IDNUMBER=%s, ADDRESS=%s where ID=%s",(
                                                                                                                                                                           
                                                                                                                                                                            self.var_cust_name.get(),
                                                                                                                                                                            self.var_cust_mother.get(),
                                                                                                                                                                            self.var_cust_gender.get(),
                                                                                                                                                                            self.var_cust_pin.get(),
                                                                                                                                                                            self.var_cust_mobile.get(),
                                                                                                                                                                            self.var_cust_email.get(),
                                                                                                                                                                            self.var_cust_nationality.get(),
                                                                                                                                                                            self.var_cust_id_proof.get(),
                                                                                                                                                                            self.var_cust_id_number.get(),
                                                                                                                                                                            self.var_cust_address.get(),
                                                                                                                                                                            self.var_cust_id.get(),
                                                                                                                                                                           ))
            var_upd.commit()
            self.fetch_data() #<-- if you want to see/ fetch updated data in side <window>
            var_upd.close()
            messagebox.showinfo("Updated","Customer Details Updated Successfully",parent=self.root)
    

    #-------------------------------- D E L E T E  -----------------------------------------------------------------------------------------------------------------------------------
    def delete_data(self):             #<--- add this function in DELETE Button LINE-174
        delete_data = messagebox.askyesno("Confirm Delete","Press YES to proceed",parent=self.root)

        #if user press OK
        if(delete_data > 0):
            conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="college")
            conn2 = conn.cursor()

            query = "delete from customer where ID=%s"
            value=(self.var_cust_id.get(),)

            conn2.execute(query,value)
        #if user press NO / Cancel
        else:
            if not delete_data:
                return

        conn.commit()
        self.fetch_data() # to see data after deletion in side <window>
        conn.close()

        

    #-------------------------------- R E S E T  -----------------------------------------------------------------------------------------------------------------------------------
    # this reset button will reset data from FORM not from DATABASE 
    # therefor no need to connect with mysql
    def reset_data(self):           #<-- add this function in RESET Button LINE-177

        reset_data = messagebox.askyesno("Reset","Press Yes to Reset")
        if(reset_data>0):
            # self.var_cust_id.set(""),  #we dont want to reset this Random ID BUT we want new ID [add random.randint()int line 399]
            self.var_cust_name.set(""),
            self.var_cust_mother.set(""),
            self.var_cust_gender.set(""),
            self.var_cust_pin.set(""),
            self.var_cust_mobile.set(""),
            self.var_cust_email.set(""),
            self.var_cust_nationality.set(""),
            self.var_cust_id_proof.set(""),
            self.var_cust_id_number.set(""),
            self.var_cust_address.set("")

            x = random.randint(1000,10000)
            self.var_cust_id.set(str(x))
        else:
            pass
    


    #-------------------------------- S E A R C H   BUTTON  -----------------------------------------------------------------------------------------------------------------------------------
    # STEPS TO SEARCH DATA:-
    #(1) : get data from combobox [Name / ID / Mobile No. / Nationality] and store this data in a variable
    #(2) : set (1)'s variable in (2)'s values=

    #data will show in side <window> aka in database table
    def search_data(self):                                  #<--- Add this function in SEARCH BUTTON
        conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="college")
        conn2 = conn.cursor()

        conn2.execute("select * from customer where "+str(self.varSearch.get())+" LIKE '%"+str(self.textSearch.get())+"%'")  #Write carefully [check spaces]

        #showing data of matched entry <combobox>
        rows = conn2.fetchall()

        if len(rows)!=0:
            self.data_table_details.delete(*self.data_table_details.get_children())
            for i in rows:
                self.data_table_details.insert("",END,values=i)
                conn.commit()
            conn.close()

       
        







        




        



        





if __name__ == "__main__":
    root = Tk()
    obj = Cust_win(root)
    root.mainloop()

