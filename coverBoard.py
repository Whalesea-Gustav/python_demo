board = [[0]*8 for i in range(8)]  #Eight by eight checkerborad
board[7][7] = -1                   #Missing corner
print(len(board))
print(board)

offsets = (0, -1), (7, 0)
print(offsets)
for y1, y2 in offsets:
    print(y1, y2)


