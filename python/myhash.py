"""
This classs implements a set of functions for implementing a hash

Operations:
  - set(hash, value)
  - value = get(hash)
"""

class MyHash(object):
    """My Hash Library"""

    def __init__(self, name):
        """For now, use positionally corresponding arrays to store hash keys and values"""
        self.hash_keys = []    # array of hash values (strings)
        self.hash_values = []  # array of hash values
        self.hash_name = name

    def set(self, hash_key, hash_value):
        """Set hash value

        Return True if value was already present
        Return False if value was not present
        """
        found = False

        # Linear search, update existing if found
        for i in range(len(self.hash_keys)):
            if self.hash_keys[i] == hash_key:
                self.hash_values[i] = hash_value
                found = True
                return True

        # Append to end, no ordering
        if not found:
            self.hash_keys.append(hash_key)
            self.hash_values.append(hash_value)

        return False

    def get(self, hash_key):
        """Set hash value

        Return value if found or None
        """
        
        # Linear search for matching element
        for i in range(len(self.hash_keys)):
            if self.hash_keys[i] == hash_key:
                return self.hash_values[i]

        return None
