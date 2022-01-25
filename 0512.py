firstname = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nickname = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]
amount = int(input())
result = [""]*amount
for i in range(0,amount) :
    search = input()
    if search in firstname :
        ind = firstname.index(search)
        result[i] = nickname[ind]
    elif search in nickname :
        ind = nickname.index(search)
        result[i] = firstname[ind]
    else :
        result[i] = "Not found"
for j in range(0,amount) :
    print(result[j])