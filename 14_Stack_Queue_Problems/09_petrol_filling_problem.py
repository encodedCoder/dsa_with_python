class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) >= sum(cost):
            surplus = 0
            deficit = 0
            start   = 0
            for i in range(len(gas)):
                if surplus + gas[i] >= cost[i]:
                    surplus += gas[i] - cost[i]
                else:
                    start    = i + 1
                    deficit += (surplus+gas[i]) - cost[i]
                    surplus  = 0
            else:
                if surplus + deficit >= 0:
                    return start
        return -1

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas  = [10,2,3,4,2]
cost = [5,7,4,2,1]

gas  = [5,1,2,3,4]
cost = [4,4,1,5,1]

gas  = [7,1,0,11,9]
cost = [5,5,9,1,2]

print(Solution.canCompleteCircuit(0, gas, cost))