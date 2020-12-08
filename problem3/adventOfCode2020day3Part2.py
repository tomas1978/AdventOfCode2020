#Advent of Code 2020 problem 3: Part 2

def move(map,stepsRight,stepsDown):
    row=0
    column=0
    trees=0
    #Move through the map, check if a tree is hit
    while(row<len(lines)-1):
        row+=stepsDown
        column+=stepsRight
        if(row>=len(lines[0])):
           row=0
        if(lines[row][column]=='#'):
            trees+=1
    return trees

lines = []
file = open('input.txt', 'r')
for line in file:
    lines.append(line)
file.close()

#Repeat the map sideways
for line in range(0,len(lines)):
    currentLine=lines[line]
    for i in range(0,len(lines[line])+100):
        lines[line]+=currentLine
        #Remove newlines in string
        lines[line]=lines[line].replace('\n', '')

slopes=[]

slopes.append(move(lines,1,1))
slopes.append(move(lines,3,1))
slopes.append(move(lines,5,1))
slopes.append(move(lines,7,1))
slopes.append(move(lines,1,2))

slopeProduct=1
for i in slopes:
    slopeProduct*=i

print("Product of paths: "+str(slopeProduct))



