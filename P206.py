import re
filename = input().strip()
fn = open(filename, 'r')
code = fn.readline().strip()
pattern = fn.readline()
if code == 'T2M':
    for line in fn:
        morse = ''
        for e in line.strip():
            if e in pattern:
                j = pattern.find('[' + e + ']')
                j += 3
                k = pattern.find('[', j)
                morse += pattern[j:k] + ' '
            else:
                print('Invalid : ' + line, end='')
                morse = ''
                break
        if len(morse) > 0:
            print(morse.strip())
elif code == 'M2T':
    for line in fn:
        text = ''
        for e in line.strip().split():
            if e in re.split('\[|\]', pattern):
                j = pattern.find(']' + e + '[')
                j -= 1
                text += pattern[j]

            else:
                print('Invalid : ' + line, end='')
                text = ''
                break
        if len(text) > 0:
            print(text.strip())
else:
    print('Invalid code')

#C:\Users\skbra\OneDrive\Desktop\data1.txt