import tkinter as tk

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("80/20 Material List")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="View Metric Material", command=self.open_window2)
        self.button.pack()

    def open_window2(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window2(self.new_window)
#Metric options
class Window2:
    def __init__(self, master,):
        self.master = master
        self.master.title("Metric Material")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="View Standard Material", command=self.open_window3)
        self.button.pack()
        self.button = tk.Button(self.master, text="40 Series", command=self.open_window4)
        self.button.pack()
        self.button = tk.Button(self.master, text="30 Series", command=self.open_window5)
        self.button.pack()
        self.button = tk.Button(self.master, text="25 Series", command=self.open_window6)
        self.button.pack()
        self.button = tk.Button(self.master, text="45 Series", command=self.open_window7)
        self.button.pack()
        self.button = tk.Button(self.master, text="20 Series", command=self.open_window8)
        self.button.pack()

    def open_window8(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window8(self.new_window)
    
    def open_window7(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window7(self.new_window)

    def open_window6(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window6(self.new_window)

    def open_window5(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window5(self.new_window)

    def open_window4(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window4(self.new_window)

    def open_window3(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window3(self.new_window)
#40 Series
class Window4:
    def __init__(self, master):
        self.master = master
        self.master.title("40 Series")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="40mm x 120mm cost $2.31 per inch", command=self.open_window12)
        self.button.pack()
        self.button = tk.Button(self.master, text="40mm x 20mm cost $.50 per inch", command=self.open_window13)
        self.button.pack()
        self.button = tk.Button(self.master, text="40mm x 40mm cost $.86 per inch", command=self.open_window14)
        self.button.pack()
        self.button = tk.Button(self.master, text="80mm x 80mm cost $2.39 per inch", command=self.open_window15)
        self.button.pack()

    def open_window12(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window12(self.new_window)

    def open_window13(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window13(self.new_window)

    def open_window14(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window14(self.new_window)

    def open_window15(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window15(self.new_window)

class Window12:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = 2.31
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")
    
    

class Window13:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .50
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window14:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .86
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window15:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = 2.39
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")       

#30 Series
class Window5:
    def __init__(self, master):
        self.master = master
        self.master.title("30 Series")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="30mm x 30mm cost $.34 per inch", command=self.open_window16)
        self.button.pack()
        self.button = tk.Button(self.master, text="30mm x 60mm cost $.84 per inch", command=self.open_window17)
        self.button.pack()
        self.button = tk.Button(self.master, text="60mm x 60mm cost $1.40 per inch", command=self.open_window18)
        self.button.pack()

    def open_window16(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window16(self.new_window) 

    def open_window17(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window17(self.new_window)

    def open_window18(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window18(self.new_window)  

class Window16:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .34
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window17:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .84
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window18:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = 1.40
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

#25 Series
class Window6:
    def __init__(self, master):
        self.master = master
        self.master.title("25 Series")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="25mm x 25mm cost $.30 per inch", command=self.open_window19)
        self.button.pack()
        self.button = tk.Button(self.master, text="25mm x 50mm cost $.54 per inch", command=self.open_window20)
        self.button.pack()
        self.button = tk.Button(self.master, text="25mm x 76mm cost $.79 per inch", command=self.open_window21)
        self.button.pack()
        self.button = tk.Button(self.master, text="50mm x 50mm cost $.84 per inch", command=self.open_window22)
        self.button.pack()

    def open_window19(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window19(self.new_window)

    def open_window20(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window20(self.new_window)

    def open_window21(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window21(self.new_window)

    def open_window22(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window22(self.new_window)

class Window19:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .30
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window20:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .54
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window21:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .79
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window22:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .84
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

#45 Series
class Window7:
    def __init__(self, master):
        self.master = master
        self.master.title("45 Series")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="45mm x 45mm cost $.79 per inch", command=self.open_window23)
        self.button.pack()
        self.button = tk.Button(self.master, text="45mm x 90mm cost $1.89 per inch", command=self.open_window24)
        self.button.pack()
        self.button = tk.Button(self.master, text="90mm x 90mm cost $3.22 per inch", command=self.open_window25)
        self.button.pack()

    def open_window23(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window23(self.new_window)

    def open_window24(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window24(self.new_window)

    def open_window25(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window25(self.new_window)  

class Window23:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .79
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window24:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = 1.89
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window25:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = 3.22
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches") 

#20 Series
class Window8:
    def __init__(self, master):
        self.master = master
        self.master.title("20 Series")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="20mm x 20mm cost $.25 per inch", command=self.open_window26)
        self.button.pack()
        self.button = tk.Button(self.master, text="20mm x 40mm cost $.42 per inch", command=self.open_window27)
        self.button.pack()
        self.button = tk.Button(self.master, text="40mm x 40mm cost $.72 per inch", command=self.open_window28)
        self.button.pack()

    def open_window26(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window26(self.new_window)

    def open_window27(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window27(self.new_window)

    def open_window28(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window28(self.new_window)

class Window26:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .25
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window27:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .42
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window28:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .72
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

#Standard Options       
class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Standard Material")
        self.master.geometry("700x700")
        self.label = tk.Label(self.master, text="80/20 Standard Material")
        self.label.pack()
        self.button = tk.Button(self.master, text="15 Series", command=self.open_window9)
        self.button.pack()
        self.button = tk.Button(self.master, text="10 Series", command=self.open_window10)
        self.button.pack()

    def open_window9(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window9(self.new_window)

    def open_window10(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window10(self.new_window)   

#15 Series
class Window9:
    def __init__(self, master):
        self.master = master
        self.master.title("15 Series")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="1.5in x 1.5in cost $.77 per inch", command=self.open_window29)
        self.button.pack()
        self.button = tk.Button(self.master, text="1.5in x 3.0in cost $1.42 per inch", command=self.open_window30)
        self.button.pack()
        self.button = tk.Button(self.master, text="1.5in x 4.5in cost $2.12 per inch", command=self.open_window31)
        self.button.pack()
        self.button = tk.Button(self.master, text="3.0in x 3.0in cost $2.25 per inch", command=self.open_window32)
        self.button.pack()

    def open_window29(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window29(self.new_window)

    def open_window30(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window30(self.new_window)

    def open_window31(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window31(self.new_window)

    def open_window32(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window32(self.new_window)

class Window29:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .77
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window30:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = 1.42
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window31:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = 2.12
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window32:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = 2.25
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

#10 Series       
class Window10:
    def __init__(self, master):
        self.master = master
        self.master.title("10 Series")
        self.master.geometry("700x700")
        self.button = tk.Button(self.master, text="1.0in x 1.0in cost $.35 per inch", command=self.open_window33)
        self.button.pack()
        self.button = tk.Button(self.master, text="1.0in x 2.0in cost $.62 per inch", command=self.open_window34)
        self.button.pack()
        self.button = tk.Button(self.master, text="1.0in x 3.0in cost $.84 per inch", command=self.open_window35)
        self.button.pack()
        self.button = tk.Button(self.master, text="2.0in x 2.0in cost $.88 per inch", command=self.open_window36)
        self.button.pack()
        self.button = tk.Button(self.master, text="2.0in x 4.0in cost $1.59 per inch", command=self.open_window37)
        self.button.pack()

    def open_window33(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window33(self.new_window)

    def open_window34(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window34(self.new_window)

    def open_window35(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window35(self.new_window)

    def open_window36(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window36(self.new_window)

    def open_window37(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window37(self.new_window)

class Window33:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .35
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window34:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .62
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window35:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .84
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window36:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = .88
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

class Window37:
    def __init__(self, master):
        self.master = master
        self.master.title("Machining/Lenght")
        self.master.geometry("700x700")
        self.label = input("What lenght would you like the bar?")
        self.price = 1.59
        total = self.label * self.price
        print(f"The lenght of you bar is {total} inches")

def main():
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()