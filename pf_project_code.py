from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
mixer.init()

mixer.music.load('pied piper.mp3')
mixer.music.play(-1)

score=0
def update_score():
    global score
    score+=1
def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()


    b=event.widget
    value=b['text']

    for i in range(15):
        if value==correct_answers[i]:
            if value==correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()
                    try:
                        with open("scores.txt", "a") as file:
                           file.write(f"Score: {score}\n")
                    except Exception as error:
                        messagebox.showerror("Error",f"An error occurred while saving the score: {str(error)}")

                def playagain():
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                    root2.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])

                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    amountLabel.config(image=amountimage)
                    try:
                        with open("scores.txt", "a") as file:
                           file.write(f"Score: {score}\n")
                    except Exception as error:
                        messagebox.showerror("Error",f"An error occurred while saving the score: {str(error)}")


                mixer.music.stop()
                mixer.music.load('won.mp3')
                mixer.music.play()

                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('1450x850+0+0')
                root2.title('You Won 0 pounds')
                imgLabel = Label(root2, image=centerImage, bd=0)
                imgLabel.pack(pady=100)

                winLabel = Label(root2, text='You Won', font=('arial', 40, 'bold'), bg='black', fg='white')
                winLabel.pack()

                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                        activebackground='black', activeforeground='white', bd=5, cursor='hand2',
                                        command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                     activebackground='black', activeforeground='white', bd=5, cursor='hand2',
                                     command=close)
                closeButton.pack()

                root2.mainloop()
                break

            update_score()
            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            amountLabel.config(image=amountimages[i])


        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()
                try:
                    with open("scores.txt", "a") as file:
                        file.write(f"Score: {score}\n")
                except Exception as error:
                    messagebox.showerror("Error", f"An error occurred while saving the score: {str(error)}")

            def tryagain():
                lifeline50Button.config(state=NORMAL,image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                root1.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,questions[0])

                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountLabel.config(image=amountimage)
                try:
                    with open("scores.txt", "a") as file:
                        file.write(f"Score: {score}\n")
                except Exception as error:
                    messagebox.showerror("Error", f"An error occurred while saving the score: {str(error)}")

            root1=Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('1450x850+0+0')
            root1.title('You Won 0 pounds')
            imgLabel=Label(root1,image=centerImage,bd=0)
            imgLabel.pack(pady=100)

            loseLabel=Label(root1,text='You Lose',font=('arial',40,'bold'),bg='black',fg='white')
            loseLabel.pack()

            tryagainButton = Button(root1,text='Try Again',font=('arial',20,'bold'),bg='black',fg='white',
                                    activebackground='black',activeforeground='white',bd=5,cursor='hand2',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1,text='Close',font=('arial', 20, 'bold'), bg='black', fg='white',
                                 activebackground='black', activeforeground='white', bd=5, cursor='hand2',
                                 command=close)
            closeButton.pack()

            root1.mainloop()
            break

def lifeline50():
    lifeline50Button.config(image=image50X,state=DISABLED)
    if questionArea.get(1.0,'end-1c')==questions[0]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[1]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[2]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[3]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[4]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[6]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[7]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[8]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[9]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[10]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[11]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[12]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[13]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[14]:
        optionButton2.config(text='')
        optionButton3.config(text='')


def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePoleX,state=DISABLED)
    progressbarA.place(x=580,y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=700, y=190)

    progressbarLabelA.place(x=580,y=320)
    progressbarLabelB.place(x=620, y=320)
    progressbarLabelC.place(x=660, y=320)
    progressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0,'end-1c')==questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[1]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[2]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=50)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[3]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=30)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[4]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[5]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=30)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[6]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0,'end-1c')==questions[7]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=50)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[8]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=50)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[9]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0,'end-1c')==questions[10]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0,'end-1c')==questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=50)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[12]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=30)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[13]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)

    if questionArea.get(1.0,'end-1c')==questions[14]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)


def phoneLifeline():
    mixer.music.load('calling.mp3')
    mixer.music.play()
    callButton.place(x=70,y=260)
    phoneLifelineButton.config(image=phoneImageX,state=DISABLED)

def phoneclick():
    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            engine.say(f'The answer is {correct_answers[i]}')
            engine.runAndWait()

