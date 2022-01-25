file1, file2 = input().strip().split()
def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0:  # ถ้าอ่านหมดแล้ว ออกจากวงวน
            break
        x = t.strip().split()  # ลบ blank ซ้ายขวา
        if len(x) == 2:  # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
            return x[0], x[1]
    return "", ""# แฟ้มหมดแล้ว คืนสตริงว

fopen1 = open(file1)
fopen2 = open(file2)
rn1 = read_next(fopen1)
rn2 = read_next(fopen2)
while rn1 != ('', '') and rn2 != ('', ''):
    if int(rn2[0][-2:]) > int(rn1[0][-2:]):
        print(rn1[0], rn1[1])
        rn1 = read_next(fopen1)
    elif int(rn1[0][-2:]) > int(rn2[0][-2:]):
        print(rn2[0], rn2[1])
        rn2 = read_next(fopen2)
    elif int(rn1[0][:8]) > int(rn2[0][:8]):
        print(rn2[0], rn2[1])
        rn2 = read_next(fopen2)
    elif int(rn2[0][:8]) > int(rn1[0][:8]):
        print(rn1[0], rn1[1])
        rn1 = read_next(fopen1)
while rn1 != ('', ''):
    print(rn1[0], rn1[1])
    rn1 = read_next(fopen1)
while rn2 != ('', ''):
    print(rn2[0], rn2[1])
    rn2 = read_next(fopen2)