commandLine = int(input().strip())
nextQ = -1
for i in range(commandLine) :
    cmdCall = input().strip().split()
    if cmdCall[0] == "reset" :
        qTicket = int(cmdCall[1])-1
        qTicketList = list()
        qTimeList = list()
        recordWaitTime = list()
    elif cmdCall[0] == "new" :
        timeNewQ = int(cmdCall[1])
        qTimeList.append(timeNewQ)
        qTicket += 1
        qTicketList.append(qTicket)
        print("ticket", qTicket)
    elif cmdCall[0] == "next" :
        nextQ += 1
        print("call", qTicketList[nextQ])
    elif cmdCall[0] == "order" :
        timeCalledQ = int(cmdCall[1])
        print("qtime", qTicketList[nextQ], timeCalledQ-qTimeList[nextQ])
        recordWaitTime.append(timeCalledQ-qTimeList[nextQ])
    elif cmdCall[0] == "avg_qtime" :
        avg = float(sum(recordWaitTime)/len(recordWaitTime))
        print("avg_qtime", round(avg, 4))