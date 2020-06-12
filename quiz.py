#Task to do

#previous need to be updaed like next




from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox
from datetime import datetime
import json
import random
from PIL import ImageTk, Image    #pip install Pillow

root= Tk()
root.title("Quiz")

root.geometry("850x400")
root.configure(background= "black")


#---------------------------------Variable-------------------------------------

indexes= [0, 1, 2, 3, 4]  #tHis is to generate serial wise quwestion
question_index=0
score= 0

user_answer_list= []
correct_answer_list= []
#--------------------------------------importinf json and using------------------------------------------------------------------------------

with open('quizqn.json', encoding="utf8") as f:
    data = json.load(f)
    #print(data[0].values())


questions = [v for v in data[0].values()]
answer_choices = [v for v in data[1].values()]
answer_list= [0, 2, 0, 1, 1]
##print(questions[indexes[1]])
##print(answer_choices[indexes[1]][1])
#------------------------------------functions----------------------------------------------------------

# Need to set valuw of radio button wrto questions
        

    
    

def to_show_score():
    pass
       
    
    
def to_exit():
    iExit= tkinter.messagebox.askyesno("Quiz", "Please confirm if you wish to exit")
    if iExit > 0:
        root.destroy()
    
   
def to_submit():
    global lblquestion, rad_button1, rad_button2, rad_button3, rad_button4, radio_selection, question_index, user_radio_answer_value, question_selection
    global btnprev, btnnxt, btnsubmit, btnexit , answer_selected, correct_answer, correct_answer_list, user_answer_list, score
    global user_answer_list, correct_answer_list, lblscore, lblanswer_selected, lblcorrect_answer, lblsuggestion, btnhappy, lblwish, btnexit

    
    answer_string= " , "

    iSubmit= tkinter.messagebox.askyesno("Quiz", "Please confirm if you wish to submit")
    if iSubmit > 0:
        
    
        lblquestion.destroy()
        rad_button1.destroy()
        rad_button2.destroy()
        rad_button3.destroy()
        rad_button4.destroy()
        #btnprev.destroy()
        btnnxt.destroy()
        btnsubmit.destroy()
        btnexit.destroy()
        #Answer_Frame.destroy()
        your_score= "Your score is:\t" + str(score) 
        print(score)
        answer_selected= "Your selected answers :\t" + answer_string.join([str(elem) for elem in user_answer_list]) 
        correct_answer= "Correct answers:\t" + answer_string.join([str(elem) for elem in correct_answer_list])
        
        pecentage= (score/len(answer_list))*100
        
        if  (pecentage >= 70):
            
            lblscore= Label(qn_Display_frame, font=("arial", 14, "bold"), width= 40, justify= "center",bg="light green", text=your_score, bd=7)
            lblscore.grid(row=0, column=0)
            
            lblanswer_selected= Label(qn_Display_frame, font=("arial", 14, "bold"), width= 40, justify= "center", bg="light green",text=answer_selected, bd=7)
            lblanswer_selected.grid(row=1, column=0)
            
            lblcorrect_answer= Label(qn_Display_frame, font=("arial", 14, "bold"), width= 40, justify= "center",bg="light green", text=correct_answer, bd=7)
            lblcorrect_answer.grid(row=2, column=0)

            lblsuggestion= Label(Answer_Frame, font=("arial", 14, "bold"), width= 40, justify= "center",bg="#911d30",fg="white", text="Press EXIT to quit", bd=7)
            lblsuggestion.grid(row=0, column=0, columnspan=2)
            
            # Select the Imagename  from a folder  
            x = r"F:\udemy_python\icons\happy.PNG" 
          
            # opens the image 
            img = Image.open(x) 
              
            # resize the image and apply a high-quality down sampling filter 
            img = img.resize((75, 75), Image.ANTIALIAS) 
          
            # PhotoImage class is used to add image to widgets, icons etc 
            img = ImageTk.PhotoImage(img)

            

            lblhappy= Label(Answer_Frame,image = img)
            lblhappy.image= img
            lblhappy.grid(row=1,column=0, padx=10, pady=10)

            lblwish= Label(Button_Frame, font=("arial", 14, "bold"), width= 40, justify= "center",bg="#911d30",fg="white", text="See you again!!", bd=7)
            lblwish.grid(row=0)


            # Select the Imagename  from a folder  
            image_path = r"F:\udemy_python\icons\exit.PNG" 
          
            # opens the image 
            img_exit = Image.open(image_path) 
              
            # resize the image and apply a high-quality down sampling filter 
            img_exit = img_exit.resize((65, 65), Image.ANTIALIAS)      
            # PhotoImage class is used to add image to widgets, icons etc 
            img_exit = ImageTk.PhotoImage(img_exit)       
            btnexit= Button(Answer_Frame,image = img_exit, bd=10, command=to_exit)
            btnexit.image= img_exit
            btnexit.grid(row=1,column=1, padx=10, pady=10)

            

            

            
        else:
            lblscore= Label(qn_Display_frame, font=("arial", 14, "bold"), width= 60, justify= "center",bg="#911d30",fg="white", text=your_score, bd=7)
            lblscore.grid(row=0, column=0)
            
            lblanswer_selected= Label(qn_Display_frame, font=("arial", 14, "bold"), width= 60, justify= "center", bg="#911d30",fg="white",text=answer_selected, bd=7)
            lblanswer_selected.grid(row=1, column=0)
            
            lblcorrect_answer= Label(qn_Display_frame, font=("arial", 14, "bold"), width= 60, justify= "center",bg="#911d30",fg="white", text=correct_answer, bd=7)
            lblcorrect_answer.grid(row=2, column=0)
            
            lblsuggestion= Label(Answer_Frame, font=("arial", 14, "bold"), justify= "center",bg="#911d30",fg="white", text="PLease click emoji to restart and exit to quit!!", bd=7)
            lblsuggestion.grid(row=0, column=0, columnspan=2)

            

            # Select the Imagename  from a folder  
            x = r"F:\udemy_python\icons\sad.PNG" 
          
            # opens the image 
            img = Image.open(x) 
              
            # resize the image and apply a high-quality down sampling filter 
            img = img.resize((65, 65), Image.ANTIALIAS) 
          
            # PhotoImage class is used to add image to widgets, icons etc 
            img = ImageTk.PhotoImage(img) 


            btnhappy= Button(Answer_Frame,image = img, bd=10, command= restart_quiz)
            btnhappy.image= img
            btnhappy.grid(row=1,column=0)
            

            lblwish= Label(Button_Frame, font=("arial", 14, "bold"), width= 60, justify= "center",bg="#911d30",fg="white", text="See you again!!", bd=7)
            lblwish.grid(row=0)

            # Select the Imagename  from a folder  
            image_path = r"F:\udemy_python\icons\exit.PNG" 
          
            # opens the image 
            img_exit = Image.open(image_path) 
              
            # resize the image and apply a high-quality down sampling filter 
            img_exit = img_exit.resize((65, 65), Image.ANTIALIAS) 
          
            # PhotoImage class is used to add image to widgets, icons etc 
            img_exit = ImageTk.PhotoImage(img_exit)

            

            btnexit= Button(Answer_Frame,image = img_exit, bd=10, command=to_exit)
            btnexit.image= img_exit
            btnexit.grid(row=1,column=1)
    
