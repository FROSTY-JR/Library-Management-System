import os
import datetime

class LMS:
    def __init__(self,list_of_books,library_name):
        self.list_of_books = "List_of_Books.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(id):{"books_title": line.replace("\n","") ,"lender_name":"","issue_data" : "","Status":"Available"}})
            id = id+1
    def display_books(self):
        print("..........................LIST OF BOOKS.......................")
        print("BOOKS ID","\t","TITLE")
        print("...............................................................")
        for key,value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "-[", value.get("Status"),"-]")
    def issue_books(self):
        books_id = input("\nEnter the book id: \n")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(f"Book Already Issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['issue_data']}")
                return self.issue_books()
            elif self.books_dict[books_id]['Status'] == "Available":
                your_name = input("Enter Your Name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['issue_data'] = current_date
                self.books_dict[books_id]['Status'] = "Issued"
                print("Books Issued Successfully!!!!!")
            else:
                print("Book ID not found!!!")
                return self.issue_books()
            
    def add_books(self):
        new_books = input("Enter the name of the book: ")
        if new_books == "":
            return self.add_books
        elif len(new_books) > 25:
            print("Books name exceeds limit (25)")
            return self.add_books
        else:
            with open(self.list_of_books , "a") as bk:
                bk.writelines(f"{new_books}")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':"", 'issue_date': "", 'Status' : "Available"}})
                print(f"The book '{new_books}' has been added successfully")
    
    def return_books(self):
        books_id = input("Enter the ID of the book to be returned: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This book already exists, please check your id")
                return return_books()
            elif not self.books_dict[books_id]['Status'] == "Available":
                self.books_dict[books_id]['lender_name'] = ""
                self.books_dict[books_id]['issue_date'] = ""
                self.books_dict[books_id]['Status'] = "Available"
                print("Succesfully returned")
            
        

try:
    mylms = LMS("List_of_Books.txt","Python's")
    press_key_list = {"D": "Display Books", "A": "Add Books" , "I": "Issue Books", "R": "Return Books","Q":"Quit"}
    key_press = False
    while not (key_press == "Q"):
        print(f"\n-----------------------Welcome To {mylms.library_name} Library Management System-----------------")
        for key, value in press_key_list.items():
            print("Print", key , "To" , value)
        key_press = input("Press Key: ").upper()
        if key_press == "I":
            print("\n Current Selection : Issue Books")
            mylms.issue_books()
        elif key_press == "A":
            print("\n Current Selection : Add Books")
            mylms.add_books()
        elif key_press == "R":
            print("\n Current Selection : Return Books")
            mylms.return_books()
        elif key_press == "D":
            print("\n Current Selection : Display Books")
            mylms.display_books()
        elif key_press == "Q":
            break
        else:
            continue
except Exception as e:
    print("Something went wrong")