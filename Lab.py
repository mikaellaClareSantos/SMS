import customtkinter
from customtkinter import *
from tkinter import * 
from tkinter import ttk 
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import StudDb

app = customtkinter.CTk()
app.title('Student Management System')
app.geometry('800x680')
app.config(bg='#0A0B0C')
app.resizable(False, False)

font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 15, 'bold')
font3 = ('Arial', 13, 'bold')

def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose an item to delete.')
    else:
        class_number = class_number_entry.get()
        name = name_entry.get()
        gender = gender_entry.get()
        add_to_treeview()
        clear()
        create_chart()
        messagebox.showinfo('Success', 'Data has been deleted.')
    
def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose an item to update.')
    else:
        class_number = class_number_entry.get()
        name = name_entry.get()
        gender = gender_entry.get()
        add_to_treeview()
        clear()
        create_chart()
        messagebox.showinfo('Success', 'Data has been updated.')


def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        class_number_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        gender_entry.insert(0, row[2])
    else:
        pass

def add_to_treeview():
    students = StudDb.fetch_students()
    tree.delete(*tree.get_children())
    for student in students:
        tree.insert('', END, values = student)

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    class_number_entry.delete(0, END)
    name_entry.delete(0, END)
    gender_entry.delete(0, END)

def create_chart():
    student_details = StudDb.fetch_students()
    student_names = [student[1] for student in student_details]
    class_number_value = [student[2] for student in student_details]

    figure = Figure(figsize(10, 3.8), dpi = 80, facecolor = '#0A0B0C')
    ax = figure.add_subplot(111)
    ax.bar = (student_names, class_number_value, width:= 0.4, color := '#11EA05')
    ax.set_xlabel('Student Name', color = '#fff', fontsize = 10)
    ax.set_ylabel('Class Number', color = '#fff', fontsize = 10)
    ax.set_title('Student Year Number', color = '#fff', fontsize = 12)
    ax.tick_params(axis = 'y', labelcolor = '#fff', labelsize = 12)
    ax.tick_params(axis = 'x', labelcolor = '#fff', labelsize = 12)
    ax.set_facecolor('#1B181B')

    canvas = FigureCanvasTkagg(figure)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 0, column = 0, padx = 0, pady = 405)


def insert():
    class_number = class_number_entry.get()
    name = name_entry.get()
    gender = gender_entry.get()
    if not (class_number and name and gender):
        messagebox.showerror('Error', 'Enter all fields.')
    elif StudDb.class_number_exists(class_number):
        messagebox.showerror('Error', 'Class Number already exists.')
    else:
        try:
            class_number_value = int(class_number)
            StudDb.insert_student(class_number, name, gender)
            add_to_treeview()
            clear()
            create_chart()
            messagebox.showinfo('Success', 'Data has been inserted.')
        except ValueError:
            messagebox.showerror('Error', 'Class Number should be an integer.')


title_label = customtkinter.CTkLabel(app, font = font1, text = 'Student Details', text_color = '#fff', bg_color = '#0A0B0C')
title_label.place(x = 35, y = 15)

frame = customtkinter.CTkFrame(app, bg_color = '#0A0B0C', fg_color = '#1B1121', corner_radius = 10, border_width = 2, border_color = '#fff', width = 200, height = 370 )
frame.place(x = 25, y = 45)

image1 = PhotoImage(file = '5.png')
image1_label = Label(frame, image = image1, bg = '#1B1B21')
image1_label.place(x = 70, y = 5)

class_number_label = customtkinter.CTkLabel(frame, font = font2, text = 'Class No. ', text_color = '#fff', bg_color = '#1B1B21')
class_number_label.place(x = 60, y = 75)

class_number_entry = customtkinter.CTkEntry(frame, font = font2, text_color = '#000', fg_color = '#fff', border_color = '#B2016C', border_width = 2, width = 160)
class_number_entry.place(x = 20, y = 105)

name_label = customtkinter.CTkLabel(frame, font = font2, text = '     Name     ', text_color = '#fff', bg_color = '#1B1B21')
name_label.place(x = 50, y = 140)

name_entry = customtkinter.CTkEntry(frame, font = font2, text_color = '#000', fg_color = '#fff', border_color = '#B2016C', border_width = 2, width = 160)
name_entry.place(x = 20, y = 175)

gender_label = customtkinter.CTkLabel(frame, font = font2, text = '  Gender   ', text_color = '#fff', bg_color = '#1B1B21')
gender_label.place(x = 60, y = 205)

gender_entry = customtkinter.CTkEntry(frame, font = font2, text_color = '#000', fg_color = '#fff', border_color = '#B2016C', border_width = 2, width = 160)
gender_entry.place(x = 20, y =240)

add_button = customtkinter.CTkButton(frame, command = insert,  font = font2, text_color = '#fff', text = 'Add', fg_color = '#047E43', hover_color = '#025B30', bg_color = '#1B1B21', cursor = 'hand2', corner_radius = 8, width = 80)
add_button.place(x = 15, y = 280)

clear_button = customtkinter.CTkButton(frame, command = lambda: clear(True),font = font2, text_color = '#fff', text = 'New', fg_color = '#E93E05', hover_color = '#A82A00', bg_color = '#1B1B21', cursor = 'hand2', corner_radius = 8,  width = 80)
clear_button.place(x = 108, y = 280)

update_button = customtkinter.CTkButton(frame, command = update,  font = font2, text_color = '#fff', text = 'Update', fg_color = '#E93E05', hover_color = '#A82A00', bg_color = '#1B1B21', cursor = 'hand2', corner_radius = 8,  width = 80)
update_button.place(x = 15, y = 320)

delete_button = customtkinter.CTkButton(frame, command = delete, font = font2, text_color = '#fff', text = 'Delete', fg_color = '#D20B02', hover_color = '#8F0600', bg_color = '#1B1B21', cursor = 'hand2', corner_radius = 8,  width = 80)
delete_button.place(x = 108, y = 320)

style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview', font = font3, foreground = '#fff', background = '#0A0B0C', fieldbackground = '#1B1B21')
style.map('Treeview', background = [('selected', '#AA0407')])

tree = ttk.Treeview(app, height = 17)

tree['columns'] = ('Class Number', 'Name', 'Gender')
tree.column('#0', width = 0, stretch = tk.NO)
tree.column('Class Number', anchor = tk.CENTER, width = 150)
tree.column('Name', anchor = tk.CENTER, width = 150)
tree.column('Gender', anchor = tk.CENTER, width = 150)

tree.heading('Class Number', text = 'Class Number')
tree.heading('Name', text = 'Name')
tree.heading('Gender', text = 'Gender')

tree.place(x = 300, y = 57)

tree.bind('<ButtonRelease>', display_data)

#add_to_treeview()
#create_chart()

app.mainloop()
