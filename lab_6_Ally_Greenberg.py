'''Ally Greenberg: encode function/menu function/main function'''
def encoder(password):
    encoded_string = ""
    for each in password:
        x = int(each)
        x += 3
        a = str(x)
        encoded_string += a
    return encoded_string

def menu():
    print("Menu")
    print("-" * 13)
    print("1. Encode\n2. Decode\n3.Quit")

def main():

    running = True

    while running:
        menu()
        option = input("Please enter an option: ")

        if option == "1":
            user_pass = input("Please enter your password to encode: ")
            encoder(user_pass)
            print("Your password has been encoded and stored!\n")

        else:
            running = False

        '''elif option == "2":
            print(f"The encoded password is {encoder(user_pass)}, and the original password is {user_pass}.\n")
        '''

if __name__ == '__main__':
    main()
