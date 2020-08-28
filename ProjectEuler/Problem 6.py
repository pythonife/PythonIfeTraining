def sumSquares(n):
     i = 0
     X = 0 #initialize the variable with the sum of individual values
     Y = 0 #initialize the variable with the square of the sum of all values 

     while (i <=n): #loop from 0 till the last value n
          X += pow(i,2) #sum of individual squares
          Y += i # sum of all values
          i+= 1 # increment i
    return pow(Y,2) - X #return the difference between the squares and sum

Value = sumSquares(10)
#Answer is 2640

Value = sumSquares(100)
#Answer is 25164150
