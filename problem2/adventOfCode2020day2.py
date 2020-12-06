#Day 2 problem from Advent of Code 2020, both first parts solved!

#Check policy according to part 1
def checkPassword(entry):
    dashIndex=entry.find("-",0,len(entry))
    colonIndex=entry.find(":",dashIndex,len(entry))
    lowestNumber=int(entry[0:dashIndex])
    highestNumber=int(entry[dashIndex+1:colonIndex-1])
    character=entry[colonIndex-1]
    password=entry[colonIndex+2:len(entry)]
    charCounter=0;
    for i in range(0,len(password)):
        if(password[i]==character):
            charCounter+=1
    if(charCounter>=lowestNumber and charCounter<=highestNumber):
        return True
    else:
        return False

#Check policy according to part 2
def checkPassword2(entry):
    dashIndex=entry.find("-",0,len(entry))
    colonIndex=entry.find(":",dashIndex,len(entry))
    index1=int(entry[0:dashIndex])-1
    index2=int(entry[dashIndex+1:colonIndex-1])-1
    character=entry[colonIndex-1]
    password=entry[colonIndex+2:len(entry)]
    if(password[index1]==character):
        if(password[index2]==character):
            return False
        else:
            return True
    else:
        if(password[index2]==character):
            return True
        else:
            return False
    

entries = []
file = open('input.txt', 'r')
for line in file:
    entries.append(line)
file.close()

correctPasswordCounterPolicy1=0
correctPasswordCounterPolicy2=0

for i in range(0,len(entries)):
    if(checkPassword(entries[i])):
        correctPasswordCounterPolicy1+=1
    if(checkPassword2(entries[i])):
        correctPasswordCounterPolicy2+=1   

print ("Number of correct passwords, policy 1: "+str(correctPasswordCounterPolicy1))
print ("Number of correct passwords, policy 2: "+str(correctPasswordCounterPolicy2))
