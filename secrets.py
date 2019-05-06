import tkinter as tk #tkinter is trash but so am i

def checkScore(name, objList):
    score = 0
    for item in objList:
        if(item[0]!="phone"):
            score+=3 #Using +=, -=, etc (3)
        elif(item[0]=="phone"):
            score+=10
    checkHighScore(name, score)

def checkHighScore(name, score):
    file = open("highscore.txt","r")
    b = []
    for line in file:
        line = line.split(":")
        line[1] = int(line[1])
        b.append(line)
    file.close()
    count = 0
    for x in b:
        if x[1] <= score and count == 0:
            b.insert(b.index(x), [name, score])
            del b[3:]
            count +=1
    if count == 1:
        addHighScore(name, score, b)
        #addHighscore(name, score, b)
    else:
        print("Score: {0} \n Sorry, you didn't get a highscore.".format(score))
        print("HIGHSCORES:\n{}:{}\n{}:{}\n{}:{}".format(b[0][0],b[0][1],b[1][0],b[1][1],b[2][0],b[2][1])) #Using the formatting for strings (with print() statement) (5)


def addHighScore(name, score, b):
    f = open("highscore.txt", "w")
    for item in b:
        f.writelines(item[0] + ":" + str(item[1]) + "\n") #File Writing (15)
    f.close()
    print("HIGHSCORES:\n{}:{}\n{}:{}\n{}:{}".format(b[0][0],b[0][1],b[1][0],b[1][1],b[2][0],b[2][1]))

def displayMap(): #https://stackoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    root = tk.Tk()
    widget = tk.Label(root, compound='top')
    root.title("Project Flow Chart")
    widget.flow_img_png = tk.PhotoImage(file="map.png")
    widget['text'] ="oh wow look at this neato map \n Authors: Amna Tanveer, Jacob Lemley, Nachiket Vamshidhar, Kaitlin Forsythe"
    widget['image'] = widget.flow_img_png
    widget.pack()
    root.mainloop()

#more refs
#https://tkdocs.com/tutorial/windows.html
#https://tkdocs.com/widgets/index.html
