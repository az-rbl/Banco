from decouple import config
import psycopg2
from psycopg2 import Error

# Function to establish connection to PostgreSQL
def connect():
    try:
        connection = psycopg2.connect(
            user=config("USR"),
            password=config("PASSWORD"),  # Update with your actual password
            host=config("HOST"),
            port=config("PORT"),
            database=config("DATABASE")
        )
        return connection
    except Error as e:
        print("Error while connecting to PostgreSQL", e)
        return None

# Function to add an account
def add_account(connection, balance):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO accounts (balance) VALUES (%s) RETURNING account_id;", (balance,))
        account_id = cursor.fetchone()[0]
        connection.commit()
        print(f"Account {account_id} created successfully with balance {balance}.")
        cursor.close()
    except Error as e:
        print("Error while adding account:", e)

# Function to make a deposit
def deposit(connection, account_id, amount):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s;", (amount, account_id))
        connection.commit()
        print(f"Deposited {amount} into account {account_id}.")
        cursor.close()
    except Error as e:
        print("Error while depositing:", e)

# Function to make a withdrawal
def withdraw(connection, account_id, amount):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s;", (amount, account_id))
        connection.commit()
        print(f"Withdrew {amount} from account {account_id}.")
        cursor.close()
    except Error as e:
        print("Error while withdrawing:", e)

# Function to make a transfer
def transfer(connection, from_account, to_account, amount):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s;", (amount, from_account))
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s;", (amount, to_account))
        connection.commit()
        print(f"Transferred {amount} from account {from_account} to account {to_account}.")
        cursor.close()
    except Error as e:
        print("Error while transferring:", e)

# Main function
def main():
    connection = connect()
    if connection:
        while True:
            print("\n1. Add Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                balance = float(input("Enter initial balance: "))
                add_account(connection, balance)
            elif choice == 2:
                account_id = int(input("Enter account ID: "))
                amount = float(input("Enter deposit amount: "))
                deposit(connection, account_id, amount)
            elif choice == 3:
                account_id = int(input("Enter account ID: "))
                amount = float(input("Enter withdrawal amount: "))
                withdraw(connection, account_id, amount)
            elif choice == 4:
                from_account = int(input("Enter account ID to transfer from: "))
                to_account = int(input("Enter account ID to transfer to: "))
                amount = float(input("Enter transfer amount: "))
                transfer(connection, from_account, to_account, amount)
            elif choice == 5:
                break
            else:
                print("Invalid choice!")
        
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
