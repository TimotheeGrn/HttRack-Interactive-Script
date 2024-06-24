import subprocess
import os
from urllib.parse import urlparse
from termcolor import colored

try:
    while True:
        print(colored("""'
 ||'  '||' '||'  .|'''.|  
 ||    ||   ||   ||..  '  
 ||''''||   ||    ''|||.  
 ||    ||   ||  .     '|| 
.||.  .||. .||. |'....|'
HttRack Interactive Script""", "green"))
        print(colored("                            by the PTCW Team", "red"))
        url = input(colored("\n\n[HIS] - Please enter a URL (including http:// or https://): ", "yellow"))
        
        # Verif de l'url
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            print(colored("[HIS] - Invalid URL. Please include the scheme (http:// or https://)", "red"))
            continue

        if not os.path.exists("websites"):
            os.makedirs("websites")
        
        os.system('clear')
        print(colored(f"[HIS] - Target = {url}\n", "blue"))
        
        domain = parsed_url.netloc
        if not domain:
            print(colored("[HIS] - Invalid URL. Could not parse domain.", "red"))
            continue
        
        # Créer le path du site web
        path = f"websites/{domain}/"
        os.makedirs(path, exist_ok=True)
        
        os.chdir(path)
        print(colored("[HIS] - Your website is cloning...\n", "yellow"))
        
        # Lancer httrack
        subprocess.run(["httrack", "--mirror", url])
        print(colored(f"\n[HIS] - {url} has been cloned to the directory {path}\n", "yellow"))
        break
except KeyboardInterrupt:
    print(colored("\n[HIS] - Program is finish.", "red"))
