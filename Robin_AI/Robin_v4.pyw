from tkinter.constants import TRUE
from tkinter.messagebox import askokcancel
import Commands
from Modules import *
from Responses_Keys import *
import GUI_Creator
import threading
import time
import traceback


i = 0


def main_commands():
    global i
    while True:
        try:
            if Commands.GUI is not None and not Commands.GUI:
                try:
                    GUI_Creator.exit_func()
                except:
                    exit()

            GUI_Creator.lab.config(bg="light green")
            GUI_Creator.change_client("")
            command = take_cmd()
            GUI_Creator.lab.config(bg="black")
            GUI_Creator.change_client(command)

            # if command != "":
            # time.sleep(1)

            if not Commands.Sleep:
                GUI_Creator.Rob.set("")
                Commands.Active = False
                Commands.run_robin("", command)
                Commands.Unable = False
            else:
                GUI_Creator.Rob.set("ROBIN IS IN SLEEP MODE!")

                for com in commands["wake_up"]:
                    if com in command and "robin" in command:
                        Commands.Sleep, Commands.Active, Commands.Unable = False, True, False
                        GUI_Creator.Rob.set("")
                        intro()
                        Commands.run_robin(com, command)
        except AttributeError:
            time.sleep(1)
            try:
                GUI_Creator.Rob.set("LOADING..")
                GUI_Creator.Cl.set("LOADING..")
                GUI_Creator.lab.config(bg="black")
        
                i += 1
                if i >= 5:
                    e = traceback.format_exc()
                    GUI_Creator.fatal(i, False, e, "Error", True)
            except AttributeError:        
                i += 1
                if i >= 5:
                    e = traceback.format_exc()
                    GUI_Creator.fatal(i, False, e, "Error", True)
            except:
                b = traceback.format_exc()
                GUI_Creator.fatal(0, True, b, "Error", True)


thread_new = threading.Thread(target=main_commands)
thread_new.setDaemon(True)
thread_new.start()

GUI_Creator.execute_gui()
