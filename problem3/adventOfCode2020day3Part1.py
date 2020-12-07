#Advent of Code 2020 problem 3: Part 1, answer: 276
lines = []
file = open('input.txt', 'r')
for line in file:
    lines.append(line)
file.close()

row=0
column=0

#Repeat the map sideways
for line in range(0,len(lines)):
    currentLine=lines[line]
    for i in range(0,len(lines[line])+1):
        lines[line]+=currentLine
        #Remove newlines in string
        lines[line]=lines[line].replace('\n', '')

trees=0 #Used to count the number of trees that are hit
    
#Move through the map, check if a tree is hit
while(row<len(lines)-1):
    row+=1
    column+=3
    if(row>=len(lines[0])):
       row=0
    if(lines[row][column]=='#'):
        trees+=1

print("Number of trees, problem part 1:"+str(trees))
