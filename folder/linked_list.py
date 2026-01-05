class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"Node({self.data!r})"


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert_at_head(self, data):
        node = Node(data, self.head)
        self.head = node
        self._size += 1

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self._size += 1

    def insert_after(self, target, data):
        cur = self.head
        while cur:
            if cur.data == target:
                new_node = Node(data, cur.next)
                cur.next = new_node
                self._size += 1
                return True
            cur = cur.next
        return False

    def delete_value(self, data):
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self._size -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def find(self, data):
        cur = self.head
        idx = 0
        while cur:
            if cur.data == data:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out

    def clear(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def __repr__(self):
        return f"LinkedList({self.to_list()})"


if __name__ == '__main__':
    ll = LinkedList()
    print('Empty list:', ll)

    for v in [1, 2, 3]:
        ll.append(v)
    print('After append 1,2,3:', ll)

    ll.insert_at_head(0)
    print('After insert_at_head(0):', ll)

    ll.insert_after(2, 2.5)
    print('After insert_after(2, 2.5):', ll)

    print('Find 2 at index:', ll.find(2))
    print('Find 99 (not present):', ll.find(99))

    ll.delete_value(2.5)
    print('After delete_value(2.5):', ll)

    ll.reverse()
    print('After reverse():', ll)

    print('Iterating values: ', list(ll))
