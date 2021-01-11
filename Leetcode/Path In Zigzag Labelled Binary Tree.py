'''
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

'''


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        k = []


        while True:
            if label ==1:
                k.append(1)

                break


            for i in range(21):
                if 2**i <= label and 2**(i+1) > label:
                    k.append(label)
                    start = 2**(i-1)
                    end = (2**i) -1


                    label = label//2

                    label = end - (label - start)


        return k[::-1]
