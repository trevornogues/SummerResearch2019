import sched, threading, time
import random


s = sched.scheduler(time.time, time.sleep)
# threadObj = threading.Thread(target=takeANap)

def print_time(currentCheck = 0, times = [0,0,0], checked = [0,0,0], priority = 0):
    print(currentCheck, checked, time.time())
    lower = currentCheck - 1
    higher = currentCheck + 1
    priority += 1
    if lower >= 0 and checked[lower] == False:
        checked[lower] = True
        s.enter(times[lower],priority,print_time,argument=(lower,times,checked,priority))
        s.run()
    if higher < len(checked) and checked[higher] == False:
        checked[higher] = True
        s.enter(times[higher],priority,print_time,argument=(higher,times,checked,priority))
        s.run()

def print_some_times():
    print("start",time.time())
    length = 10
    times = [0]*length
    checked = [False]*length
    for i in range(length):
        times[i] = random.randint(1,10)
    currentCheck = random.randint(0,9)
    checked[currentCheck] = True
    priority = 1
    print(currentCheck,times)
    s.enter(times[currentCheck], priority, print_time, argument=(currentCheck,times,checked,priority))
    s.run() 
    print("end",time.time())

# print_some_times()

def threadingHelper(delay, thread):
    print("start of", thread, time.time())
    for currentDelay in delay:
        time.sleep(currentDelay)
        print(thread, "slept for", currentDelay, "seconds", time.time())
    print("end of", thread, time.time())

def threadingExample():
    trev = [0]*10
    small = []
    large = []
    for i in range(9):
        trev[i] = random.randint(1,10)
        if trev[i] <= 5:
            small.append(trev[i])
        else:
            large.append(trev[i])

    threadA = threading.Thread(target=threadingHelper, args=(small,"thread a"))
    threadB = threading.Thread(target=threadingHelper, args=(large,"thread b"))
    threadA.start()
    threadB.start()

    # print("end:", time.time())

threadingExample()