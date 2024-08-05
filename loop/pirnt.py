color = ['red', 'blue', 'pink', 'white', 'yellow']

i = 0 
while i < len(color):
    if color[i] == "red":
        print(color[i])
        break
    else:
        print(i)
    i += 1

#continue

i = 0 
while i < len(color):
    i += 1
    if i == 2:
        continue
    print(i)

#else if elif

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("I is longer")