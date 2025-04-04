# Write a method that receives a grid of letters and a word, and returns
# a boolean telling us if said word can be found in the grid of letters.

# For example, the following grid contains the word "HELLO"

# G S H Q C
# X N E L R
# H A F L C
# Q P I O N
# H S Y B U

# E  S [H]  Q   C
# X  N [E] [L]  R
# H  A  F  [L]  C
# Q  P  I  [O]  N
# H  S  Y   B   U

#Aproach:
# Check every cell, if the cell has first character of the word to search, then recur one by one and try all 4 directions from that cell for a match.
# Mark the position in the grid as visited and recur in the 4 possible directions.
# After recurring, again mark the position as unvisited.
# Once all the letters in the word is matched, return true.


# Python3 program to check if the word 
# exists in the grid or not 
  
r = 5
c = 5
  
# Function to check if a word exists 
# in a grid starting from the first 
# match in the grid level: index till  
# which pattern is matched x, y: current 
# position in 2D array 
def findmatch(mat, pat, x, y, 
              nrow, ncol, level) :
  
    l = len(pat) 
  
    # Pattern matched 
    if (level == l) :
        return True
  
    # Out of Boundary 
    if (x < 0 or y < 0 or 
        x >= nrow or y >= ncol) :
        return False
  
    # If grid matches with a letter 
    # while recursion 
    if (mat[x][y] == pat[level]) :
  
        # Marking this cell as visited 
        temp = mat[x][y]
        mat[x].replace(mat[x][y], "#")
  
        # finding subpattern in 4 directions 
        res = (findmatch(mat, pat, x - 1, y, nrow, ncol, level + 1) | 
               findmatch(mat, pat, x + 1, y, nrow, ncol, level + 1) | 
               findmatch(mat, pat, x, y - 1, nrow, ncol, level + 1) |
               findmatch(mat, pat, x, y + 1, nrow, ncol, level + 1)) 
  
        # marking this cell as unvisited again 
        mat[x].replace(mat[x][y], temp)
        return res
      
    else : # Not matching then false 
        return False
  
# Function to check if the word
# exists in the grid or not 
def checkMatch(mat, pat, nrow, ncol) :
  
    l = len(pat)
  
    # if totl characteres in matrix is 
    # less then pattern lenghth 
    if (l > nrow * ncol) :
        return False
  
    # Traverse in the grid 
    for i in range(nrow) :
        for j in range(ncol) :
  
            # If first letter matches, then 
            # recur and check 
            if (mat[i][j] == pat[0]) :
                if (findmatch(mat, pat, i, j, 
                              nrow, ncol, 0)) :
                    return True
    return False
  
# Driver Code 
if __name__ == "__main__" :
  
    grid = ["GSHQC", "XNELR", 
            "HAFLC", "QPION",
            "HSYBU"]
  
    # Function to check if word 
    # exists or not 
    if (checkMatch(grid, "HELLO", r, c)) :
        print("Yes")
    else :
        print("No") 