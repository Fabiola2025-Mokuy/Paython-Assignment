# 1.Create an empty list called my_list.
print ("my_list is empty")
my_list=[]
print (my_list)

#2.	Append the following elements to my_list: 10, 20, 30, 40
print("there is same content in the list")
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print (my_list)

#3.	Insert the value 15 at the second position in the list.
my_list.insert (1,"15")
print (my_list)
print("list_a")
list_a=[50, 60, 70]
print (list_a)


print ("my_list extend")
#4.	Extend my_list with another list_a
my_list.extend(list_a)
print (my_list)

#5.	Remove the last element from my_list
my_list.pop(-1)
print("last number deleted")
print (my_list)

#6.	Sort my_list in ascending order
print ("number in ascendig order")
my_list= [60, 15, 20, 40,30, 50, 10]
my_list.sort ()
print (my_list)

#7.	Find and print the index of the value 30 in my_list
print ("the index 3, is the value ") 
print (my_list[3])





