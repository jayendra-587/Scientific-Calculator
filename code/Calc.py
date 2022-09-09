# Liberaries
import os
from sys import flags
import tkinter 
#import sci_calculator 
from tkinter import *  
from tkinter import messagebox  
  
# setting the initial values of some variables  
var = ""  
A = 0  
operator = "" 


#scientific calculator button
def button_sci_is_Clicked():
    os.system(r"D:\UPES\Project\Minor\Scientific-Calculator\code\sci_calculator.py")
    # guiWindow.destroy() 
  
# defining the function for Button 1  
def button_1_is_Clicked():  
    global var  
    var = var + "1"  
    the_data.set(var)  
  
# defining the function for Button 2  
def button_2_is_Clicked():  
    global var  
    var = var + "2"  
    the_data.set(var)  
  
# defining the function for Button 3  
def button_3_is_Clicked():  
    global var  
    var = var + "3"  
    the_data.set(var)  
  
# defining the function for Button 4  
def button_4_is_Clicked():  
    global var  
    var = var + "4"  
    the_data.set(var)  
  
# defining the function for Button 5  
def button_5_is_Clicked():  
    global var  
    var = var + "5"  
    the_data.set(var)  
  
# defining the function for Button 6  
def button_6_is_Clicked():  
    global var  
    var = var + "6"  
    the_data.set(var)  
  
# defining the function for Button 7  
def button_7_is_Clicked():  
    global var  
    var = var + "7"  
    the_data.set(var)  
  
# defining the function for Button 8  
def button_8_is_Clicked():  
    global var  
    var = var + "8"  
    the_data.set(var)  
  
# defining the function for Button 9  
def button_9_is_Clicked():  
    global var  
    var = var + "9"  
    the_data.set(var)  
  
# defining the function for Button 0  
def button_0_is_Clicked():  
    global var  
    var = var + "0"  
    the_data.set(var)  
  
# defining the function for Button +  
def button_Add_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    the_data.set(var)  
  
# defining the function for Button -  
def button_Sub_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    the_data.set(var)  
  
# defining the function for Button *  
def button_Mul_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    the_data.set(var)  
  
# defining the function for Button /  
def button_Div_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    the_data.set(var)  
  
# defining the function for Button =  
def button_Equal_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "="  
    var = var + "="  
    the_data.set(var)  
  
# defining the function for Button C  
def button_C_is_Clicked():  
    global A  
    global var  
    global operator  
    var = ""  
    A = 0  
    operator = ""  
    the_data.set(var)  
  
# defining the function to display result  
def res():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1])) 
        print("var = ", var)
        print("a = ", a)
        print("A = ", A)
        x = A - a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:  
            messagebox.showerror("Error!", "Division by 0 Not Allowed.")  
            A == ""  
            var = ""  
            the_data.set(var)  
        else:  
            x = float(A/a)  
            the_data.set(x)  
            var = str(x)  
  
# creating an object of the Tk() class  
guiWindow = tkinter.Tk()

# setting the size and position of the window  
guiWindow.geometry("320x500+400+30") 


# we can disable GUI resizing function through this 
# guiWindow.resizable(0, 0) 


# Title of the basic calc window  
guiWindow.title("Calculator")  


# creating the label (display) for the window  
the_data = StringVar()  
guiLabel = Label(  
    guiWindow,  
    # text = "Label",  
    anchor = E,  
    font = ("Cambria Math", 20),  
    textvariable = the_data,  # text gets override when textvariable is present
    background = "#ffffff",  
    fg = "#000000",
    cursor="arrow"
)  

# using the pack() method for display or label
guiLabel.pack(expand = True, fill = "both")  
  

# creating the frames for the buttons  
# first frame  
frameOne = Frame(guiWindow, bg = "#F0F0F0")  
frameOne.pack(expand = True, fill = "x") # frame can expand if it gets some space  
  
# second frame  
frameTwo = Frame(guiWindow, bg = "#000000")  
frameTwo.pack(expand = True, fill = "both")  
  
# third frame  
frameThree = Frame(guiWindow, bg = "#000000")  
frameThree.pack(expand = True, fill = "both")  
  
# fourth frame  
frameFour = Frame(guiWindow, bg = "#000000")  
frameFour.pack(expand = True, fill = "both")  
  
