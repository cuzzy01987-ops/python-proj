
# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",       # or IP address of your MySQL server
    user="root",            # your MySQL username
    password="yourpassword",# your MySQL password
    database="world"        # database you want to use
)

# Create a cursor object
cursor = conn.cursor()



