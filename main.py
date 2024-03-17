import subprocess
import os
from urllib.parse import urlparse
from termcolor import colored

try:
    while True:
        print(colored(""" __     ___    _        _____  _    _ _____ 
 \ \   / / |  | |      |  __ \| |  | |_   _|
  \ \_/ /| |  | |______| |__) | |__| | | |  
   \   / | |  | |______|  ___/|  __  | | |  
    | |  | |__| |      | |    | |  | |_| |_ 
    |_|   \____/       |_|    |_|  |_|_____|
                                            """, "green"))
        print(colored("                             by Timothée Guérin", "red"))
        url = input(colored("\n\n[YU-PHI] - Please enter a url: ", "yellow"))
        os.system('clear')
        print(colored(f"[YU-PHI] - Target = {url}\n", "blue"))
        domain = urlparse(url).netloc
        os.chdir("websites")
        os.mkdir(domain)
        os.chdir(domain)
        print(colored("[YU-PHI] - Your website is cloning...\n", "yellow"))
        subprocess.run(["httrack", "--mirror", url])
        print(colored("\n[YU-PHI] - A php server will be run...\n", "yellow"))
        print(colored("[YU-PHI] - Press [CTRL]+[C] to stop the php server...", "yellow"))
        subprocess.run(["php", "-S", "localhost:8000"])

        pass
except KeyboardInterrupt:
    print(colored("\n[YU-PHI] - Program is finish.", "red"))

