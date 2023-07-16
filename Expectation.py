#Error and expectation
#Type error
a=5+"10"
#import error
import module
#Name Error
a=4
b=c
#file error
f = open(somfile.txt)
#value error
a=[1,2,3]
a.remove(4)
#index error
a[4]
#key error
dictionary={"name":"max"}
dictionary["age"]

#expectation
#method1
x=-5
if x<0:
    raise Exception("x should be positive")

#method2
x=-5
assert(x>=0)

x=-5
assert(x>=0),'x is not positive'

#method3
try:
    a=5/0
except:
    print('an error happened')

try:
    a=5/0
except Exception as e:
    print(e)

try:
    a=5/0
except ZeroDivisionError:
    print()

try:
    a=5/1
    b=a+"10"
except ZeroDivisionError as e:
    print(e)   
except TypeError as e:
    print(e)
else:
    print("everything is fine")
finally:
    print("cleaning up...")

#define your own exceptions
class ValueTooHighError(Exception):
    pass
def test_value(x):
    if x>100:
        raise ValueTooHighError("value is too high")
    
test_value(200)

class ValueTooHighError(Exception):
    pass
def test_value(x):
    if x>100:
        raise ValueTooHighError("value is too high")
    
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)


#anothe way
class ValueTooHighError(Exception):
    def __init__(self, message,value):
        self.message=message
        self.value=value



class ValueToSmallError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value 

def test_value(x):
    if x<5:
        raise ValueToSmallError("value is too small")
    if x>100:
        raise ValueTooHighError("value is too high")
    
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueToSmallError as e:
    print(e.message, e.value)


