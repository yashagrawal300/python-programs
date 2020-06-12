'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
'''



class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.x = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.x:
            self.x.append(val)
            return True
        else:
            return False
            

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.x:
            self.x.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.choice(self.x)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
