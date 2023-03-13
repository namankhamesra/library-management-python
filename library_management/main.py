from library import Library
import sqlConnection

if __name__ == '__main__':
    library = Library()
    library.library_menu()
    sqlConnection.mydb.close()