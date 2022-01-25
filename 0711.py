word = input().strip()
if word[-1] in ['s', 'x'] or word[-2:] == 'ch':
    print(word + 'es')
elif word[-1] == 'y' and word[-2] not in ['a', 'e', 'i', 'o', 'u']:
    print(word[:-1] + 'ies')
else:
    print(word + 's')