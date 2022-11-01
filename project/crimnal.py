
from ast import Delete
from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1358x765+0+0')
        root.maxsize(1360, 768)
        root.minsize(1027, 580)
        self.root.title('CRIMINAL MANAGMENT SYSTEM')

        # @@@@@@@@@@@@@@@@VAriavle
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_Arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthmark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()


        lbl_title = Label(self.root, text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE', font=(
            'times new roman', 40, 'bold'), bg='black', fg='gold')
        lbl_title.place(x=0, y=0, width=1360, height=55)

        # @MAINLOGO_CODEX_12012625
        img_logo = Image.open('images/mainlogo.png')
        img_logo = img_logo.resize((50, 50), Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        # position of logo
        self.logo.place(x=5, y=3, width=50, height=50)

        # Image_Frame

        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=55, width=1366, height=140)

        # First_image
        img1 = Image.open('images/img1.png')
        img1 = img1.resize((455, 160), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=455, height=160)

        # SecOndImage@codex12012625

        img2 = Image.open('images/img2.png')
        img2 = img2.resize((455, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=455, y=0, width=455, height=160)

        # IMAGE@3_CODEX12012625
        img3 = Image.open('images/img3.png')
        img3 = img3.resize((910, 160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=910, y=0, width=455, height=160)

        # MAIN_FEAME@CODEX12012625
        Main_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_Frame.place(x=0, y=200, width=1360, height=535)

        # SubFram_UpperInside main @codex12012625  (Criminal Information)
        Sub_Frame = LabelFrame(Main_Frame, bd=2, relief=RIDGE, text='Criminal Informations', font=(
            'times new roman', 11, 'bold'), fg='red', bg='white')
        Sub_Frame.place(x=5, y=5, width=1340, height=260)

        # Labels_intry
        # case id
        caseid = Label(Sub_Frame, text='Case ID:',
                       font=('arial', 11, 'bold'), bg='white')
        caseid.grid(row=0, column=0, padx=2, pady=0, sticky=W)

        caseintry = ttk.Entry(
            Sub_Frame, textvariable=self.var_case_id, width=22, font=('arial', 11, 'bold'))
        caseintry.grid(row=0, column=1, padx=2, sticky=W)

        # Criminal_No
        Criminal_number = Label(Sub_Frame, text='Criminal No:', font=(
            'arial', 11, 'bold'), bg='white')
        Criminal_number.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        text_criminal_no = ttk.Entry(
            Sub_Frame, textvariable=self.var_criminal_no, width=22, font=('arial', 11, 'bold'))
        text_criminal_no.grid(row=0, column=3, padx=2, pady=7)

        # CriminalName
        lbl_name = Label(Sub_Frame, text='Criminal Name:',
                         font=('arial', 11, 'bold'), bg='white')
        lbl_name.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        text_Name = ttk.Entry(
            Sub_Frame, textvariable=self.var_name, width=22, font=('arial', 11, 'bold'))
        text_Name.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # NickName
        lbl_name = Label(Sub_Frame, text='Nic name:',
                         font=('arial', 11, 'bold'), bg='white')
        lbl_name.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        text_Name = ttk.Entry(
            Sub_Frame, textvariable=self.var_nickname, width=22, font=('arial', 11, 'bold'))
        text_Name.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        # Arrestdate
        lbl_arrestdate = Label(Sub_Frame, text='Arrest Date:', font=(
            'arial', 11, 'bold'), bg='white')
        lbl_arrestdate.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        text_Name = ttk.Entry(
            Sub_Frame, textvariable=self.var_Arrest_date, width=22, font=('arial', 11, 'bold'))
        text_Name.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # DadateofCrime
        lbl_dateofCrime = Label(Sub_Frame, text='Date of Crime:', font=(
            'arial', 11, 'bold'), bg='white')
        lbl_dateofCrime.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        text_Name = ttk.Entry(
            Sub_Frame, textvariable=self.var_date_of_crime, width=22, font=('arial', 11, 'bold'))
        text_Name.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # Addres
        lbl_arrestdate = Label(Sub_Frame, text='Address',
                               font=('arial', 11, 'bold'), bg='white')
        lbl_arrestdate.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        text_Name = ttk.Entry(
            Sub_Frame, textvariable=self.var_address, width=22, font=('arial', 11, 'bold'))
        text_Name.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # Age
        lbl_age = Label(Sub_Frame, text='Age:', font=(
            'arial', 11, 'bold'), bg='white')
        lbl_age.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        text_Name = ttk.Entry(
            Sub_Frame, textvariable=self.var_age, width=22, font=('arial', 11, 'bold'))
        text_Name.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # Occupution
        lbl_Occupution = Label(Sub_Frame, text='occupution:', font=(
            'arial', 11, 'bold'), bg='white')
        lbl_Occupution.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        text_Name = ttk.Entry(
            Sub_Frame, textvariable=self.var_occupation, width=22, font=('arial', 11, 'bold'))
        text_Name.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        # Birthmark
        lbl_Birthmark = Label(Sub_Frame, text='Birth Mark:',
                              font=('arial', 11, 'bold'), bg='white')
        lbl_Birthmark.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        text_Name = ttk.Entry(
            Sub_Frame, textvariable=self.var_birthmark, width=22, font=('arial', 11, 'bold'))
        text_Name.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        # crimetype
        lbl_crimetype = Label(Sub_Frame, text='Crime Type:',
                              font=('arial', 11, 'bold'), bg='white')
        lbl_crimetype.grid(row=0, column=4, padx=2, pady=7, sticky=W)

        text_Name = ttk.Entry(
            Sub_Frame, textvariable=self.var_crime_type, width=22, font=('arial', 11, 'bold'))
        text_Name.grid(row=0, column=5, padx=2, pady=7, sticky=W)

        # FatherName
        lbl_FatherName = Label(Sub_Frame, text='Father name:', font=(
            'arial', 11, 'bold'), bg='white')
        lbl_FatherName.grid(row=1, column=4, padx=2, pady=7, sticky=W)

        text_Name = ttk.Entry(
            Sub_Frame, textvariable=self.var_father_name, width=22, font=('arial', 11, 'bold'))
        text_Name.grid(row=1, column=5, padx=2, pady=9, sticky=W)

        # label for gender
        lbl_gender = Label(Sub_Frame, text='Gender:',
                           font=('arial', 11, 'bold'), bg='white')
        lbl_gender.grid(row=2, column=4, padx=2, pady=7, sticky=W)

        # label for wanted
        lbl_wanted = Label(Sub_Frame, text='Most wanted:',
                           font=('arial', 11, 'bold'), bg='white')
        lbl_wanted.grid(row=3, column=4, padx=2, pady=7, sticky=W)

        # radioButton for gender

        radio_frame_gender = Frame(Sub_Frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=703, y=86, width=186, height=28)

        male = Radiobutton(radio_frame_gender, variable=self.var_gender,
                           text='Male', value='male', font=('arial', 9, 'bold'), bg='white')
        male.grid(row=0, column=0, padx=2, pady=0, sticky=W)

        female = Radiobutton(radio_frame_gender, text='Female', variable=self.var_gender,
                             value='female', font=('arial', 9, 'bold'), bg='white')
        female.grid(row=0, column=1, padx=2, pady=0, sticky=W)

        # radioButton for most wanted

        radio_frame_wanted = Frame(Sub_Frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_wanted.place(x=703, y=125, width=186, height=28)

        yes = Radiobutton(radio_frame_wanted, text='Yes', variable=self.var_wanted,
                          value='yes', font=('arial', 9, 'bold'), bg='white')
        yes.grid(row=0, column=0, padx=2, pady=0, sticky=W)

        no = Radiobutton(radio_frame_wanted, text='No', variable=self.var_wanted,
                         value='no', font=('arial', 9, 'bold'), bg='white')
        no.grid(row=0, column=1, padx=2, pady=0, sticky=W)

        ##################### Buttons ########################
        button_frame = Frame(Sub_Frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=2, y=195, width=597, height=40)

        # add_button_RECORD SAVE

        btn_add = Button(button_frame, command=self.add_data, text='record Save', font=(
            'arial', 12, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=2)

        # Update Button

        btn_update = Button(button_frame, command=self.update_data, text='Update', font=(
            'arial', 12, 'bold'), width=14, bg='blue', fg='white')
        btn_update.grid(row=0, column=1, padx=3, pady=2)

        # Delet Button
        btn_delete = Button(button_frame,command=self.delet_data, text='Delete ', font=(
            'arial', 12, 'bold'), width=14, bg='blue', fg='white')
        btn_delete.grid(row=0, column=2, padx=3, pady=2)

        # clear button
        btn_clear = Button(button_frame,command=self.clear_data, text='Clear', font=(
            'arial', 12, 'bold'), width=14, bg='blue', fg='white')
        btn_clear.grid(row=0, column=3, padx=3, pady=2)

        # background_right_side_img
        img_right = Image.open('images/right.jpg')
        img_right = img_right.resize((440, 245), Image.ANTIALIAS)
        self.photocrime = ImageTk.PhotoImage(img_right)

        self.img_right = Label(Sub_Frame, image=self.photocrime)
        self.img_right.place(x=900, y=0, width=440, height=250)

        # SECONnd SubframeCriminal Information Table
        Down_Frame = LabelFrame(Main_Frame, bd=2, relief=RIDGE, text='Criminal Information Table', font=(
            'times new roman', 11, 'bold'), fg='red', bg='white')
        Down_Frame.place(x=5, y=270, width=1340, height=260)

        #Search_frame /downframe
        Search_Frame = LabelFrame(Down_Frame, bd=2, relief=RIDGE, text='Search Criminal Record', font=(
            'times new roman', 11, 'bold'), fg='red', bg='white')
        Search_Frame.place(x=0, y=0, width=1336, height=60)

        search_by = Label(Search_Frame, text='Search By:',
                          font=('arial', 11, 'bold'), bg='red')
        search_by.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        # combobox search
        self.var_com_search=StringVar()
        combo_search_box = ttk.Combobox(Search_Frame,textvariable=self.var_com_search, font=(
            'arial', 11, 'bold'), width=18, state='readonly')
        combo_search_box['value'] = ('Select Option', 'Case_id', 'criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=2, padx=2, sticky=W)

        self.var_search=StringVar()
        search_text = ttk.Entry(Search_Frame,textvariable=self.var_search, width=22,
                                font=('arial', 11, 'bold'))
        search_text.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        # search button
        btn_search = Button(Search_Frame,command=self.Search_data, text='Search ', font=(
            'arial', 12, 'bold'), width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=4, padx=2, pady=7, sticky=W)

        # search all
        btn_all = Button(Search_Frame,command=self.fetch_data, text='Show all', font=(
            'arial', 12, 'bold'), width=14, bg='blue', fg='white')
        btn_all.grid(row=0, column=5, padx=2, pady=7, sticky=W)

        crime_agency = Label(Search_Frame, text='NATIONAL CRIME AGENCY', font=(
            'arial', 30, 'bold'), bg='white', fg='crimson')
        crime_agency.grid(row=0, column=6, padx=25, pady=0, sticky=W)

        # table_frame
        table_frame = Frame(Down_Frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        # Scrollbar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.criminal_table = ttk.Treeview(table_frame, columns=('1', '2', '3', '4', '5', '6', '7', '8',
                                           '9', '10', '11', '12', '13', '14'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1', text="CaseId")
        self.criminal_table.heading('2', text="CriminalNo")
        self.criminal_table.heading('3', text="Criminal Name")
        self.criminal_table.heading('4', text="NickName")
        self.criminal_table.heading('5', text="ArrestDate")
        self.criminal_table.heading('6', text="CrimeDate")
        self.criminal_table.heading('7', text="Address")
        self.criminal_table.heading('8', text="Age")
        self.criminal_table.heading('9', text="Occupation")
        self.criminal_table.heading('10', text="Birth Mark")
        self.criminal_table.heading('11', text="Crime Type")
        self.criminal_table.heading('12', text="Father Name")
        self.criminal_table.heading('13', text="Gender")
        self.criminal_table.heading('14', text="Wanted")

        self.criminal_table['show'] = 'headings'  # ho hide ho rha vo ayega
        self.criminal_table.column('1', width=95)
        self.criminal_table.column('2', width=95)
        self.criminal_table.column('3', width=95)
        self.criminal_table.column('4', width=95)
        self.criminal_table.column('5', width=95)
        self.criminal_table.column('6', width=95)
        self.criminal_table.column('7', width=95)
        self.criminal_table.column('8', width=95)
        self.criminal_table.column('9', width=95)
        self.criminal_table.column('10', width=95)
        self.criminal_table.column('11', width=95)
        self.criminal_table.column('12', width=95)
        self.criminal_table.column('13', width=95)
        self.criminal_table.column('14', width=95)
        self.criminal_table.pack(fill=BOTH, expand=1)

        self.criminal_table.bind("<ButtonRelease>", self.get_cusor)
        self.fetch_data()

    # ADD FUNCTION

    def add_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'All fiels are required ')
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='', database='criminal_record')
                my_curser = conn.cursor()
                my_curser.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nickname.get(),
                    self.var_Arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birthmark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender .get(),
                    self.var_wanted .get()


                ))

                conn.commit()
                
                self.fetch_data()
                # self.clear_data()
                conn.close()
                messagebox.showinfo(
                    'Succes', 'criminal Record has been saved ')

            except Exception as es:
                messagebox.showerror('Error', f'Due to{str(es)}')

    # function for data fetch

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', username='root', password='', database='criminal_record')
        my_curser = conn.cursor()
        my_curser.execute('select * from criminal')
        data = my_curser.fetchall()
        if len(data) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('', END, values=i)
            conn.commit()
            conn.close()

    # getCurser
    def get_cusor(self, event=""):
        cursor_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        data = content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_Arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender .set(data[12])
        self.var_wanted .get(data[13])

    # update_data_function
    def update_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'All fiels are required ')
        else:
            try:
                update = messagebox.askyesno(
                    'Update', 'Are You Sure update criminal record')
                if update > 0:
                    conn = mysql.connector.connect(
                        host='localhost', username='root', password='', database='criminal_record')
                    my_curser = conn.cursor()
                    my_curser.execute(
                        'update criminal set criminal_no=%s,Nick_Name=%s,arrest_date=%s,dateOfcrome=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s,name=%s where Case_id=%s', (




                            self.var_criminal_no.get(),
                            self.var_name.get(),
                            self.var_nickname.get(),
                            self.var_Arrest_date.get(),
                            self.var_date_of_crime.get(),
                            self.var_address.get(),
                            self.var_age.get(),
                            self.var_occupation.get(),
                            self.var_birthmark.get(),
                            self.var_crime_type.get(),
                            self.var_father_name.get(),
                            self.var_gender .get(),
                            self.var_wanted .get(),
                            self.var_case_id.get()



                        ))
                else:
                    if not update:
                        return
                conn.commit()
                
                self.fetch_data()
                # self.clear_data()
                conn.close()
                messagebox.showinfo(
                    'Success', 'Criminal record succesfully updated')
            except Exception as es:

                messagebox.showerror('Errore', f'Due to {str(es)}')

    # @@@@@@@DELETE FUNCTION@@@@@@@@@@@@@

    def delet_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'All fiels are required ')
        else:
            try:
                Delete = messagebox.askyesno(
                    'Delete', 'Are You Sure Delete criminal record')
                if Delete > 0:
                        conn = mysql.connector.connect(
                            host='localhost', username='root', password='', database='criminal_record')
                        my_curser = conn.cursor()
                        sql = 'delete from criminal where case_id=%s'
                        value = (self.var_case_id.get(),)
                        my_curser.execute(sql, value)
                else:
                    if not Delete:
                            return
                conn.commit()
                self.fetch_data()
               
                conn.close()
                messagebox.showinfo(
                        'Success', 'Criminal record succesfully Deleted')
            except Exception as es:

                messagebox.showerror('Errore', f'Due to {str(es)}')

    #@@@@@@@@@@@CLEARE DATA @@@@@@@@@@@@@@@@@@@@@@@@@
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_Arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender .set("")
        self.var_wanted .get("")

#@@@@@@@@@@@@@@SEARCH DATA @@@@@@@@@@@@@@@@@

    def Search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Errore','All Fields are required ')

        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='', database='criminal_record')
                my_curser = conn.cursor()
                my_curser.execute('select * from criminal where ' + str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_curser.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert("",END,values=i)
                conn.commit()
                conn.close()        

            except Exception as es:

                messagebox.showerror('Errore', f'Due to {str(es)}')





if __name__ == "__main__":
    root = Tk()
    obj = criminal(root)
    root.mainloop()
