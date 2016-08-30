
class hashmap:

	def __init__(self, num_buckets=256):
    """Initializes a Map with the given number of buckets."""
	    self.aMap = []
	    for i in range(0, num_buckets):
	        aMap.append([])
	    return aMap

	def hash_key(self, aMap, key):
	    """Given a key this will create a number and then convert it to
	    an index for the aMap's buckets."""
	    return hash(key) % len(aMap)

	def get_bucket(self, aMap, key):
	    """Given a key, find the bucket where it would go."""
	    bucket_id = self.hash_key(aMap, key)
	    return aMap[bucket_id]

	def get_slot(self, aMap, key, default=None):
	    """
	    Returns the index, key, and value of a slot found in a bucket.
	    Returns -1, key, and default (None if not set) when not found.
	    """
	    bucket = self.get_bucket(aMap, key)
	    for i, kv in enumerate(bucket):
	        k, v = kv
	        if key == k:
	            return i, k, v

	    return -1, key, default

	def get(self, aMap, key, default=None):
	    """Gets the value in a bucket for the given key, or the default."""
	    i, k, v = self.get_slot(aMap, key, default=default)
	    return v

	def set(self, aMap, key, value):
	    """Sets the key to the value, replacing any existing value."""
	    bucket = self.get_bucket(aMap, key)
	    i, k, v = self.get_slot(aMap, key)

	    if i >= 0:
	        # the key exists, replace it
	        bucket[i] = (key, value)
	    else:
	        # the key does not, append to create it
	        bucket.append((key, value))

	def delete(self, aMap, key):
	    """Deletes the given key from the Map."""
	    bucket = self.get_bucket(aMap, key)

	    for i in xrange(len(bucket)):
	        k, v = bucket[i]
	        if key == k:
	            del bucket[i]
	            break

	def list(self, aMap):
	    """Prints out what's in the Map."""
	    for bucket in aMap:
	        if bucket:
	            for k, v in bucket:
	                print k, v