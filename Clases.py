# Class
class MyClass:
    # Constructor
    def __init__(self, nums):
        #Create member variables
        self.nums = nums
        self.size = len(nums)

        #Self keyword required as a parameter
        def getLength(self):
            return self.size
        
        def getDoubleLength(self):
            return 2* self.getLength()