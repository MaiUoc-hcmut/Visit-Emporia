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

    def checkPossiblePosition(self, r, c):
        if r < self.rows and c < self.cols and r >= 0 and c >= 0 and (self.matrix[r][c] == 0 or self.matrix[r][c] == 3):
            return True
        
        return False

    #This method check 
    def isVisitedAll(self):
        for r in self.matrix:
            for c in r:
                if c == 0:
                    return False
        
        return True

    def findPath(self, r, c, path):

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
            self.findPath(r + 1, c, path)

        #Move up
        if self.checkPossiblePosition(r - 1, c) == True:
            self.findPath(r - 1, c, path)

        #Move right
        if self.checkPossiblePosition(r, c + 1) == True:
            self.findPath(r, c + 1, path)

        #Move left
        if self.checkPossiblePosition(r, c - 1) == True:
            self.findPath(r, c - 1, path)

        if self.matrix[r][c] != 3:
            self.matrix[r][c] = 0

        
        return
        # 3 1 1 2
        # 0 0 0 0
        # 0 0 0 0
        # 0 0 0 0
        

matrix, rows, cols = readInput()
test = Emporia(matrix, rows, cols)
path = []
test.determineParameter()
sourceX = test.sourceX
sourceY = test.sourceY
test.findPath(sourceX, sourceY, path)
print(test.result)