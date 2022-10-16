class node:
  def __init__(self, val, left=None, right=None):
    self.left=left
    self.val=val
    self.right=right
  
  

root=node(4)
root.left=node(1)
root.right=node(5)
root.left.left=node(7)
root.left.right=node(3)
root.right.right=node(6)
 

def isChild(node):
    if node.right or node.left:
        return True
    else:
        return False


def printPostOrderWithoutRec(node):
    liNode = []
    if node:
        liNode.append([node, isChild(node)])
    else:
        print("Tree is empty.")
        return

    while liNode:
        curNode, bChild = liNode[-1]

        if bChild:
            liNode[-1][1] = 0
            if curNode.right:
                liNode.append([curNode.right, isChild(curNode.right)])
            if curNode.left:
                liNode.append([curNode.left, isChild(curNode.left)])
        else:
            print(curNode.val)
            del liNode[-1]

printPostOrderWithoutRec(root)