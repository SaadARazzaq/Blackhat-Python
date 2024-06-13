import paramiko

def ssh_command(IP, PORT, USER, PASSWD, CMD):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(IP, port= PORT, username= USER, password= PASSWD)

    _, stdout, stderr = client.exec_command(CMD)

    output = stdout.readlines() + stderr.readlines()

    if output:
        print('--- OUTPUT ---')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()

    ip = input("Enter server IP: ") or '192.168.1.203'
    port = input("Enter port or <CR>: ") or '2222'
    cmd = input("Enter command or <CR>: ") or 'id'
    ssh_command(ip, port, user, password, cmd)
