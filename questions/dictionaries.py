#Basic
#Create a dictionary with three key-value pairs representing a student's information:
#name, age, and grade. Print each key-value pair on a new line
student_info ={
    'name':'Ela',
    'age' :'22',
    'grade':'2nd'
}
for key , value in student_info.items():
  print(f"{key}:{value}")



#intermediate
#Write a function that takes a dictionary of people's names and their ages, 
#{'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def adults(people_dict):
   return[name for name ,age in people_dict.items()if age >=21]
people={'Alice':24,'Bob':19,'Charlie':30}
result=adults(people)
print(result)



#Advanced
#Given a dictionary representing items in a store with their prices, 
#{'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes 
#a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
Fruits=['apple','orange','banana','banana']
fruit_prices={'apple':0.5,'orange':0.7,'banana':0.3}
total_cost=(0.5+0.7+0.3+0.3)
print(f"The total cost of apple,orange,banana is {total_cost}")

#challenged
#Write a program that counts the occurrences of each word in a given 
#sentence. Example: for the sentence "hello world hello," the output should be 
#{'hello': 2, 'world': 1}.
sentence="hello world hello,"
x=sentence.count("hello")
y=sentence.count("world")
print(f"hello:{x},world:{y}")
