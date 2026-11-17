hh = 0
while True:
    mm = 0
    while True:
        ss = 0
        while True:
            print(hh, ":", mm, ":", ss, sep="")
            ss = ss + 1
            if segundos > 59:
                break
        mm = mm + 1
        if mm > 59:
            break
    hh = hh + 1
    if hh > 23:
        break
