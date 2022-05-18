'''Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.'''
# declare our own string class
class String:
      
    # magic method to initiate object
    def __init__(self, string):
        self.string = string
          
# Driver Code
if __name__ == '__main__':
      
    # object creation
    string1 = String('Hello')
  
    # print object location
    print(string1)



#If we try to add a string to it :
class String:
      
    # magic method to initiate object
    def __init__(self, string):
        self.string = string
          
    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)
  
# Driver Code
if __name__ == '__main__':
      
    # object creation
    string1 = String('Hello')
      
    # concatenate String object and a string
    print(string1 +' world')

#TypeError: unsupported operand type(s) for +: 'String' and 'str'

#Now add __add__ method to String class :
class String:
      
    # magic method to initiate object
    def __init__(self, string):
        self.string = string 
          
    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)
          
    def __add__(self, other):
        return self.string + other
  
# Driver Code
if __name__ == '__main__':
      
    # object creation
    string1 = String('Hello')
      
    # concatenate String object and a string
    print(string1 +' Geeks')

# Output :
# Hello Geeks