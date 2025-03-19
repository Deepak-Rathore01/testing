import mysql.connector

# Database connection details
host = "localhost"  # Since you're on the same machine, use localhost
user = "deepak"  # Your MariaDB user
password = "password"  # Your password
database = "DEEPAK"  # Your database name

connection = None  # Initialize connection variable

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    if connection.is_connected():
        print("Successfully connected to the database")
        
        # Create a cursor object and perform database operations
        cursor = connection.cursor()
        
        # Example query: Fetching all records from a table
        cursor.execute("SHOW TABLES")  # This will list all tables in the DEEPAK database
        result = cursor.fetchall()
        print("Tables in the database:")
        for row in result:
            print(row)
        cursor.execute("select * from EMPLOYEE")
        result= cursor.fetchall()
        print("the employee table is:")
        for row in result:
            print(row)
	


except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection and connection.is_connected():
        connection.close()  # Close the connection
        print("Connection closed")

