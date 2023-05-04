# # HERE WE WRITE A FUNCTION THAT WHENEVER THE COMPUTER GUESSES A NUMBER THAT WE HAVE IN MIND:
import random

# Computer Vs ME:
# my End side
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) # F  string formatters
        if guess < random_number:
            print("Sorry, guess again, Your guess is Low!...")
        elif guess > random_number:
            print("Sorry, guess again, Your guess is High!...")
    print(f'Yay, Congrates!! You have guessed the {random_number} Correctly!!!')

# the computer
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': # you telling the computer is correct!
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(H), or too low(L), or correct(c)???').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l': # this is a small letter for L
            low = guess + 1
    print(f'Yay! The Computer guessed your number, {guess}, correctly!')


computer_guess(100)

# Me vs computer
def mindGame(a):
    mind_number = random.randint(1, a)
    mindGame = 0
    while mindGame != mind_number:
        mindGame = int(input(f'Guess a number between 1 and {a}: '))
        if mindGame < mind_number:
            print('Sorry, guess again, Too Low...')
        elif mindGame > mind_number:
            print('Sorry, guess again, Too high...')
    print(f'Yay, Congrate You have guessed the number {mind_number} Correctly!')

mindGame(100)


# Iterate through every number in a list to separate out even and odd numbers, here we identify the possible outlier
# values

my_list = [1,2,3,4,5,6,7,100,110,21,33,32,2,4]
even = []
not_even = []
outlier = []

for i in my_list:
    if i > 90:
        outlier.append(i)
    elif i%2 == 0:
        even.append(i)
    else:
        not_even.append(i)

print('Even Numbers: ', even)
print('Odd Number is: ', not_even)
print('outlier: ', outlier)


# Finding the sum of all numbers in a list
num_sum = 0
for k in my_list:
    num_sum += k
print('Sum of the element in the list is: ', num_sum)

# Calculate the sum of even numbers in a list

# Count the number of the number in a list

# calculate the cumulative sum of all elements in a list
print("Cumulative sum")
initial_val = 0
cumsum = []
for i in my_list:
    initial_val += i
    cumsum.append(initial_val)
print('The cummulative sums of the list', cumsum)

# loop for combining numbers and words in a tuple
student_id = [1, 2, 3]
student = ['cakahal', 'Peter', 'Uba']

for l, m in zip(student_id, student):
    print(f'{l} {m}')

# where loop through a tuple of mixed data type and extract only the integer values

my_tuple = (1, 2, 'Cakahal', 3, 4, 'Peter', 'Uba', 5)
for a in my_tuple:
    if type(a) == int:
        print('this is only the integer in the tuple list', a)


# Unpacking Tuples and also extract the tuples stored in a list as nested arrays

myTup_list = [(1,2), (3, 4), (5, 6)]
list1 = []
list2 = []

for b, c in myTup_list:
    list1.append(b)
    list2.append(c)

print('List of first tuple item', list1)
print('list of second tuple items', list2)

# using enumerate() function to extract elements in a tuple
myTup = ('Java', 'python', 'php')
for d, e in enumerate(myTup, start=1):
    print(d, e)


# String loops
myStr = 'CakahalJohnson'
for f in myStr:
    print(f, end=' : ')

# Slicing loop the String alternating in Twos
myString = 'CakahalJohnson'
for g in myString[0: len(myString): 2]:
    print(g, end=' ')
print("======================================================================")
# Iterate through a sentence and print each word using split()
sent = 'It is a dark night'
# splitting the sentence into words
sent_split = sent.split()
# extract each word with a loop
for h in sent_split:
    print(h, end=' / ')

