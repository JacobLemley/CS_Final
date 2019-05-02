import textwrap as tw #https://pymotw.com/3/textwrap/
import sys

class Player: #class to store player data, like inventory, location, etc.
    def __init__(self):
        self.name = ""
        self.inventory = []
        self.loc = "sign"


class Room:
    def __init__(self, name):
        self.name = name
        self.filepath = name + ".txt"
        self.objects = []
        self.locations = []
        self.initialDescription = ""
        self.normalDescription = ""
        self.visited = False
        self.assignDefaults()

    def assignDefaults(self):
        #read default file into a list of each line
        file = open(self.filepath, "r")
        raw = []
        for line in file:
            line = line.rstrip("\n")
            raw.append(line)
        file.close()

        self.title = raw[0]
        # set of while and for loops to sort default room data into appropriate attributes, allows for varied numbers of locations and objects
        n = 2
        while raw[n] != "NORMAL": #set initial description attribute, should copy exactly what you put in INITIAL area in the txt file
            self.initialDescription = self.initialDescription + str(raw[n]) + "\n"
            n += 1
        n+=1
        while raw[n] != "LOCATIONS": #set normal description attribute, should copy exactly what you put in NORMAL area in the txt file
            self.normalDescription = self.normalDescription + str(raw[n]) + "\n"
            n+=1
        self.normalDescription = (self.normalDescription).rstrip("\n") #remove whitespace on last line
        n+=1
        while raw[n] != "OBJECTS": # set list of locations available
            temp = []
            temp = raw[n].split(":")
            self.locations.append(temp)
            n+=1
        n+=1
        for i in (raw[n:]): #set list of objects (formatted as a list of lists containing an object and description)
            temp = []
            temp = i.split(":")
            self.objects.append(temp)         #read defaults from room file https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

    def printInitial(self):
            print(self.title)
            print(tw.fill(self.initialDescription, width=50))
            self.visited = True

    def roomDescription(self):
        objstr = "There is a "
        print(self.title)
        print(tw.fill(self.normalDescription, width=50))
        for i in self.objects:
            if self.objects.index(i) != len(self.objects)-1:
                objstr = objstr + i[0] + ", "
            else:
                objstr = objstr + "and " + i[0] + " in here."
        if len(self.objects) > 0 :
            print(tw.fill(objstr, width=50))


def goTo(room, player): #function to instantiate/change rooms
    try:
        player.loc = room.name
        if room.visited == True:
            room.roomDescription()
        else:
            room.printInitial()
    except:
        print("You have entered the astral plane, good luck traveler")

def dropObj(room, player, object):
    pass



def pickUp(room, player, object):
    pass

def moveObj(room, player, object):
    pass

def look(player, object):
    pass

def lookAround(room, player):
    pass

def usePhone(player): #hasn't been tested yet, just needed a home for the reference code
    if any("batteries" in s for s in player.inventory): #https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
        phoneNum = str(input("Enter the phone number you would like to call for help: "))
        if len(phoneNum) == 10 or len(phoneNum) == 11:
            endGame()
    else:
        print("It looks like the batteries are dead.")

def checkInput(raw):
    if raw == "exit":
        endGame()
    if raw == "help":
        print("help screen goes here")

    #check for verbs

def help():
    pass

def endGame():
    print("exit message")
    check = input("Want to start again? (Y/N) ").lower()
    if check == "yes" or check == "y":
        main()
    else:
        sys.exit() #https://stackoverflow.com/questions/73663/terminating-a-python-script

def main():
    player1 = Player()
    rooms = {
    "yakshack":Room("yakshack"),
    "sign" : Room("sign"),
    "river" : Room("river"),
    "souvenir" : Room("souvenir"),
    "lodge" : Room("lodge"),
    "well" : Room("well")
    }
    goTo(rooms["sign"], player1)
    #rooms["yakshack"].title = "changed"
    #print(rooms["yakshack"].title)
    #print(rooms[player1.loc].filepath)
    #yakshack = Room("yakshack")

    #print(rooms[player1.loc].filepath)
    while True:
        try: #https://www.w3schools.com/python/python_try_except.asp
            checkInput(input().lower())
        except RuntimeError:
            print("It looks like you did that incorrectly.")
        except EOFError: #https://www.programiz.com/python-programming/exceptions
            print("Please enter alphanumeric character only.")

main()
