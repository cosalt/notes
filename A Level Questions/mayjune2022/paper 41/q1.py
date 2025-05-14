playerscores = [[" ", " "] for i in range(11)]

def ReadHighScores():
    with open("HighScore.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]
        for i in range(0, min(len(lines), 22), 2):
            name = lines[i]
            score = int(lines[i + 1])
            playerscores[i // 2] = [name, score]


def OutputHighScores():
    for name, score in playerscores:
        print(f"{name} {score}")

ReadHighScores()
OutputHighScores()


while True:
    player = input("Player: ")
    if len(player) != 3:
        print("must be 3 characters")
        continue

    while True:
        score = int(input("score: "))
        if score >= 100000 or score <= 1:
            print("score must be 100,000-1")
            continue
        break
    break


def topten(playername, playerscore):
    OutputHighScores()
    playerscores[-1] = ([playername, playerscore])
    playerscores.sort(key=lambda x: x[1], reverse=True)
    OutputHighScores()
    

topten(player,score)

def WriteTopTen():
    with open("NewHighScore.txt", "w") as file:
        for name, score in playerscores:
            file.write(name)
            file.write(str(score))

WriteTopTen()
