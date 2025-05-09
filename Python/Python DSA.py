### LISTS ###
 # 1.  Lists are nothing but dynamic arrays
class arrays :
    def __init__(self,data):
        self.data = data
    def common_lists_functions(self,val):

        self.data.append(val) ## to insert at the end of the array
        print(f"valued appended to array is {val} and the modified array is {self.data}")
        self.data.insert(1,val) ### to insert at the given position
        print(f"values inserted to array is {val} and the modified array is {self.data}")
        popped = self.data.pop() ### for popping an element
        print(f"values popped from array is {popped} and the modified array is {self.data}")
    def printdata(self):
        print(f"This is an array class and the data is : {self.data}")

### LINKED LISTS ###

class createnode:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def frontinsert(self,val):
        node = createnode(val, self.head)
        self.head = node

    def endinsert(self, val):
        node = createnode(val)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def traverselist(self): ####### to traverse the linked list

        if self.head is None:
            print(f"linked list is empty")
            return

        itr = self.head
        while itr:
            print(f"the data is {itr.data} ->")
            itr = itr.next



if __name__ == '__main__':
    ### create a class object as and when required from the defined classes ###
    print("Python Dsa")



