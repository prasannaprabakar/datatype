# creating list
emptyList = ()
print("empty list", emptyList)
# list with same datatype
same_datatype_list = list([10, 20, 30, 40])
print("list with same datatype", same_datatype_list)
# list with different datatype
different_datatype_list = list([10, 'prasanna', 10.2])
print("list with different datatype", different_datatype_list)
# Accessing elements in list
print(same_datatype_list[0])
# common operation
print(10 in same_datatype_list)
print(10 not in same_datatype_list)
# concatenation
print("list concatenation", same_datatype_list + different_datatype_list)
print("list duplication", same_datatype_list * 2)

# slicing
print(same_datatype_list[1:2])
print(same_datatype_list[:3])
print(same_datatype_list[-1])
# Methods
print("length", len(same_datatype_list))
print("minimum value ", min(same_datatype_list))
print("maximum value ", max(same_datatype_list))
print("sum of list ", sum(same_datatype_list))
print("appending at end of list 40 ", same_datatype_list.append(40), " ", same_datatype_list)
print("insert new value ", same_datatype_list.insert(2, 22))
print("count 40 ", same_datatype_list.count(40))
print("sorting in list ", same_datatype_list.sort())
print("exdend differentDatatypeList ", same_datatype_list.extend(different_datatype_list))
print("index of 40 ", same_datatype_list.index(40))
print("remove 40 from list ", same_datatype_list.remove(40))
print("reverse the list ", same_datatype_list.reverse())
# travers using loop
for temp in same_datatype_list:
    print(temp)
# list comprehension
list1 = [temp + 1 for temp in range(10)]
print(list1)
evenList = [temp for temp in range(100) if temp % 2 == 0]
print(evenList)
