import json
from difflib import get_close_matches

jsonfile = json.load(open("users.json"))

print()
name = input("Enter your name: ")
print()


print("Welcome to Software Service Provider LTD, Welcome MR.",name.upper())
print()

def repeat():
    print()
    ap = input("Are u need a developer? if yes means 'y' or no means 'n'! ")
    print()

    if ap == 'y' or ap == 'Y':
        print("1. Backend")
        print("2. Frontend")
        print("3. Database")
        print("4. UI/UX")
        print("5. App")
        print("6. Game")
        print()

        def repeat1():
            print()
            a = input("Enter an domain which given in option above: ")
            print()
            def check(d):
                d = d.lower()
                if d in jsonfile:
                    return jsonfile[d]
                elif len(get_close_matches(d,jsonfile.keys()))>0:
                        choice = input("Did you mean %s,Enter yes means 'Y' or no means 'N' "%get_close_matches(d,jsonfile.keys()))
                        print()
                        if choice == 'y' or choice == 'Y':
                            return jsonfile[get_close_matches(d,jsonfile.keys())[0]]
                        elif choice == 'n' or choice == 'N':
                            r = "Enter a correct option above "
                            print(r)
                            repeat1()
                        else:
                            r1 = "You entered wrong option"
                            print(r1)
                            repeat1()
                else:
                    r2 = "You entered a wrong value"
                    print(r2)
                    repeat1()

            result = (check(a))
            if type(result) == dict:
                for key, value in result.items():
                    print(key, ':', value)
            else:
                print(result)

        repeat1()
        print()
        print("Thank you ,Help us by giving your valuable feedback")
        print()


        def rating():
            print()
            rate = input("Rate a experience with us,from 1 to 5 ! ")
            print()
            if rate == '1' or rate == '2':
                print("Thank you ,visit again")
            elif rate == '3' or rate == '4':
                print("Thanks for ur valuable feedback , We will improve that")
            elif rate == '5':
                print("Thanks for ur valuable feedback, Hope it helpful")
            else:
                print("Sorry invalid ratings,please rate ur experience from 1 to 5")
                rating()

        rating()

    elif ap == 'n' or ap == 'N':
        print("If anything needed visit us ,Thank you")
    else:
        print("You entered wrong, Please enter Y or N")
        repeat()

repeat()

