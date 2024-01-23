import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
#from sqlite3 import sqlite3
from StudDbSqlite import StudDbSqlite

class StudGuiCtk(customtkinter.CTk):

    def __init__(self, dataBase=StudDbSqlite('AppDb.db')):
        super().__init__()
        self.db = dataBase

        self.title('Student Management System')
        self.geometry('1000x600')
        self.config(bg='#9AB7D3')
        self.resizable(False, False)

        self.font1 = ('Angsana New', 20, 'bold')
        self.font2 = ('Angsana New', 12, 'bold')

        # Data Entry Form
        # 'Class Number' Label and Entry Widgets
        self.class_number_label = self.newCtkLabel('Class Number')
        self.class_number_label.place(x=30, y=70)
        self.class_number_entry = self.newCtkEntry()
        self.class_number_entry.place(x=150, y=60)

        # 'Name' Label and Entry Widgets
        self.name_label = self.newCtkLabel('Name')
        self.name_label.place(x=30, y=120)
        self.name_entry = self.newCtkEntry()
        self.name_entry.place(x=110, y=110)

        # 'Course' Label and Combo Box Widgets
        self.course_label = self.newCtkLabel('Gender')
        self.course_label.place(x=30, y=170)
        self.course_cboxVar = StringVar()
        self.course_cboxOptions = ['Eletronics Engineering', 'Electrical Engineering', 'Computer Engineering', 'Chemical Engineering', 'Mechanical Engineering', 'Others']
        self.course_cbox = self.newCtkComboBox(options=self.course_cboxOptions, 
                                    entryVariable=self.course_cboxVar)
        self.course_cbox.place(x=110, y=170)

        # 'Gender' Label and Combo Box Widgets
        self.gender_label = self.newCtkLabel('Gender')
        self.gender_label.place(x=30, y=230)
        self.gender_cboxVar = StringVar()
        self.gender_cboxOptions = ['Female', 'Male']
        self.gender_cbox = self.newCtkComboBox(options=self.gender_cboxOptions, 
                                    entryVariable=self.gender_cboxVar)
        self.gender_cbox.place(x=110, y=230)

        # 'College Department' Label and Combo Box Widgets
        self.college_department_label = self.newCtkLabel('College Department')
        self.college_department_label.place(x=20, y=280)
        self.college_department_cboxVar = StringVar()
        self.college_department_cboxOptions = ['Engineering', 'Law', 'Science', 'Education', 'Arts and Letters', 'Others']
        self.college_department_cbox = self.newCtkComboBox(options=self.college_department_cboxOptions, 
                                    entryVariable=self.college_department_cboxVar)
        self.college_department_cbox.place(x=110, y=290)


        self.add_button = self.newCtkButton(text='Add Student',
                                onClickHandler=self.add_entry,
                                fgColor='#EDEAE5',
                                hoverColor='#C7DBDA',
                                borderColor='#DFCCF1')
        self.add_button.place(x=60,y=360)

        self.new_button = self.newCtkButton(text='New Student',
                                onClickHandler=lambda:self.clear_form(True))
        self.new_button.place(x=60,y=450)

        self.update_button = self.newCtkButton(text='Update Student',
                                    onClickHandler=self.update_entry)
        self.update_button.place(x=370,y=450)

        self.delete_button = self.newCtkButton(text='Delete Student',
                                    onClickHandler=self.delete_entry,
                                    fgColor='#FFB8B1',
                                    hoverColor='#FFDAC1',
                                    borderColor='#FCE1E4')
        self.delete_button.place(x=680,y=410)

        self.export_button = self.newCtkButton(text='Export to CSV',
                                    onClickHandler=self.export_to_csv)
        self.export_button.place(x=990,y=410)

        # Tree View for Database Entries
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Treeview', 
                        font=self.font2, 
                        foreground='#EAEAEA',
                        background='#97C1A9',
                        fieldlbackground='#CCE2CB')

        self.style.map('Treeview', background=[('selected', '#B5EAD6')])

        self.tree = ttk.Treeview(self, height=16)
        self.tree['columns'] = ('Class Number', 'Name', 'Gender', 'College Department', 'Course')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('Class Number', anchor=tk.CENTER, width=10)
        self.tree.column('Name', anchor=tk.CENTER, width=150)
        self.tree.column('Gender', anchor=tk.CENTER, width=150)
        self.tree.column('College Department', anchor=tk.CENTER, width=10)
        self.tree.column('Course', anchor=tk.CENTER, width=150)

        self.tree.heading('Class Number', text='Class Number')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('College Department', text='College Department')
        self.tree.heading('Course', text='Course')

        self.tree.place(x=370, y=30, width=1010, height=360)
        self.tree.bind('<ButtonRelease>', self.read_display_data)

        self.add_to_treeview()

    # new Label Widget
    def newCtkLabel(self, text = 'CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#F5D2D3'
        widget_BgColor='#F7E1D3'

        widget = customtkinter.CTkLabel(self, 
                                    text=text,
                                    font=widget_Font, 
                                    text_color=widget_TextColor,
                                    bg_color=widget_BgColor)
        return widget

    # new Entry Widget
    def newCtkEntry(self, text = 'CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#DFCCF1'
        widget_FgColor='#FFE1E9'
        widget_BorderColor='#9AB7D3'
        widget_BorderWidth=2
        widget_Width=260

        widget = customtkinter.CTkEntry(self,
                                    font=widget_Font,
                                    text_color=widget_TextColor,
                                    fg_color=widget_FgColor,
                                    border_color=widget_BorderColor,
                                    border_width=widget_BorderWidth,
                                    width=widget_Width)
        return widget

    # new Combo Box Widget
    def newCtkComboBox(self, options=['DEFAULT', 'OTHER'], entryVariable=None):
        widget_Font=self.font1
        widget_TextColor='#A3E1DC'
        widget_FgColor='#EDEAE5'
        widget_DropdownHoverColor='#B7CFB7'
        widget_ButtonColor='#F6EAC2'
        widget_ButtonHoverColor='E2F0CB'
        widget_BorderColor='#FFE1E9'
        widget_BorderWidth=2
        widget_Width=260
        widget_Options=options

        widget = customtkinter.CTkComboBox(self,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        border_color=widget_BorderColor,
                                        width=widget_Width,
                                        variable=entryVariable,
                                        values=options,
                                        state='readonly')
        
        # set default value to 1st option
        widget.set(options[0])

        return widget

    # new Button Widget
    def newCtkButton(self, text = 'CTK Button', onClickHandler=None, fgColor='#C7DBDA', hoverColor='#55CBCD', bgColor='#B5EAD6', borderColor='#9AB7D3'):
        widget_Font=self.font1
        widget_TextColor='#F5D2D3'
        widget_FgColor=fgColor
        widget_HoverColor=hoverColor
        widget_BackgroundColor=bgColor
        widget_BorderColor=borderColor
        widget_BorderWidth=2
        widget_Cursor='hand2'
        widget_CornerRadius=16
        widget_Width=270
        widget_Function=onClickHandler

        widget = customtkinter.CTkButton(self,
                                        text=text,
                                        command=widget_Function,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        hover_color=widget_HoverColor,
                                        bg_color=widget_BackgroundColor,
                                        border_color=widget_BorderColor,
                                        border_width=widget_BorderWidth,
                                        cursor=widget_Cursor,
                                        corner_radius=widget_CornerRadius,
                                        width=widget_Width)
       
        return widget

    # Handles
    def add_to_treeview(self):
        students = self.db.fetch_students()
        self.tree.delete(*self.tree.get_children())
        for student in students:
            print(student)
            self.tree.insert('', END, values=student)

    def clear_form(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
            self.tree.focus('')
        self.class_number_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.gender_cboxVar.set('Female')
        self.college_department_cboxVar.set('Engineering')
        self.course_cboxVar.set('Electronics Engineering')

    def read_display_data(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            row = self.tree.item(selected_item)['values']
            self.clear_form()
            self.class_number_entry.insert(0, row[0])
            self.name_entry.insert(0, row[1])
            self.gender_cboxVar.set(row[2])
            self.college_department_cboxVar.set(row[3])
            self.course_cboxVar.set(row[4])
        else:
            pass

    def add_entry(self):
        class_number=self.class_number_entry.get()
        name=self.name_entry.get()
        gender=self.gender_cboxVar.get()
        college_department=self.college_department_cboxVar.get()
        course=self.course_cboxVar.get()

        if not (class_number and name and gender and college_department and course):
            messagebox.showerror('Error', 'Enter all fields.')
        elif self.db.class_number_exists(class_number):
            messagebox.showerror('Error', 'Class Number already exists')
        else:
            self.db.insert_student(class_number, name, gender, college_department, course)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been inserted')

    def delete_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose a student to delete')
        else:
            class_number = self.class_number_entry.get()
            self.db.delete_student(class_number)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been deleted')

    def update_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose an student to update')
        else:
            class_number=self.class_number_entry.get()
            name=self.name_entry.get()
            gender=self.gender_cboxVar.get()
            college_department=self.college_department_cboxVar.get()
            course=self.course_cboxVar.get()
            self.db.update_student(name, gender, college_department, course, class_number)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Data has been updated')

    def export_to_csv(self):
        self.db.export_csv()
        messagebox.showinfo('Success', f'Data exported to {self.db.dbName}.csv')





