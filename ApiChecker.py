# API CHECKER 
# Version 1.3
# by Luis Hernandez
# contact: luis_hernandez3357416@jabil.com

import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
from datetime import datetime


########################################################################################################################################################################

# Compute Pack CQA1	     GDLDWCQAS205
# Controller CQA1	     GDLDWCQAS204
# Controller CQA2	     GDLDWCQAS266
# Wearable CQA1	         GDLDWCQAS201
# Wearpack CQA1	         GDLDWCQAS202
# Wearpack CQA2	         GDLDWCQAS203
# Wearpack CQA3	         GDLDWCQAS207
# WBST	                 GDLDWWBST201 http://10.55.20.35/GE/v1/api/routing/routecheck?process=WBST&equipmentName=GDLDWWBST201&serialNumber=G6732T0000KC
# WETT	                 GDLNWWETT201 http://10.55.20.35/GE/v1/api/routing/routecheck?process=WETT&equipmentName=GDLNWWETT201&serialNumber=G672GT0001SB
# WFMT	                 GDLDWWFMT201 http://10.55.20.35/GE/v1/api/routing/routecheck?process=WFMT&equipmentName=GDLDWWFMT201&serialNumber=
# WITT	                 GDLDWWITT201
# WSBT	                 GDLDWWSBT201
# WSDT	                 GDLDWWSDT201
# WSMT	                 GDLDWWSMT201 http://10.55.20.35/GE/v1/api/routing/routecheck?process=WSMT&equipmentName=GDLDWWSMT201&serialNumber=G772FT0000V2
# WVBT	                 GDLDWWVBT201
# WAAT	                 GDLDWWAAT201
# WAVT	                 GDLNWWAVT201
# WETA	                 GDLNWWETA201
# WETI	                 GDLNWWETI201
# WETP	                 GDLNWWETP201
# WPAT	                 GDLDWWPAT201
# CARRY CASE LABEL	     GDLDWWPCP201
# LASER MARK CONTROL	 GDLDWTAMM201
# LASER MARK WAEARABLE   GDLDWWPMM201
# OBAT	                 GDLDWOBAS201
# WCSF	                 GDLDWWCSF201
# WUSF	                 GDLDWWUSF201


########################################################################################################################################################################
#Date
date = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))


########################################################################################################################################################################

equipment_dict = {
    "WBST":"GDLDWWBST201", 
    "WETT":"GDLNWWETT201", 
    "WFMT":"GDLDWWFMT201", 
    "WITT":"GDLDWWITT201",
    "WSBT":"GDLDWWSBT201",
    "WSDT":"GDLDWWSDT201",
    "WSMT":"GDLDWWSMT201", 
    "WVBT":"GDLDWWVBT201",
    "WAAT":"GDLDWWAAT201",
    "WAVT":"GDLNWWAVT201",
    "WETA":"GDLNWWETA201",
    "WETI":"GDLNWWETI201",
    "WETP":"GDLNWWETP201",
    "WPAT":"GDLDWWPAT201",
    "OBAT":"GDLDWOBAS201",
    "WCSF":"GDLDWWCSF201",
    "WUSF":"GDLDWWUSF201",
    "Wearpack%20CQA1%":"GDLDWCQAS202",
}





########################################################################################################################################################################


#Station configuration
with open('step.txt') as f:
    process = f.read()

equipment = equipment_dict[process] 

########################################################################################################################################################################

# WCSF testing serial number = g672xt10018s

# CQA link api = http://10.55.20.35/GE/v1/api/routing/routecheck?process=Wearpack%20CQA1%&equipmentName=GDLDWCQAS202&serialNumber=
# serial = "G772XT10001Q"

########################################################################################################################################################################

#ASCII art library
logo_art = '''
                _____ _____    _____ _    _ ______ _____ _  ________ _____        
          /\   |  __ \_   _|  / ____| |  | |  ____/ ____| |/ /  ____|  __ \       
  ______ /  \  | |__) || |   | |    | |__| | |__ | |    | ' /| |__  | |__) |_____ 
 |______/ /\ \ |  ___/ | |   | |    |  __  |  __|| |    |  < |  __| |  _  /______|
       / ____ \| |    _| |_  | |____| |  | | |___| |____| . \| |____| | \ \       
      /_/    \_\_|   |_____|  \_____|_|  |_|______\_____|_|\_\______|_|  \_\                                                                                                                                                                        
'''

pass_art = ''''
  _____         _____ _____ 
 |  __ \ /\    / ____/ ____|
 | |__) /  \  | (___| (___  
 |  ___/ /\ \  \___ \\___ \ 
 | |  / ____ \ ____) |___) |
 |_| /_/    \_\_____/_____/ 
                            
                            
'''

fail_art = '''
  ______      _____ _      
 |  ____/\   |_   _| |     
 | |__ /  \    | | | |     
 |  __/ /\ \   | | | |     
 | | / ____ \ _| |_| |____ 
 |_|/_/    \_\_____|______|
                           
                           
'''

