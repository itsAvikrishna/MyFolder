print()
print("ADMIN EMPLOYEE ENTRY SYSTEM")


def login():
    print()
    admin = input("Enter your name: ")
    print()
    password = input("Enter your password: ")
    print()
    if admin == "avikrishna" and password == "Ak2001@":
        print("Welcome, Admin")
        print()
        print("Register form")

        def detail():
            print()
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            experience = input("Enter Experience: ")
            rating = input("Enter Rating in alphanum: ")
            contact = input("Enter Phone number: ")
            address = input("Enter Place: ")
            print()
            print("Please verify the Data")
            print()
            print("Name: ", name)
            print("Age: ", age)
            print("Gender: ", gender)
            print("Experience: ", experience)
            print("Rating: ", rating)
            print("Contact: ", contact)
            print("address: ", address)
            print()

            def option():
                print()
                a = input("If you entered wrong, fill again, if yes means 'Y' or no means 'N'! ")
                print()
                if a == 'y' or a == 'Y':
                    print("Fine , you can fill the form")
                    detail()
                elif a == 'n' or a == 'N':
                    print("Okay, Details attached")
                else:
                    print("you enter wrong value")
                    option()

            option()

        detail()
    elif admin == "avikrishna" and password != "Ak2001@":
        print("your password is wrong, kindly verify")
        login()
    elif admin != "avikrishna" and password == "Ak2001@":
        print("you entered user name is not correct, kindly verify")
        login()
    else:
        print("Sorry invalid user")
        login()


login()
