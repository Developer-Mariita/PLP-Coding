#create empty list
my_list=[]

#append elements one by one
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert the value 15 at the second position in the list.
my_list.insert(1,15)

#create another list(my_list1) then extend to my_list
my_list1=[50,60,70]
my_list.extend(my_list1)

#remove the last element from my_list
del my_list[-1]

#sort the list in ascending order
my_list.sort()

#find and print the index of the value 20 in my_list
print("The index of 30 is:", my_list.index(30))


