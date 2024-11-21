# loops
#basic
# Write a python program that prints all even numbers between 1 and 20 using a for loop
def even_numbers():
   for even in range(2,21,2):
       print (even)
even_numbers()


# Intermediate
# use a loop to ask the user to input a number until they provide a number greater than 10
number =float(input("please enter a number greater than 10:"))
if number > 10:
       print("correct")
else:
       print("fail")



# Advanced
# write a program that prints the multiplication table(from 1 t0 10) for numbers from 1 to 5 using nested for loops
for i in range (1,6):
     print(f"mutliplication table for{i}:") 
for j in range(1,11):
       print(f"{i}x{j} ={i*j}")    
       print(1)

#challlenged 
# given a list of intergers [4,7,2,9,12,15] , write a program using a for loop to find
# the sum of all odd numbers and print the result
numbers=[4,7,2,9,12,15]
sum_of_odds=0
for num in numbers:
    if num % 2 !=0:
     sum_of_odds +=num
print("The sum of all odd numbers is:",(sum_of_odds))       






