error_art = '''
         ______ _____  _____   ____  _____        
        |  ____|  __ \|  __ \ / __ \|  __ \       
  ______| |__  | |__) | |__) | |  | | |__) |_____ 
 |______|  __| |  _  /|  _  /| |  | |  _  /______|
        | |____| | \ \| | \ \| |__| | | \ \       
        |______|_|  \_\_|  \_\_____/|_|  \_\      
                                                  
                                                  
'''

banner_art = '''

                                                        
  ______ ______ ______ ______ ______ ______ ______ ______ 
 |______|______|______|______|______|______|______|______|
                                                          
                                                                                                                      
'''

divider_art = '''->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->'''

dolphin_art = '''
                                  ,-._
                               _.-'  '--.
                             .'      _  -`\_
                            / .----.`_.'----'
                           ;/     `
                          /_;

                        ._      ._      ._      ._
                    _.-._)`\_.-._)`\_.-._)`\_.-._)`\_.-._
'''





########################################################################################################################################################################
os.system('cls' if os.name == 'nt' else 'clear')

#Home screen
print(Fore.GREEN)
print("version 1.3 // 2023 by Luis Hernandez \n")

print(Fore.CYAN)

print(divider_art)
print(dolphin_art)
print(logo_art)

print(Fore.CYAN)

print(divider_art)

print(Fore.WHITE) 

print("Estacion actual: " + Fore.GREEN + process + Fore.RESET )
input("\nPresiona Enter para empezar")

########################################################################################################################################################################

#Main Function
while True:
    #Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #Check for valid Serial Number
    print(divider_art + "\n")

    print("Estacion actual: " + Fore.GREEN + process + Fore.RESET + "\n")
    date = str(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    print("Fecha: " + Fore.GREEN + date + Fore.RESET + "\n")

    print(divider_art + "\n")
    serial = input("Ingrese el serial: ")
    print(Fore.RESET)
    print("\n" + divider_art + "\n")

    letter_counter = 0
    for letter in serial:
        letter_counter += 1

    #If valid SN is entered then run the main funciton
    if letter_counter == 12:    
        
        #Generate API url based con previous Configuration. Check HEADER
        url = "http://10.55.20.35/GE/v1/api/routing/routecheck?process=" + process + "&equipmentName=" + equipment + "&serialNumber=" + serial
        # http://mxgdlm7tis03/GE/v1/api/routing/routecheck?process=
        # http://10.55.20.35/GE/v1/api/routing/routecheck?process=
               
        #Retrieve API content
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        #Print API content.(This can be commented if not needed)
        print("\n Message: \n" )
        print(url + "\n")
        print(soup)
        print("\n\n")
        #Turn API's HTML to string
        message = str(soup)

        #Looks for the keyword "PASS" on HTML content. And locates it's index.
        status_index = message.find('PASS')

        #With that index we slice the string to obtain the keyword "PASS"
        status = message[status_index:status_index+4]
        
        
        #If the keyword "PASS" is found then we print the PASS ASCII art and we color it GREEN
        if status == "PASS":
            print(Fore.GREEN + banner_art)
            print(pass_art)
            
            print("Serial Escaneado: " + serial)
            
            print("Esta unidad SI se puede probar\n")

         
            print(banner_art)
            
        #If the keyword "PASS" is NOT found then we print the FAIL ASCII art and we color it RED   
        else:
            #Verifies if the Serial Number is real.
            error_status_index = message.find('Tester verify correct location')

            error_status = message[error_status_index:error_status_index+30]

            #If the serial number is not a real one then an ERROR alert will be printed
            if error_status == 'Tester verify correct location':

                print("Message:")
                print(f"Este serial {Fore.RED}NO{Fore.RESET} existe\n")


                print("\n\n")
                print(divider_art)

                print(Fore.MAGENTA + error_art)
                print("Message:")
            
                print(f"Este numero de serie {Fore.RED}<<{serial}>>{Fore.MAGENTA} no es valido.\nPorfavor intente de nuevo con un serial valido. \n")
                print(Fore.RESET)

                print(divider_art)
                print("\n\n")
            #If the serial number is real but shouldn't be tested in this station then a FAIL alert will be printed
            else:
                print(Fore.RED + banner_art)
                print(fail_art)
                print("Message:")
                print("Serial Escaneado: " + serial)
                print("Esta unidad NO se puede probar\n")
                print(banner_art)
            
        
       
    #If no valid serial number is found the ERROR ASCII art is printed and colored MAGENTA
    else:
        print("Message:")
        print("Serial Escaneado Erroneo: "+ Fore.RED + serial +Fore.RESET)
        print(f"Tu Serial tiene {Fore.RED}{letter_counter}{Fore.RESET} Caracteres")
        print(f"Revisa el numero de caracteres (Tienen que ser {Fore.GREEN}12{Fore.RESET})")
        
        print("\n\n")

        print(divider_art)

        print(Fore.MAGENTA + error_art)
        print("Message:")
        print(f"Este numero de serie {Fore.RED}<<{serial}>>{Fore.MAGENTA} no es valido.\nPorfavor intente de nuevo con un serial valido. \n")
        #Color is reseted to WHITE
        print(Fore.RESET)
        print(divider_art)
        print("\n\n")

    print(Style.BRIGHT + Fore.CYAN + "para escanear otro serial presione Enter\n")
    input()
    print(Fore.RESET)
    
    
########################################################################################################################################################################
  