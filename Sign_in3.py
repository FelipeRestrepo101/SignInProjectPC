import tkinter as tk
import datetime



def get_input():
    user_input_Name = entry_label_Name.get()
    user_input_Email = entry_label_Email.get()

    print(user_input_Email, ',',  user_input_Name, ',', datetime.date.today())

    entry_label_Name.delete(0, tk.END)  # Clear the entry field
    entry_label_Email.delete(0, tk.END)  

window = tk.Tk()
window.title("Sign In Sheet")
window.geometry("600x400")

label_Name = tk.Label(window, text="Enter Your Name:")
label_Name.pack()
#label_Name.grid(row=0, column=0)

entry_label_Name = tk.Entry(window)
entry_label_Name.pack()
#entry_label_Name.grid(row=0, column=1)

label_Email = tk.Label(window, text="Enter Your Student Email:")
label_Email.pack()

entry_label_Email = tk.Entry(window)
entry_label_Email.pack()

button = tk.Button(window, text="Sign in", command=get_input)
button.pack()

window.mainloop()
