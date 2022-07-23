from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint


ActivePlayer = 1  # set active player
p1 = []   # what player 1 selected
p2 = []   # what player 2 selected

root = Tk()
root.title("Tic Tac Toy : Player1")  # title
style=ttk.Style()
style.theme_use('classic')  # to make difference shape

# ----------------------------button1--------------------------------------------------
bu1=ttk.Button(root,text=' ')  # to do button
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)  # dimensions of button 1
bu1.config(command=lambda : BuClick(1))  # when click on button, sending '1'
# ----------------------------button2--------------------------------------------------
bu2=ttk.Button(root,text=' ')
bu2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda : BuClick(2) )
# ----------------------------button3--------------------------------------------------
bu3=ttk.Button(root,text=' ')
bu3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda : BuClick(3) )
# ----------------------------button4--------------------------------------------------
bu4=ttk.Button(root,text=' ')
bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda : BuClick(4) )
# ----------------------------button5--------------------------------------------------
bu5=ttk.Button(root,text=' ')
bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda : BuClick(5) )
# ----------------------------button6--------------------------------------------------
bu6=ttk.Button(root,text=' ')
bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda : BuClick(6) )
# ----------------------------button7--------------------------------------------------
bu7=ttk.Button(root,text=' ')
bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda : BuClick(7) )
# ----------------------------button8--------------------------------------------------
bu8=ttk.Button(root,text=' ')
bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda : BuClick(8) )
# ----------------------------button9--------------------------------------------------
bu9=ttk.Button(root,text=' ')
bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda  : BuClick(9) )






def BuClick(id):
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(id, 'X')  # send id of button and X
        p1.append(id)  # call id (X) and add to p1
        root.title('Tic Tac Toy : Player2')  # change title when p1 end turn
        ActivePlayer = 2  # change p1 to p2
        print('P1:{}'.format(p1))  # print info. about p1
        AutoPlay()  # call function to play with machine


    elif (ActivePlayer == 2):
        SetLayout(id, 'O')  # send id of button and O
        p2.append(id)  # call id (O) and add to p2
        root.title('Tic Tac Toy : Player1')  # change title when p2 end turn
        ActivePlayer = 1  # change p2 to p1
        print('P2:{}'.format(p2))  # print info. about p2

    CheckWinner()





def SetLayout(id, text):  # function to send id , text
    if(id==1):
        bu1.config(text=text)  # change status
        bu1.state(['disabled'])  # default state

    elif (id == 2):
        bu2.config(text=text)
        bu2.state(['disabled'])

    elif (id == 3):
        bu3.config(text=text)
        bu3.state(['disabled'])

    elif (id == 4):
        bu4.config(text=text)
        bu4.state(['disabled'])

    elif (id == 5):
        bu5.config(text=text)
        bu5.state(['disabled'])

    elif (id == 6):
        bu6.config(text=text)
        bu6.state(['disabled'])

    elif (id == 7):
        bu7.config(text=text)
        bu7.state(['disabled'])

    elif (id == 8):
        bu8.config(text=text)
        bu8.state(['disabled'])

    elif (id == 9):
        bu9.config(text=text)
        bu9.state(['disabled'])

def CheckWinner():
    Winner = -1
# -----------------------------------------------------rows-------------------------------------------------
    if((1 in p1) and (2 in p1) and (3 in p1)):
        Winner=1

    if ((1 in p2) and (2 in p2) and (3 in p2)):
        Winner = 2


    if ((4 in p1) and (5 in p1) and (6 in p1)):
        Winner = 1

    if ((4 in p2) and (5 in p2) and (6 in p2)):
        Winner = 2


    if ((7 in p1) and (8 in p1) and (9 in p1)):
        Winner = 1

    if ((7 in p2) and (8 in p2) and (9 in p2)):
        Winner = 2

# -------------------------------------------Column--------------------------------------------------
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        Winner = 1

    if ((1 in p2) and (4 in p2) and (7 in p2)):
        Winner = 2

    if ((2 in p1) and (5 in p1) and (8 in p1)):
        Winner = 1

    if ((2 in p2) and (5 in p2) and (8 in p2)):
        Winner = 2

    if((3 in p1) and (6 in p1) and (9 in p1)):
        Winner=1

    if ((3 in p2) and (6 in p2) and (9 in p2)):
        Winner = 2

# ------------------------------------------------------Diagonal---------------------------------------
    if((1 in p1) and (5 in p1) and (9 in p1)):
        Winner=1

    if ((1 in p2) and (5 in p2) and (9 in p2)):
        Winner = 2


    if ((3 in p1) and (5 in p1) and (7 in p1)):
        Winner = 1

    if ((3 in p2) and (5 in p2) and (7 in p2)):
        Winner = 2

# ----------------------------------------------- message to winner---------------------------------


    if Winner == 1:
        messagebox.showinfo(title='Cong.', message='Player1 is Winner')
        exit()

    if Winner == 2:
        messagebox.showinfo(title='Cong.', message='Player2 is Winner')
        exit()


# ------------------------------------------------play with machine----------------------------------------------

def AutoPlay():
    global p1
    global p2
    EmptyCell=[]
    for cell in range(9):
        if(not( (cell+1 in p1) or (cell+1 in p2) ) ):   # if cell didn't choose by p1 or p2
            EmptyCell.append(cell+1)  # add it into empty cell 
    RandIndex=randint(0, len(EmptyCell)-1)  # choose random empty cell 
    BuClick(EmptyCell[RandIndex]) # click on chosen cell


root.mainloop()

