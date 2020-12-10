entries = []
file = open('input.txt', 'r')
for line in file:
    entries.append(line)
file.close()

#Trying to read all but empty lines
for i in range(0,20):
    if(entries[i] != ""):
        print(entries[i])
