# Lecture 08

## exercise 1

(CLRS 12.3-1) Implement a recursive variant of the Tree-Insert procedure.

```ruby
Tree-Insert(T,z)
y = NIL
x = T.root
while x != NIL
    y = x
    if z.key < x.key
        x = x.left
    else 
        x = x.right
z.p = y
if y == NIL
    T.root = z
elseif z.key < y.key
    y.left = z
else y.right = z
```
!!! warning

    gpt output
    
```py
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def tree_insert(self, z):
        self.root = self._tree_insert_recursive(self.root, None, z)

    def _tree_insert_recursive(self, x, y, z):
        if x is None:
            z.parent = y
            return z
        if z.key < x.key:
            x.left = self._tree_insert_recursive(x.left, x, z)
        else:
            x.right = self._tree_insert_recursive(x.right, x, z)
        return x

```
## exercise 2

(CLRS 12.3-3) We can sort a sequence of n numbers by iteratively inserting each number in a binary search tree and then performing an inorder tree walk. Write the pseudocode of this algorithm. What are the worst-case and best-case running times for this sorting algorithm?
Here's the pseudocode for sorting a sequence of n numbers using binary search tree insertion and inorder tree walk:

!!! warning

    gpt output


```ruby
Sort-Sequence(A)
1. Create an empty binary search tree T
2. for i = 1 to length(A)
3.     Create a new TreeNode with key A[i]
4.     Tree-Insert(T, new TreeNode)
5. Perform Inorder-Tree-Walk(T.root)
```

To perform the Inorder-Tree-Walk:

```ruby
Inorder-Tree-Walk(x)
1. if x != NIL
2.     Inorder-Tree-Walk(x.left)
3.     print(x.key)
4.     Inorder-Tree-Walk(x.right)
```

The running time of this sorting algorithm depends on the height of the binary search tree:

1. Best-case: The best-case scenario occurs when the binary search tree is perfectly balanced, and the height of the tree is log(n). In this case, both the insertion and inorder tree walk operations take O(log(n)) time, and since we perform these operations for n elements, the total running time is O(n*log(n)).

2. Worst-case: The worst-case scenario occurs when the binary search tree becomes completely unbalanced, degenerating into a linked list. This can happen when the input sequence is already sorted or reverse sorted. In this case, the height of the tree is n, and the insertion operation takes O(n) time. As we perform this operation for n elements, the insertion part takes O(n^2) time. The inorder tree walk takes O(n) time. Thus, the total worst-case running time is O(n^2).

In summary, the best-case running time for this sorting algorithm is O(n*log(n)), and the worst-case running time is O(n^2). It's important to note that using a self-balancing binary search tree (like AVL tree or red-black tree) would guarantee a balanced tree, resulting in a consistently O(n*log(n)) time complexity for sorting.


## exercise 3
Consider the binary search tree T depicted in Figure 1. Delete the node with key = 10 from T by applying the procedure Tree-Delete(T, z) as described in CLRS








## exercise 4
Show the red-black trees that result after successively inserting the keys 41; 38; 31; 12; 19; 8 into an initially empty red-black tree.

## exercise 5
Consider the red-black tree T depicted in Figure 2. Insert first a node with key = 15 in T, then delete the node with key = 8. Show all the intermediate transformations of the red-black tree with particular emphasis on the rotations.
