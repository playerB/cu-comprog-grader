n = int(input()); allSong = dict()
for i in range(n):
    song, singer, genre, time = input().strip().split(',')
    mi, se = [int(e) for e in time.split(':')]
    if genre not in allSong:
        allSong.update({genre: [mi, se]})
    else:
        allSong[genre][0] += mi
        allSong[genre][1] += se
        if allSong[genre][1] >= 60:
            allSong[genre][0] += 1
            allSong[genre][1] -= 60
for i in sorted([[v, k] for k, v in allSong.items()])[-1:-4:-1]:
    if i[0][1] < 10:
        print(i[1], '-->', str(i[0][0]) + ':0' + str(i[0][1]))
    else:
        print(i[1], '-->', str(i[0][0]) + ':' + str(i[0][1]))