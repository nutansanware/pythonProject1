#val = None # None is to initialize
#print(type(val))

#name = None
#print(name) #first None was assign to name
#name = "Amit"
#print(name)#now name has change fom None to amit

#data type - List

#list
#add item
#remove item
#update item
#view item
#exit

my_shopping_list = ["Milk", "Bread", "Flour"]
#print(my_shopping_list)
#print(type(my_shopping_list))
#my_list = [1,2,3,'four',5.0,True]
#print(my_list)
#print(type(my_list))

#add item in end of the list use append function
my_shopping_list.append("Sugar")
print(my_shopping_list)
#insert function to add item syntax insert(index, value)
#my_shopping_list.insert(1, "Eggs")
#print(my_shopping_list)
#extend funcion to add item in list syntax extend([value1, value2])
my_shopping_list.extend(["Oil", "Salt","Onion"])
print(my_shopping_list)
#remove item in list use remove function
#my_shopping_list.remove("Flour")
print(my_shopping_list.index("Oil"))
#pop function to remove item from list and return the value
#print(my_shopping_list.pop())# last item from the list
#print(my_shopping_list)
#print(my_shopping_list.pop(1))#index 1 value remove from the list
#reverse function to reverse the list
my_shopping_list.reverse()
print(my_shopping_list)
#sort function to sort the list
my_shopping_list.sort()
print(my_shopping_list)

#mutalble mean can be chnage so in list we can change the value from the list
a_list = ["apple", "egg"]
a_list[1] = "Nutan"
print(a_list)

# Literals - use to assign value to variable
#tuple literal - its an order,unchangeble(can not add or remove from the list), allow duplicate value
#a_tuple = (1, 2, 4, 3, "ab", "2.5")
#print(a_tuple)
#a_tuple.append(5)
#print(a_tuple) # 'tuple' object has no attribute 'append'
#a_tuple1 = [1, 2, 4, 3, "ab", "2.5"]
#print(a_tuple1)




