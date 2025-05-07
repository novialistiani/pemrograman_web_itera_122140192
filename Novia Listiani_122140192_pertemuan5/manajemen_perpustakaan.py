from abc import ABC, abstractmethod

# Abstract class LibraryItem
class LibraryItem(ABC):
    """
    Kelas abstrak yang menjadi dasar untuk item perpustakaan.
    Setiap item harus memiliki id dan judul.
    """

    def __init__(self, id_item, title):
        self._id_item = id_item  # Menggunakan private attribute untuk id_item
        self._title = title      # Menggunakan private attribute untuk title

    @property
    def id_item(self):
        """Getter untuk id_item"""
        return self._id_item

    @property
    def title(self):
        """Getter untuk title"""
        return self._title

    @abstractmethod
    def display_info(self):
        """Method abstrak untuk menampilkan informasi item"""
        pass


# Subclass Book yang mewarisi dari LibraryItem
class Book(LibraryItem):
    """
    Kelas Book mewarisi LibraryItem dan mengimplementasikan method display_info.
    """

    def __init__(self, id_item, title, author, pages):
        super().__init__(id_item, title)
        self._author = author    # Menggunakan private attribute untuk author
        self._pages = pages      # Menggunakan private attribute untuk pages

    @property
    def author(self):
        """Getter untuk author"""
        return self._author

    @property
    def pages(self):
        """Getter untuk pages"""
        return self._pages

    def display_info(self):
        """Menampilkan informasi buku"""
        return f"Book ID: {self.id_item}, Title: {self.title}, Author: {self.author}, Pages: {self.pages}"


# Subclass Magazine yang mewarisi dari LibraryItem
class Magazine(LibraryItem):
    """
    Kelas Magazine mewarisi LibraryItem dan mengimplementasikan method display_info.
    """

    def __init__(self, id_item, title, issue_number, publisher):
        super().__init__(id_item, title)
        self._issue_number = issue_number  # Menggunakan private attribute untuk issue_number
        self._publisher = publisher        # Menggunakan private attribute untuk publisher

    @property
    def issue_number(self):
        """Getter untuk issue_number"""
        return self._issue_number

    @property
    def publisher(self):
        """Getter untuk publisher"""
        return self._publisher

    def display_info(self):
        """Menampilkan informasi majalah"""
        return f"Magazine ID: {self.id_item}, Title: {self.title}, Issue: {self.issue_number}, Publisher: {self.publisher}"


# Class Library untuk mengelola koleksi item perpustakaan
class Library:
    """
    Kelas Library untuk menyimpan dan mengelola koleksi item perpustakaan.
    """

    def __init__(self):
        self._items = []  # Menggunakan private attribute untuk menyimpan daftar item

    def add_item(self, item):
        """Menambahkan item ke perpustakaan"""
        self._items.append(item)

    def display_items(self):
        """Menampilkan semua item yang tersedia di perpustakaan"""
        for item in self._items:
            print(item.display_info())

    def find_item(self, search_term):
        """Mencari item berdasarkan judul atau id"""
        # Jika search_term adalah integer (ID), kita langsung bandingkan
        if isinstance(search_term, int):
            found_items = [item for item in self._items if search_term == item.id_item]
        else:
            # Jika search_term adalah string (judul), kita bandingkan dengan .lower()
            found_items = [item for item in self._items if search_term.lower() in item.title.lower()]
        
        if found_items:
            for item in found_items:
                print(item.display_info())
        else:
            print("Item tidak ditemukan.")


# Fungsi untuk input manual item
def input_book():
    """Fungsi untuk input buku secara manual"""
    id_item = int(input("Masukkan ID Buku: "))  # ID dalam bentuk angka bukan huruf
    title = input("Masukkan Judul Buku: ")
    author = input("Masukkan Penulis Buku: ")
    pages = int(input("Masukkan Jumlah Halaman Buku: "))
    return Book(id_item, title, author, pages)


def input_magazine():
    """Fungsi untuk input majalah secara manual"""
    id_item = int(input("Masukkan ID Majalah: "))  # ID dalam bentuk angka bukan huruf
    title = input("Masukkan Judul Majalah: ")
    issue_number = int(input("Masukkan Nomor Edisi Majalah: "))
    publisher = input("Masukkan Penerbit Majalah: ")
    return Magazine(id_item, title, issue_number, publisher)


# Contoh penggunaan program
if __name__ == "__main__":
    # Membuat objek Library
    library = Library()

    # Menambahkan item ke perpustakaan dengan input manual
    print("Masukkan data buku pertama:")
    book1 = input_book()
    print("Masukkan data majalah pertama:")
    magazine1 = input_magazine()

    # Menambahkan item ke dalam perpustakaan
    library.add_item(book1)
    library.add_item(magazine1)

    # Menampilkan semua item di perpustakaan
    print("\nDaftar Item Perpustakaan:")
    library.display_items()

    # Mencari item berdasarkan judul
    search_title = input("\nMasukkan judul yang ingin dicari: ")
    print(f"\nMencari item dengan judul '{search_title}':")
    library.find_item(search_title)

    # Mencari item berdasarkan ID
    search_id = int(input("\nMasukkan ID yang ingin dicari: "))
    print(f"\nMencari item dengan ID {search_id}:")
    library.find_item(search_id)
