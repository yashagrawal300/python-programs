class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        
        ans = []
        queue = []
        queue.append(root)
        queue.append(None)
        s = []
        
        count = 0
        
        while len(queue) != 0:
            a = queue.pop(0)
 
            
            if a == None:
                count+=1
                if count >1:
                    break
                else:
                    queue.append(None)
                    ans.append(s)
                    s = []
                    count+=1
            
            else:
                if a.left:
                    queue.append(a.left)
                if a.right:

                    queue.append(a.right)
                s.append(a.val)
                count=0
                

        return sum(ans[-1])
                
                
        
                
        
