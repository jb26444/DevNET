import re

#user_name = input("Please enter your name: ")
#if not re.match("^[A-Za-z]*$", user_name):
    #print ("Error! Make sure you only use letters in your name")
#else:
    #print("Hello "+ user_name)

ipv4_address = "10.128.10.11/28"
if not re.match("^(\d{1,3}\.){3}\d{1,3}\/\d{1,2}", ipv4_address):
    print("Error! Wrong IP")
else:
    print("IPV4 " + ipv4_address)