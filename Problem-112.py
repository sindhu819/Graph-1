'''
leetcode- 997- https://leetcode.com/problems/find-the-town-judge/
time complexity - O(N)
space complexity- O(N)
approach - topological sorting - works only for directed array. 
town judge won't trust anybody, but everyone trusts town judge 
if we have element that doesn't have incoming edges and the it should contain N-1.

'''
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if trust==[]:
            if N==1:
                return 1
            else:
                return -1
        
        t=[0]*N
        trust_someone=[0]*N
        for i in range(len(trust)):
            a=trust[i][0]
            b=trust[i][1]
            trust_someone[b-1]+=1
            t[a-1]=1
        print(t)
        print(trust_someone)
        for i in range(N):
            if t[i]==0 and trust_someone[i]==N-1:
                return i+1
        return -1
