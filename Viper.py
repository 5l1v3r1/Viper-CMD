import os
import sys
import subprocess
import socket
import shutil
import urllib
import base64
import Overwrite
import commands
import tc
import pyxhook
#import pygame
from os import listdir
from os.path import isfile, join

class Vipercmd(object):

    def __init__(self):
        self.cmd = ''
        self.done = False

    def cmd_loop(self):
        while not self.done:
            commands.Command().event_loop()

    def greet(self):
        print(tc.tcolors.WARNING + "hi" + tc.tcolors.ENDC)

    def help(self):
        print('Current list of commands: greet, portscan, honeypot,'
              ' listcd, dirchange, dl, listf, remf, autocleanup, clean_trash, remdir, readf, runf, sechash, b64, monitor, exit')

    def keyboard_m(self):
       os.system('python keyboardmonitor.py')
       
    #def playmusic(self):
        #Works in Windows.
        #To-do add list.
        #pygame.init()
        #pygame.mixer.pre_init(44100, -16, 2, 128)
        #print(tc.tcolors.SYNTAX + 'Type the name of the song name with extension. ex: song.ogg' + tc.tcolors.ENDC)
        #print(tc.tcolors.WARNING + 'WARNING: Needs to be in same directory.' + tc.tcolors.ENDC)
        #try: 
            #music = input('What music would you like to play? ')
            #pygame.mixer.music.load(music)
            #pygame.mixer.music.play()
        #except pygame.error:
            #print(tc.tcolors.SYNTAX + 'No song with that name in this directory.' + tc.tcolors.ENDC)

    #Security Functions.
    #---------------------------------------------------------------------
    def portscan(self):
        try:
            server_address = int(input("Enter a remote host: "))
            remoteconnectionIP = socket.gethostbyname(server_address)
            for port in range(1,1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteconnectionIP, port))
                if result == 0:
                    print(tc.tcolors.SYNTAX + "Port {}: \t Open".format(port) + tc.tcolors.ENDC)
                    sock.close()
                    return
        except socket.error:
            print(tc.tcolors.SYNTAX + "Couldn't connect to server!" + tc.tcolors.ENDC)
        except socket.gaierror:
            print(tc.tcolors.SYNTAX + "Invalid address!" + tc.tcolors.ENDC)
        except ValueError:
            print(tc.tcolors.SYNTAX + "Invalid input value!" + tc.tcolors.ENDC)

    def honeypot(sock, server_address):

       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       server_address = ('', 22)
       try:
           sock.bind(server_address)
       except socket.error:
           print(tc.tcolors.SYNTAX + "Socket error, sudo run Viper or change ports." + tc.tcolors.ENDC)
       else:
           while True:
               print('starting up on', server_address, file = sys.stderr)
               sock.getsockname()
               sock.listen(1)
               print('waiting for a connection from sneaky mofackles.', file = sys.stderr)
               connection, client_address = sock.accept()
               compname = socket.gethostname()
               try:
                   print('client connected:', client_address, file = sys.stderr)
                   print('Computer name:', compname, file = sys.stderr)
                   while True:
                       connection.send(bytes('Jokes on you.', 'UTF-8'))
                       data = connection.recv(16)
                       print('recieved "%s"', data, file = sys.stderr)
                       if data:
                           connection.sendall(data)
                           f = open("person.txt", "a")
                           f.write(str("\n"))
                           f.write(str(connection))
                           f.write(str(client_address))
                           f.write(str(compname))
                           f.close()

                       else:
                           break

               finally:
                   print('restarting')

    def netping(self):
        print('Pinging network ips')
        for ping in range(1,10):
            ip = '127.0.0.' + str(ping)
            resp = subprocess.call(['ping', '-c', '3', ip])
            if resp == 0:
                print('pinging', ip, 'OK')
            elif resp == 2:
                print('no response from', ip)
            else:
                print('pinging', ip, 'NO!')

	#File and Navigation functions --------------------------------------

    def dl(self):
       print(tc.tcolors.SYNTAX + 'Downloads file to Viper directory.' + tc.tcolors.ENDC)
       try:
           web = input('What is the url?')
           files = input('What file?')
           urllib.urlretrieve(web,files)
       except IOError:
           print(tc.tcolors.SYNTAX + 'File does not exist or url.' + tc.tcolors.ENDC)
       except AttributeError:
           print(tc.tcolors.SYNTAX + 'File does not exist or url may have been mistyped.' + tc.tcolors.ENDC)
       else:
           print(tc.tcolors.SUCCESS + 'File downloaded!' + tc.tcolors.ENDC)

    def runf(self):
        print('If executing C or C++ program put ./ for Bash or Perl sh in front of file name.')
        #C and Bash work so far.
        f = subprocess.call(raw_input("Which file would you like to run? :"), shell=True)
            			
    def autocleanup(self):
       print(tc.tcolors.WARNING + "Only works on Debian or Arch Linux type distros." + tc.tcolors.ENDC)
       clean = 'sh ./Cleanup.sh'
       try:
           subprocess.call(clean, shell = True)
           print(tc.tcolors.SUCCESS + "Finished system cleanup!" + tc.tcolors.ENDC)
       except:
       	   print(tc.tcolors.WARNING + "Not a Debian or Arch Linux distro?" + tc.tcolors.ENDC)

    def clean_trash(self):
       print(tc.tcolors.WARNING + "Only works on Debian or Arch Linux type distros." + tc.tcolors.ENDC)
       t = 'sh ./cleantrash.sh'
       try:
           subprocess.call(t, shell = True)
           print(tc.tcolors.SUCCESS + "Finished trashbin cleanup!" + tc.tcolors.ENDC)
       except:
           print(tc.tcolors.WARNING + "Not a Debian or Arch Linux distro?" + tc.tcolors.ENDC)

    def nautilus(self):
       print(tc.tcolors.WARNING + "Only works on Debian and Arch Linux type distros." + tc.tcolors.ENDC)
       o = 'sh ./opennautilus.sh'
       try:
           subprocess.call(o, shell = True)
           print(tc.tcolors.SUCCESS + "Opened Nautilus!" + tc.tcolors.ENDC)
       except:
           print(tc.tcolors.WARNING + "Not a Debian or Arch Linux distro?" + tc.tcolors.ENDC)
    
    def connected(self):
        scan = 'sh ./connected.sh'
        try:
            subprocess.call(scan, shell = True)
            print(tc.tcolors.SUCCESS + "Scan completed!" + tc.tcolors.ENDC)
        except:
            print(tc.tcolors.WARNING + "Uh oh wtf." + tc.tcolors.ENDC)

    def listcd(self):
	    cd = os.getcwd()
	    print(cd)

    def dirchange(self):
        cd = os.getcwd()
        print(cd)
        try:
	    #Had to switch to 2.7 string input because input() and os.chdir() are incompatable?
            mow = raw_input("What directory?: ")
            os.chdir(mow)
        except NameError:
            print('Name error Uh oh.')
        except SyntaxError:
            print('Syntax error Uh oh.')
        except WindowsError:
            print('Windows can not find the specified directory.'
                  'Did you include the entire path?')
        else:
            print('Directory changed to', mow)

    def listf(self):
        mypath = os.getcwd()
        print(os.listdir(mypath))

    def remf(self):
        print(tc.tcolors.WARNING + 'File does not get sent to trashbin! It gets permanently deleted!' + tc.tcolors.ENDC)
        F = input("What file would you like to remove? :")
        try:
            os.remove(F)
        except OSError:
            print(tc.tcolors.SYNTAX + 'File does not exist.' + tc.tcolors.ENDC)
        else:
            print(tc.tcolors.SUCCESS + 'File removed!' + tc.tcolors.ENDC)

    def remdir(self):
        print(tc.tcolors.WARNING + 'WARNING: This command deletes the whole directory and contents.' + tc.tcolors.ENDC)
        F = input("What directory would you like to remove? :")
        try:
            shutil.rmtree(F)
        except OSError:
            print(tc.tcolors.SYNTAX + 'Directory does not exist' + tc.tcolors.ENDC)
        else:
            print(tc.tcolors.SUCCESS + 'Entire directory removed!' + tc.tcolors.ENDC)

    def readf(self):
        yeeee = input('What file do you want to read? :')
        try:
            f = open(yeeee)
            print(f.readlines())
        except IOError:
            print(tc.tcolors.SYNTAX + 'File not found.' + tc.tcolors.ENDC)

    def overwrite(self):
        yo = Overwrite.Mystuff()
        yo.overwrite()

    def b64(self):
        riot = input('Input password to encrypt. :')
        woh = base64.b64encode(riot.encode('ascii'))
        print(tc.tcolors.SUCCESS + woh.decode() + tc.tcolors.ENDC)

    def decryptb64(self):
        decode = input('Input password to decrypt. :')
        decrypt = base64.b64decode(decode.encode('ascii'))
        print(tc.tcolors.SUCCESS + decrypt.decode() + tc.tcolors.ENDC)

    def exit(self):
        self.done = True
        exit()

def main():
    com = commands.Command()
    com.event_loop()
    start = Vipercmd()
    start.cmd_loop()

if __name__ == '__main__':
    main()
