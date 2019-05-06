import tkinter as tk #tkinter is trash but so am i

def checkScore(name, objList):
    score = 0
    for item in objList:
        if(item[0]!="phone"):
            score+=3
        elif(item[0]=="phone"):
            score+=10
    fileToWrite = open("highscore.txt","w")
    fileToWrite.write(name+":"+score)
    fileToWrite.close()
    fileToRead = open("highscore.txt","r")
    b = []
    for line in fileToRead:
        b.append(line.split(":"))
    fileToRead.close()
    checkHighScore(b)


def checkHighScore(b):
    for i in range(0,len(b)):
        for j in range(i,len(b)):
            if b[j][1]<b[i][1]:
                temp = b[i][1]
                tempname = b[i][0]
                b[i][1] = b[j][1]
                b[i][0] = b[j][0]
                b[j][1] = temp
                b[j][0] = tempname
    print("The top 3 players are {0},{1},{2}".format(b[0][0],b[1][0],b[2][0]))


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
