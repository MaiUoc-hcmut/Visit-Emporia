def readInput():
    dimenMatrix = input("Please enter the number of rows and column: ").split(" ")
    rows = int(dimenMatrix[0])
    cols = int(dimenMatrix[1])
    #Initialize matrix
    matrix = []

    #For user input
    for  i in range(rows):
        #Each loop require user to enter a row of matrix, an element separate by a space
        matrix.append([int(item) for item in input("Please enter your row {} of Emporia matrix: ".format(i)).split(" ")])

    return matrix, rows, cols

    


class Emporia():
    #Init attribute
    def __init__(self, matrix, rows, cols):
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
        self.sourceX = 0
        self.sourceY = 0
        self.desX = 0
        self.desY = 0
        self.empty = 0
        self.result = 0
    
    #Determine the source and destination of matrix
    def determineParameter(self):
        for r in self.matrix:

            for ele in r:
                if ele == 2:
                    self.sourceX = self.matrix.index(r)
                    self.sourceY = r.index(ele)
                elif ele == 3:
                    self.desX = self.matrix.index(r)
                    self.desY = r.index(ele)
                elif ele == 0:
                    self.empty += 1

    #Check the position that possible to traverse or not
    def checkPossiblePosition(self, r, c):
        if r < self.rows and c < self.cols and r >= 0 and c >= 0 and (self.matrix[r][c] == 0 or self.matrix[r][c] == 3):
            return True
        
        return False

    
    def isVisitedAll(self):
        for r in self.matrix:
            for c in r:
                if c == 0:
                    return False
        
        return True

    
    # r for index of row of current position
    # c for index of column of current position
    def findPath(self, r, c):

        #Chek if current position is at the destination and visited all the cells in matrix
        if r == self.desX and c == self.desY and self.isVisitedAll():
            self.result += 1
            return


        #Mark current position as visited
        if self.matrix[r][c] != 3:
            self.matrix[r][c] = 1
        
        #Traverse and backtrack
        #Move down
        if self.checkPossiblePosition(r + 1, c) == True:
            self.findPath(r + 1, c)

        #Move up
        if self.checkPossiblePosition(r - 1, c) == True:
            self.findPath(r - 1, c)

        #Move right
        if self.checkPossiblePosition(r, c + 1) == True:
            self.findPath(r, c + 1)

        #Move left
        if self.checkPossiblePosition(r, c - 1) == True:
            self.findPath(r, c - 1)

        #Before back to previous position, mark current position as not visited yet
        if self.matrix[r][c] != 3:
            self.matrix[r][c] = 0

        
        return
        # 3 1 1 2
        # 0 0 0 0
        # 0 0 0 0
        # 0 0 0 0
        

matrix, rows, cols = readInput()
test = Emporia(matrix, rows, cols)
test.determineParameter()
sourceX = test.sourceX
sourceY = test.sourceY
test.findPath(sourceX, sourceY)
print(test.result)


