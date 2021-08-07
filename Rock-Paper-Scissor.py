# Import Required Library
from tkinter import *
import random
from PIL import ImageTk,Image
  
# Create Object
root = Tk()
  
# Set geometry
root.geometry("400x400")
  
# Set title
root.title("Rock Paper Scissor Game")

#set window color
#root['background']='#856ff8'
root.configure(bg='yellow')
  
# Computer Value
computer_value = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}
  
# Reset The Game
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Player              ")
    l3.config(text = "Computer")
    l4.config(text = "")
  
# Disable the Button
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
  
# If player selected rock
def isrock():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v=="Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l4.config(text = match_result)
    l1.config(text = "Rock            ")
    l3.config(text = c_v)
    button_disable()
  
# If player selected paper
def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v=="Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    l4.config(text = match_result)
    l1.config(text = "Paper           ")
    l3.config(text = c_v)
    button_disable()
  
# If player selected scissor
def isscissor():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Computer Win"
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    l4.config(text = match_result)
    l1.config(text = "Scissor         ")
    l3.config(text = c_v)
    button_disable()
  
# Add Labels, Frames and Button
Label(root,
      text = "Rock Paper Scissor",
      font = "normal 20 bold",
      fg = "blue").pack(pady = 20)
  
frame = Frame(root)
frame.pack()
  
l1 = Label(frame,
           text = "Player              ",
           font = 10)
  
l2 = Label(frame,
           text = "VS             ",
           font = "normal 10 bold")
  
l3 = Label(frame, text = "Computer", font = 10)
  
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()
  
l4 = Label(root,
           text = " ",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 20)
  
frame1 = Frame(root)
frame1.pack()

# Read the Image
image = Image.open("C:/Users/SayantiMondal/Desktop/Data_science/rock.png")
# Reszie the image using resize() method
resize_image = image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(frame1,image=img)
label1.image = img
label1.pack(side = "left",padx = 20)
#label1.grid(column=0,row=0)

# Read the Image
image = Image.open("C:/Users/SayantiMondal/Desktop/Data_science/paper.jpg")
# Reszie the image using resize() method
resize_image = image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label2 = Label(frame1,image=img)
label2.image = img
label2.pack(side = LEFT,padx = 30)
#label2.grid(column=1,row=0)

# Read the Image
image = Image.open("C:/Users/SayantiMondal/Desktop/Data_science/scissor.jpg")
# Reszie the image using resize() method
resize_image = image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label3 = Label(frame1,image=img)
label3.image = img
label3.pack(padx = 30)
#label2.grid(column=1,row=0)

frame2 = Frame(root)
frame2.pack()
  
b1 = Button(frame2, text = "Rock",
            font = 10, width = 7,
            command = isrock)
  
b2 = Button(frame2, text = "Paper ",
            font = 10, width = 7,
            command = ispaper)
  
b3 = Button(frame2, text = "Scissor",
            font = 10, width = 7,
            command = isscissor)
  
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)
  
Button(root, text = "Reset Game",
       font = 10, fg = "red",
       bg = "black", command = reset_game).pack(pady = 20)
  
# Excecute Tkinter
root.mainloop()