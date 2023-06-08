# Wrapper script made in the VIRT2 module - CPNV
# Goal : Manage Proxmox LXC Containers without using the Web Interface
# Version : 1.0
# Author : David Varoso Gomes - SI-T1b

import os
import re

attacker = 102 #Container Kali
pentest = 103 #Container Pentester Lab

#Index for cloned containers -> Kali starts at 201 ; Pentest starts at 301
## Max 3 instances for the Proxmox config we have, could be augemented if needed

def perform_action(option, number ,attacker ,pentest):
    if option == "1":
        print(f"Creating {number} instances ...")
        # Perform create action here
        if number == "1":
            #Create 201 only
            for id_attacker in range(201, 202):
                print(f'Creating container {id_attacker}')
                os.system(f'pct clone {attacker} {id_attacker}')
            #Create 301 only
            for id_pentest in range(301, 302):
                print(f'Creating container {id_pentest}')
                os.system(f'pct clone {pentest} {id_pentest}')

        if number == "2":
            #Create 201 and 202
            for id_attacker in range(201, 203):
                print(f'! ! ! Creating container {id_attacker} ! ! !')
                os.system(f'pct clone {attacker} {id_attacker}')
            #Create 301 and 302
            for id_pentest in range(301, 303):
                print(f'! ! ! Creating container {id_pentest} ! ! !')
                os.system(f'pct clone {pentest} {id_pentest}')

        if number == "3":
            #Create 201 to 203
            for id_attacker in range(201, 204):
                print(f'! ! ! Creating container {id_attacker} ! ! !')
                os.system(f'pct clone {attacker} {id_attacker}')
            #Create 301 to 303
            for id_pentest in range(301, 304):
                print(f'! ! ! Creating container {id_pentest} ! ! !')
                os.system(f'pct clone {pentest} {id_pentest}')

    elif option == "2":
        print(f"Starting {number} instances ...")
        # Perform start action here
        if number == "1":
            for id_attacker in range(201, 202):
                print(f'Starting container {id_attacker}')
                os.system(f'pct start {id_attacker}')
            for id_pentest in range(301, 302):
                print(f'Starting container {id_pentest}')
                os.system(f'pct start {id_pentest}')

        if number == "2":
            for id_attacker in range(201, 203):
                print(f'Starting container {id_attacker}')
                os.system(f'pct start {id_attacker}')
            for id_pentest in range(301, 303):
                print(f'Starting container {id_pentest}')
                os.system(f'pct start {id_pentest}')

        if number == "3":
            for id_attacker in range(201, 204):
                print(f'Starting container {id_attacker}')
                os.system(f'pct start {id_attacker}')
            for id_pentest in range(301, 304):
                print(f'Starting container {id_pentest}')
                os.system(f'pct start {id_pentest}')

        user_ip = input ("Show IPs ? Y/N : ")
        show_ip(user_ip)

    elif option == "3":
        print(f"Stopping {number} instances ...")
        # Perform stop action here
        if number == "1":
            for id_attacker in range(201, 202):
                print(f'Stopping container {id_attacker}')
                os.system(f'pct stop {id_attacker}')
            for id_pentest in range(301, 302):
                print(f'Stopping container {id_pentest}')
                os.system(f'pct stop {id_pentest}')

        if number == "2":
            for id_attacker in range(201, 203):
                print(f'Stopping container {id_attacker}')
                os.system(f'pct stop {id_attacker}')
            for id_pentest in range(301, 303):
                print(f'Stopping container {id_pentest}')
                os.system(f'pct stop {id_pentest}')

        if number == "3":
            for id_attacker in range(201, 204):
                print(f'Stopping container {id_attacker}')
                os.system(f'pct stop {id_attacker}')
            for id_pentest in range(301, 304):
                print(f'Stopping container {id_pentest}')
                os.system(f'pct stop {id_pentest}')

    elif option == "4":
        print(f"Destroying {number} instances ...")
        # Perform destroy action here
        if number == "1":
            for id_attacker in range(201, 202):
                print(f'Destroying container {id_attacker}')
                os.system(f'pct destroy {id_attacker}')
            for id_pentest in range(301, 302):
                print(f'Destroying container {id_pentest}')
                os.system(f'pct destroy {id_pentest}')

        if number == "2":
            for id_attacker in range(201, 203):
                print(f'Destroying container {id_attacker}')
                os.system(f'pct destroy {id_attacker}')
            for id_pentest in range(301, 303):
                print(f'Destroying container {id_pentest}')
                os.system(f'pct destroy {id_pentest}')

        if number == "3":
            for id_attacker in range(201, 204):
                print(f'Destroying container {id_attacker}')
                os.system(f'pct destroy {id_attacker}')
            for id_pentest in range(301, 304):
                print(f'Destroying container {id_pentest}')
                os.system(f'pct destroy {id_pentest}')

    else:
        print("Invalid option!")

user_option = input("Enter an option (1. create, 2. start, 3. stop, 4. destroy): ")
user_number = input("Enter the number of instances\n Chose : 1-3 : ")

def show_ip(ip):
    if ip == "Y":
        print('Loading IPs')
        output = os.popen('lxc-ls -f').read()
        pattern = r"(\S+)\s+RUNNING\s+\S+\s+-\s+(\S+)"
        matches = re.findall(pattern, output)
        for match in matches:
            container_name, ip_address = match
            print(f"Name: {container_name}, IP Address: {ip_address}")
    if ip == "N":
        print('Alright sure')

################################################

perform_action(user_option, user_number,attacker ,pentest)
