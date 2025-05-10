from collections import deque ## for queue
from collections import defaultdict
from collections.abc import Reversible
from queue import Queue, LifoQueue, SimpleQueue, PriorityQueue
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
        if self.head == None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def insertlist(self,lst):
        for value in lst:
            self.endinsert(value)

    def traverselist(self): ####### to traverse the linked list
        if self.head is None:
            print(f"linked list is empty")
            return

        itr = self.head
        while itr:
            print(f"the data is {itr.data} ->")
            itr = itr.next


######### STACK ###########
class stack:
    def __init__(self):
        self.stk = []

    def push(self,val):
        self.stk.append(val)
        print(f"after pushing {val} the updated stack is {self.stk}")

    def pop(self):
        if len(self.stk) == 0:
            print(f"Stack empty! nothing to pop ")
            return
        popped = self.stk.pop()
        print(f"the popped element is {popped}, after popping the list is {self.stk}")


######### QUEUE ############
class Queues:  ###### need to  import deque from collections
    def __init__(self):
        self.que = deque()

    def push(self,val):
        self.que.append(val)
        print(f"after inserting {val} the queue is {self.que}")

    def pop(self):
        if len(self.que) == 0:
            print("queue is empty! nothing to pop")
            return
        popped = self.que.popleft()
        print(f"after popping {popped} the queue is {self.que}")

########## PRIORITY QUEUE #############
#### PQ works on tuples so insert the elements in tuples
class priorityque(PriorityQueue): ###### import PriorityQueue from queue
    def __init__(self,reverse = False):
        super().__init__()
        self.reverse = reverse

    def put(self,val,item):
        items = (val,item)
        if self.reverse:
            items = (-val,item)
        super().put(items)

    def printpq(self):
            while not self.empty():
                priority, val = self.get()
                if self.reverse:
                    print(f"{-priority},{val}")
                else:
                    print(f"{priority},{val}")

if __name__ == '__main__':
    ### create a class object as and when required from the defined classes ###
    print("Python Dsa")
    pqs = priorityque(reverse=False)
    pqs.put(5,"test")
    pqs.put(4, "test")
    pqs.put(6, "test")
    pqs.put(2, "test")
    pqs.printpq()



