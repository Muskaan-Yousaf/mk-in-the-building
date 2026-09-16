#task one

# songs = ["Dirty Harry", "Tally", "Guns for Hands", "Crimewave", "19-2000", "Fake You Out", "Ain't In LA", "Cottonwood", "Kitchen Sink"]

# print(songs[0])
# print(songs[2])
# print(songs[4])

# songTwo = input("Add your own song! ")
# songs[1] = songTwo
# print(songs[1])

# for songy in range(len(songs)):
#     print("Song " + str(songy + 1) + " = " + songs[songy])

# print("There are " + str(len(songs)) + " songs.")


#task two


steps = [6840, 9120, 7750, 10420, 8320]
days = ["Mon", "Tue", "Wed", "Thurs", "Fri"]

total = 0
count = 0
getNumber = int(input("Enter a number: "))

for x in range(len(steps)):
    print(days[x] + " " + str(steps[x]))
    total = total + steps[x]
    if steps[x] >= 8000:
        count = count + 1

print(total)
print(count)
average = total / len(days)
roundedAverage = round(average, 2)
print("Average = " + str(roundedAverage) + " .")

