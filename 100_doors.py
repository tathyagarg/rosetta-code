# https://rosettacode.org/wiki/100_doors

doors = [False]*100
for n in range(1, 101):
    for index, door in enumerate(doors):
        if index % n == 0:
            doors[index] = not door

for i, door in enumerate(doors):
    if door: print(i, end=' ')
print()
