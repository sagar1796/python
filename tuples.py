#tuple is collection data type which is ordered and immutable
#immutable means can't be change after creation
#tuple creation
#method1
employees=("max",20)
print(type(employees))
print(employees)

#method2
employees_list=["max",20]
print(tuple(employees_list))

#slice work as list
em=employees[1]
em1=employees[:2]
em2=employees[::-1] # reversing
print(em)



#tuples are immutable means you can't add or del from tuples 
employees[0]="Tim"
print(employees)


#print items in tuples
for i in employees:
    print(i)

# test whether that item is in tuple
if "max" in employees:
    print("yes")
else:
    print("no")

#count letters in tuples
lettters= ("a","p","p","l","e")
print(f"number of letters in tuples{lettters.count('p')}")
print(f"idex in tuples{lettters.index('p')}")

#
my_tuples="max",28,"delhi"
name,age,city=my_tuples
print(name)
print(age)
# use * if you want to upack few items
tuples="Dinesh",23,"banglore"
name,*age=tuples
print(name)


# list acquire more spaces  and take less time to execute
import sys
import timeit
tuples="Dinesh",23,"banglore"
print(sys.getsizeof(tuples),"bytes")
lists=["Dinesh",23,"banglore"]
print(sys.getsizeof(lists),"bytes")

print(timeit.timeit(stmt="(1,2,3)",number=1000000))
print(timeit.timeit(stmt="[1,2,3]",number=1000000))





