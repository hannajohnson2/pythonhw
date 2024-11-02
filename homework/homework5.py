import numpy as np

#1
def only_odd(arr):
    empty_array = np.array([])
    for row in arr:
        if np.all(row % 2 != 0):
            empty_array = np.append(empty_array, row)
    return empty_array
            
a = np.array([[1,2,3], [5,7,9], [1,4,7], [5, 9, 13]])
print(only_odd(a))

#2

#2.1

def checkerboard():
    return np.zeros((8,8))

print(checkerboard())

#2.2

#def checkerboard2():
    #board = np.zeros((8,8))
    #for row in np.arange(0, len(board), 2):
        #for col in np.arange(0, len(board[row]), 2):
            #board[row][col] = 1
    #return board

#print(checkerboard2())
#board[::2, ::2] = 1

#2.3

def checkerboard3():
    board = np.zeros((8,8))
    for row in np.arange(0, len(board), 2):
        for col in np.arange(0, len(board[row]), 2):
            board[row][col] = 1
    for row in np.arange(1, len(board), 2):
        for col in np.arange(1, len(board[row]), 2):
            board[row][col] = 1
    
    return board
   
print(checkerboard3())

#2.4

def checkerboard4():
    board = np.zeros((8,8))
    for row in np.arange(0, len(board), 2):
        for col in np.arange(1, len(board[row]), 2):
            board[row][col] = 1
    for row in np.arange(1, len(board), 2):
        for col in np.arange(0, len(board[row]), 2):
            board[row][col] = 1
    
    return board
   
print(checkerboard4())

#3 

def expansion(saying, spaces):
    arb_spaces = " " * spaces
    final = np.array([])
    for word in saying:
        s = word.replace("", arb_spaces)
        final = np.append(final, s)
    return final

m = np.array(["galaxy", "cluster"])
print(expansion(m, 3))

#4

def secondLargest(planets):
    empty = np.array([])
    transposed = planets.T
    for col in transposed:
        col.sort()
        sliced = col[-2]
        empty = np.append(empty, sliced)
    return empty

np.random.seed(42)
planets = np.random.randint(100, 1000, (5, 5))
print(planets)
print(secondLargest(planets))
       






