# client.py

import socket
import threading
import keyboard

# Function to send keyboard inputs to the server
def send_keys(client_socket):
    def on_key_event(event):
        client_socket.send(event.name.encode('utf-8'))

    keyboard.hook(on_key_event)
    keyboard.wait()

# Main function to connect to the server
def start_client(server_ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, 9999))
    print("Connected to server.")
    
    send_thread = threading.Thread(target=send_keys, args=(client,))
    send_thread.start()

if __name__ == "__main__":
    server_ip = input("Enter the server IP address: ")
    start_client(server_ip)
