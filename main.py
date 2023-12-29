from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list= password_letters + password_symbols +password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    #for char in password_list:
    #  password += char

    password_entry.insert(0,password)
    pyperclip.copy(password)


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data={website: {
                "email" :email,
                "password": password,
        }
    }

    if len(website) == 0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open("data.json","r") as data_file:
                #Reading the old data
                data = json.load((data_file))
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)

        else:
            # upadating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()

        messagebox.askokcancel(title="Message",message="Your information has been stored")

window = Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)

canvas = Canvas(height=200,width=200)
logo_img= PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)


canvas.grid(row=0,column=1)
#Labels
website_label = Label(text="Website :")
website_label.grid(row=1,column=0)
website_label.config(padx=20,pady=20)

email_label = Label(text="Email/Username")
email_label.grid(column=0,row=2)
email_label.config(padx=5,pady=5)

password_label=Label(text="Password")
password_label.grid(column=0,row=3)
password_label.config(padx=20,pady=20)

#entries
website_entry = Entry(width=70)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=70)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"abc@gmail.com")
password_entry = Entry(width=40)
password_entry.grid(row=3,column=1)

#Buttons
generate_password = Button(text="Generate Password",width=22,command=generate_password)
generate_password.grid(row=3,column=2)
#generate_password.config(padx=20,pady=20)

add_button =Button(text="Add",width=33,command=save)
add_button.grid(row=4,column=1)


window.mainloop()