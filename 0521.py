studentID = []
studentGrade = []
changeGradeID = []
finalGrade = []
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
    print(studentID[j], finalGrade[j])