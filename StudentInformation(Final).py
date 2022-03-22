import os
from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog
from tkinter import messagebox
import csv
from collections import defaultdict

class Student_Information():

    def __init__(self, root):
        self.root = root
        self.root.title('Student Information System')
        self.root.geometry('1920x1080+0+0')

        self.ID_Number = StringVar()
        self.Full_Name = StringVar()
        self.Year_Level = StringVar()
        self.Gender = StringVar()
        self.Course = StringVar()
        self.Search = StringVar()
        self.selections = defaultdict(list)
        self.last_lookup = ""

        #============Menu=================
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)
        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Open", menu=self.file_menu)
        self.file_menu.add_command(label="Open csv", command=self.file_open)

        self.save_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Save", menu=self.save_menu)
        self.save_menu.add_command(label="Save as csv", command=self.save_info)

        #===========First Frame==========
        self.First_Frame = Frame(self.root, bd=8, relief=FLAT, bg='#fb8263')
        self.First_Frame.place(y=0, width=400, height=627)

        self.Inside_First_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='#ffffff')
        self.Inside_First_Frame.place(y=150, width=400, height=535)

        self.First_Frame_title = Label(self.First_Frame, text='STUDENT DATA', font=('Century Gothic', 25, 'bold'),
                                  fg='#ffffff', bg='#fb8263', justify=CENTER)
        self.First_Frame_title.grid(row=0, columnspan=2,ipady=20, padx=70)
        self.First_Frame1_title = Label(self.First_Frame, text='Hello. We are glad to see you!', font=('Century Gothic', 12, 'italic'),
                                       fg='#ffffff', bg='#fb8263', justify=CENTER)
        self.First_Frame1_title.grid(row=1, columnspan=2, padx=75)

        self.Label_id = Label(self.Inside_First_Frame, text='ID Number:', font=('Lato', 15), fg='#333438', bg='#ffffff')
        self.Label_id.grid(row=1, column=0, pady=10, padx=20, sticky='w')
        self.Label_id_entry = Entry(self.Inside_First_Frame, textvariable=self.ID_Number, font=('Lato', 12), bd=2, relief=GROOVE)
        self.Label_id_entry.grid(row=1, column=1, ipady=3, pady=30, padx=20, sticky='w')

        self. Label_name = Label(self.Inside_First_Frame, text='Full Name:', font=('Lato', 15), fg='#333438', bg='#ffffff')
        self.Label_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')
        self.Label_name_entry = Entry(self.Inside_First_Frame, textvariable=self.Full_Name, font=('Lato', 12), bd=2, relief=GROOVE)
        self.Label_name_entry.grid(row=2, column=1, ipady=3, pady=30, padx=20, sticky='w')

        self.Label_course = Label(self.Inside_First_Frame, text='Course:', font=('Lato', 15), fg='#333438', bg='#ffffff')
        self.Label_course.grid(row=3, column=0, pady=10, padx=20, sticky='w')
        self.Label_course_entry = Entry(self.Inside_First_Frame, textvariable=self.Course, font=('Lato', 12), bd=2,relief=GROOVE)
        self.Label_course_entry.grid(row=3, column=1, ipady=3, pady=30, padx=20, sticky='w')

        self.Label_year = Label(self.Inside_First_Frame, text='Year Level:', font=('Lato', 15), fg='#333438', bg='#ffffff')
        self.Label_year.grid(row=4, column=0, pady=10, padx=20, sticky='w')
        self.Label_year_entry = Entry(self.Inside_First_Frame, textvariable=self.Year_Level, font=('Lato', 12), bd=2, relief=GROOVE)
        self.Label_year_entry.grid(row=4, column=1, ipady=3,pady=30, padx=20, sticky='w')

        self.Label_gender = Label(self.Inside_First_Frame, text='Gender:', font=('Lato', 15), fg='#333438', bg='#ffffff')
        self.Label_gender.grid(row=5, column=0, pady=10, padx=20, sticky='w')
        self.Label_gender_entry = Entry(self.Inside_First_Frame, textvariable=self.Gender,font=('Lato', 12), bd=2, relief=GROOVE)
        self.Label_gender_entry.grid(row=5, column=1, ipady=3, pady=30, padx=20, sticky='w')

        # ====================Buttons===========
        self.button_frame = Frame(self.Inside_First_Frame, bd=1, relief=RIDGE, bg='#fb8263')
        self.button_frame.place(x=12, y=450, width=370)

        self.Add_button = Button(self.button_frame, text='Add',command=self.add_student, font=('Century Gothic', 13), bg='#ffffff', relief=GROOVE)
        self.Add_button.grid(row=0,column=0,padx=13,pady=10)
        self.Update_button = Button(self.button_frame, text='Update',command=self.update, font=('Century Gothic', 13), bg='#ffffff', relief=GROOVE)
        self.Update_button.grid(row=0, column=1, padx=13, pady=10)
        self.Delete_button = Button(self.button_frame, text='Delete',command=self.delete, font=('Century Gothic', 13), bg='#ffffff', relief=GROOVE)
        self.Delete_button.grid(row=0, column=2, padx=13, pady=10)
        self.Clear_button = Button(self.button_frame, text='Clear',command=self.clear, font=('Century Gothic', 13), bg='#ffffff', relief=GROOVE)
        self.Clear_button.grid(row=0, column=3, padx=13, pady=10)

        # ====================Records===========
        self.Records_Frame = Frame(self.root, bd=8, relief=FLAT, bg='#fb8263')
        self.Records_Frame.place(x=400, y=0, width=966, height=800)

        self.Label_Student = Frame(self.root,  bd=2, relief=RIDGE, bg='white')
        self.Label_Student.place(x=400, y=0, width=966, height=150)

        self.Title_Student = Label(self.Label_Student, text="STUDENT INFORMATION SYSTEM", font=('Century Gothic', 40, 'bold'),
                                   fg ='#fb8263', bg='white', justify=CENTER)
        self.Title_Student.pack(side=LEFT, fill=Y, padx=85, pady=30)

        # ===================Search Bar==========
        self.Label_search = Label(self.Records_Frame, text='Search by ID Number:', font=('Lato', 15, 'bold'), fg='#fefefe', bg='#fb8263')
        self.Label_search.grid(row=0, column=0, pady=180, padx=20, sticky='w')
        self.Label_search_entry = Entry(self.Records_Frame,textvariable=self.Search, font=('Lato', 12), bd=2, relief=RIDGE, width=15)
        self.Label_search_entry.grid(row=0, column=1, padx=10, sticky='w')

        self.Search_button = Button(self.Records_Frame, text='Search',command=self.search, font=('Century Gothic', 10), bg='#ffffff', relief=GROOVE)
        self.Search_button.grid(row=0, column=2,padx=10, pady=30)

        self.List = Label(self.Records_Frame, text='Number of Students:', font=('Lato', 15, 'bold'),fg='#fefefe', bg='#fb8263')
        self.List.grid(row=0, column=3, padx=40, sticky='w')
        self.List_entry = Entry(self.Records_Frame, font=('Lato', 12), bd=2, relief=RIDGE, width=8)
        self.List_entry.grid(row=0, column=3,padx=240, sticky='w')

        # =============Records(cont.)==========
        self.Details_Frame = Frame(self.Records_Frame, bd=4, relief=RIDGE, bg='white')
        self.Details_Frame.place(x=20, y=240, width=910, height=400)

        # ============Scroll Bar and Treeview=========
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",
                             background = "#f1e2df",
                             foreground = "black",
                             rowheight = 25,
                             fieldbackground = "#f1e2df"
                             )
        self.style.map("Treeview",
                       background = [('selected', '#f56f4c')])

        self.Student_Record = ttk.Treeview(self.Details_Frame)
        self.Student_Record["columns"] = ("ID Number", "Full Name", "Course", "Year Level", "Gender")

        self.scroll_horizontal = Scrollbar(self.Details_Frame, orient=HORIZONTAL)
        self.scroll_horizontal.pack(side=BOTTOM, fill=X)
        self.scroll_vertical = Scrollbar(self.Details_Frame, orient=VERTICAL)
        self.scroll_vertical.pack(side=RIGHT, fill=Y)

        self.Student_Record.config(yscrollcommand=self.scroll_vertical.set)
        self.Student_Record.config(xscrollcommand=self.scroll_horizontal.set)

        self.scroll_horizontal.config(command=self.Student_Record.xview)
        self.scroll_vertical.config(command=self.Student_Record.yview)

        self.Student_Record['show'] = 'headings'
        self.Student_Record.column("ID Number", minwidth=10)
        self.Student_Record.column("Full Name", minwidth=80)
        self.Student_Record.column("Course", minwidth=80)
        self.Student_Record.column("Year Level", minwidth=10)
        self.Student_Record.column("Gender", minwidth=80)

        self.Student_Record.heading("ID Number", text="ID Number")
        self.Student_Record.heading("Full Name", text="Full Name")
        self.Student_Record.heading("Course", text="Course")
        self.Student_Record.heading("Year Level", text="Year Level")
        self.Student_Record.heading("Gender", text="Gender")
        self.Student_Record.bind('<ButtonRelease-1>', self.select_item)

        self.Student_Record.pack(fill=BOTH, expand=1)

    # Open A File Function
    def file_open(self):
        file_name = filedialog.askopenfilename(initialdir="C:/Users/", title="Open a File",
                                                   filetypes=(("csv files", "*.csv"), ("All Files", "*.*")))
        if file_name:
            try:
                file_name = r"{}".format(file_name)
                data = pd.read_csv(file_name)
            except ValueError:
                messagebox.showerror("Error", "File Could Not Be Opened")
            except FileNotFoundError:
                messagebox.showerror("Error", "File Could Not Be Found")

        self.clear_tree()

        self.Student_Record["column"] = list(data.columns)
        self.Student_Record["show"] = "headings"

        for column in self.Student_Record["column"]:
            self.Student_Record.column(column, anchor='center')
            self.Student_Record.heading(column, text=column)

        data_rows = data.to_numpy().tolist()
        for row in data_rows:
            self.Student_Record.insert("", "end", values=row)

        self.update_list()

        self.Student_Record.pack()

        self.Label_id_entry.delete(0, END)
        self.Label_name_entry.delete(0, END)
        self.Label_course_entry.delete(0, END)
        self.Label_year_entry.delete(0, END)
        self.Label_gender_entry.delete(0, END)
        self.Label_search_entry.delete(0, END)

    # Clear Current Tree
    def clear_tree(self):
        self.Student_Record.delete(*self.Student_Record.get_children())

    def save_info(self):
        if len(self.Student_Record.get_children()) < 1:
            messagebox.showinfo("No Data", "No data available to export")
            return False

        file = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Save CSV',
                                            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
        with open(file, 'w', newline='') as output:
            output_data = csv.writer(output, delimiter=',')
            csv_writer = csv.writer(output, delimiter=',')
            csv_writer.writerow(['ID Number', 'Full Name', 'Course', 'Year Level', 'Gender'])
            for x in self.Student_Record.get_children():
                row = self.Student_Record.item(x)['values']
                output_data.writerow(row)
        messagebox.showinfo("File Saved", "Data exported successfully!")

    def add_student(self):
        if(len(self.ID_Number.get()) == 0 or len(self.Full_Name.get()) == 0 or len(self.Year_Level.get()) == 0 or len(self.Gender.get()) == '' or len(self.Course.get()) ==0):
            messagebox.showerror("Error", "All fields should be filled!")
        else:
            self.Student_Record.insert("", "end", text="", values=(self.ID_Number.get(),
                                                                   self.Full_Name.get(),
                                                                   self.Course.get(),
                                                                   self.Year_Level.get(),
                                                                   self.Gender.get()
                                                                   ))
            for column in self.Student_Record["column"]:
                self.Student_Record.column(column, anchor='center')

            self.update_list()

            self.Label_id_entry.delete(0, END)
            self.Label_name_entry.delete(0, END)
            self.Label_year_entry.delete(0, END)
            self.Label_gender_entry.delete(0, END)
            self.Label_course_entry.delete(0, END)

    def update(self):
        selected = self.Student_Record.focus()
        self.Student_Record.item(selected, text='', values=(self.ID_Number.get(),
                                                            self.Full_Name.get(),
                                                            self.Course.get(),
                                                            self.Year_Level.get(),
                                                            self.Gender.get(),
                                                            ))
        self.Label_id_entry.delete(0, END)
        self.Label_name_entry.delete(0, END)
        self.Label_year_entry.delete(0, END)
        self.Label_gender_entry.delete(0, END)
        self.Label_course_entry.delete(0, END)

        messagebox.showinfo("Update Student", "Successfully updated!")

    def delete(self):
        response = messagebox.askyesno("Delete Student", "Delete student from the list?")
        if not response:
           pass
        else:
            x = self.Student_Record.selection()[0]
            self.Student_Record.delete(x)
            self.Label_id_entry.delete(0, END)
            self.Label_name_entry.delete(0, END)
            self.Label_year_entry.delete(0, END)
            self.Label_gender_entry.delete(0, END)
            self.Label_course_entry.delete(0, END)
            self.Label_search_entry.delete(0, END)
            self.update_list()

    def clear(self):
        self.Label_id_entry.delete(0, END)
        self.Label_name_entry.delete(0, END)
        self.Label_year_entry.delete(0, END)
        self.Label_gender_entry.delete(0, END)
        self.Label_course_entry.delete(0, END)

    def search(self):
        query = str(self.Search.get())
        if not query:
            return
        children = self.Student_Record.get_children()
        for child in children:
            curr = self.Student_Record.item(child)["values"][0]
            if query in curr and child not in self.selections[query]:
                self.selections[query].append(child)
                self.Student_Record.selection_set(child)
                self.Student_Record.focus(child)
                self.Student_Record.see(child)
                self.last_lookup = query

                self.ID_Number.set('')
                self.Full_Name.set('')
                self.Year_Level.set('')
                self.Gender.set('')
                self.Course.set('')

                selected = self.Student_Record.focus()
                values = self.Student_Record.item(selected, 'values')

                self.Label_id_entry.insert(0, values[0])
                self.Label_name_entry.insert(0, values[1])
                self.Label_course_entry.insert(0, values[2])
                self.Label_year_entry.insert(0, values[3])
                self.Label_gender_entry.insert(0, values[4])
                self.Label_search_entry.delete(0, END)
                return
            elif query != self.last_lookup:
                self.selections = defaultdict(list)
        messagebox.showerror('Error', 'Student is not in the list')

    def select_item(self, a):
        self.ID_Number.set('')
        self.Full_Name.set('')
        self.Year_Level.set('')
        self.Gender.set('')
        self.Course.set('')

        selected = self.Student_Record.focus()
        values = self.Student_Record.item(selected, 'values')

        self.Label_id_entry.insert(0, values[0])
        self.Label_name_entry.insert(0, values[1])
        self.Label_course_entry.insert(0, values[2])
        self.Label_year_entry.insert(0, values[3])
        self.Label_gender_entry.insert(0, values[4])

    def update_list(self):
        self.List_entry.delete(0, END)
        self.List_entry.insert(0, str(len(self.Student_Record.get_children())))

root = Tk()
ob = Student_Information(root)
root.mainloop()