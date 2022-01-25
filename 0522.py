studentID = []
studentGrade = []
changeGradeID = []
finalGrade = []
sortedID = []
sortedGrade = []
grade = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
while True :
    rawData = input()
    if rawData == 'q' :
        break
    else :
        studentData = rawData.split()
        studentID.append(int(studentData[0]))
        if studentData[1] in grade :
            studentGrade.append(grade.index(studentData[1]))
changeGradeID = [int(x) for x in input().split()]
i = 0
while True :
    if i == len(changeGradeID) :
        break
    elif changeGradeID[i] in studentID :
        if studentGrade[studentID.index(changeGradeID[i])] != 0 :
            studentGrade[studentID.index(changeGradeID[i])] -= 1
    i += 1
for j in range(0, len(studentID)) :
    finalGrade.append(grade[studentGrade[j]])
sortedID = sorted(studentID)
n = 0
while True :
    if n == len(sortedID) :
        break
    elif sortedID[n] in studentID :
        sortedGrade.append(finalGrade[studentID.index(sortedID[n])])
    n += 1
for k in range(0, len(sortedID)) :
    print(sortedID[k], sortedGrade[k])