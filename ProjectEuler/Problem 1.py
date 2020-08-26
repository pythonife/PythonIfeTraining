def sumNumbers(n):
  i = 0 
  NumList = []
  while i < n: #while the current number is less than n.
    if (i%3)==0 or (i%5) == 0: #Check if i is divisible by 3 or 5
      NumList.append(i) #append the number to our list.
    else:
      pass
    i+= 1 #increment by i until it is equal to n.
  return sum(NumList) #return the sum of list.

x = sumNumbers(1000) #Test the function
print(x)

#Answer: 233168
