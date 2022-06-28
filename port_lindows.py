import sys
import socket
from datetime import datetime



print('''
     ____    ___   ____   _____     ____   ____  _____  _   _  _   _  _____  ____  
    |  _ \  / _ \ |  _ \ |_   _|   / ___| /  __||  _  || \ | || \ | ||  ___||  _ \ 
    | |_| || | | || |_| |  | |    | |__  |  /   | | | ||  \| ||  \| || |___ | |_| |
    |  __/ | | | ||    /   | |     \__ \ | |    | |_| || |\  || |\  ||  ___||    / 
    | |    | | | || |\ \   | |        | || |    |  _  || | | || | | || |    | |\ \ 
    | |    | |_| || | | |  | |     ___| ||  \__ | | | || | | || | | || |___ | | | |
    |_|     \___/ |_| |_|  |_|    |____/  \____||_| |_||_| |_||_| |_||_____||_| |_|

****** Tool Name ::Port Scanning Tool ******
       Why This tool :: This tool Is Made for Port Scannig Windows,Linux,Termux
       Contact with Me : https://github.com/mrwnknown
    ** Donot try to Copy This. All right Reserved By MR.UNKOWN 
     ''')

print('''
01. For Windows
02. For Linux and Termux
''')

num = str(input("Enter the Number:"))


if(num == '1'):
    


    target = str(input("Target IP :"))

    print("_" * 50)
    print("Scanning Target :",target)
    print("Scannig Started At :",str(datetime.now()))
    print("_" * 50)


    try:
        for port in range(1,655535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)


            result = s.connect_ex((target,port))
            if result == 0:
                print("[*] port {} is open".format(port))
            s.close()    

    except KeyboardInterrupt:
        print("\n Exiting :(")
        sys.exit()

    except socket.error:
        print("\ Host not Responding :(")
        sys.exit()



    else:
        print("ERROR")


if(num == '2'):
    


    target = raw_input("Target IP :")

    print("_" * 50)
    print("Scanning Target :",target)
    print("Scannig Started At :",str(datetime.now()))
    print("_" * 50)


    try:
        for port in range(1,655535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)


            result = s.connect_ex((target,port))
            if result == 0:
                print("[*] port {} is open".format(port))
            s.close()    

    except KeyboardInterrupt:
        print("\n Exiting :(")
        sys.exit()

    except socket.error:
        print("\ Host not Responding :(")
        sys.exit()



    else:
        print("ERROR")

else:
        print("ERROR")        

