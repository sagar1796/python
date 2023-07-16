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
    print(e)