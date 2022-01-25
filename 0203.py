dmy = input().split("/")
month = ["","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(month[int(dmy[1])] + " " + str(dmy[0]) + ", " + str(dmy[2]))