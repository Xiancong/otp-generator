from Generator.secret import get_secret
import onetimepass as otp
import pyperclip

def main():
    secret = get_secret()
    my_otp = str(otp.get_totp(my_secret))
    my_otp = my_otp.rjust(6,'0') # if otp is less than 6 digits that means that the first x digits are 0
    pyperclip.copy(my_otp) # Copy to clipboard

if __name__ == "__main__":
    main()