correct_answers=['Mercury','Jasmine','Whale','7','Photosynthesis',
             '1945','Pacific Ocean','J.K Rowling','Russia',
             'Magnetic Bond','Skin','Leonardo Vinci','Femur',
             'Mao zedong','Antarctica']



questions=['What is the smallest planet in our solar system?',
           'What is the name of Pakistan National Flower?',
           'What is the name of world largest animal?',
           'What is the value of y in the equation 2y+5=19?',
           'What is the name of the process in which the plants make their own food?',
           'In what year did World War II ended?',
           'What is the name of the largest ocean in the world?',
           'Who wrote the Harry Potter series?',
           'What is the largest country in the world by area?',
           'Which of the following is not a type of chemical bond?',
           'What is the largest organ in the human body?',
           'Who painted the Mona Lisa?',
           'What is the strongest bone in the human body?',
           'Which person made revolution in China?',
           'Which continent has the highest rate of ozone depletion?']

first_option=['Mars','Rose','Giraffe','7','Respiration',
              '1945','Atlantic Ocean','Suzanne Collins',
              'America','Covalent bond','Kidney','Pablo Picasso',
              'Femur','Feng Cheng','Europe']

second_option=['Jupiter','Sunflower','Whale','8','Digestion',
               '1948','Indian Ocean','J.K Rowling','Russia','Hydrogen bond',
               'Heart','Leonardo Vinci','Carpel', 'Jun Shi','Africa']

third_option=['Mercury','Jasmine','Elephant','9','Photosynthesis',
              '1965','Artic Ocean','Veronica Roth','Australia','Ionic Bond',
              'Liver','Vincent Van','Tarsals','Mao zedong','South America']

fourth_option=['Earth','Lily','Shark','10','Fermentation','1940',
               'Pacific Ocean','Stephenie Meyer','Canada','Magnetic Bond',
               'Skin','Michael angelo','Backbone','Lin Ming','Antarctica']
def start_game():
    name= name_entry.get()
    messagebox.showinfo("Game Start",f"Hello,{name}! Let's start the game")
    window.destroy()
    with open("scores.txt","w") as file:
        file.write(f"Player Name: {name}\n")

window= Tk()
window.title("Cash Your Luck")
window.geometry("1450x850+0+0")
window.config(bg="black")
centerImage=PhotoImage(file='cashyourluck1.png')
imgLabel=Label(window,image=centerImage,bd=0)
imgLabel.pack(pady=100)
loseLabel=Label(window,text='Welcome To Cash Your luck',font=('arial',20,'bold'),bg='black',fg='white')
loseLabel.pack()
name_label=Label(window,text="Enter your name",font=('arial',20),bg='black',fg='pink')
name_label.pack()

name_entry=Entry(window)
name_entry.pack()
start_button=Button(window,text="Start Game",font=('arial',10,'bold'),
                    command=start_game,padx=20,pady=10,bd=0,bg="purple",fg="white",activebackground='purple',
                    activeforeground='white',cursor='hand2')
start_button.pack()
window.mainloop()

root = Tk()
root.geometry('1450x850+0+0')
root.title('Cash Your Luck')
root.config(bg='black')

leftframe=Frame(root,bg='black',padx=90)
leftframe.grid(row=0,column=0)

topFrame=Frame(leftframe,bg='black',pady=15)
topFrame.grid()

centerFrame=Frame(leftframe,bg='black',pady=15)
centerFrame.grid(row=1,column=0)

bottomFrame=Frame(leftframe)
bottomFrame.grid(row=2,column=0)

rightframe=Frame(root,pady=25,padx=50,bg='black')
rightframe.grid(row=0,column=1)

image50=PhotoImage(file='50-50.png')
image50X=PhotoImage(file='50-50-X.png')

lifeline50Button=Button(topFrame,image=image50,bg='black',bd=0,activebackground='black',width=180,height=80,
                        command=lifeline50)
lifeline50Button.grid(row=0,column=0)


audiencePole=PhotoImage(file='audiencePole.png')
audiencePoleX=PhotoImage(file='audiencePoleX.png')

audiencePoleButton=Button(topFrame,image=audiencePole,bg='black',bd=0,activebackground='black',width=180,height=80,
                          command=audiencePoleLifeline)
audiencePoleButton.grid(row=0,column=1)


phoneImage=PhotoImage(file='phoneAFriend.png')
phoneImageX=PhotoImage(file='phoneAFriendX.png')