def to_gonext():
    global lblquestion, rad_button1, rad_button2, rad_button3, rad_button4, radio_selection, question_index, score,  user_radio_answer_value, question_selection
    global user_answer_list, correct_answer_list, score
    
    try :
        
        if (question_index < 5):
            question_index += 1
            lblquestion.config(text= questions[indexes[question_index]])
            rad_button1["text"]= answer_choices[indexes[question_index]][0]
            rad_button2["text"]= answer_choices[indexes[question_index]][1]
            rad_button3["text"]= answer_choices[indexes[question_index]][2]
            rad_button4["text"]= answer_choices[indexes[question_index]][3]
            
            
            #print(question_index)
        else:
            print("Question ends here")

        question_selection= questions[indexes[question_index-1]]
        user_radio_answer_value= radio_selection.get()

    except IndexError:
        question_selection= questions[indexes[question_index-1]]
        user_radio_answer_value= radio_selection.get()
        
    
    
    
    
    if (user_radio_answer_value == answer_list[question_index-1]):
        score += 1
    if (len(user_answer_list) < 5):
        user_answer_list.append(user_radio_answer_value)
        correct_answer_list.append(answer_list[question_index-1])
        print("Inside next", user_answer_list)
    
    
##def to_goprev():
##    global lblquestion, rad_button1, rad_button2, rad_button3, rad_button4, radio_selection, question_index, score, question_selection, user_radio_answer_value
##    #print(question_index)
##    try :
##        
##        if (question_index > 0):
##            question_index -= 1
##            lblquestion.config(text= questions[indexes[question_index]])
##            rad_button1["text"]= answer_choices[indexes[question_index]][0]
##            rad_button2["text"]= answer_choices[indexes[question_index]][1]
##            rad_button3["text"]= answer_choices[indexes[question_index]][2]
##            rad_button4["text"]= answer_choices[indexes[question_index]][3]
##            
##            
##        else:
##            print("You are in the first qquestion of quiz")
##
##        question_selection= questions[indexes[question_index-1]]
##        user_radio_answer_value= radio_selection.get()
##    except IndexError:
##        
##         
##        question_selection= questions[indexes[question_index-1]]
##        user_radio_answer_value= radio_selection.get()

