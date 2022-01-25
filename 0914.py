f1 = input().strip()
f2 = input().strip()
f3 = input().strip()
infile = open(f1, 'r')
idc = dict(); prof = dict()
for line in infile:
    code, id = line.strip().split(',')
    idc.update({code: id})
infile.close()
infile = open(f2, 'r')
for line in infile:
    code, tc = line.strip().split(',')
    prof.update({code: tc})
infile.close()
infile = open(f3, 'r')
for line in infile:
    codeid, codetc = line.strip().split(',')
    if codeid in idc and codetc in prof:
        print(idc[codeid] + ',' + prof[codetc])
    else:
        print('record error')
infile.close()