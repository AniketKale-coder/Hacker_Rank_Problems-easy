def breakingRecords(scores):
    maxscore = scores[0]
    maxscore_count = 0
    minscore = scores[0]
    minscore_count = 0
    for i in scores:
        if(i < minscore):
            minscore = i
            minscore_count += 1
        if(i > maxscore):
            maxscore = i
            maxscore_count += 1
        print(minscore, minscore_count)
    return list([maxscore_count, minscore_count])


scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
result = breakingRecords(scores)