phoneLifelineButton=Button(topFrame,image=phoneImage,bg='black',bd=0,activebackground='black',width=180,height=80,
                           command=phoneLifeline)
phoneLifelineButton.grid(row=0,column=2)


callimage=PhotoImage(file='phone.png')
callButton=Button(root,image=callimage,bd=0,bg='black',activebackground='black',cursor='hand2',
                  command=phoneclick)


centerImage=PhotoImage(file='cashyourluck1.png')
logoLabel=Label(centerFrame,image=centerImage,bg='black',width=300,height=200)
logoLabel.grid(row=0,column=0)


amountimage=PhotoImage(file='Picture0.png')
amountimage1=PhotoImage(file='Picture1.png')
amountimage2=PhotoImage(file='Picture2.png')
amountimage3=PhotoImage(file='Picture3.png')
amountimage4=PhotoImage(file='Picture4.png')
amountimage5=PhotoImage(file='Picture5.png')
amountimage6=PhotoImage(file='Picture6.png')
amountimage7=PhotoImage(file='Picture7.png')
amountimage8=PhotoImage(file='Picture8.png')
amountimage9=PhotoImage(file='Picture9.png')
amountimage10=PhotoImage(file='Picture10.png')
amountimage11=PhotoImage(file='Picture11.png')
amountimage12=PhotoImage(file='Picture12.png')
amountimage13=PhotoImage(file='Picture13.png')
amountimage14=PhotoImage(file='Picture14.png')
amountimage15=PhotoImage(file='Picture15.png')

amountimages=[amountimage1,amountimage2,amountimage3,amountimage4,amountimage5,
              amountimage6,amountimage7,amountimage8,amountimage9,amountimage10,
              amountimage11,amountimage12,amountimage13,amountimage14,amountimage15]

amountLabel=Label(rightframe,image=amountimage,bg='black',height=700)
amountLabel.grid(row=0,column=0)

LayoutImage=PhotoImage(file='lay.png')

LayoutLabel=Label(bottomFrame,image=LayoutImage,bg='black')
LayoutLabel.grid(row=0,column=0)

questionArea=Text(bottomFrame,font=('arial',17,'bold'),width=34,height=2,wrap='word',bg='black',fg='white',bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END,questions[0])

labelA=Label(bottomFrame,text='A:',bg='black',fg='white',font=('arial',16,'bold'))
labelA.place(x=60,y=110)

optionButton1=Button(bottomFrame,text=first_option[0],font=('arial',15,'bold'),bg='black',fg='white',bd=0,
                     activebackground='black',activeforeground='white',cursor='hand2')
optionButton1.place(x=100,y=100)


labelB=Label(bottomFrame,text='B:',bg='black',fg='white',font=('arial',16,'bold'))
labelB.place(x=330,y=110)

optionButton2=Button(bottomFrame,text=second_option[0],font=('arial',15,'bold'),bg='black',fg='white',bd=0,
                     activebackground='black',activeforeground='white',cursor='hand2')
optionButton2.place(x=370,y=100)


labelC=Label(bottomFrame,text='C:',bg='black',fg='white',font=('arial',16,'bold'))
labelC.place(x=60,y=190)

optionButton3=Button(bottomFrame,text=third_option[0],font=('arial',15,'bold'),bg='black',fg='white',bd=0,
                     activebackground='black',activeforeground='white',cursor='hand2')
optionButton3.place(x=100,y=180)


labelD=Label(bottomFrame,text='D:',bg='black',fg='white',font=('arial',16,'bold'))
labelD.place(x=330,y=190)

optionButton4=Button(bottomFrame,text=fourth_option[0],font=('arial',15,'bold'),bg='black',fg='white',bd=0,
                     activebackground='black',activeforeground='white',cursor='hand2')
optionButton4.place(x=370,y=180)

progressbarA=Progressbar(root,orient=VERTICAL,length=120)
progressbarB=Progressbar(root,orient=VERTICAL,length=120)
progressbarC=Progressbar(root,orient=VERTICAL,length=120)
progressbarD=Progressbar(root,orient=VERTICAL,length=120)

progressbarLabelA=Label(root,text='A',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLabelB=Label(root,text='B',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLabelC=Label(root,text='C',font=('arial',20,'bold'),bg='black',fg='white')
progressbarLabelD=Label(root,text='D',font=('arial',20,'bold'),bg='black',fg='white')


optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)


root.mainloop()

