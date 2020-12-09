entries = []
file = open('input.txt', 'r')
for line in file:
    entries.append(line)
file.close()

for i in range(0,20):
    print(entries[i])

