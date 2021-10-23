def trav(root):
  if not root:
    return 
  trav(root.left)
  print(root.val)
  trav(root.right)
 
