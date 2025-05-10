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


########## TREES ############

class generaltree:
    def __init__(self,name):
        self.name = name
        self.child = []
        self.parent = None

    def addchild(self,name):
        name.parent = self
        self.child.append(name)

    def treelevel(self):
        count = 0
        itr = self
        while itr.parent is not None:
            itr = itr.parent
            count += 1

        return count

    def printtree(self):
        stk = []
        stk.append(self)
        while len(stk) > 0:
            itr = stk.pop()
            print(itr.name)
            for i in itr.child:
                stk.append(i)

    def printtreestack(self):

        if self is not None:
            print('    ' * 3 * self.treelevel() + self.name )
            for i in self.child:
                i.printtreestack()


######### BINARY TREES ############

class binarytrees:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addchild(self,val):

        if val > self.data :
            if self.right is None:
                self.right = binarytrees(val)
            else:
                self.right.addchild(val)
        else:
            if self.left is None:
                self.left = binarytrees(val)
            else:
                self.left.addchild(val)

    def preorder(self):

        print(self.data)
        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def inorder(self):

        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def postorder(self):

        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()
        print(self.data)

    def min_val(self):
        if self.left:
            return self.left.min_val()
        return self.data

    def max_val(self):
        if self.right is None:
            return self.data
        return self.right.max_val()

    def delete_node(self,val):
        if val < self.data:
            if self.left:
                  self.left = self.left.delete_node(val)

        elif val > self.data:
            if self.right:
                 self.right = self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right

            mins = self.right.min_val()
            self.data = mins
            self.right = self.right.delete_node(mins)
        return self


######## BINARY SEARCH #########

class binarysearch:

    def __init__(self,data):
        self.data = data

    def bsrch(self,key):

        l = 0
        r = len(self.data) - 1
        mid = 0
        while(l <= r):
            mid = (l + r) // 2
            if self.data[mid] == key:
                return mid
            elif key < self.data[mid]:
                r = mid - 1
            else:
                l = mid + 1

    def rbsrch(self,key,l,r):  ### recursive binary search

        mid = (l + r) // 2
        if l > r or mid >= len(self.data) or mid < 0:
            return -1


        if self.data[mid] == key:
            return mid
        elif key < self.data[mid]:
            r = mid - 1
        else:
            l = mid + 1

        return self.rbsrch(key,l, r)


###########  GRAPHS #############
### WE USE DICTIONARIES FOR GRAPHS
class graph:
    def __init__(self,edges):
        self.edges = edges
        self.paths = defaultdict(list)
        for i,j in edges:
            self.paths[i].append(j)

    def bfs(self,start): ######### BREADTH FIRST SEARCH
        visited = set()
        que = deque()
        que.append(start)
        while que:
            itr = que.popleft()
            if itr not in visited:
                print(f"{itr}", end=' -> ')
                visited.add(itr)
                for path in self.paths[itr]:
                        que.append(path)

    def dfs(self,start):
        visited = set()
        stck = []
        stck.append(start)
        while stck:
            popped = stck.pop()
            if popped not in visited:
                print(f"{popped}", end = ' -> ')
                visited.add(popped)
                for path in self.paths[popped]:
                    stck.append(path)



    def rdfs(self,start, visited = set()): ######### RECURSIVE ###########

        if start not in visited:
            print(f"{start}",end = ' -> ')
            visited.add(start)
            for path in self.paths[start]:
                self.rdfs(path,visited)

    def allpaths(self,source,destination, res = []):

            res = res + [source]

            if source == destination :
                return [res]

            if source not in self.paths:
                return []

            allpath = []
            for itr in self.paths[source]:
                if itr not in res:
                    new_path = self.allpaths(itr,destination,res)
                    for p in new_path:
                        allpath.append(p)
            return allpath
                



if __name__ == '__main__':
    ### create a class object as and when required from the defined classes ###
    print("Python Dsa")
    routes = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E")
    ]
    gph = graph(routes)
    print(gph.allpaths('A','E'))