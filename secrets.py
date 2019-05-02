import tkinter as tk #tkinter is trash but so am i

def checkScore(name, objList):
    score = 0

    if checkHighScore(score):
        addHighScore(name, score)
    return(score)

def checkHighScore(score):
    pass

def addHighScore(name, score):
    pass

def displayMap(): #https://stackoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    root = tk.Tk()
    widget = tk.Label(root, compound='top')
    root.title("Project Flow Chart")
    widget.flow_img_png = tk.PhotoImage(file="flow_chart.png")
    widget['text'] ="oh wow look at this neato map \n Authors: Amna Tanveer, Jacob Lemley, Nachiket Vamshidhar, Kaitlin Forsythe" 
    widget['image'] = widget.flow_img_png
    widget.pack()
    root.mainloop()

#more refs
#https://tkdocs.com/tutorial/windows.html
#https://tkdocs.com/widgets/index.html
