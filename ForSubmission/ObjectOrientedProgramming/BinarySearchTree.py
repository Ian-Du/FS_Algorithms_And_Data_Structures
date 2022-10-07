class Node:
    def __init__(self, key, data, reference=None):
        self.key = key
        self.data = data
        self.reference = reference
        if self.reference is None:
            self.reference_key = None
            self.reference_data = None
        else:
            self.reference_key = reference.key
            self.reference_data = reference.data

    def Insert_Node(self, key, data):
        if self.reference is None:
            self.reference = Node(key, data)
        else:
            self.reference = Node(key, data, self.reference)
        self.reference_key = key
        self.reference_data = data

    def Get_Node(self, key):
        if self.key == key:
            return self
        else:
            return self.reference.Get_Node(key)

    def __str__(self):
        return f"Key: {self.key}, Data: {self.data}, Next Node: {self.reference_key}"


tree = Node('Vahe', 40)
tree.Insert_Node('Thomas', 41)
tree.Insert_Node('Alex', 30)
tree.Insert_Node('Lilian', 25)
tree.reference.Insert_Node('Anna', 13)

print(tree.Get_Node('Alex'))
print(tree.Get_Node('Anna'))
print(tree.Get_Node('Lilian'))
print(tree)