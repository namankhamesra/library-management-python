import sqlConnection
import sql_query
from admin import Admin
from user import User
from books import Book

class Library:
    def __init__(self):
        self.book_object = Book()
        self.user_object = User()
        self.admin_object = Admin()

    def issue(self,user_id):
        try:
            query = "select book_id from issued_item where User_Id = %s;"
            vals = (user_id,)
            result = sql_query.execute_query(query, vals)
            if(len(result) == 5):
                print("Limit Exceed you can not issue more than 5 books.")
            else:
                book_subject = input("Enter the subject of book which you want to issue (ex. python,java,os): ")
                query = "select book_id,book_name,author_name from book where book_name like '%"+book_subject+"%';"
                result = sql_query.execute_query(query)
                if(len(result) != 0):
                    print("These are the books related to your subject are available")
                    print("Book Id".ljust(10), "Book Name".ljust(30), "Author Name".ljust(20))
                    print("-" * 60)
                    for i in result:
                        print(str(i[0]).ljust(10),str(i[1]).ljust(30),str(i[2]).ljust(20))
                    book_id = int(input("Enter the id of book which you want to issue : "))
                    # book = books.Book()
                    if(self.book_object.check_book(book_id)):
                        query = "select quantity from book where book_id = %s;"
                        vals = (book_id,)
                        result = sql_query.execute_query(query, vals)
                        if(result[0][0] != 0):
                            query = "insert into issued_item(user_id,book_id) values (%s,%s);"
                            vals = (user_id,book_id)
                            result = sql_query.execute_query(query, vals)
                            query = "update book set quantity = quantity - 1 where book_id = %s;"
                            vals = (book_id,)
                            result = sql_query.execute_query(query, vals)
                            sqlConnection.mydb.commit()
                            print("Book issued")
                    else:
                        print("Invalid book id")
                else:
                    print("No book with your intrest is currently available.")
        except Exception as e:
            print(e)

    def return_item(self,user_id):
        try:
            no_of_book = self.my_issued_items(user_id)
            if(no_of_book != 0):
                book_id = int(input("Enter book id : "))
                # book = books.Book()
                if(self.book_object.check_book(book_id)):
                    query = "delete from issued_item where book_id = %s and user_id = %s;"
                    vals = (book_id,user_id)
                    result = sql_query.execute_query(query, vals)
                    query = "update book set quantity = quantity + 1 where book_id = %s;"
                    vals = (book_id,)
                    result = sql_query.execute_query(query, vals)
                    sqlConnection.mydb.commit()
                    print("Book Returned")
        except Exception as e:
            print(e)

    def library_menu(self):
        in_library = True
        while in_library:
            user_choice = input('''
Select your identity
    
1. User
2. Admin
3. Exit
    
Enter option : ''')
            if (user_choice == '1'):
                user_id = int(input("Enter user id : "))
                # user = User()
                if (self.user_object.check_user(user_id)):
                    self.user_object.user_menu(user_id,self)
            elif (user_choice == '2'):
                admin_id = int(input("Enter admin id : "))
                # admin = Admin()
                if (self.admin_object.check_admin(admin_id)):
                    self.admin_object.admin_menu(self)
            elif (user_choice == '3'):
                print("Thank you for using library")
                in_library = False
            else:
                print("Invalid Input")

    def my_issued_items(self,user_id):
        result = []
        try:
            query = "select book_id,book_name,author_name from book where book_id in (select book_id from issued_item where user_id = %s);"
            vals = (user_id,)
            result = sql_query.execute_query(query, vals)
            if(len(result) == 0):
                print("You don't have any books right now")
            else:
                print("Book Id".ljust(10), "Book Name".ljust(30), "Author Name".ljust(20))
                print("-" * 60)
                for i in result:
                    print(str(i[0]).ljust(10),str(i[1]).ljust(30),str(i[2]).ljust(20))
        except Exception as e:
            print(e)
        return len(result)