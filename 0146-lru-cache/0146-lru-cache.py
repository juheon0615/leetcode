class _Node:
    """Doubly-linked list node used internally by LRUCache."""
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key: int, value: int):
        self.key   = key
        self.value = value
        self.prev  = None        # type: _Node | None
        self.next  = None        # type: _Node | None


class LRUCache:
    """
    O(1) get / put LRU cache.

    Internals
    ---------
    • _map   : dict[int, _Node]  – fast key → node lookup
    • _head  : _Node | None      – least-recently-used node
    • _tail  : _Node | None      – most-recently-used node
    """
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self._capacity = capacity
        self._map: dict[int, _Node] = {}
        self._head: _Node | None = None
        self._tail: _Node | None = None

    # ────────────────────────────── public API ──────────────────────────────
    def get(self, key: int) -> int:
        """Return value if key exists; else -1.  Updates recency."""
        node = self._map.get(key)
        if node is None:
            return -1
        self._move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update (key, value).
        If the cache is at capacity, evict the least-recently-used item.
        """
        node = self._map.get(key)
        if node is not None:                      # update path
            node.value = value
            self._move_to_tail(node)
            return

        # insert path
        if len(self._map) == self._capacity:      # evict LRU
            assert self._head                    # never None here
            lru = self._head
            self._remove_node(lru)
            del self._map[lru.key]

        new_node = _Node(key, value)
        self._append_to_tail(new_node)
        self._map[key] = new_node

    # ───────────────────────────── helper methods ───────────────────────────
    def _move_to_tail(self, node: _Node) -> None:
        """Detach *node* from its current position and make it most-recent."""
        if node is self._tail:
            return                               # already MRU
        self._remove_node(node)
        self._append_to_tail(node)

    def _remove_node(self, node: _Node) -> None:
        """Detach *node* (but do not touch the dict)."""
        if node.prev:
            node.prev.next = node.next
        else:                                    # node was head
            self._head = node.next

        if node.next:
            node.next.prev = node.prev
        else:                                    # node was tail
            self._tail = node.prev

        node.prev = node.next = None             # help GC

    def _append_to_tail(self, node: _Node) -> None:
        """Make *node* the new tail (most-recent)."""
        node.prev = self._tail
        node.next = None
        if self._tail:
            self._tail.next = node
        else:                                    # list was empty
            self._head = node
        self._tail = node
