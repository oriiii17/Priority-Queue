# • Cari posisi data baru berdasarkan tingkat prioritasnya.
#  • Gunakan variabel bantu dan bantu2 untuk melakukan penyisipan.
#  • Variabel bantu harus diletakkan pada posisi setelah data akan disisipkan.
#  • Variabel bantu2 harus diletakkan pada posisi sebelum data akan disisipkan.
#  • Lakukan penyisipan data.

# add: harus memastikan linked list selalu terurut berdasarkan prioritas
def add(self, data, priority):
    baru = Node(data, priority)
    if self.is_empty():
        self._head = baru
        self._tail = baru
    elif self._size == 1:
    # isinya cuma 1, insert sebelum atau setelah head?
        if self._head._priority > priority:
            # insert sebelum head
            baru._next = self._head
            self._head._prev = baru
            self._head = baru
        else:
            # insert setelah head
            self._head._next = baru
            baru._prev = self._head
            self._tail = baru
    else:
         # cek apakah harus insert depan?
        if self._head._priority > priority:
            baru._next = self._head
            self._head._prev = baru
            self._head = baru
            # cek apakah harus insert belakang?
        elif self._tail._priority <= priority:
            self._tail._next = baru
            baru._prev = self._tail
            self._tail = baru
            self._tail._next = None
        else:
            # berarti insert di tengah
            # letakkan bantu di posisi setelah insertion point
            bantu = self._head
            while bantu._priority < priority:
                bantu = bantu._next
            # gunakan bantu2 di posisi sebelum insertion point
            bantu2 = bantu._prev
            baru._next = bantu
            bantu._prev = baru
            bantu2._next = baru
            baru._prev = bantu2
    self._size = self._size + 1


#Pengujian Implementasi

myQueue = PriorityQueueSorted()
myQueue.add('Amber', 5)
myQueue.add('Diluc', 1)
myQueue.print_all()
myQueue.add('Beidou', 3)
myQueue.add('Kaeya', 4)
myQueue.print_all()
data, priority = myQueue.peek()
print(data)
print(priority)
myQueue.remove()
myQueue.print_all()
myQueue.remove()
myQueue.print_all()
myQueue.remove()
myQueue.print_all()
myQueue.add('Venti', 1)
myQueue.print_all()