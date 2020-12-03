def findSumOfTwo(entryList):
    product=0
    for i in range(0,len(entryList)):
        for j in range(0,len(entryList)):
            if(int(entryList[i])+int(entryList[j])==2020):
                product=int(entryList[i])*int(entryList[j])
    return product

def findSumOfThree(entryList):
    product=0
    for i in range(0,len(entryList)):
        for j in range(0,len(entryList)):
            for k in range(0,len(entryList)):
                if(int(entryList[i])+int(entryList[j])+int(entryList[k])==2020):
                    product=int(entryList[i])*int(entryList[j])*int(entryList[k])
    return product


entries = []
file = open('input.txt', 'r')
for line in file:
    entries.append(line)
file.close()
print("Svar på del 1: "+str(findSumOfTwo(entries)))
print("Svar på del 2: "+str(findSumOfThree(entries)))


