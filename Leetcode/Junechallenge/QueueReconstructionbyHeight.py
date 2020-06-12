'''Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
 '''
 
 
 class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        ret = [[]]*len(people)
        people.sort(key = lambda x: (x[0],-x[1])) 
        indices = [i for i in range(len(people))]
        for j,(_,pk) in enumerate(people):
            i = indices.pop(pk)
            ret[i] = people[j]
        return ret
