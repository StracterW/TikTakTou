
import random

max_depth = 9

possibleWin = [[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)]]

def draw(dic):
    print(dic[(0,0)] + "|"+ dic[(1,0)] + "|" + dic[(2,0)] + "                            00|10|20")
    print(dic[(0,1)] + "|"+ dic[(1,1)] + "|" + dic[(2,1)] + "                            01|11|21")
    print(dic[(0,2)] + "|"+ dic[(1,2)] + "|" + dic[(2,2)] + "                            02|12|22")
    print()

def all_placed(dic):
    for d in dic: 
        if dic[d] == " ":
            return 1
    return 0
def result(dic):
    global possibleWin
    for win in possibleWin:
        if dic[win[0]] == dic[win[1]] == dic[win[2]]:
            if dic[win[0]] == "X":
                return -1
            elif dic[win[0]] == "O":
                return 1

def miniMax(dic, depth, is_maximizing,turn):
    depth += 1
    if all_placed(dic) == 0 or max_depth == depth:
        return 0
    elif result(dic) == -1:
        return -100//depth 
    elif result(dic) == 1:
        return 100 // depth
    pos_move = [i for i in dic if dic[i] == " "]
    if is_maximizing:
        best_score = -1000
        for move in pos_move:
            dic[move] = turn
            score = miniMax(dic, depth, False,turn)
            dic[move] = " "
            if score > best_score:
                best_score = score
    if not is_maximizing:
        best_score = 1000
        for move in pos_move:
            dic[move] = "X"
            score = miniMax(dic, depth, True,turn)
            dic[move] = " "
            if score < best_score:
                best_score = score
    
    return best_score

def compMove(dic,turn):
    scorea = []
    best_score = -1000
    pos_move = [i for i in dic if dic[i] == " "]
    for move in pos_move:
        dic[move] = turn
        score = miniMax(dic, 0, False,turn)
        dic[move] = " "
        if score >= best_score:
            best_score = score
            scorea.append([move,score])
            best_move = move
    scorea = [i for i in scorea if i[1] == scorea[len(scorea)-1][1]]
    best_move = scorea[random.randint(0,len(scorea)-1)][0]
    
    return best_move

def new_game():
    turn = "O"
    run = True
    dic = {
        (0,0): " ",
        (1,0): " ",
        (2,0): " ",
        (0,1): " ",
        (1,1): " ",
        (2,1): " ",
        (0,2): " ",
        (1,2): " ",
        (2,2): " ",}
    while run:
        try:
            if turn == "X":
                inp = [int(i) for i in input()]
                if dic[(inp[0],inp[1])] == " ":
                    dic[(inp[0],inp[1])] = turn
                    turn = "X" if turn == "O" else "O"
            else: 
                move = compMove(dic,turn)
                dic[move] = turn
                turn = "X" if turn == "O" else "O"
        except:
            run = False
            print("Wrong input")

        draw(dic)
        for win in possibleWin:
            if dic[win[0]] == dic[win[1]] == dic[win[2]]:
                if dic[win[0]] == "X":
                    print("Player win")
                    run = False
                    print("Game over")
                elif dic[win[0]] == "O":
                    print("Computer Win")
                    run = False
                    print("Game over")
        if all_placed(dic) == 0:
            print("Draw")
            run = False
            new_game()

new_game()