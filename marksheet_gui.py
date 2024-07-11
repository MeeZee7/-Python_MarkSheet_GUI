import pandas as pd
from tkinter import *
import tkinter as tk

# Load the data
df = pd.read_csv("marksheet.csv", index_col="Roll No.")

def key_press(event):
    global roll_number
    roll_number = Roll_no_box.get()

def show(event=0):
    global roll_number
    fetch_marksheet(int(roll_number))

def fetch_marksheet(roll_number):
    try:
        result = df.loc[roll_number]
        
        name = result["Name"]
        maths_marks = result["Maths"]
        physics_marks = result["Physics"]
        chemistry_marks = result["Chemistry"]

        # Calculation of additional information
        total_marks_obtained = maths_marks + physics_marks + chemistry_marks
        percentage_obtained = (total_marks_obtained / 300) * 100

        # Grade calculation
        if percentage_obtained >= 40:
            grade = "PASS"
            message = "Congratulations, you did well!"
        else:
            grade = "Fail"
            message = "Sorry, better try hard next time."

        # Update the GUI with the fetched data
        name_box.delete(0, END)
        name_box.insert(0, name)
        
        maths_marks_box.delete(0, END)
        maths_marks_box.insert(0, maths_marks)
        
        physics_marks_box.delete(0, END)
        physics_marks_box.insert(0, physics_marks)
        
        chemistry_marks_box.delete(0, END)
        chemistry_marks_box.insert(0, chemistry_marks)
        
        total_marks_box.delete(0, END)
        total_marks_box.insert(0, total_marks_obtained)
        
        Percentage_box.delete(0, END)
        Percentage_box.insert(0, f"{percentage_obtained:.2f}")
        
        Result_box.delete(0, END)
        Result_box.insert(0, grade)

        result_label.config(text=message, font=("Arial", 14, "bold"))
    except KeyError:
        result_label.config(text="No record found for the given roll number", font=("Arial", 14, "bold"))

# Create the main window
top = Tk()
top.geometry("800x600")

# College name on top
College_name = Label(top, text="St. Vincent Pallotti College of Engineering and Technology Nagpur", font=("Arial", 20, "bold"))
College_name.place(relx=0.5, rely=0.05, anchor='center')

# Enter Roll no text
Roll_no = Label(top, text="Enter your Roll No.", font=("Arial", 11, "bold"))
Roll_no.place(relx=0.35, rely=0.15, anchor='center')

# Roll no enter box
Roll_no_box = Entry(top, width=30, font=('Arial', 18))
Roll_no_box.place(relx=0.57, rely=0.15, anchor='center')
Roll_no_box.bind('<Key>', key_press)
Roll_no_box.focus_set()

# Button to show result
result_button = Button(top, text="Show Result", command=show)
result_button.place(relx=0.78, rely=0.15, anchor='center')

# Name label
name_label = Label(top, text="Name", font=("Arial", 11, "bold"))
name_label.place(relx=0.35, rely=0.25, anchor='center')

# Name box
name_box = Entry(top, width=20, font=('Arial', 18))
name_box.place(relx=0.52, rely=0.25, anchor='center')

# Serial number label
serial_number_label = Label(top, text="Serial No.", font=("Arial", 11, "bold"))
serial_number_label.place(relx=0.35, rely=0.4, anchor='center')

# Serial numbers
serial_number_label1 = Label(top, text="1", font=("Arial", 11, "bold"))
serial_number_label1.place(relx=0.35, rely=0.48, anchor='center')

serial_number_label2 = Label(top, text="2", font=("Arial", 11, "bold"))
serial_number_label2.place(relx=0.35, rely=0.53, anchor='center')

serial_number_label3 = Label(top, text="3", font=("Arial", 11, "bold"))
serial_number_label3.place(relx=0.35, rely=0.58, anchor='center')

# Subject heading
subject_heading_label = Label(top, text="Subjects", font=("Arial", 11, "bold"))
subject_heading_label.place(relx=0.51, rely=0.4, anchor='center')

# Subject names
maths_label = Label(top, text="Mathematics", font=("Arial", 11, "bold"))
maths_label.place(relx=0.51, rely=0.48, anchor='center')

physics_label = Label(top, text="Physics", font=("Arial", 11, "bold"))
physics_label.place(relx=0.51, rely=0.53, anchor='center')

chemistry_label = Label(top, text="Chemistry", font=("Arial", 11, "bold"))
chemistry_label.place(relx=0.51, rely=0.58, anchor='center')

# Marks obtained heading
marks_obtained_label = Label(top, text="Marks obtained", font=("Arial", 11, "bold"))
marks_obtained_label.place(relx=0.7, rely=0.4, anchor='center')

# Marks obtained boxes
maths_marks_box = Entry(top, width=10, font=('Arial', 18))
maths_marks_box.place(relx=0.7, rely=0.48, anchor='center')

physics_marks_box = Entry(top, width=10, font=('Arial', 18))
physics_marks_box.place(relx=0.7, rely=0.53, anchor='center')

chemistry_marks_box = Entry(top, width=10, font=('Arial', 18))
chemistry_marks_box.place(relx=0.7, rely=0.58, anchor='center')

# Total marks obtained label
Total_marks_label = Label(top, text="Total Marks:", font=("Arial", 16, "bold"))
Total_marks_label.place(relx=0.2, rely=0.75, anchor='center')

# Total marks obtained box
total_marks_box = Entry(top, width=7, font=('Arial', 18))
total_marks_box.place(relx=0.3, rely=0.75, anchor='center')

# Percentage obtained label
Percentage_label = Label(top, text="Percentage(%):", font=("Arial", 16, "bold"))
Percentage_label.place(relx=0.45, rely=0.75, anchor='center')

# Percentage obtained box
Percentage_box = Entry(top, width=7, font=('Arial', 18))
Percentage_box.place(relx=0.56, rely=0.75, anchor='center')

# Result label
Result_label = Label(top, text="Result:", font=("Arial", 16, "bold"))
Result_label.place(relx=0.7, rely=0.75, anchor='center')

# Result box
Result_box = Entry(top, width=7, font=('Arial', 18))
Result_box.place(relx=0.78, rely=0.75, anchor='center')

# Create a Label to display the result
result_label = Label(top, text="", font=("Arial", 14, "bold"))
result_label.place(relx=0.5, rely=0.85, anchor='center')

# College logo
image = tk.PhotoImage(file="Svpcet-removebg.png")
label = tk.Label(top, image=image)
label.place(x=90, y=120)  # Adjust x and y for precise positioning

# Bind the Enter key to the window
top.bind('<Return>', show)

top.mainloop()