##    if (user_radio_answer_value == answer_list[question_index-1]):
##        score += 1

def restart_quiz():
    global lblscore, lblanswer_selected, lblcorrect_answer, lblsuggestion, btnhappy, lblwish, btnexit
    global user_answer_list, correct_answer_list, score, question_index
    score= 0
    user_answer_list= []
    correct_answer_list= []
    question_index= 0
    print("Inside restart_quiz", user_answer_list)

    iRestart = tkinter.messagebox.askyesno("Quiz", "Please confirm if you wish to restart ")
    if iRestart > 0:

        lblscore.destroy()
        lblanswer_selected.destroy()
        lblcorrect_answer.destroy()
        lblsuggestion.destroy()
        btnhappy.destroy()
        lblwish.destroy()
        btnexit.destroy()
        
        start_quiz()
        
def start_quiz():
    global lblquestion, rad_button1, rad_button2, rad_button3, rad_button4, radio_selection
    global btnprev, btnnxt, btnsubmit, btnexit
    
    
    radio_selection=IntVar()
    #radio_selection.set(-1)
    
    lblquestion= Label(qn_Display_frame, font=("arial", 14, "bold"), width= 60, justify= "center", bg= "#ba4a5f",fg= "white", text=questions[indexes[0]], bd=7)
    lblquestion.grid(row=0, column=0)
    rad_button1= Radiobutton(Answer_Frame, text=answer_choices[indexes[0]][0],padx = 20,variable=radio_selection, bg= "light green", font= ("arial", 16, "bold"), value= 0)
    rad_button1.grid(row=1, column=0, sticky= W)
    rad_button2= Radiobutton(Answer_Frame, text=answer_choices[indexes[0]][1], padx = 20,variable=radio_selection, bg= "light green", font= ("arial", 16, "bold"), value= 1)
    rad_button2.grid(row=2, column=0,sticky= W)
    rad_button3= Radiobutton(Answer_Frame, text=answer_choices[indexes[0]][2],padx = 20,variable=radio_selection, bg= "light green", font= ("arial", 16, "bold"), value= 2)
    rad_button3.grid(row=3, column=0,sticky= W)
    rad_button4= Radiobutton(Answer_Frame, text=answer_choices[indexes[0]][3],padx = 20,variable=radio_selection, bg= "light green", font= ("arial", 16, "bold"),  value= 3)
    rad_button4.grid(row=4, column=0,sticky= W)

##    btnprev= Button(Button_Frame, padx=18, bd=7, font= ("arial", 14, "bold"), width= 10, text= "PREV", command= to_goprev)
##    btnprev.grid(row=0, column=1)

