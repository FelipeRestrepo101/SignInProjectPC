import tkinter as tk
import datetime
# import sqlite3 as sql
import mysql.connector as mysql


def get_input():
    user_input_Name = entry_label_Name.get()
    user_input_Email = entry_label_Email.get()

    # start of db code

    #"usersdb" database must already be created in MySQL server
    #upon clicking the  'sign in' button this script will now create the users table if it does not exist
    #Otherwise it will access the existing 'users' table, and insert the sign in entry as a new record. 
    db = mysql.connect(
      host='localhost',
      user='root',        #replace with MySQL authorized username
      password='****',    #replace with password
      database='usersdb', 
      #port used to specify MySQL instance port, otherwise defaults to 3306
      port=3307
    )
    c = db.cursor()

    #STRING is sometimes a valid datatype for databases, but TEXT or VARCHAR(255) is more reliable
    c.execute('''
            CREATE TABLE IF NOT EXISTS users
            (name TEXT, email TEXT, datetime DATETIME)
              ''')
    
    #(? ? ?) as placeholders is used for sqlite, (%s, %s, %s) is used for mysql
    #also changed previous "age INT" column to "email TEXT", below and above, not sure why that worked before
    c.execute('''
            INSERT INTO users (name, email, datetime) VALUES (%s, %s, %s) 
              ''', (user_input_Name, user_input_Email, datetime.datetime.now())
             )
    
    db.commit()
    # end of db code
    

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
