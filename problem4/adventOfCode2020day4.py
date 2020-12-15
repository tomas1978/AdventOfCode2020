#Day 4 part 1, answer: 210

validPassports = 0
lines = []      #lines read from the file
entries = []    #for complete lines of passport entries

file = open('input.txt', 'r')

for line in file:
    if(line!="\n"):
        lines.append(line.strip())
    else:
        lines.append(line)
file.close()

#Remove newlines to create entries with all data for
#one passport on a single line
str=""
for i in range(0,len(lines)):
    if(lines[i]!="\n"):
        str+=lines[i]
    else:
        entries.append(str)
        str=""

#Check and count valid passports
for i in range(0,len(entries)):
    if(entries[i].find("byr",0,len(entries[i]))!=-1 and 
       entries[i].find("iyr",0,len(entries[i]))!=-1 and
       entries[i].find("eyr",0,len(entries[i]))!=-1 and
       entries[i].find("hgt",0,len(entries[i]))!=-1 and
       entries[i].find("hcl",0,len(entries[i]))!=-1 and
       entries[i].find("ecl",0,len(entries[i]))!=-1 and
       entries[i].find("pid",0,len(entries[i]))!=-1):
        validPassports+=1

print("Number of valid passports: ")
print(validPassports)
