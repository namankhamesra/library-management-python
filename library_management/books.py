import sqlConnection
import sql_query

class Book:
    def __init__(self,book_name=None,author_name=None,quantity=None):
        self.book_name = book_name
        self.author_name = author_name
        self.quantity = quantity

    def check_book(self,book_id):
        bookFound = False
        query = "Select * from book where book_id = %s;"
        vals = (book_id,)
        result = sql_query.execute_query(query,vals)
        if(len(result) != 0):
            return True
        else:
            return False

    def update_book_quantity(self,quantity,book_id):
        if(self.check_book(book_id)):
            try:
                if(quantity>0):
                    query = "update book set quantity = quantity + %s where book_id = %s;"
                    vals = (quantity,book_id)
                    result = sql_query.execute_query(query,vals)
                    sqlConnection.mydb.commit()
                    print("Quantity updated successfully")
                else:
                    print("Invalid Quantity")
            except Exception as e:
                print(e)
        else:
            return

    def add_new_book(self):
        try:
            query = "insert into book(Book_Name,Author_Name,Quantity) values (%s,%s,%s);"
            vals = (self.book_name,self.author_name,self.quantity)
            result = sql_query.execute_query(query,vals)
            sqlConnection.mydb.commit()
        except Exception as e:
            print(e)
        else:
            print("Book added successfully.")

    def display_books(self):
        try:
            result = sql_query.execute_query("select * from book;")
            print("Book Id".ljust(10), "Book Name".ljust(30), "Author Name".ljust(20), "Quantity".ljust(0))
            print("-"*75)
            for i in result:
                print(str(i[0]).ljust(10),str(i[1]).ljust(30),str(i[2]).ljust(20),str(i[3]).ljust(0))
        except Exception as e:
            print(e)