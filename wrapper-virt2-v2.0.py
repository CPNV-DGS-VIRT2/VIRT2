# Wrapper script made in the VIRT2 module - CPNV
# Goal : Manage Proxmox LXC Containers without using the Web Interface
# Version 2.0
# Author : David Varoso Gomes - SI-T1b

import os
import re

attacker = 102 # Template Attacker
pentest = 103 # Template Pentester Lab
# Index for cloned containers
index_attacker = 201 # Kali starts at 201
index_pentest = 301  # Pentest starts at 301
# Asking what the user wants to do with an input
user_option = input("Enter an option (1. create, 2. start, 3. stop, 4. destroy, 5. Show IPs): ") 
# Max 1-3 because of the proxmox configuration, the script can scale as high as you want
user_number = input("Enter the number of instances\n Not needed for the 5th option, just use 0 \n Chose : 1-3 : ") 
counter = int(user_number)

#Main function
def perform_action(option,number,attacker,pentest,index_attacker,index_pentest,counter):
    if option == "1":
        print(f" >> Creating {number} instances << ")
        # Perform create action here

        for id_attacker in range(index_attacker, index_attacker+int(counter)):
                print(f' > Creating container {id_attacker} < ')
                #print (f'pct clone {attacker} {id_attacker}')
                os.system(f'pct clone {attacker} {id_attacker}')

        for id_pentest in range(index_pentest, index_pentest+int(counter)):
                print(f' > Creating container {id_pentest} < ')
                #print (f'pct clone {pentest} {id_pentest}')
                os.system(f'pct clone {pentest} {id_pentest}')
        
        # Start after create feature
        user_option = input (" > Start created containers ? Y/N : ")
        start_after_create(user_option)

    elif option == "2":
        print(f" >> Starting {number} instances ... << ")
        # Perform start action here

        for id_attacker in range(index_attacker, index_attacker+int(counter)):
                print(f' > Starting container {id_attacker} < ')
                #print (f'pct start {id_attacker}')
                os.system(f'pct start {id_attacker}')

        for id_pentest in range(index_pentest, index_pentest+int(counter)):
                print(f' > Starting container {id_pentest} < ')
                #print (f'pct start {id_pentest}')
                os.system(f'pct start {id_pentest}')

        user_ip = input (" > Show IPs ? Y/N : ")
        show_ip(user_ip)

    elif option == "3":
        print(f" >> Stopping {number} instances ... << ")
        # Perform stop action here

        for id_attacker in range(index_attacker, index_attacker+int(counter)):
                print(f' > Stopping container {id_attacker} < ')
                #print (f'pct stop {id_attacker}')
                os.system(f'pct stop {id_attacker}')

        for id_pentest in range(index_pentest, index_pentest+int(counter)):
                print(f' > Stopping container {id_pentest} < ')
                #print (f'pct stop {id_pentest}')
                os.system(f'pct stop {id_pentest}')

    elif option == "4":
        print(f" >> Destroying {number} instances ... << ")
        # Perform destroy action here

        for id_attacker in range(index_attacker, index_attacker+int(counter)):
                print(f' > Destroying container {id_attacker} < ')
                #print (f'pct destroy {id_attacker}')
                os.system(f'pct stop {id_attacker}')
                os.system(f'pct destroy {id_attacker}')

        for id_pentest in range(index_pentest, index_pentest+int(counter)):
                print(f' > Destroying container {id_pentest} < ')
                #print (f'pct destroy {id_pentest}')
                os.system(f'pct stop {id_pentest}')
                os.system(f'pct destroy {id_pentest}')
                
    elif option == "5":
        # Showing IPs on menu if it didn't work properly on the start
        print(' >>> Loading IPs <<< ')
        #print(f"[ Username : root ; Password : Pa$$w0rd ]")
        output = os.popen('lxc-ls -f').read()
        pattern = r"(\S+)\s+RUNNING\s+\S+\s+-\s+(\S+)"
        matches = re.findall(pattern, output)
        for match in matches:
            container_name, ip_address = match
            print(f"[Name] : {container_name} [IP Address] : {ip_address}")
        
    else:
      print("Invalid option!")

#Function to show the IPs of the new containers and the login
def show_ip(ip):
    if ip == "Y":
        print(' >>> Loading IPs <<< ')
        #print(f"[ Username : root ; Password : Pa$$w0rd ]")
        output = os.popen('lxc-ls -f').read()
        pattern = r"(\S+)\s+RUNNING\s+\S+\s+-\s+(\S+)"
        matches = re.findall(pattern, output)
        for match in matches:
            container_name, ip_address = match
            print(f"[Name] : {container_name} [IP Address] : {ip_address}")
    if ip == "N":
        print('Alright sure')

def start_after_create(option):
    if option == "Y":
      print (' >> Starting << ')
      
      for id_attacker in range(index_attacker, index_attacker+int(counter)):
        print(f' > Starting container {id_attacker} < ')
        #print (f'pct start {id_attacker}')
        os.system(f'pct start {id_attacker}')
      for id_pentest in range(index_pentest, index_pentest+int(counter)):
        print(f' > Starting container {id_pentest} < ')
        #print (f'pct start {id_pentest}')
        os.system(f'pct start {id_pentest}')
      
      if option == "N":
        print(' > You can also start them with the option 2 of the menu < ')

#Execution of the main function
perform_action(user_option,user_number,attacker,pentest,index_attacker,index_pentest,counter)
