# Lecutre 06

## Exercise 1

in class we have seen that using arrays for implementing stack may lead to underflow and overflow problems. Propose an alternative implementation of the stack operations Stack-Empty, Push and, Pop that make use of doubly linked lists to implement a stack. What is the worst-case running time for the Pop and Push operations? May we still incur in situations where the stack underflows or overflows?

non modified code
```ruby
Stack-Empty(S):
    if(S.top == 0)
        return true
    else
        return false

Push(S,x)
    S.top = S.top+1
    S[S.top] = x


Pop(S):
    if(Stack-Empty(S))
        error "underflow"
    else
        S.top= S.top -1
        return S[S.top+1]
```


Rewritten for doubly linked lists:
```ruby
def Stack_Empty(S)
    if(S.Head != null)
        return true
    else
        return false

def Push(S,x)
    x.next = S.Head;
    x.previous = null
    S.Head = x



def Pop(S)
    free(S.head)
    S.head = S.head.next
    S.head.prev = null
```
## exercise 2

(a) [CLRS-3 10.4-2] Write an O(n)-time recursive procedure that, given an n-node binary tree, prints out the key of each node in the tree.
```py
class TreeNode:
    def __init__(self, key, parent=None, sibling=None, child=None):
        self.parent = parent
        self.key = key
        self.sibling = sibling
        self.child = child




def printTee(node):
    if node is None:
        return
    print(node.key)

    printTee(node.sibling)
    printTee(node.child)


root = TreeNode(1)
root.child = TreeNode(2)
root.sibling = TreeNode(3)
root.child.child = TreeNode(4)
root.child.sibling = TreeNode(5)

printTee(root)
```

(b) [CLRS-3 10.4-3] Write an O(n)-time nonrecursive procedure that, given an n-node binary tree, prints out the key of each node in the tree. Use a stack as an auxiliary data structure.

```py
class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def printTree(node):
    if root is None:
        return

    stack = [root]

    while stack:
        # Pop the top item from the stack and print its key
        if node is not None:
            print(node.key)
            stack.append(node.right)
            stack.append(node.left)
        # Push the right child first, then the left child to the stack
        node = stack.pop()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

printTree(root)
```

## Exercise 3.

Singly linked lists are a variant of linked lists where each element x has two attributes, x.key that stores the key, and x.next that points to the next element in the list. Can you implement the dynamic-set operation Insert on a singly linked list in O(1) time? How about Delete?


```ruby
List_insert(L,x)
    x.next = L.head
    L.head = x
```



Aim to skip the x element in the single linked list
```ruby
List_delete_(L,x)
    if x.next == null
        normal_List_delete(L,x) //a funtion that finds the last element and set the next last pointer to null
    else
        n = x.next 
        x.key = n.key 
        x.next = n.next

```




## Exercise 4

Give a Θ(n)-time nonrecursive procedure that reverses a singly linked list of n elements by updating its pointers. The procedure should use no more than constant storage beyond that needed for the list itself.

```ruby
class listt:
    def __init__(self):
        self.next = None
        
        
def reverse_list(L):
    prev = None
    current = L.head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    L.head = prev
        
    
```

## Exercise 5

Implement a queue by a singly linked list Q. The operations Enqueue and Dequeue should still take O(1) time.
***Hint: You can assume that in addition to the usual attribute Q.head, pointing to the head of the list, the list Q has also the attribute Q.tail which points to the last element of the linked list.***




