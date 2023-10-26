'''Ally Greenberg: encode function/menu function/main function'''
def encoder(password):
    global encoded_string
    encoded_string = ""
    for each in password:
        x = int(each)
        x += 3
        a = str(x)
        encoded_string
        encoded_string += a
    return encoded_string


# decode function by Anna Wheeler
def decode(encoded_string):
    decoded_string = ''

    # iterates through string subtracting 3 from each digit
    for digit in encoded_string:
        num = int(digit)
        num -= 3
        str_num = str(num)
        decoded_string += str_num

    # returns decoded string
    return decoded_string


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
            encoded_sting = encoder(user_pass)
            print("Your password has been encoded and stored!\n")

        elif option == "2":
            print(f"The encoded password is {encoder(user_pass)}, and the original password is {decode(encoded_string)}.\n")

        else:
            running = False

if __name__ == '__main__':
    main()
