# Greet user
# Ask if retrieving information or inputing information

# if retrieving information, ask for name of character desired
# can also take inputs such as "daughter of" "sister of"
# if a name is entered, look for the entry of that name
# if a relationship is entered, entries whose attributes matches the relationship are returned
# an entry can have multiple relationships

# if adding information, ask to confirm. "Do you want to create a new character?"
# Accepts yes/no
# if No return to start
# if yes, ask for Character name
# check if character name is in use
# if not, create Character
# Ask if user wants to add more attributes. Give list of attributes or "save and finish"
# loop through adding attributes until user is done
# add Character name to list when finished, listOfAllCharacters

# after save/finish, prompt: "Retrieve, Add, close?"


class Character:
    def __init__(self, firstName):
        self.firstName = firstName

    def addLastName(self):
        self.lastName = input("What is the character's last name? \n")

    relationshipList = []

    def addRelationship(self):
        self.newRelationship = Relationship()
        self.newRelationship.type = input("What kind of relationship is it? Type 'daughter of' 'brother of' etc.\n")
        self.newRelationship.targetCharacter = input("To whom is this relationship?\n")
        self.relationshipList.append(self.newRelationship)
        print("Your character is " + self.firstName,  self.relationshipList)
        pass
    

class Relationship:
    def __init__(self):
        self.type = None
        self.targetCharacter = None
        # How do I get the console to print all of a Character's relationships? 
        
listOfAllCharacters = []

def addCharacter():
    characterName = input("What is the Character's name?\n")

    newCharacter = Character(characterName)
    print("Your new Character's name is " + newCharacter.firstName)
    listOfAllCharacters.append(newCharacter.firstName)
    print("Would you like to add any attributes to your character?\nType 'last name' or 'relationship' or hit ENTER to return")
    userInput = input()
    if userInput == "last name":
        newCharacter.addLastName()
        print("Your character's full name is " + newCharacter.firstName + " " + newCharacter.lastName)
        print("Would you like to add any more attributes?\nType 'relationship' or press ENTER")
        userInput = input()
        if userInput == "relationship":
            newCharacter.addRelationship()
        if userInput == "":
            pass
        else:
            print("Unrecognized input")
            startProgram()
   
    if userInput == "relationship":
        newCharacter.addRelationship()

    if userInput == "":
        startProgram()

    

def startProgram():


    print("Hello! Would you like to ADD a Character or RETRIEVE a Character?\n")

    userInput = input("Press 1 for ADD\nPress 2 for RETRIEVE\n")

    if userInput == "1":
        addCharacter()
    if userInput == "2":
        print("Enter the name of the character you would like to retrieve\nOr type 'all characters' to print a list of all characters currently stored")
        userInput = input()
        if userInput == "all characters":
            print(listOfAllCharacters)
        

startProgram()
