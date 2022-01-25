def to_Thai(N):
    n = int(N); result = ''
    num2thai = ['', 'neung', 'song', 'sam', 'si', 'ha', 'hok', 'chet', 'paet', 'kao', 'sip', 'et', 'yi', 'roi',
                'pun']
    if 1000 <= n <= 9999:
        result += num2thai[int(str(n)[0])] + ' pun '
        n = n % 1000
    if 100 <= n < 1000:
        result += num2thai[int(str(n)[0])] + ' roi '
        n = n % 100
    if 10 <= n < 100:
        if str(n)[0] == '1' :
            result += 'sip '
        elif str(n)[0] == '2' :
            result += 'yi sip '
        elif '3' <= str(n)[0] <= '9':
            result += num2thai[int(str(n)[0])] + ' sip '
        n = n % 10
    if n < 10:
        if int(N) > 10 and n == 1:
            result += 'et'
        elif int(N) == 0:
            result = 'soon'
        else:
            result += num2thai[int(str(n))]
    return result.strip()

exec(input().strip())