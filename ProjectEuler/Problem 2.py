## Two functions
## function 1 is fibonacci: This function finds the whole list of numbers with values less than n.
## sumEvenValue: This is function 2, this finds the sum of all numbers in the list that is divisible by 2.
 
def fibonacci(n):
 c = 0
 SequenceList = [1,2] #initialize your list with 2 starting numbers 1&2
 while c < n: # loop from 0 until c is greater than n
   c = SequenceList[-1] + SequenceList[-2] #sum the last 2 numbers in the list.
   SequenceList.append(c) #append the sum of the last 2 numbers.
   if c >n: #if the last number added is greater than n, break
     break
   else:
     Continue # else continue the program
 return SequenceList[:-1] #return all in the list except the number greater than n
 
def SumEvenValue(n):
 Total = 0
 sequence = fibonacci(n) #call the function fibonacci and pass in n.
 for i in sequence: #loop through the fibonacci sequence
   if i%2 == 0: #test if current value is divisible by 2
     Total+= i #if so add the number to total.
 
   else:
     Pass # if not, do nothing
 
 return Total #return the total number when program is done
 
x = SumEvenValue(4000000) #call the program to run
print(x) #print your answer

#Answer: 4613732
