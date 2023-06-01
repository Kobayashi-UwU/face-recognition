import tkinter as tk
import tkinter.font as tkFont
import subprocess


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        scanning_but = tk.Button(root)
        scanning_but["bg"] = "#6b6b6b"
        ft = tkFont.Font(family="Times", size=10)
        scanning_but["font"] = ft
        scanning_but["fg"] = "#ffffff"
        scanning_but["justify"] = "center"
        scanning_but["text"] = "Scanning"
        scanning_but.place(x=220, y=220, width=148, height=43)
        scanning_but["command"] = self.scanning_but_command

        add_new_person = tk.Button(root)
        add_new_person["bg"] = "#6b6b6b"
        ft = tkFont.Font(family="Times", size=10)
        add_new_person["font"] = ft
        add_new_person["fg"] = "#ffffff"
        add_new_person["justify"] = "center"
        add_new_person["text"] = "Add new person"
        add_new_person.place(x=220, y=290, width=144, height=43)
        add_new_person["command"] = self.add_new_person_command

        delete_person = tk.Button(root)
        delete_person["bg"] = "#6b6b6b"
        ft = tkFont.Font(family="Times", size=10)
        delete_person["font"] = ft
        delete_person["fg"] = "#ffffff"
        delete_person["justify"] = "center"
        delete_person["text"] = "Delete person"
        delete_person.place(x=220, y=360, width=144, height=43)
        delete_person["command"] = self.delete_person_command

        GLabel_250 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=38)
        GLabel_250["font"] = ft
        GLabel_250["fg"] = "#c8c3bc"
        GLabel_250["justify"] = "center"
        GLabel_250["text"] = "Face scanning"
        GLabel_250.place(x=130, y=90, width=331, height=75)

    def scanning_but_command(self):
        subprocess.run(["python", "./recognition.py"])

    def add_new_person_command(self):
        subprocess.run(["python", "./addimage.py"])

    def delete_person_command(self):
        subprocess.run(["python", "./deletemember.py"])


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
