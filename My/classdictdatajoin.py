
class Something:
    def __init__(self, data:dict):
        self.__dict__ = data

    def __str__(self):
        # dict1 = {}
        # dict1 = ', '.join(f"{x} = {y}"  for x, y in self.__dict__.items())
        # return dict1
        # return ', '.join([f'{key}={value}' for key,value in self.__dict__.items()])
        
        #using a generator avoids creating an unneccessary list in memory
        return ', '.join(f'{key}={value}' for key,value in self.__dict__.items())
    
data_dict1 = {
    'a' : 10,
    'b' : 20,
    'name': 'one'
}

data_dict2 = {
    'a' : 15,
    'b' : 25,
    
}

d1 = Something(data_dict1)
d2 = Something(data_dict2)
print(d1)
print(d2)
