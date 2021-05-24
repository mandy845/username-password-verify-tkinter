from tkinter import *
from tkinter import messagebox


def clear_entry():

    userentry.delete(0, 'end')
    entrypass.delete(0, 'end')

user_pass = {"Vuyani": "Vuya@2021", "Ikraam": "carsthemovie",
             "Nathan": "blue1",
             "Amanda": "@amanda28"}



def user_pass_search(username, _password, _dict):
     if username in _dict:
        if _password == _dict[username]:
             return 1
        else:
            return 0
     else:
        return -1

def verify():
    user = userentry.get()
    password = entrypass.get()

    x = int(user_pass_search(user, password, user_pass))
    print(" ")
    if x == 1:
        root.destroy()
        import verify

    elif x == 0:
        messagebox.showinfo("Alert","Incorrect password ")
    elif x == -1:
        messagebox.showinfo("Alert","Username Doesn't Exist")

def exit():
    mgbox=messagebox.askquestion("exit application", "are you sure you want to exit", icon="warning")

    if mgbox == "yes":
        root.destroy()
    else:
        messagebox.showinfo("return", "you'll return to your application")
root = Tk()
root.title("Password and username Verification")
root.geometry("500x400")

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

lbluser = Label(frame, text="Enter your Username")
lbluser.grid(row=1, column=1)

userentry = Entry(frame,)
userentry.grid(row=1, column=2, pady=5)

lblpass = Label(frame, text="Enter your Password")
lblpass.grid(row=2, column=1)

entrypass = Entry(frame,)
entrypass.grid(row=2, column=2, pady=5)

reset_btn = Button(frame, text='clear', bg='#346ab3', command=clear_entry)
reset_btn.grid(row=5, column=3, pady=5)

exit_btn = Button(frame, text='Exit', bg='#346ab3', command=exit)
exit_btn.grid(row=5, column=1, pady=5)

cal_btn = Button(frame, text='sign in', bg='#346ab3', command=verify)
cal_btn.grid(row=5, column=2, pady=5)


root.mainloop()