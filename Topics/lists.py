#Create a list
list = ["apple", "banana", "cherry"]
print(list)
print(type(list))

#List allows duplicate values
list1 = ["apple", "banana", "cherry", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1)

#Print the list length
print(len(list))

#A list can contain different data types
list2 = ["abc", 34, True, 40, "male"]
print(list2)

#Access the list
print(list[0])
print(list1[-1])    # -1 refers to the last item
print(list2[-2])     # -2 refers to the second last item
print(list2[2])
print(list1[2:5])    #Return the third, fourth, and fifth items
print(list1[:4])    #This example returns the items from the beginning to 4th item
print(list1[2:])    #returns the items from "cherry" to the end
print(list1[-4:-1])

if "apple" in list1:
  print("Yes, 'apple' is in the fruits list")