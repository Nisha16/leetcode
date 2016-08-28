class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.output = []
        self.index = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            return False
        self.index[val] = len(self.output)
        self.output.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            return False
        index = self.index[val]
        last=self.output[-1]
        self.index[last] = index
        self.output[index] = last
        self.output.pop()
        del self.index[val]
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        index = random.randint(0,len(self.output)-1)
        return self.output[index]
