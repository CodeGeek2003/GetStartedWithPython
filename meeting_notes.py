# Basic syntax: variables, data types, input, and output.
# Control Flow: if, else, elif ,,, while, for loops
# Functions
# Lists
# Dictionaries
# Tuples
# Sets
#//////////////////////////
#difference between c++ and python, python is interpreted language, c++ is compiled language
#//////////////////////////
#exmaples of basic syntax
boolean = True
integer = 1
floating_point = 1.0
string = "Hello World"
character = 'a'
#//////////////////////////
#examples of input and output
#input
name=input("Enter your name: ")
#output
print("Hello",name)
#//////////////////////////
#examples of control flow
if boolean:
    print("This is true")
else:
    print("This is false")
#short-handed if statement:
print("true") if boolean else print("false")
while integer < 10:
    print(integer)
    integer += 1

for i in range(10):
    print(i)
#//////////////////////////
#examples of functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def recursive_function_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_function_factorial(n - 1)
#//
#built in functions
#//
#len
#len only works for array and string
#len doesnt work with any numiric variable
x=675
y='ABCD'
z=[3,4,'abc']
print('length of y= ',len(y),'length of z= ',len(z))
#//
#type
#type returns the type of the variable
print(type(x))
print(type(y))
print(type(z))
#//
#input
#input takes input from the user
#input always returns a string
#so if you want to take input as an integer
#you have to convert it to an integer
#using int()
#or you can take input as a float
#using float()
#or you can take input as a boolean
#using bool()
#or you can take input as a string
#using str()
#//
#output
#output is done using print()
#sort
#//////////////////////////
#examples of lists
list1 = [1, 2, 3, 4, 5]
list2 = [1, "Hello", 3.0, True]
list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list4=[]
list4.append(1)
list4.insert(0,2)
list2.remove("hello")
list2.remove("Hello")
list2.pop(0)
length=len(list2)
sublist=list2[0:2]
#list comprehension
list5=[i for i in range(10)]
#2D list initialization
li=[[_ for _ in range(5)] for _ in range(6)]
li2=[[0]*5]*6
for i in range(6):
    for j in range(5):
        li[i][j]=1
        li2[i][j]=j+1
print(li)
print(li2)
#//////////////////////////
#examples of dictionaries
dict1 = {"key1": 1, "key2": 2, "key3": 3}
dict2 = {"key1": 1, "key2": "Hello", "key3": 3.0}
dict3 = {"key1": [1, 2, 3], "key2": [4, 5, 6], "key3": [7, 8, 9]}
dict4={}
dict4["key1"]=1
dict1["key2"]=44
dict4["key3"]=3
poped_item=dict4.pop("key1")
del dict4["key3"]
keys=dict1.keys()
values=dict1.values()
items=dict1.items()

#//////////////////////////
#examples of tuples
#note tuples are immutable once created you cant change them
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, "Hello", 3.0, True)
tuple3 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
tuple4=(1,2,3)
tuple4=tuple4+(4,)
lenght=len(tuple4)
subtuple=tuple4[0:2]
#//////////////////////////
#examples of sets
#--
#note sets are unordered and unindexed
#--
#difference between sets and
#lists is that sets don't allow duplicates
#--
#difference between sets and dictionaries
# is that sets don't have keys
#--
set1 = {1, 2, 3, 4, 5}
set2 = {1, "Hello", 3.0, True}
set3 = {(1, 2, 3), (4, 5, 6), (7, 8, 9)}
set4=set()
set4.add(1)
set4.add(2)
set4.add(3)
#the update method can be used to add multiple
#items to a set
set4.update([4,5,6])
set4.remove(1)
set4.discard(2)
#difference between remove and discard is that remove will
# throw an error if the item doesn't exist in the set
poped_item_set=set4.pop()
union_set=set1.union(set4)
intersection_set=set1.intersection(set4)
difference_set=set1.difference(set4)
#//////////////////////////
#final project
def main():
    phone_record={}
    while True:
        print('''1. Add a new phone number
2. Delete a phone number
3. Update a phone number
4. Search a phone number
5. Display all phone numbers
6. Quit''')
        choice=int(input('Enter your choice: '))
        if choice ==6:
            break
        elif choice==1:
            add_contact(input('Enter name: '),input('Enter number: '),phone_record)
        elif choice==2:
            delete_contact(input('Enter name: '),phone_record)
        elif choice==3:
            update_contact(input('Enter name: '),input('Enter number: '),phone_record)
        elif choice==4:
            search_contact(input('Enter name: '),phone_record)
        elif choice==5:
            display_all(phone_record)
        else:
            print('Invalid choice')
def add_contact(name,number,phone_record):
    if (name in phone_record):
        print('Contact already exists with this name')
    else:
        phone_record[name]=number
        print('Contact added successfully')
def delete_contact(name,phone_record):
    if name in phone_record:
        del phone_record[name]
        print('Contact deleted successfully')
    else:
        print('Contact not found')
def update_contact(name,number,phone_record):
    if name in phone_record:
        phone_record[name]=number
        print('Contact updated successfully')
    else:
        print('Contact not found')
def search_contact(name,phone_record):
    if name in phone_record:
        print('Contact found')
        print('Name: ',name,'Number: ',phone_record[name])
    else:
        print('Contact not found')
def display_all(phone_record):
    for name,number in phone_record.items():
        print('Name: ',name,'Number: ',number)
if __name__=='__main__':
    main()
#//////////////////////////