# fifth frame
frameFive = Frame(guiWindow, bg = "#000000")
frameFive.pack(expand = True, fill = "both")

# creating buttons for each frame  
# buttons for first frame 

# Change to scientific calculator window
b = Button(
    frameOne,
    text = "Scientific Calculator",
    font = ("Cambria", 17),
    # bg="#FF69B4",
    relief = GROOVE,  
    # highlightthickness = 4, 
    command = button_sci_is_Clicked  
)

b.pack()

# button 1  
buttonONE = Button(  
    frameTwo,  
    text = "1",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_1_is_Clicked  
)  
# placing buttons side by side  
buttonONE.pack(side = LEFT, expand = True, fill = "both")  


  
# button 2  
buttonTWO = Button(  
    frameTwo,  
    text = "2",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_2_is_Clicked  
)  
# placing buttons side by side  
buttonTWO.pack(side = LEFT, expand = True, fill = "both")  
  
# button 3  
buttonTHREE = Button(  
    frameTwo,  
    text = "3",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_3_is_Clicked  
)  
# placing buttons side by side  
buttonTHREE.pack(side = LEFT, expand = True, fill = "both")  
  
# button C  
buttonC = Button(  
    frameTwo,  
    text = "C",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_C_is_Clicked  
)  
# placing buttons side by side  
buttonC.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for second frame  
# button 4  
buttonFOUR = Button(  
    frameThree,  
    text = "4",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_4_is_Clicked  
)  
# placing buttons side by side  
buttonFOUR.pack(side = LEFT, expand = True, fill = "both")  
  
# button 5  
buttonFIVE = Button(  
    frameThree,  
    text = "5",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_5_is_Clicked  
)  
# placing buttons side by side  
buttonFIVE.pack(side = LEFT, expand = True, fill = "both")  
  
# button 6  
buttonSIX = Button(  
    frameThree,  
    text = "6",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_6_is_Clicked  
)  
# placing buttons side by side  
buttonSIX.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonADD = Button(  
    frameThree,  
    text = "+",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Add_is_Clicked  
)  
# placing buttons side by side  
buttonADD.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for third frame  
# button 7  
buttonSEVEN = Button(  
    frameFour,  
    text = "7",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_7_is_Clicked  
)  
# placing buttons side by side  
buttonSEVEN.pack(side = LEFT, expand = True, fill = "both")  
  
# button 8  
buttonEIGHT = Button(  
    frameFour,  
    text = "8",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_8_is_Clicked  
)  
# placing buttons side by side  
buttonEIGHT.pack(side = LEFT, expand = True, fill = "both")  
  
# button 9  
buttonNINE = Button(  
    frameFour,  
    text = "9",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_9_is_Clicked  
)  
# placing buttons side by side  
buttonNINE.pack(side = LEFT, expand = True, fill = "both")  
  
# button -  
buttonSUB = Button(  
    frameFour,  
    text = "-",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Sub_is_Clicked  
)  
# placing buttons side by side  
buttonSUB.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for fourth frame  
# button 0  
buttonZERO = Button(  
    frameFive,  
    text = "0",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_0_is_Clicked  
)  
# placing buttons side by side  
buttonZERO.pack(side = LEFT, expand = True, fill = "both")  
  
# button *  
buttonMUL = Button(  
    frameFive,  
    text = "*",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Mul_is_Clicked  
)  
# placing buttons side by side  
buttonMUL.pack(side = LEFT, expand = True, fill = "both")  
  
# button /  
buttonDIV = Button(  
    frameFive,  
    text = "/",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Div_is_Clicked  
)  
# placing buttons side by side  
buttonDIV.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonEQUAL = Button(  
    frameFive,  
    text = "=",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = res  
)  
# placing buttons side by side  
buttonEQUAL.pack(side = LEFT, expand = True, fill = "both") 


# # replacing default tkinter logo
# guiWindow.wm_attributes('-toolwindow', 'True') # it is used to completely remove the logo
photo = PhotoImage(file = r'D:\UPES\Project\Minor\Scientific-Calculator\logo\logo.png')
guiWindow.iconphoto(False, photo)

# running the GUI  
guiWindow.mainloop()