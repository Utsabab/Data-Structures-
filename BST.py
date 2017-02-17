#BST:   
class Node:
  def__init__(self,data):
    self.l_child = None
    self.r_child = None 
    self.data = data 
    
class Searchtree:
  
  def __init__(self):
    self.root = None 
    
  def create(self, info):
    if self.root = None
      self.root = Node(info)
    else:
      current = self.root 
      while True:
        if info < current.data:
          if current.left:
            current = current.left 
          else:
            current.left = Node(info)
            break;
        elif info > current.data:
          if current.right:
            current = current.right 
          else:
            current.right = Node(info)
            break;
        else:
          break
        
  def insert(root, val):
    if root is None:
      root = val
    else:
      if root.data > node.data:
        if root.l_child = None:
          root.l_child = val
        else:
          insert(root.l_child, val)
      else root.data < node.data:
        if root.r_child = None:
          root.r_child = val
        else:
          insert(root.r_child, val)