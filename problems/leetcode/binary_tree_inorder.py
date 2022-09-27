
from turtle import right


class treenode:
    def __init__(self,x):
        self.value=x
        self.left=None
        self.right=None
        


def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = treenode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = treenode(data)
    return node

root2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(root2.value)


def traverse_in(self,node):
    if node is None:
        return []
    return (self.traverse_in(node.left)+[node.value]+self.traverse_in(node.right))
traverse_in(root2)
