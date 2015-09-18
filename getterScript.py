#This script goes through a Java file and writes all the needed getter methods
#for **private** instance variables in a new java file.

#@author - Mostafa Bhuiyan


#VALID_DEFAULT_TYPES = ["String", "int", "double", "float", "byte", "long", "short", "boolean", "char"]

while True:
    try:
        fileName = str(input("Enter the name of the file you wish to use, including the extension. "))
        reader = open(str(fileName))
        break
    except FileNotFoundError:
        print("That's not a valid file name! Try again. ")

numLines = int(input("Up to what line do you have instance variables? "))
newGetters = open("newGetters.java", "w")

def getterScript():
    readFile = open(str(fileName))
    newLines = readFile.readlines()
    modified = newLines[:numLines]
    #print(modified)
    noWhite_List = []
    privateVars = []
    varTypes = []
    
    #Gets rid of white space in different lines
    for lines in modified:
        noWhiteSpace = lines.strip()
        noWhite_List.append(noWhiteSpace)

    #Finds all the private instance variables
    for lines in noWhite_List:
        if "private" in lines and "private static" not in lines:
            privateVars.append(lines)
    
    #print(privateVars)
    #newGetters.write(str(privateVars))

    #Gets the variable type
    for lines in privateVars:
        varSplit = lines.split(" ")
        varTypes.append(varSplit)

    #print(varTypes)
        
    print("Getters instantiated: " + "\n")
    #Writes the getters
    count = 0
    for brackets in varTypes:
        bracketLen = len(brackets[2])
        firstUpperCase = str(brackets[2][0].upper())
        newGetters.write("public " + brackets[1] + " get" + firstUpperCase + brackets[2][1:bracketLen - 1] + "() { \n" + "    return " + brackets[2] + "\n" + "}" + "\n \n")
        print("public " + brackets[1] + " get" + firstUpperCase + brackets[2][1:bracketLen - 1] + "()") 
        count += 1

    print("\n" + "Total getter methods: " + str(count))
    print("Getters are in newGetters.java")
    newGetters.close()
    
getterScript()
