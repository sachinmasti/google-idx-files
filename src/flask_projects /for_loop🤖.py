# This loop iterates through numbers from 1 to 6 (exclusive), with a step of 2, and prints each number followed by a space.
for i in range(1,7, 2):
        print(i, end=" ")
      
      # This line prints a message to indicate the start of the next program.
print('this is a next programe')
      
      # This loop iterates through numbers from 1 to 5 (exclusive) and prints the square of each number, followed by a space.
for i in range(1,6):
          print(i**2, end=" ")
      
      # This line prints a message to indicate the start of a new program.
print('this is a new programe')
      
      # This loop iterates through numbers from 1 to 10 (exclusive), checks if the number is odd, and prints the odd number on a new line.
for i in range(1,11):
          if i%2==1:
              print(i)
      
      # This line prints a separator with stars.
print('---------⭐⭐--------')
      
      # Initialize the total to 0.
total=0
      # This loop iterates through the numbers from 1 to 10 (inclusive) and adds each number to the total.
for i in range(1,11):
          total+=i
      # This line prints the final total.
print(total)
      
      # Assign the string 'python' to the variable s.
s='python'
      # This loop iterates through the string s in reverse order, printing each character followed by a space.
for i in range(len(s)-1,-1,-1):
          print(s[i],end=" ")
      
      # Assign the string 'aeiou' to the variable vowel.
vowel ='aeiou'
      # Assign the string 'elephant' to the variable word.
word='elephant'
      # Initialize a counter for vowels to 0.
count=0
      # This loop iterates through each character in the word.
for char in word:
          # Checks if the character is present in the string of vowels.
          if char in vowel:
              # If it is a vowel, increment the counter.
              count +=1
      # Prints the total count of vowels in the given word.
print(f'this is a {count} of vowels in {word}')
      
      # Initialize a to 0
a=0
      # Initialize b to 1
b=1
      # This loop iterates 10 times to generate the fibonacci series.
for _ in range(10):
          # Generates a new term of the fibonacci series.
          new_term=a+b
          # Print new term followed by a space.
          print(new_term,end=" ")
          # Update a and b for the next term
          a,b=b,new_term
      
      # Assign the integer 8 to the variable n.
n=8
      # Initialize factorial to 1.
factorial=1
      # This loop iterates from 1 to n and multiplies each number with factorial to get the factorial of n.
for i in range(1,n+1):
          factorial*=i
      # Print the factorial of n.
print(f'this is a factorial of {n} is {factorial}')
      
      # Takes input from user and stores it in the variable num.
num = int(input('enter your number: '))
      
      # Initialize is_prime to True for checking prime numbers.
is_prime = True
      # Iterate through number from 2 to num
for i in range(2,num):
        # check if num is divisible by any number if yes then it's not a prime
          if num%i==0:
            # if num is not prime change is_prime to false and break the loop
              is_prime=False
              break
      # checks if the number is a prime number.
if is_prime:
        # Print if its a prime number
          print(f'{num} is a prime number')
else:
          # Print if its not prime number.
          print('this is a not a prime member ')
      
      # Assign 'programming' to variable word.
word='programming'
      # Initialize char_count as empty dictionary.
char_count = {}
      
      # This loop iterates through each character in the word.
for char in word:
          # check if the char is already present in dict.
          if char in char_count:
              # If char is present then increment its count by 1.
              char_count[char]+=1
          else:
              # If not present then add it to dict and initialize its value to 1.
              char_count[char]=1
      # This loop iterates through dictionary items key value pair.
for key,value in char_count.items():
        # Prints each char along with its count in the word.
          print(f'{key}:{value}')
