item = [1,2,3,4]

def changeItem(it = []):
    temp = []
    for element in range(len(it)):
        it[element] = it[element] + 1
    return it
   


print(changeItem(item))
print(item)


