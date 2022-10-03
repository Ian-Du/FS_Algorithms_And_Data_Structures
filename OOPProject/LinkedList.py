class Node:
    # Initializes the class Node with parameters name and reference. Reference has a default value of None,
    #  so during initialization we can disregard putting in a reference.
    def __init__(self, name, reference=None):
        self.name = name
        self._reference = reference
        if self._reference is None:
            self.reference_name = None
        else:
            self.reference_name = reference.name

    # We have overridden the "to string" function that was inherited from the Object class. So whenever
    # we try to do a print, this function will be called instead
    def __str__(self):
        return f"Name: {self.name}, Reference: {self.reference_name}"

    # Uses recursion to find the tail of the linked list. Tail is the item on the list with a reference
    # value of None
    def find_tail(self):
        if self._reference is None:
            return self
        else:
            return self._reference.find_tail()

    # This portion of the class is just to provide a set and get mechanism for reference so that whenever
    # we set the reference it will also set the name of the reference.
    # This is totally optional and is only here for ease of use.
    def get_reference(self):
        return self._reference

    def set_reference(self, value):
        self._reference = value
        if value is None:
            self.reference_name = None
        else:
            self.reference_name = self._reference.name

    reference = property(get_reference, set_reference)


# Create linked list
node2 = Node(name="name2")
node1 = Node(name="name1", reference=node2)
head = Node(name="name0", reference=node1)

# Finds the tail node
tail_node = head.find_tail()
print(f"Get current tail node from head --> {tail_node}")
# Finding the tail node doesn't have to start at the head
tail_node = node1.find_tail()
print(f"Get current tail node from node1 --> {tail_node}")

new_tail = Node(name="name3")
print(f"Create new tail node --> {new_tail}")

# The extra bit of code in the Node class is so that we only need to do one line of code instead of
# having to do the set of code below everytime we want to add a new tail to the list:
#       tail_node.reference = new_tail
#       tail_node.reference_name = new_tail.name
tail_node.reference = new_tail
print(f"Previous tail node --> {tail_node}")
