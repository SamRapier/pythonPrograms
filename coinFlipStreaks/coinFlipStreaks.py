def flipCoin():
    import random
    flip = random.randint(0, 1)

    return flip

def multipleFlips(n):
    coinList = []
    for i in range(n):
        coinList.append(flipCoin())
    
    return coinList

def analyseList(lst):
    prevItem = None
    streakCount = 1
    bestStreak = 0

    for item in lst:
        if item == prevItem:
            streakCount = streakCount + 1
            if streakCount > bestStreak:
                bestStreak = streakCount
        else:
            streakCount = 1

        prevItem = item

    return bestStreak


def streakProbability(n):
    streakDict = dict()

    for i in range(n):
        streak = analyseList(multipleFlips(200))

        if streak in streakDict:
            streakDict[streak] += 1
        else:
            streakDict[streak] = 1

    return streakDict




# coinFlipList = multipleFlips(200)

# print(coinFlipList)
# print(analyseList(coinFlipList))

print(streakProbability(20000))

# d = dict()

# for i in range(100):
#     key = i % 10
#     if key in d:
#         d[key] += 1
#     else:
#         d[key] = 1

# print(d)



