correct = input().strip().upper()
answer = input().upper()
if len(correct) != len(answer) :
    print("Incomplete answer")
else :
    score = 0
    for i in range(0,len(correct),1) :
        if correct[i] == answer[i] :
            score += 1
    print(score)