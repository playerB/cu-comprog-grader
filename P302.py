pos = input().strip()
row = ''
col = ''
if len(pos) <= 3:
    row = pos[0]
    col = pos[1:3]
else:
    roworcol = ''; pos1 = ''; pos2 = ''
    for i in range(len(pos)):
        if pos[i] == '=': break
        roworcol += pos[i]
    roworcol = roworcol.strip()
    for j in range(i+1, len(pos)):
        if pos[j] == ',':break
        pos1 += pos[j]
    pos1 = pos1.strip()
    for k in range(j+1, len(pos)):
        if pos[k] == '=':break
    for l in range(k+1, len(pos)):
        pos2 += pos[l]
    pos2 = pos2.strip()
    if roworcol == 'row':
        row = pos1
        col = pos2
    else:
        row = pos2
        col = pos1
#-----------------------------------------
valid_row = False
valid_col = False
if ('A' <= row <= 'z') and (len(row) == 1):
    valid_row = True
try:
    col = int(col)
    if 1 <= col <= 52:
        valid_col = True
except:
    pass
#-----------------------------------------
if (valid_row == True) and (valid_col == True):
    r = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(row)
    if r%2 == col%2 :
        print('Black')
    else:
        print('White')
elif (valid_row == True) and (valid_col == False):
    print('Invalid column')
elif (valid_row == False) and (valid_col == True):
    print('Invalid row')
else:
    print('Invalid row and column')