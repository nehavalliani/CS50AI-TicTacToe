"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    if board==[[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]:
            return X
    countX=0
    countO=0
    for i in board:
        for j in i:
            if j==X:
                countX+=1
            elif j==O:
                countO+=1
    if countX>countO:
        return O
    else:
        return X


    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    if not terminal(board):
        possibleactions=[]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==EMPTY:
                    possibleactions.append((i,j))
        return possibleactions
    else:
        return "GAME OVER."

    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    import copy
    newboard=copy.deepcopy(board)
    currentplayer=player(board)
    # if newboard[action[0]][action[1]]!=EMPTY:
    #     raise Exception("Invalid board")
    newboard[action[0]][action[1]]=currentplayer
    return newboard



def winner(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            player=board[i][j]
            if player!=EMPTY:
                if i==0:

                    if board[i][j]==board[i+1][j]==board[i+2][j]:
                        return player
                    
                    if j==0:
                        if board[i][j]==board[i+1][j+1]==board[i+2][j+2]:
                            return player
                        if board[i][j]==board[i][j+1]==board[i][j+2]:
                            return player 
                    if j==2:
                        if board[i][j]==board[i+1][j-1]==board[i+2][j-2]:
                            return player
                            
                if i==1 and j==0:
                    if board[i][j]==board[i][j+1]==board[i][j+2]:
                        return player
                if i==2 and j==0:
                    if board[i][j]==board[i][j+1]==board[i][j+2]:
                        return player
                


    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError


def terminal(board):
    val=False
    if winner(board):
        val=True
        return val
    countempty=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            player=board[i][j]
            if player==EMPTY:
                countempty+=1
    if countempty==0:
        val=True
        return val
    return val


    
    



def utility(board):
    if terminal(board):
        utility=0
        if winner(board)==X:
            utility=1
        elif winner(board)==O:
            utility=-1
        
        return utility



def max_value(board):
    import math
    if terminal(board):
        return utility(board)
    v=-(math.inf)
    for action in actions(board):
        new=min_value(result(board,action))
        v=max(v,new)
    return v
def min_value(board):
    import math
    if terminal(board):
        return utility(board)
    v=math.inf
    for action in actions(board):
        new=max_value(result(board,action))
        v=min(v,new)
    return v

def minimax(board):
    if terminal(board):
        return None
    optimal=actions(board)[0]
    import math
    if player(board)==X:
        val=-math.inf
        for action in actions(board):
            current_val=min_value(result(board,action))
            if current_val>val:
                optimal=action
                val=current_val
        return optimal
    else:
        val=math.inf
        for action in actions(board):
            current_val=max_value(result(board,action))
            if current_val<val:
                optimal=action
                val=current_val
        return optimal


