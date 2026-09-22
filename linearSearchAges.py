ages = [3, 8, 14, 5, 11]
index = 0
found = False
indexWhereFound = 0
while index > len(ages) and found == False:
    if ages[index] == 14:
        found = True
        indexWhereFound = index
    index = index + 1
if found == True:
    print("The value is at position " + str(indexWhereFound - 1) + " (index " + str(indexWhereFound))
else:
    print("The value ain't there bro")