import random
 
numbers = list(range(1, 11))  # create a list of numbers from 1 to 10
random.shuffle(numbers)  # shuffle the list in place
for num in numbers:
       print(num, end="")  # print each number in the shuffled list