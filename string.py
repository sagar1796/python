#strings: ordered, immutable, text representaiton
#create
word="hello world"
print(word)
word1='I\'m a programmer'
print(word1)
word2=""""hello world"""
print(word2)
word3="""hello\
    world"""
print(word3)

#slicing
char=word[1]
chars=word[1:5]
chars=word[0:5]
chars=word[::2] # 2 steps
chars=word[::-1]# reverse 



print(char)
#immutable
#word[0]="H" # get an error
#concated string
sent="hello" +""+"world"


#print every letter
for x in word:
    print(x)

#letter in word

if "i" in "home":
    print("yes")
else:
    print("np")


#remove white space
my_string="  Hello world"
my_string=my_string.strip()
print(my_string)

#upper case
my_string="  Hello world"
my_string=my_string.upper()
print(my_string)

#lower case
my_string="  Hello world"
my_string=my_string.lower()
print(my_string)

#title case
my_string="  Hello world"
my_string=my_string.title()
print(my_string)

#start with 
my_string="Hello world"
my_string=my_string.startswith("H")
my_string=my_string.startswith("Hello")
print(my_string)

#end with
my_string="  Hello world"
my_string=my_string.endswith("d")
print(my_string)

#find
my_string="  Hello world"
my_string=my_string.find("w")
print(my_string)

my_string="  Hello world"
my_string=my_string.find("world")
print(my_string)

my_string="  Hello world"
my_string=my_string.find("pp")
print(my_string)

#cout
my_string="  Hello world"
my_string=my_string.count("o")
print(my_string)

#replace
my_string="  Hello world"
my_string=my_string.replace("world","universe")
print(my_string)

#string and list
my_string="how are you ?"
my_list=my_string.split("")
print(my_list)

my_string="Hi \n how are you ?"
my_list=my_string.split("\n")
print(my_list)

#list to string
my_list=['Hi ', ' how are you ?']
new_string=" ".join(my_list)
print(new_string)

from timeit import default_timer as timer

a=["a"]*100
#bad way of doing this
start=timer()

my_string=""
for i in a:
    my_string+=i
stop=timer()
print(start-stop)

#good way as it consume less time to run the file
start=timer()
my_string="".join("a")
stop=timer()
print(start-stop)

#formating the string
#%,.formate(),f-string
var="vickey"
b=3.2343
my_string="your name is %s"%var
my_string="your name is %.2f"%b

print(my_string)
#another way of format
var="vickey"
b=3.2343
my_string="your name is {}".format(var)


print(my_string)









