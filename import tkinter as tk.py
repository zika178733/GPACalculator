import tkinter as tk
from tkinter import messagebox

# Grade to point mapping
grade_points = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

courses = []

# Add course function
def add_course():
    name = course_name_entry.get()
    grade = grade_entry.get().upper()
    try:
        unit = int(unit_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Unit must be a number.")
        return

    if grade not in grade_points:
        messagebox.showerror("Invalid grade", "Enter grade A to F.")
        return

    point = grade_points[grade]
    courses.append((name, grade, unit, point))
    course_listbox.insert(tk.END, f"{name} - Grade: {grade}, Unit: {unit}, Point: {point}")
    
    # Clear input fields
    course_name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    unit_entry.delete(0, tk.END)

# Calculate GPA function
def calculate_gpa():
    if not courses:
        messagebox.showinfo("No Courses", "Add at least one course.")
        return

    total_units = sum(course[2] for course in courses)
    total_points = sum(course[2] * course[3] for course in courses)
    gpa = total_points / total_units
    result_label.config(text=f"🎓 Your GPA is: {gpa:.2f}", fg="blue")

# Save to file function
def save_to_file():
    if not courses:
        messagebox.showinfo("No Data", "No courses to save.")
        return

    total_units = sum(course[2] for course in courses)
    total_points = sum(course[2] * course[3] for course in courses)
    gpa = total_points / total_units

    with open("gpa_result.txt", "w") as file:
        file.write("GPA Result Summary\n\n")
        for course in courses:
            file.write(f"{course[0]} - Grade: {course[1]}, Unit: {course[2]}, Point: {course[3]}\n")
        file.write(f"\nTotal Units: {total_units}\n")
        file.write(f"GPA: {gpa:.2f}\n")

    messagebox.showinfo("Saved", "Results saved to 'gpa_result.txt'.")

# Clear everything
def clear_all():
    courses.clear()
    course_listbox.delete(0, tk.END)
    result_label.config(text="")
    course_name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    unit_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("🎓 Student GPA Calculator")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

# Title Label
title = tk.Label(root, text="GPA Calculator", font=("Helvetica", 18, "bold"), bg="#f2f2f2", fg="#333")
title.pack(pady=10)

# Input frame
input_frame = tk.Frame(root, bg="#f2f2f2")
input_frame.pack(pady=5)

tk.Label(input_frame, text="Course Name:", bg="#f2f2f2").grid(row=0, column=0, sticky="w")
course_name_entry = tk.Entry(input_frame, width=30)
course_name_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Grade (A-F):", bg="#f2f2f2").grid(row=1, column=0, sticky="w")
grade_entry = tk.Entry(input_frame, width=30)
grade_entry.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="Course Unit:", bg="#f2f2f2").grid(row=2, column=0, sticky="w")
unit_entry = tk.Entry(input_frame, width=30)
unit_entry.grid(row=2, column=1, pady=5)

# Button frame
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Course", bg="#4CAF50", fg="white", width=12, command=add_course).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Calculate GPA", bg="#2196F3", fg="white", width=12, command=calculate_gpa).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Save to File", bg="#FF9800", fg="white", width=12, command=save_to_file).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Clear All", bg="#F44336", fg="white", width=12, command=clear_all).grid(row=0, column=3, padx=5)

# Listbox to show added courses
course_listbox = tk.Listbox(root, width=60, height=10)
course_listbox.pack(pady=10)

# GPA Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f2f2f2")
result_label.pack(pady=10)

# Start the app
root.mainloop()
