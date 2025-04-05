import os

class PersonalLibraryManager:
    def __init__(self):
        self.library = []
        self.load_library()

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        publication_year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ")
        read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'
        book = {
            "Title": title,
            "Author": author,
            "Publication Year": publication_year,
            "Genre": genre,
            "Read Status": read_status
        }
        self.library.append(book)
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        for book in self.library:
            if book["Title"].lower() == title.lower():
                self.library.remove(book)
                print("Book removed successfully!")
                return
        print("Book not found.")

    def search_book(self):
        print("Search by: \n1. Title\n2. Author")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter the title: ")
            matches = [book for book in self.library if title.lower() in book["Title"].lower()]
        elif choice == '2':
            author = input("Enter the author: ")
            matches = [book for book in self.library if author.lower() in book["Author"].lower()]
        else:
            print("Invalid choice.")
            return

        if matches:
            print("Matching Books:")
            for idx, book in enumerate(matches, 1):
                print(f"{idx}. {book['Title']} by {book['Author']} ({book['Publication Year']}) - {book['Genre']} - {'Read' if book['Read Status'] else 'Unread'}")
        else:
            print("No matching books found.")

    def display_books(self):
        if not self.library:
            print("No books in the library.")
        else:
            print("Your Library:")
            for idx, book in enumerate(self.library, 1):
                print(f"{idx}. {book['Title']} by {book['Author']} ({book['Publication Year']}) - {book['Genre']} - {'Read' if book['Read Status'] else 'Unread'}")

    def display_statistics(self):
        total_books = len(self.library)
        if total_books == 0:
            print("No books in the library.")
        else:
            read_books = sum(1 for book in self.library if book['Read Status'])
            percentage_read = (read_books / total_books) * 100
            print(f"Total books: {total_books}")
            print(f"Percentage read: {percentage_read:.2f}%")

    def save_library(self):
        with open("library.txt", "w") as file:
            for book in self.library:
                file.write(f"{book['Title']}|{book['Author']}|{book['Publication Year']}|{book['Genre']}|{book['Read Status']}\n")
        print("Library saved to file.")

    def load_library(self):
        if os.path.exists("library.txt"):
            with open("library.txt", "r") as file:
                for line in file:
                    title, author, publication_year, genre, read_status = line.strip().split("|")
                    self.library.append({
                        "Title": title,
                        "Author": author,
                        "Publication Year": int(publication_year),
                        "Genre": genre,
                        "Read Status": read_status.lower() == 'true'
                    })

    def menu(self):
        while True:
            print("\nMenu")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                self.display_statistics()
            elif choice == '6':
                self.save_library()
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library_manager = PersonalLibraryManager()
    library_manager.menu()
