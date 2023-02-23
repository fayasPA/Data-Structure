# my_dict = {'fayas':'123', 'fazil':'145','fay':'435', 'salm':434}
# print(my_dict)
# print(type(my_dict))

# new_dict = dict(fay='123',fazil='345')
# print(new_dict)
# print(type(new_dict))

# emp_details = {'Employee':{'Dave':{'ID':'001','salary':'20000'},'Eva':{'ID':'002','salary':'5000'}}}
# emp_details['fay'] = 21545
# print(type(emp_details))

# print(4322%10)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for i in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            temp = self.table[index]
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(key, value)

    def get(self, key):
        index = self.hash_function(key)
        temp = self.table[index]
        while temp is not None and temp.key != key:
            temp = temp.next
        if temp is None:
            return None
        else:
            return temp.value

new_hashtable = HashTable(10)
new_hashtable.add(1, "fayas")
new_hashtable.add(2, "asfsef")
print(new_hashtable.get(1))

{5:fatyad}