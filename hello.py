# create function to print general menu
def print_menu():
    print("""Choose an option:
    1. print all books
    2. add a book
    3. update a book
    4. delete a book
    """)

while True:
    print_menu()
    response = int(input())
    if response == 1:
        print("Printing all books now")
    elif response == 2:
        print("Adding a book")
    elif response == 3:
        print("Updating book now")
    elif response == 4:
        print("Deleting book now")
    else:
        print("Thanks for using our app")
        break
       