validPassports=0

entries = []
file = open('input.txt', 'r')

str=""
for line in file:
    str+=line
    if(str=="\n"):
        str="";
    entries.append(str)
file.close()

#for i in range(0,len(entries)):
#    entries[i]=entries[i].replace('\n'," ")

for i in range(0,20):
    print(entries[i])




