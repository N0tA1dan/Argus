import requests

def phonelookup(number):
  print("-----------------------------------")
  print("Data Base Results For", number + "\n")
  print("https://thatsthem.com/phone/"+number)
  print("https://www.fastpeoplesearch.com/"+number)
  print("https://www.usphonebook.com/"+number)


def namelookup(fname, lname, city, state):
  print("-----------------------------------")
  print("Data Base Results For", fname, lname + "\n")

  print("https://thatsthem.com/name/"+fname + "-"+lname+"/"+city+"-"+state)


def iplookup(ipaddress):
  print("-----------------------------------")
  print("Results for", ipaddress + "\n")
  ipsearch = requests.get("http://ip-api.com/json/" + ipaddress).json()
  print("Country:", ipsearch['country'])
  print("State:", ipsearch['regionName'])
  print("City:", ipsearch['city'])
  print("Zip:", ipsearch['zip'])
  print("Latitude:", ipsearch['lat'])
  print("Longitude:", ipsearch['lon'])
  print("Timezone:", ipsearch['timezone'])
  print("ISP:", ipsearch['isp'])

def emaillookup(email):
  print("--------------------------")
  print("Results for", email + "\n")
  print("https://thatsthem.com/email/" + email)
  print("\nhttps://www.google.com/search?q=site%3Atwitter.com+intext%3A" + email)
  print("https://www.google.com/search?q=site%3Afacebook.com+intext%3A" + email)
  print("https://www.google.com/search?q=site%3Ainstagram.com+intext%3A" + email)
  print("https://www.google.com/search?q=intext%3A" + email)

def googledork():
  



print('''
 * * * * * * * * * * * * * * * *
*     _                         *
*    / \   _ __ __ _ _   _ ___  *
*   / _ \ | '__/ _` | | | / __| *
*  / ___ \| | | (_| | |_| \__ \ *
* /_/   \_\_|  \__, |\__,_|___/ *
*              |___/            *
* Argus                         *
* Coded by NotAidan             *
 * * * * * * * * * * * * * * * * 
''')

print('''
[!] Menu:
    [1] Phone Look Up - Finds information on a given phone number
    [2] Name Look Up - Finds information on a given Name
    [3] IP Look Up - Finds information on a given IP
    [4] Email Look Up - Finds information on given email
    [5] Google dorker - Probably can find anything you type in
''')

start = input("Please enter in a number: ")
print("----------------------------------------------------------------")


if(start == "1"):
  usrphone = input("Please enter a phone number in the following format (555-555-5555): ")
  phonelookup(usrphone)

if(start == "2"):
  fname = input("Please enter the FIRST name of your target: ")
  lname = input("Please enter the LAST name of your target: ")
  city = input("Enter City of your target (blank if none): ")
  state = input("Enter the state of your target (blank if none): ")
  namelookup(fname, lname, city, state)

if(start == "3"):
  usrip = input("Please enter the ip you would like to search: ")
  iplookup(usrip)


if(start == "4"):
  email = input("Please enter your targets email: ")
  emaillookup(email)
