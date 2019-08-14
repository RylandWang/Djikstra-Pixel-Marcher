class Marcher:
    
    class PixelNode():
        '''
        A node represents one pixel (and its attributes)
        '''
        def __init__(self, x, y, cost, previous = None):
            # Previous pixel - for backtracking a path
            self.prev = previous 
            # pixel coordinates
            self.coord = (x,y)
            self.x = x
            self.y = y
            # cost of travel between this pixel and its previous pixel
            self.cost = cost
      
    class PriorityQueue():
        '''
        Min heap (list) implementation of priority queue
        '''
        class PQNode():
            def __init__(self, data, priority):
                self.data = data
                self.priority = priority        
            
        def __init__(self):
            self.nodes = []
            self.size = 0
        
        def add(self, data, priority):
            
            node = Marcher.PriorityQueue.PQNode(data, priority)
            
            self.nodes.append(node)
            self.size += 1
            
            # update new node position to maintain heap property
            self._heapifyUp()
            
        def pop(self):
            '''
            Return element of min priority from PQ, consequently removing it
            from the heap
            '''
            if self.size == 0:
                return None
            popped = self.nodes[0].data
            
            # replace root node with right-bottom-most child node
            self.nodes[0] = self.nodes[-1]
            del self.nodes[-1]
            self.size -= 1
            
            if self.size > 1:
                # restore heap property
                self._heapifyDown()
            
            return popped
        
        def _heapifyDown(self):
            '''
            Update (percolate down) root node position until heap properties is satisfied
            '''
            parent = 0
            children = self._childrenIndex(parent)
            
            while children[0] is not None and children[1] is not None:
                
                p = self.nodes[parent] # parent node
                c1 = self.nodes[children[0]] # left child node
                c2 = None 
                if children[1] is not None:
                    c2 = self.nodes[children[1]] # right child node
                
                # if heap condition satisfied, ie parent <= its children
                if (c2 is None and p.priority <= c1.priority
                    or (p.priority <= c1.priority and p.priority <= c2.priority)):
                    break
                
                # if parent has two children
                if c2 is not None:
                    
                    # right child is smallest
                    if p.priority >= c1.priority > c2.priority:
                        # swap parent with its right child
                        temp = p
                        self.nodes[parent] = c2
                        self.nodes[children[1]] = temp
                        # update parent node index
                        parent = children[1]
                        
                    # left child is smallest
                    elif p.priority >= c2.priority >= c1.priority:
                        # swap parent with its left child
                        temp = p
                        self.nodes[parent] = c1
                        self.nodes[children[0]] = temp
                        # update parent node index
                        parent = children[0]
                        
                    elif p.priority > c2.priority:
                        # swap parent with its right child
                        temp = p
                        self.nodes[parent] = c2
                        self.nodes[children[1]] = temp
                        # update parent node index
                        parent = children[1]
                        
                    elif p.priority > c1.priority:
                        # swap parent with its left child
                        temp = p
                        self.nodes[parent] = c1
                        self.nodes[children[0]] = temp
                        # update parent node index
                        parent = children[0]
                        
                # if parent has one child
                else:
                    # left child (only child) is smaller
                    if p.priority > c1.priority:
                        # swap parent with its left child
                        temp = p
                        self.nodes[parent] = c1
                        self.nodes[children[0]] = temp
                        # update parent node index
                        parent = children[0]                        
                        
                children = self._childrenIndex(parent)
              
        def _childrenIndex(self, index):
            '''
            Compute and returns indices of children nodes and given parent index
            '''
            child1 = index*2 + 1
            child2 = index*2 + 2
            
            if (child1 >= self.size):
                child1 = None
                
            if (child2 >= self.size):
                child2 = None
            
            return (child1, child2)
                
        def _parentIndex(self, index):
            '''
            Compute and returns index of parent node at specified child index
            '''
            
            # ceiling of (index - 2) / 2 
            result = -(-(index - 2) // 2)
            if result < 0:
                return None
            return result
                
        def _heapifyUp(self):
            '''
            Update (percolate up) newly inserted node position until heap property is satisfied
            '''
            
            child = self.size -1 # child index 
            parent = self._parentIndex(child) # parent index
             
            # percolate new node up until heap property is no longer violated         
            while (parent is not None 
                   and self.nodes[parent].priority > self.nodes[child].priority):
                # swap parent and child
                temp = self.nodes[parent]
                self.nodes[parent] = self.nodes[child]
                self.nodes[child] = temp
                # update indexes
                child = parent
                parent = self._parentIndex(child)
                
     
    @staticmethod
    def findPath(mp, weight):
        """
        Finds the least-energy path from pixel (0,0) to pixel(sx-1, sy-1), along
        with the amount of energy required to traverse this path. Here, sx and sy are the x and y 
        dimensions of the image. (These are stored in 'mp')
        """
        
        PQ = Marcher.PriorityQueue()
        
        # add starting pixel to priority queue with default weight 0
        PQ.add(Marcher.PixelNode(0,0,0, None), 0)
        
        # store visited coordinates in set for O(1) lookup
        visited = {}
        visited[(0,0)] = True
        
        cur = PQ.pop()
        end_node = None # construct PixelNode once end reached
        end = False
        
        # check current pixel's neighbors
        # add each neighbor to priority queue if not already visited
        while cur is not None:
            # # visit each of 4 neighboring pixels starting at top in clockwise fashion
            for (x,y) in [(cur.x, cur.y-1), (cur.x+1, cur.y), (cur.x, cur.y+1), (cur.x-1, cur.y)]:
                
                if ((x!=cur.x and 0 <= x <= mp.sx-1) 
                    or (y!=cur.y and 0 <= y <= mp.sy-1) 
                    and (x, y) not in visited):

                    cost = weight(mp, (cur.x, cur.y), (x, y)) + cur.cost
                    n = Marcher.PixelNode(x, y, cost, cur)
                    
                    # if end pixel reached
                    if x == mp.sx-1 and y == mp.sy-1:
                        end_node = n
                        end = True
                        break
                    # otherwise continue adding new pixel node to PQ
                    PQ.add(n, cost)

            if end:
                break
            cur = PQ.pop()
            
            while (cur.x, cur.y) in visited:
                cur = PQ.pop()

            visited[(cur.x, cur.y)] = True                

        # retrace all nodes of the least path
        # sum up total cost and add coordinate of each node to mp.path
        if end_node is not None:
            prev_node = end_node.prev
            while prev_node is not None:
                # print(prev_node.coord, prev_node.cost)
                mp.path.append(prev_node.coord)
                prev_node = prev_node.prev

        return end_node.cost