# Select the Imagename  from a folder  
    image_path_next = r"F:\udemy_python\icons\next.PNG"   
    # opens the image 
    img_next = Image.open(image_path_next)       
    # resize the image and apply a high-quality down sampling filter 
    img_next = img_next.resize((65, 65), Image.ANTIALIAS)   
    # PhotoImage class is used to add image to widgets, icons etc 
    img_next = ImageTk.PhotoImage(img_next)
    btnnxt= Button(Button_Frame,  bd=7,  image = img_next, command= to_gonext)
    btnnxt.image= img_next
    btnnxt.grid(row=0, column=0)


    image_path_submit = r"F:\udemy_python\icons\submit.PNG"   
    # opens the image 
    img_submit = Image.open(image_path_submit)       
    # resize the image and apply a high-quality down sampling filter 
    img_submit = img_submit.resize((65, 65), Image.ANTIALIAS)   
    # PhotoImage class is used to add image to widgets, icons etc 
    img_submit = ImageTk.PhotoImage(img_submit)
    btnsubmit= Button(Button_Frame, bd=7, image = img_submit, command= to_submit)
    btnsubmit.image= img_submit
    btnsubmit.grid(row=0, column=1)



    image_path = r"F:\udemy_python\icons\exit.PNG" 
    # opens the image 
    img_exit = Image.open(image_path) 
    # resize the image and apply a high-quality down sampling filter 
    img_exit = img_exit.resize((65, 65), Image.ANTIALIAS) 
    # PhotoImage class is used to add image to widgets, icons etc 
    img_exit = ImageTk.PhotoImage(img_exit)    
    btnexit= Button(Button_Frame,image = img_exit, bd=10, command=to_exit)
    btnexit.image= img_exit
    btnexit.grid(row=0,column=2)
    
   

#To generate random  questions
def gen():
    global indexes
    
    while(len(indexes) < 5):
        x = random.randint(0,4)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    #print(len(indexes))


            
def to_strt():
    lblRules.destroy()
    lblexit.destroy()
    lblsubmit.destroy()
    #lblprevious.destroy()
    lblnext.destroy()
    btnstart.destroy()
    #gen()
    start_quiz()
   
   
    
#-----------------------------------------------variables---------------------------------------------



#---------------------------------------For heading and frames----------------------------------------------

MainFrame= Frame(root)
MainFrame.grid()

Top= Frame(MainFrame, bd= 15, width= 800, relief= RIDGE)
Top.pack(side= TOP)

MainTitle= Label(Top, font=("arial", 20, "bold"), text= "QUIZ")
MainTitle.grid()
MainTitle.configure(bg='light green', fg= "red")

qn_Display_frame = Frame(MainFrame, bd= 10, width= 350, height= 20, pady=10, relief= RIDGE)
qn_Display_frame.pack(side= BOTTOM)

Answer_Frame= LabelFrame(qn_Display_frame, font=("arial", 12, "bold"), width= 350,  bg= "light green", height= 100, relief= RIDGE )
Answer_Frame.grid(row=3, column=0)

Button_Frame= LabelFrame(qn_Display_frame, font=("arial", 12, "bold"), width= 350, height= 40, relief= RIDGE )
Button_Frame.grid(row=4, column=0)

#------------------------entry-------------------------------------------------------------------------------------
lblRules = Label(
    Answer_Frame,
    text = "This quiz contains 5 questions. This quiz will start once pressed the  start button. Good luck start well",
     bg= "light green",
    font = ("Times",14),
    
)
lblRules.grid(row=0, column=0, rowspan=3, columnspan=3)


lblnext = Label(
    Answer_Frame,
    text = "=> Next Symbol.It will be your final choice",
    bg= "light green",
    font = ("Times",14, "bold"),
    
)
lblnext.grid(row=3, column=0, columnspan=3)

##lblprevious = Label(
##    Answer_Frame,
##    text = "<= Previous Symbol. It wil get you the Previous question in quiz",
##    bg= "light green",
####    font = ("Times",14, "bold"),
##    
##)
##lblprevious.grid(row=4, column=0, columnspan=3)
##
lblsubmit = Label(
    Answer_Frame,
    text = "submit Button. Quiz will be submitted and final score will get displayed",
    bg= "light green",
    font = ("Times",14, "bold"),
    
)
lblsubmit.grid(row=4, column=0, columnspan=3)


lblexit = Label(
    Answer_Frame,
    text = "Exit Button. Quiz will end and window will be terminated",
    bg= "light green",
    font = ("Times",14, "bold"),
    
)
lblexit.grid(row=5, column=0, columnspan=3)


#-------------------------------------------------------buttons--------------------------------------------

photo = PhotoImage(file = r"F:\udemy_python\icons\start.PNG")

# Resizing image to fit on button 
photoimage = photo.subsample(4, 4) 

btnstart= Button(Button_Frame, padx=18, bd=7,  bg= "light green",image = photoimage, command= to_strt)
btnstart.grid(row=0, column=0, pady=10)






#----------------------------------------------------radio btns---------------------------------------------------------






root.mainloop()




