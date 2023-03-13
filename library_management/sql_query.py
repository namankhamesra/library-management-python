import sqlConnection
def execute_query(query,values=None):
    try:
        if(values == None):
            sqlConnection.myCursor.execute(query)
            result = sqlConnection.myCursor.fetchall()
        else:
            sqlConnection.myCursor.execute(query,values)
            result = sqlConnection.myCursor.fetchall()
    except Exception as e:
        print(e)
    else:
        return result