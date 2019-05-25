
class Marcher:
    
    class PixelNode():
        '''
        A node represents one pixel (and its attributes) in the image
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
        Objective: To find the least-energy path from pixel (0,0) to pixel(sx-1, sy-1), along
            with the amount of energy required to traverse this path. Here, sx and sy are the x and y 
            dimensions of the image. (These are stored in 'mp')
        
        Input: 
            mp - This is a Map object representing the image you are working on. Look at the Map
                class to see details on how we are representing the data.

            weight - This is the weight **function**. You are supposed to use this to find the energy
                required for each step by the Pixel Marcher. This function should be called like this:
        total_cost = 0 # total energy cost
                      weight(mp, (x        total_cost = 0 # total energy cost,y), (a, b))
        total_cost = 0 # total energy cost
                to find the energy         total_cost = 0 # total energy costneeded to step from pixel (x,y) to pixel (a,b). Note that
                this function may return a value for *any* pair of pixels, and it is your job
                to only be consider valid steps (More on this below). In general this returns a float.

                The return value of this function will always be non-negative, and it is not necessarily
                the case that weight(mp, a, b) = weight(mp, b, a).
        """
        
        PQ = Marcher.PriorityQueue()
        
        # add starting pixel to priority queue with default weight 0
        PQ.add(Marcher.PixelNode(0,0,0, None), 0)
        
        # store visited coordinates for constant lookup
        visited = {}
        visited[(0,0)] = True
        
        cur = PQ.pop()
        end_node = None # construct PixelNode once end reached
        
        # check current pixel's neighbors
        # add each neighbor to priority queue if not already visited
        while cur is not None:
            
            # visit above pixel
            if ((0 <= cur.y-1 <= mp.sy-1) 
                and (cur.x, cur.y-1) not in visited):
                # next pixel coordinates
                i = cur.x
                j = cur.y-1
                
                w = weight(mp, (cur.x, cur.y), (i, j)) + cur.cost
                n = Marcher.PixelNode(i, j, w, cur)
                
                # if end pixel reached
                if i == mp.sx-1 and j == mp.sy-1:
                    end_node = n
                    break
                
                # otherwise continue adding new pixel node to PQ
                PQ.add(n, w)
                 
            
            # visit right pixel
            if ((0 <= cur.x+1 <= mp.sx-1)
                and (cur.x+1, cur.y) not in visited):
                i = cur.x+1
                j = cur.y
                
                w = weight(mp, (cur.x, cur.y), (i, j)) + cur.cost
                n = Marcher.PixelNode(i, j, w, cur)
                
                # if end pixel reached
                if i == mp.sx-1 and j == mp.sy-1:
                    end_node = n
                    break
                
                # otherwise continue adding new pixel node to PQ
                PQ.add(n, w)
      
            
            # visit below pixel
            if ((0 <= cur.y+1 <= mp.sy-1)
                and (cur.x, cur.y+1) not in visited):
                i = cur.x
                j = cur.y+1
                
                w = weight(mp, (cur.x, cur.y), (i, j)) + cur.cost
                n = Marcher.PixelNode(i, j, w, cur)
                
                # if end pixel reached
                if i == mp.sx-1 and j == mp.sy-1:
                    end_node = n
                    break
                
                # otherwise continue adding new pixel node to PQ
                PQ.add(n, w)
                          

            # visit left pixel
            if ((0 <= cur.x-1 <= mp.sx-1)
                and (cur.x-1, cur.y) not in visited):
                i = cur.x-1
                j = cur.y
                
                w = weight(mp, (cur.x, cur.y), (i, j)) + cur.cost
                n = Marcher.PixelNode(i, j, w, cur)
                
                # if end pixel reached
                if i == mp.sx-1 and j == mp.sy-1:
                    end_node = n
                    break
                
                # otherwise continue adding new pixel node to PQ
                PQ.add(n, w)
     

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


        #print(total_cost)
        return end_node.cost