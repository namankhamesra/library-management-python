import sqlConnection
import sql_query

class User:
    def __init__(self,user_name=None,user_password=None):
        self.user_name = user_name
        self.user_password = user_password

    def check_user(self,user_id):
        user_found = False
        query = "Select user_id from user;"
        result = sql_query.execute_query(query)
        for i in result:
            if (i[0] == user_id):
                user_found = True
                user_password = input("Enter password : ")
                query = "select user_password from user where user_id = %s;"
                vals = (user_id,)
                password = sql_query.execute_query(query,vals)
                if (password[0][0] == user_password):
                    return True
                else:
                    print("Incorrect Password")
        if (not user_found):
            print("User with id", user_id, "not found.")
            return False

    def user_menu(self,user_id, library):
        in_user = True
        while in_user:
            user_choice = input('''
What do you want to do..
    
1. Issue book
2. Return book
3. Display available books
4. Display my issued books
5. Go back
    
Enter your choice : ''')
            if(user_choice == '1'):
                library.issue(user_id)
            elif(user_choice == '2'):
                library.return_item(user_id)
            elif(user_choice == '3'):
                # book = Book()
                library.book_object.display_books()
            elif(user_choice == '4'):
                temp = library.my_issued_items(user_id)
            elif(user_choice == '5'):
                in_user = False
            else:
                print("Invalid Choice")

    def add_new_user(self):
        try:
            query = "select user_id from user order by user_id desc limit 1"
            result = sql_query.execute_query(query)
            if(len(result) != 0):
                print("Your id is",result[0][0]+1,"please remember this.")
            else:
                print("Your id is 101 please remember this.")
            query = "insert into user(User_Name,user_password) values (%s,%s);"
            vals = (self.user_name,self.user_password)
            result = sql_query.execute_query(query,vals)
            sqlConnection.mydb.commit()
        except Exception as e:
            print(e)
        else:
            print("User added successfully")