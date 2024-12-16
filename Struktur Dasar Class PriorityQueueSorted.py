class PriorityQueueSorted:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False
    def __len__(self):
        return self._size
    def print_all(self):
        if self.is_empty() == True:
            print('Priority Queue is empty')
        else:
            bantu = self._head
            while bantu != None:
                print('(', bantu._data, ',', bantu._priority, ')', end=' ')
                bantu = bantu._next
        print()

# • Fungsi __init__() yang merupakan constructor. Tugasnya untuk menginisialisasi nilai dari
#  head, tail dan jumlah data di dalam Priority Queue tersebut.
#  • Fungsi is_empty() yang digunakan untuk mengecek apakan Priority Queue kosong atau
#  tidak. Fungsi ini akan berguna pada saat akan menghapus data.
#  • Fungsi __len__() yang digunakan untuk mendapatkan informasi berapa jumlah data yang
#  ada di dalam Priority Queue.
#  • Fungsi print_all() yang digunakan untuk menampilkan isi dari Priority Queue.