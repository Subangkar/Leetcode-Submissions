class ListNode:
    def __init__(self, key: int, value: int, prev: ListNode=None, next: ListNode=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next


    def __repr__(self):
        return f'[{self.val}/{hex(id(self))}]'
        


class LRUCache:

    def __init__(self, capacity: int):
        self.n = 0
        self.cap = capacity
        self.head = None
        self.tail = None
        self.ht = {}


    def get(self, key: int) -> int:
        # print(self.ht, f'for get={key}', end=": ")
        self.print_lru()
        if key in self.ht:
            node = self.ht[key]
            if self.n>1 and node!=self.tail:
                if node != self.head:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                else:
                    self.head = node.next
                    self.head.prev = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = self.tail.next
                self.tail.next = None
                self.ht[key] = self.tail
            self.print_lru()
            return self.ht[key].val
        self.print_lru()
        return -1
        

    def put(self, key: int, value: int) -> None:
        # print(self.ht, f'for put={key}', end=": ")
        self.print_lru()
        if self.n==0:
            self.tail = self.head = ListNode(key, value)
            self.ht[key] = self.tail
            self.n += 1
        elif key in self.ht:
            node = self.ht[key]
            node.val = value
            if self.n>1 and node!=self.tail:
                if node != self.head:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                else:
                    self.head = node.next
                    self.head.prev = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = self.tail.next
                self.tail.next = None
                self.ht[key] = self.tail
        elif self.n<self.cap:
            self.tail.next = ListNode(key=key, value=value, prev=self.tail)
            self.tail = self.tail.next
            self.ht[key] = self.tail
            self.n += 1
        else:
            if self.n==1:
                self.ht.pop(self.head.key)

                self.ht[key] = self.head
                self.head.key=key
                self.head.val=value
            else:
                phead = self.head
                self.head = self.head.next
                self.head.prev = None
                self.ht.pop(phead.key)
                del phead
                self.n -= 1

                self.put(key, value)
        self.n = len(self.ht)
        self.print_lru()


    def print_lru(self):
        pass
        # x = self.head
        # while x:
        #     print(f'[{x.val}]->', end=' ')
        #     x=x.next
        # x = self.tail
        # while x:
        #     print(f'<-[{x.val}]', end=' ')
        #     x=x.prev
        # print()


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)