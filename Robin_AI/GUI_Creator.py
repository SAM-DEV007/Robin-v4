from time import time
from tkinter import *
import tkinter
import tkinter.font as font
from tkinter import messagebox
import Commands
from Responses_Keys import *
from Data import *
import Modules
import time

Rob, Cl, User, Option, a_user, a_voice, root, lab = None, None, None, None, None, None, None, None
Settings_Open, dest = False, False


class GUI(Frame):

    def __init__(self, window):
        global Rob, Cl, lab

        Frame.__init__(self, window)
        window.geometry("750x550")

        self.pack()

        # Main Labels

        label = Label(window, text="VIRTUAL ASSISTANT", foreground="blue", bg="white", width="500")
        label['font'] = font.Font(family="Cooper", size="30")
        label.pack(side="top")

        cred = Label(window, text="Robin is currently Under Development!", width="500",
                     bg="black", fg="white")
        cred['font'] = font.Font(family="Cooper", size="9")
        cred.pack(side="bottom")

        # Robin Text Display

        robin = Label(window, text="Robin", bg="white", width="50")
        robin['font'] = font.Font(family="Arial", size="15")
        robin.pack(pady="20")

        Rob = StringVar()
        Rob.set("LOADING..")
        lbl = Label(window, textvariable=Rob, bg="yellow", width="50", height="4",
                    wraplength="400", justify="left")
        lbl['font'] = font.Font(family="Cooper", size="10")
        lbl.pack(pady="20")

        lab = Label(window, bg="black", width="10", text="Listening...", fg="black")
        lab.pack(pady="10")

        # Client Text Display

        client = Label(window, text="User", bg="white", width="50")
        client['font'] = font.Font(family="Cooper", size="15")
        client.pack(pady="20")

        Cl = StringVar()
        Cl.set("LOADING..")
        label = Label(window, textvariable=Cl, bg="yellow", width="50", height="4",
                      wraplength="400", justify="left")
        label['font'] = font.Font(family="Cooper", size="10")
        label.pack(pady="20")

        # Settings Menu

        button = Button(window, text="SETTINGS", width="30", height="1", command=settings_frame)
        button.pack(pady="20")

        # Function with `after` loop

        def rip_win():
            global dest

            if dest:
                window.destroy()
                exit()

            window.after(1000, rip_win)

        window.after(1000, rip_win)


class Settings(Frame):
    def __init__(self, win):
        global User, Option

        Frame.__init__(self, win)
        win.geometry("750x500")

        self.pack()

        # Main Frames

        label = Label(win, text="SETTINGS", foreground="blue", bg="white", width="500")
        label['font'] = font.Font(family="Cooper", size="30")
        label.pack(side="top")

        cred = Label(win, text="Robin is currently Under Development!", width="500",
                     bg="black", fg="white")
        cred['font'] = font.Font(family="Cooper", size="9")
        cred.pack(side="bottom")

        # User Name

        user_title = Label(win, text="WHAT SHOULD ASSISTANT CALL YOU?", foreground="white", bg="black", width="40",
                           height="2")
        user_title['font'] = font.Font(family="Cooper", size="10")
        user_title.pack(pady="20")

        User = StringVar()
        User.set(str(a_user))
        user = Entry(win, text="", foreground="BLACK", bg="YELLOW", width="40",
                     textvariable=User)
        user['font'] = font.Font(family="Cooper", size="10")
        user.pack(pady="10")

        # Assistant Voice

        user_title = Label(win, text="ASSISTANT VOICE", foreground="white", bg="black", width="40",
                           height="2")
        user_title['font'] = font.Font(family="Cooper", size="10")
        user_title.pack(pady="20")

        Option = StringVar()
        Option.set(str(a_voice))
        option_list = ["Male", "Female"]
        menu = OptionMenu(win, Option, *option_list)
        menu.pack(pady="10")

        # Auto_Save

        def save_info():
            save_data_to_file()
            win.after(1000, save_info)

        win.after(1000, save_info)



def save_data_to_file():
    button_execute_voice()
    main_function(True, User.get(), Option.get())


def execute_gui():
    global root, a_user, a_voice

    rto = Tk()
    root = rto
    root.title("Robin AI")

    data_received = main_function(False)
    a_user = data_received["User"]
    a_voice = data_received["Voice"]
    button_execute_voice(True)

    win = GUI(root)
    Commands.GUI = True
    win.mainloop()
    Commands.GUI = False


def button_execute_voice(load=False):
    voices = Modules.replier.getProperty('voices')

    if load:
        data = main_function(False)
        if data["Voice"] == "Male":
            Modules.replier.setProperty('voice', voices[0].id)
        else:
            Modules.replier.setProperty('voice', voices[1].id)
        return None
    else:
        option_selected = Option.get()
        Option.set(option_selected)
        if Option.set == "Male":
            Modules.replier.setProperty('voice', voices[0].id)
        else:
            Modules.replier.setProperty('voice', voices[1].id)


def settings_frame():
    global a_user, a_voice, root

    rt = Toplevel(root)
    rt.title("Settings")

    data_received = main_function(False)
    a_user = data_received["User"]
    a_voice = data_received["Voice"]

    Settings(rt)
    # window.mainloop()


def change_client(command_given):
    global Cl

    Cl.set(command_given)


def fatal(i_val=0, veto=False, msg="", box="Error", exit_func=False):
    global dest

    if i_val >= 5 or veto:
        if box == "Error":
            messagebox.showerror("ERROR", "A fatal error occured!")         
        elif box == "Warn":
            messagebox.showwarning("WARNING", "A server error occured! Please try again later!")
        
        response = messagebox.askokcancel("Confirmation", "Do you wish to see the error?")      
        if response:
            messagebox.showinfo("ERROR", msg)
        if exit_func:
            dest = True


def exit_func():
    global dest
    dest = True


# execute_gui()
# settings_frame()
