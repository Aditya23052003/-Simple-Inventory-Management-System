import pymysql

# Connect to MySQL database
connection = pymysql.connect(host='localhost',
                             user='username',
                             password='password',
                             database='inventory_db',
                             cursorclass=pymysql.cursors.DictCursor)

# Function to add a new item to the inventory
def add_item(name, quantity, price):
    with connection.cursor() as cursor:
        sql = "INSERT INTO inventory (name, quantity, price) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, quantity, price))
    connection.commit()

# Function to view all items in the inventory
def view_items():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM inventory"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)

# Function to update details of an existing item
def update_item(id, quantity, price):
    with connection.cursor() as cursor:
        sql = "UPDATE inventory SET quantity=%s, price=%s WHERE id=%s"
        cursor.execute(sql, (quantity, price, id))
    connection.commit()

# Function to delete an item from the inventory
def delete_item(id):
    with connection.cursor() as cursor:
        sql = "DELETE FROM inventory WHERE id=%s"
        cursor.execute(sql, (id,))
    connection.commit()

# Example usage
add_item("Laptop", 10, 800)
view_items()
update_item(1, 8, 750)
delete_item(1)
