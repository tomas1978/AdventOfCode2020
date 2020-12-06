#Day 2 problem from Advent of Code 2020, only first part solved!

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


entries = []
file = open('input.txt', 'r')
for line in file:
    entries.append(line)
file.close()

correctPasswordCounter=0

for i in range(0,len(entries)):
    if(checkPassword(entries[i])):
        correctPasswordCounter+=1

print ("Number of correct passwords: "+str(correctPasswordCounter))
