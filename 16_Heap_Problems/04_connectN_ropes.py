from queue import PriorityQueue

def connectNRopes(ropes):
    pQ = PriorityQueue()

    for rope in ropes:
        pQ.put(rope)

    cost = 0
    while pQ.qsize() != 1:
        rope1 = pQ.get()
        rope2 = pQ.get()
        cost += rope1 + rope2
        pQ.put(rope1 + rope2)

    return cost

ropes = [5,2,3,9]
# ropes = [4,3,2,6]
print(connectNRopes(ropes))

# print(dir(PriorityQueue))