from tkinter import *
from random import randint
from tkinter import ttk

window = Tk()
window.title('Rock Paper Scissors')
pl = PhotoImage(file='images/rockpaperscissors.png')
window.iconphoto(False,pl)
window.geometry('450x600')

# define our images
rock = PhotoImage(file='images/rock.png')
paper = PhotoImage(file='images/paper.png')
scissors = PhotoImage(file='images/scissors.png')

# add images to a list
imageList = [rock, paper, scissors]

# pick random number between 0 and 2
pickNumber = randint(0,2)


def hide():
    rivalLabel.pack_forget()
    imageLabel.pack_forget()
    resultLabel.pack_forget()


def spin():
    global rivalLabel
    global imageLabel
    global resultLabel
    # rival's pick
    rivalLabel = Label(window, text='Your rival pick', font=('Helvetica, 13'), fg='#0000FF')
    rivalLabel.pack(pady=30)

    # throw an image when the program starts
    imageLabel = Label(window, image=None, bd=0)
    imageLabel.pack()

    # label for showing if you win or not
    resultLabel = Label(window, text='', font=('Helvetica, 18'), fg='#ff0000')
    resultLabel.pack()
    
    # pick random number
    pickNumber = randint(0,2)
    # show image
    imageLabel.config(image=imageList[pickNumber])

    # 0=rock, 1=paper, 2=scissors
    # convert dropdown choice to a number
    if userChoice.get() == 'Rock':
        userChoiceValue = 0
    elif userChoice.get() == 'Paper':
        userChoiceValue = 1
    elif userChoice.get() == 'Scissors':
        userChoiceValue = 2

    # determine if user win or lose
    # if user picks rock, show results based on what rival picks
    if userChoiceValue == 0: 
        if pickNumber == 0:
            resultLabel.config(text="It's a Tie! Spin again!")
        elif pickNumber == 1:
            resultLabel.config(text='Paper covers Rock! You lose!')
        elif pickNumber == 2:
            resultLabel.config(text='Rock smashes Scissors! You win!')
    # if user picks paper, show results based on what rival picks    
    if userChoiceValue == 1:
        if pickNumber == 1:
            resultLabel.config(text="It's a Tie! Spin again!")
        elif pickNumber == 0:
            resultLabel.config(text='Paper covers Rock! You win!')
        elif pickNumber == 2:
            resultLabel.config(text='Scissors cuts paper! You lose')
    # if user picks scissors, show results based on what rival picks   
    if userChoiceValue == 2:
        if pickNumber == 2:
            resultLabel.config(text="It's a Tie! Spin again!")
        elif pickNumber == 0:
            resultLabel.config(text='Rock smashes Scissors! You lose!')
        elif pickNumber == 1:
            resultLabel.config(text='Scissors cuts paper! You win!')

    # after a few seconds, rival image and result disappear to wait for new match
    imageLabel.after(5000, hide)    

# label to ask user to make choice 
userLabel = Label(window, text='Pick your choice, then press Spin', font=('Helvetica, 13'), fg='#0000FF')
userLabel.pack()

# user picks choice
userChoice = ttk.Combobox(window, value=('--','Rock','Paper','Scissors'), font=('Helvetica, 15'))
userChoice.current(0)
userChoice.pack(pady=20)

# create spin button
spinButton = Button(window, text='Spin!', command=spin, width=10, font=('Helvetica, 18'), fg='#cc6600')
spinButton.pack(pady=10)




window.mainloop()