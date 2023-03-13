import sqlConnection
import sql_query

class Admin:
    def __init__(self,admin_name=None,admin_password=None):
        self.admin_name = admin_name
        self.admin_password = admin_password

    def check_admin(self,admin_id):
        admin_found = False
        query = "Select admin_id from admin;"
        result = sql_query.execute_query(query)
        for i in result:
            if (i[0] == admin_id):
                admin_found = True
                admin_password = input("Enter your password : ")
                query = "select admin_password from admin where admin_id = %s;"
                vals = (admin_id,)
                password = sql_query.execute_query(query,vals)
                if (password[0][0] == admin_password):
                    return True
                else:
                    print("Incorrect Password")
        if (not admin_found):
            print("Admin with id", admin_id, "not found.")
            return False

    def admin_menu(self,library):
        inAdmin = True
        while inAdmin:
            user_choice = input('''
What do you want to do..

1. Add new admin
2. Update book quantity
3. Add new book to library
4. Add new user
5. Display books
6. Go back

Enter your choice : ''')
            if (user_choice == '1'):
                self.admin_name = input("Enter admin name : ")
                self.admin_password = input("Enter password : ")
                self.add_new_admin()
            elif (user_choice == '2'):
                print("These are the books present in our library.")
                # book = Book()
                library.book_object.display_books()
                book_id = int(input("Enter book id : "))
                quantity = int(input("Enter quantity : "))
                # book = Book()
                library.book_object.update_book_quantity(quantity,book_id)
            elif (user_choice == '3'):
                book_name = input("Enter book name : ")
                author_name = input("Enter author name : ")
                quantity = input("Enter quantity : ")
                # book = Book(book_name,author_name,quantity)
                library.book_object.book_name = book_name
                library.book_object.author_name = author_name
                library.book_object.quantity = quantity
                library.book_object.add_new_book()
            elif (user_choice == '4'):
                user_name = input("Enter user name : ")
                user_password = input("Enter password : ")
                # user = User(user_name,user_password)
                library.user_object.user_name = user_name
                library.user_object.user_password = user_password
                library.user_object.add_new_user()
            elif(user_choice == '5'):
                # book = Book()
                library.book_object.display_books()
            elif (user_choice == '6'):
                inAdmin = False
            else:
                print("Invalid choice")

    def add_new_admin(self):
        try:
            query = "select admin_id from admin order by admin_id desc limit 1"
            result = sql_query.execute_query(query)
            if (len(result) != 0):
                print("Your id is", result[0][0] + 1, "please remember this.")
            else:
                print("Your id is 101 please remember this.")
            query = "insert into admin(Admin_Name,Admin_Password) values (%s,%s);"
            vals = (self.admin_name,self.admin_password)
            result = sql_query.execute_query(query,vals)
            sqlConnection.mydb.commit()
        except Exception as e:
            print(e)
        else:
            print("Admin created successfully")