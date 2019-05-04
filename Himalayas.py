from textwrap import fill  #https://pymotw.com/3/textwrap/
from sys import exit
import secrets as shh ##Import another Python file and use functionality (10) this is another python file in the same directory as the main script

class Player: #class to store player data, like inventory, location, etc.
    def __init__(self):
        self.name = ""
        self.inventory = []
        self.loc = "sign"


class Room: #A Class (20)
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
        #File Reading (15)
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
        n+=1
        while raw[n] != "OBJECTS": # set list of locations available
            temp = []
            temp = raw[n].split(":")
            self.locations.append(temp) #Using build-in List (or other data structure) functionality (so a function like insert or append) (3)
            n+=1
        n+=1 ##Using +=, -=, etc (3)
        for i in (raw[n:]): #set list of objects (formatted as a list of lists containing an object and description)
            temp = []
            temp = i.split(":")
            self.objects.append(temp)         #read defaults from room file https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

    def printInitial(self):
            print(self.title)
            print(fill(self.initialDescription, width=50))
            self.visited = True

    def roomDescription(self):
        objstr = "There is a "
        print(self.title)
        print(fill(self.normalDescription, width=50))
        for i in self.objects:
            if self.objects.index(i) != len(self.objects)-1:
                objstr = objstr + i[0] + ", "
            else:
                objstr = objstr + "and " + i[0] + " in here."
        if len(self.objects) > 0 : #Using len with a purpose (and not within a different piece of code you are getting points for) (2)
            print(fill(objstr, width=50))


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
    if item.name == object[1]:
        self.location.inventory.append(item)
        self.inventory.remove(item)
        print("You dropped the", item.name)
        return
    print(object[1] + " is not here!")

def pickUp(room, player, object):
    for item in self.location.inventory:
        if item.name == object[1]:
            self.inventory.append(item)
            self.locations.inventory.remove(item)
            print("You picked up the", item.name)
            return
    print(object[1] + " is not here!")

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
            player.name = str(input("What is your name?"))
            score = shh.checkScore(player.name, player.inventory)
            print(score)
            endGame()  #Nested if statement (7)
    else:
        print("It looks like the batteries are dead.") ##print() statement (2)

def help():
    pass #map : shows a map of the project

def endGame():
    check = input("Want to start again? (Y/N) ").lower()
    if check == "yes" or check == "y":
        main()
    else:
        exit() #https://stackoverflow.com/questions/73663/terminating-a-python-script


def checkVerbs(raw, player, room):
    verb = ""
    verbList = [["go", "head", "travel"]] #list of lists of synonyms for each command ##A list that contains lists (20)
    verbDict = { #matches each list of synonyms with a functions
    "goTo" : verbList[0],
    }
    #for loop checking if synonym matches any list for each key
    for word in raw:
        for k, v in verbDict.items():
            if word in v:
                verb = k
    return verb

def checkSubject(raw, player, room, verb): #Function Definition with Parameters and Function Call (10)
    sub = ""  #Assignment Statement (3)
    pos = ""
    count = 0
    for word in raw: ##Nested Loops (12)
        # check if in room inventory
        for item in player.inventory:
            if word in item[0]:
                sub = item[0]
                pos = "player"
                count += 1
        for item in room.objects: ##Python code that “walks” through the contents of an List (or other data structure) (7)
            if word in item[0]:
                sub = item[0]
                pos = "room"
                count += 1
        if verb == "goTo":
            for item in room.locations: #For loop (7)
                if word in item[1]:
                    sub = item[0]
                    count +=1
        if count > 1:
            sub = ""
    return sub, pos

def sortCommand(player, rooms, verb, subject, pos): #sorts the subject and verb options to check for continuity
    normVerbList = ["drop", "pickup", "move"] #List (10)
    if verb in normVerbList:
        print("normal") #check if pos = player or room, separate pickup and drop then either call drop or pickup with room, player, object, worry about move later
    if verb == "look" and subject != "":
        pass #check if object is in room or player then pass room, player, object to look function
    if verb == "look" and subject == "":
        pass #pass room and player to lookAround function
    if verb == "goTo":
        goTo(rooms[subject], player)

def checkInput(raw, player, rooms): #A function that calls another function (main not included) (5)
    #print(rooms[player.loc].name)
    raw = raw.split(" ")
    subject = ""
    room = rooms[player.loc]
    if "exit" in raw: #If Statement (5)
        endGame()
    if "help" in raw:
        help()
    if "map" in raw:
        shh.displayMap()
    verb = checkVerbs(raw, player, room)
    subject, pos = checkSubject(raw, player, room, verb)
    sortCommand(player, rooms, verb, subject, pos)

def main(): #function definition and call (7)
    player1 = Player()
    rooms = { #Dictionary (15)
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

    #print(rooms[player1.loc].objects)
    while True: #While loop (7)
        try: #https://www.w3schools.com/python/python_try_except.asp ##Try/Except Block (15)
            checkInput(input().lower(), player1, rooms)
        except RuntimeError:
            print("It looks like you did that incorrectly.")
        except EOFError: #https://www.programiz.com/python-programming/exceptions
            print("Please enter alphanumeric character only.")

main()

''' 2 Styles of Comments (single and multiline) (3)
#Function Definition and Function Call (7)
#Function Definition with Parameters and Function Call 10
    Function Definition with Default Parameters and Function Call 12
    Recursive Function Definition and Recursive Function Call 17
#A function that calls another function (main not included) 5
#Assignment Statement 3
#2 Styles of Comments (single and multiline) 3
#File Reading 15
    File Writing 15
#If Statement 5
#Nested If Statement 7
#For loop 7
#While loop 7
#A Class 20
#List 10
    Tuple 15
    Set 15
#Dictionary 15
#A list that contains lists 20
    Convert between Data Structures (List, Tuple, Set, etc.) for a purpose 13
    Convert between string and list (or list and string) for a purpose 7
#Nested Loops 12
#Python code that “walks” through the contents of an List (or other data structure) 7
    Finding the largest or smallest item in an List (not built-in) 10
#Using build-in List (or other data structure) functionality (so a function like insert or append) (3)
    Sorting of the contents of an List (not the built-in sort) 20
#Try/Except Block 15
#Using +=, -=, etc (3)
#Using len with a purpose (and not within a different piece of code you are getting points for) (2)
#print() statement (2)
    Using the formatting for strings (with print() statement) 5
    Random Number Generator 10
#Import another Python file and use functionality 10
--
    Flowchart or Design of the Entire Program (required) 20
'''
