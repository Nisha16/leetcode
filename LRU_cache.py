class LRU_cache:

	def __init__(self, capacity):

		self.capacity = capacity
		self.tm = 0
		self.cache = {}
		self.lru = {}

	def get(self,key):
		
		if key in self.cache:
			self.lru[key] = self.tm
			self.tm += 1
			return self.cache[key]
		return -1
		
	def set(self,key,value):

		if key in self.cache:
			self.cache[key] = value
			self.lru[key] = self.tm
			self.tm += 1
			return 'ok'

		if len(self.cache) >= self.capacity:
			old_key = min(self.lru.keys(), key=lambda k: self.lru[k])
			self.cache.pop(old_key)
			self.lru.pop(old_key)	
		self.cache[key] = value
		print 'self: ', self.cache
		self.lru[key] = self.tm
		self.tm += 1

obj = LRU_cache(2)

print obj.get(2)
print obj.set(2,6)
print obj.get(1)
print obj.set(1,5)
print obj.set(1,2)
print obj.get(1)
print obj.get(2)							
