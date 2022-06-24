import socket
import sys
import os

# insert helper loader
sys.path.append('/home/snydem/Documents/RomLoader/lib');
import messages

try:
    # Create the socket with which to connect
    host = '127.0.0.1';
    port = 12345;

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    server.connect((host, port));
    

    choice = '';
    while(True):
        choice = input("please choose from the following:", "[1] - ROM STATUS: print the current file tree", "[2] - ROM_UPDATE: Send a new ROM to server", "[3] - ROM CLOSE: End your connection with the server (inactivity will also cause timeout)");

        if choice == '1':
            server.send(ROM_STAT.encode());
            break;

        elif choice == '2':
            server.send(ROM_UPDT.encode());
            break;

        elif choice = '3':
            server.send(ROM_CLOS.encode());
            break;
        
        else:
            print("Your choice was unclear");
            continue;

except:
    print("unable to connect to server");

