name1, month1, date1, year1 = input().strip().split()
name2, month2, date2, year2 = input().strip().split()
mo = ['', "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
if month1 in mo :
    mo1 = mo.index(month1)
if month2 in mo :
    mo2 = mo.index(month2)
dob1 = [int(year1), mo1, int(date1[:-1])]
dob2 = [int(year2), mo2, int(date2[:-1])]
if dob2 > dob1 :
    print(name1)
elif dob1 > dob2:
    print(name2)
else:
    print(name1, name2)