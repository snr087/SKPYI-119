class Book:
    def _init_(self, title, author, publisher, price, author_royalty):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.author_royalty = author_royalty

    def royalty(self, copies_sold):
        if copies_sold <= 500:
            return 0.10 * self.price * copies_sold
        elif copies_sold <= 1500:
            return 0.125 * self.price * (copies_sold - 500) + 0.10 * self.price * 500
        else:
            return 0.15 * self.price * (copies_sold - 1500) + 0.125 * self.price * 1000 + 0.10 * self.price * 500

class Ebook(Book):
    def _init_(self, title, author, publisher, price, author_royalty, ebook_format):
        super()._init_(title, author, publisher, price, author_royalty)
        self.ebook_format = ebook_format

    def royalty(self, copies_sold):
        gst_deduction = 0.12 * self.price * copies_sold
        return super().royalty(copies_sold) - gst_deduction

# Example usage:
my_book = Book("The Great Novel", "John Doe", "Best Publishers", 25.99, 0.15)
print(my_book.royalty(1000))  # Calculate royalty for 1000 copies sold

my_ebook = Ebook("Ebook Magic", "Jane Smith", "Digital Press", 19.99, 0.12, "EPUB")
print(my_ebook.royalty(800))  # Calculate royalty for 800 ebook copies sold

#program completed
