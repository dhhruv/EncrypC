import sys 
import subprocess 
import os
# importing urllib.requests for internet cheking funtions 
import urllib.request 
  
# To check if the system is connected to the internet
def connect(host='https://google.com/'):
    try: 
        urllib.request.urlopen(host) 
        return True
    # trying to catch exception when internet is not ON. 
    except: 
        return False
package_q = ['pycryptodomex']

def setup_a(module_name): 
  
    # updating pip to latest version 
    subprocess.run('python -m pip install --upgrade pip') 
  
    # commanding terminal to pip install required modules
    p = subprocess.run('python3 -m pip3 install '+module_name) 
    
    # Not connected to the internet
    if(p.returncode == 1 and connect() == False): 
        print("Error!! occured check\nInternet Conection.") 
  
    # Every thing worked fine 
    elif(p.returncode == 0): 
        print(module_name, " is installed successfully.") 
  
    # Name of module is wrong 
    elif(p.returncode == 1 and connect() == True): 
        print("Error!! occured check\nModule Name.") 

print('Installing')
print('Please wait....')
print('Do not close this program')
for package in package_q:#sending module names to the setup_a funtion
    setup_a(package)
print('Installation finished')
subprocess.run('python3 EncrypC.py')#to run the main file