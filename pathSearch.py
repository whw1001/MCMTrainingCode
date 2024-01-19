import heapq

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)


class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """
    def  __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction      # store the priority function
        PriorityQueue.__init__(self)        # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))

# aStar算法
def aStarSearch(list, start_vertex, end_vertex, heuristic):
    fringe = PriorityQueue()
    class NODE:
        def __init__(self, *args):
            self.vertex = args[0]
            if args[2] != '':
                self.path = args[2].path[:]
                self.path.append(args[0])
                self.cost = args[1] + args[2].cost
            else:
                self.path = [start_vertex]
                self.cost = 0

    visited = [start_vertex]
    fringe.push(NODE(start_vertex, 0, ''), 0)

    while not fringe.isEmpty():
        currentNODE = fringe.pop()

        if currentNODE.vertex == end_vertex:
            return currentNODE.path, currentNODE.cost
        else:
            successors = list[currentNODE.vertex]
            for successor in successors:
                next_vertex = successor[0]
                next_cost = successor[1]
                if next_vertex not in visited:
                    visited.append(next_vertex)
                    fringe.push(NODE(next_vertex, next_cost, currentNODE), currentNODE.cost + next_cost)

    if fringe.isEmpty():
        return []


