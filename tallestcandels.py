def bdayCakeCandles(cndls):
    print(cndls.count(max(cndls)))


def birthdayCakeCandles(candles):
    a = 0
    c = 0
    for i in candles:
        if(i > a):
            a = i
    for i in candles:
        if(a == i):
            c += 1
    print(c)


candel_cout = 5
candles = [2, 10, 10, 9, 2]
birthdayCakeCandles(candles)
bdayCakeCandles(candles)
