# basic
#Create a list of 5 fruits and print each fruit on a new line using a for loop.
Fruits=["apple","orange","peaches","mango","berries"]
for fruit in Fruits :
    print(fruit)
 
 # intermediate
 # Write a function that takes a list of numbers and returns a new list with each number squared.
# Example: [1, 2, 3] should become [1, 4, 9].
def list_of_numbers():
   squared_list=[]
   numbers=[1,2,3]
   for num in numbers:
      squared_list.append(num**2)

   return squared_list
result=list_of_numbers()
print(result)
list_of_numbers


#advanced
#Write a Python program that takes two lists, list1 = [1, 2, 3] 
#and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
first_list=[1,2,3]
second_list=[4,5,6]
combined=[x for pair in zip(first_list,second_list) for x in pair]
print(combined)


#challenged
#Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], 
 #write a program to find and print the two largest numbers in the list without using the max() function.
numbers=[3,1,4,1,5,9,2]
largest=float('-inf')
second_largest=float('-inf')
for num in numbers:
  if num > largest:
    second_largest = largest
    largest=num
  elif num > second_largest:
     second_largest=num
print("largest number:",largest)
print("second largest:",second_largest)