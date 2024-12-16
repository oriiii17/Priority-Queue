def remove(self):
    # implementasi ini tidak return
    if self.is_empty() == False:
    # yang akan dihapus pasti head
        hapus = self._head
        # jika cuma ada 1 node
        if self._size == 1:
            self._head = None
        else:
            self._head = self._head._next
            self._head._prev = None
        # hapus node
        del hapus
        self._size = self._size- 1