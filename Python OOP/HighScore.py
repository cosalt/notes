HighScore = [] # DECLARE HIGHSCORE : ARRAY[0:7]

def ReadData():
    try:
        with open("HighScoreTable.txt") as f:
            temp = []
            lines = f.readlines()
            for i in range(0, len(lines), 3):
                temp.append([line.strip() for line in lines[i:i+3]])
            return temp
    except:
        print("No file found!")

def OutputHighScores(arr):
    for i, j in enumerate(arr):
        print(f"{arr[i][0]} reached level {arr[i][1]} with a score of {arr[i][2]}")

def SortScores():
    global HighScore
    arr = HighScore
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            level1, level2 = int(arr[j][1]), int(arr[j+1][1])
            score1, score2 = int(arr[j][2]), int(arr[j+1][2])
            if level1 > level2:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            elif level1 == level2:
                if score1 > score2: 
                    arr[j+1], arr[j] = arr[j], arr[j+1]
    HighScore = arr
    return HighScore



HighScore = ReadData()
print("before")
OutputHighScores(HighScore)
SortScores()
print("after")
OutputHighScores(HighScore)
