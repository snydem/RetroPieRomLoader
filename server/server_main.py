import socket
import sys
import os

# insert helper loader
sys.path.append('/home/snydem/Documents/RomLoader/lib');
import messages

try:
    # Create the socket for which communication will occur
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
except:
    print("Creation of the listener socket failed")
    sys.exit(1);

# find a port number for the listener
port = 12345

# bind the port to the listener
listener.bind(('', port));
print ("listener bound to %s" %(port));

# Start a forever loop to accept clients
while True:
    # Listen for connection (this is a blocking call)
    listener.listen(5);
    print("LISTENING...");

    # Establish connection with the client
    client, addr = listener.accept();
    print('connection received from: ', addr);
    
    # Send back connection confimation
    client.send('ACCEPTED'.encode());

    # Await command from client
    rec_string = client.recv(4096).decode();

    command = rec_string[0:8];


    # The case that the client wants to send us a ROM to load to the pi
    if command == "ROM UPDATE":
        print("received ROM UPDATE command from client");

        # The case that the client just wants to see what ROMS currently exist on the pi
    elif command == "ROM STATUS":
        print("received ROM STATUS command from client");

        # Print the ROM file structure to show the user which ROMS are present on the machine
        os.listdir(path='.')
            
    else:
        print("unrecognized command:" + str(command));
