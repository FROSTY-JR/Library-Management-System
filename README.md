# Library Management System

A simple command-line Library Management System built with Python that allows you to manage books in a library.

## Features

- **Display Books**: View all available books with their IDs and status
- **Add Books**: Add new books to the library collection
- **Issue Books**: Issue books to users with date tracking
- **Return Books**: Return issued books back to the library
- **Book Status Tracking**: Track whether books are available or issued

## Files

- `lms.py` - Main Library Management System code
- `List_of_Books.txt` - Text file containing the list of books

## How to Run

1. Make sure you have Python installed on your system
2. Clone this repository or download the files
3. Ensure both `lms.py` and `List_of_Books.txt` are in the same directory
4. Run the program:
   ```bash
   python lms.py
   ```

## Usage

When you run the program, you'll see a menu with the following options:

- **D** - Display Books: Shows all books with their IDs and availability status
- **A** - Add Books: Add a new book to the library (book name must be 25 characters or less)
- **I** - Issue Books: Issue a book to a user (requires book ID and user name)
- **R** - Return Books: Return a previously issued book (requires book ID)
- **Q** - Quit: Exit the program

## Book Collection

The library currently includes over 100 books across various genres including:
- Classic Literature (1984, Animal Farm, Pride and Prejudice)
- Modern Fiction (Gone Girl, The Silent Patient)
- Fantasy (Harry Potter, The Cruel Prince)
- Manga/Anime (Naruto, Death Note, Attack on Titan)
- Self-Help (Atomic Habits, Deep Work)
- And many more!

## Code Structure

The main `LMS` class includes:
- `__init__()` - Initializes the library with books from the text file
- `display_books()` - Shows all books and their status
- `issue_books()` - Handles book issuing with date tracking
- `add_books()` - Adds new books to the collection
- `return_books()` - Processes book returns

## Requirements

- Python 3.x
- No external dependencies required

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes!

## License

This project is open source and available under the MIT License.
