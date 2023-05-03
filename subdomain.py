import os,requests,sys,time
black="\033[1;90m"
white="\033[1;97m"
red="\033[1;91m"
green="\033[1;92m"
yellow="\033[1;93m"
blue="\033[1;94m"
purple="\033[1;95m"
cyan="\033[1;96m"  
rst="\033[0m"

os.system("clear")

def animetion (text):
  for i in text:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.005)
    
    
    
banner = f'''   {red}_____ _______           __         
  {yellow}/ ___// ____(_)___  ____/ /__  _____
  {green}\__ \/ /_  / / __ \/ __  / _ \/ ___/
 {blue}___/ / __/ / / / / / /_/ /  __/ /    
{purple}/____/_/   /_/_/ /_/\__,_/\___/_/      \n'''

details = f"""
{green}       Author   : Macgaiver
       Github   : https://github.com/macgaiver11996
       Telegram : t.me/M4C641V3R{rst}
       """
           

symbol = f"{green}\n****************************************************************{rst}"

animetion (banner)
animetion (details)
animetion (symbol)


site = input(f"{yellow}[*] Enter Your Terget Site: ")
replace = site.replace("https://",'').replace("http://",'').replace("/",'')

url = f"https://api.hackertarget.com/hostsearch/?q={site}"
response = requests.get(url)
if response.status_code == 200:
  subdomains = response.text
  print (f"{green}{subdomains}")
else:
  print(f"{red}{'Domain Not Found'}")