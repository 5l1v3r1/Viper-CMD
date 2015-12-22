import cmd
import os
import sys
import subprocess
import socket
import shutil
import urllib
import base64
import Overwrite
import tc
import pygame
from os import listdir
from os.path import isfile, join

print(tc.tcolors.WARNING +'/$/       //                         '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'\$\      //                          '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +' \$\    //  __                       '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'  \$\  //   ||  $$$$$  $$$$$  $$$$   '+ tc.tcolors.ENDC)
print(tc.tcolors.SYNTAX +'   \$\//    ||  $    $ $   $  $   $  '+ tc.tcolors.ENDC)
print(tc.tcolors.SYNTAX +'    \$/     ||  $    $ $ $$$  $      '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'            --  $$$$$  $      $      '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'                $       $$$$  $      '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'                $                    '+ tc.tcolors.ENDC)
print('\n')
print(tc.tcolors.SUCCESS +'Viper-CMD Alpha 1.0.0\n'
      'by B3nac'+ tc.tcolors.ENDC)
print(tc.tcolors.SYNTAX +'Welcome to Viper command terminal. Type help for list of commands.'+ tc.tcolors.ENDC)

class Vipercmd(cmd.Cmd):
    #Command example

    def do_greet(self, person):
        print(tc.tcolors.WARNING + "hi" + tc.tcolors.ENDC)

    def do_help(self, commands):
        print('Current list of commands: greet, portscan, honeypot,'
              ' listcd, dirchange, dl, listf, remf, autocleanup, clean_trash, remdir, readf, runf, sechash, b64, exit')

    def do_playmusic(self, music):
        #Works in Windows.
        #To-do add list.
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 128)
        print(tc.tcolors.SYNTAX + 'Type the name of the song name with extension. ex: song.ogg' + tc.tcolors.ENDC)
        print(tc.tcolors.WARNING + 'WARNING: Needs to be in same directory.' + tc.tcolors.ENDC)
        try: 
            music = input('What music would you like to play? ')
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()
        except pygame.error:
            print(tc.tcolors.SYNTAX + 'No song with that name in this directory.' + tc.tcolors.ENDC)

    #Security Functions.
    #---------------------------------------------------------------------
    def do_portscan(server_address, self):
        try:
            server_address = int(raw_input("Enter a remote host: "))
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

    def do_honeypot(sock, server_address):

       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       server_address = ('', 443)
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
                   connection.close()

    def do_netping(self, ping):
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

    def do_dl(web, files):
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

    def do_runf(self, f):
        print('If executing C or C++ program put ./ for Bash or Perl sh in front of file name.')
        #C and Bash work so far.
        f = subprocess.call(raw_input("Which file would you like to run? :"), shell=True)
            			
    def do_autocleanup(self, clean):
       print(tc.tcolors.WARNING + "Only works on Debian or Arch Linux type distros." + tc.tcolors.ENDC)
       clean = 'sh ./Cleanup.sh'
       try:
           subprocess.call(clean, shell = True)
           print(tc.tcolors.SUCCESS + "Finished system cleanup!" + tc.tcolors.ENDC)
       except:
       	   print(tc.tcolors.WARNING + "Not a Debian or Arch Linux distro?" + tc.tcolors.ENDC)

    def do_clean_trash(self, t):
       print(tc.tcolors.WARNING + "Only works on Debian or Arch Linux type distros." + tc.tcolors.ENDC)
       t = 'sh ./cleantrash.sh'
       try:
           subprocess.call(t, shell = True)
           print(tc.tcolors.SUCCESS + "Finished trashbin cleanup!" + tc.tcolors.ENDC)
       except:
           print(tc.tcolors.WARNING + "Not a Debian or Arch Linux distro?" + tc.tcolors.ENDC)

    def do_nautilus(self, o):
       print(tc.tcolors.WARNING + "Only works on Debian and Arch Linux type distros." + tc.tcolors.ENDC)
       o = 'sh ./opennautilus.sh'
       try:
           subprocess.call(o, shell = True)
           print(tc.tcolors.SUCCESS + "Opened Nautilus!" + tc.tcolors.ENDC)
       except:
           print(tc.tcolors.WARNING + "Not a Debian or Arch Linux distro?" + tc.tcolors.ENDC)

    def do_listcd(self, cd):
	    cd = os.getcwd()
	    print(cd)

    def do_dirchange(self, mow):
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

    def do_listf(self, files):
        mypath = os.getcwd()
        print(os.listdir(mypath))

    def do_remf(self, F):
        print(tc.tcolors.WARNING + 'File does not get sent to trashbin! It gets permanently deleted!' + tc.tcolors.ENDC)
        F = input("What file would you like to remove? :")
        try:
            os.remove(F)
        except OSError:
            print(tc.tcolors.SYNTAX + 'File does not exist.' + tc.tcolors.ENDC)
        else:
            print(tc.tcolors.SUCCESS + 'File removed!' + tc.tcolors.ENDC)

    def do_remdir(self, F):
        print(tc.tcolors.WARNING + 'WARNING: This command deletes the whole directory and contents.' + tc.tcolors.ENDC)
        F = input("What directory would you like to remove? :")
        try:
            shutil.rmtree(F)
        except OSError:
            print(tc.tcolors.SYNTAX + 'Directory does not exist' + tc.tcolors.ENDC)
        else:
            print(tc.tcolors.SUCCESS + 'Entire directory removed!' + tc.tcolors.ENDC)

    def do_readf(self, yeeee):
        yeeee = input('What file do you want to read? :')
        try:
            f = open(yeeee)
            print(f.readlines())
        except IOError:
            print(tc.tcolors.SYNTAX + 'File not found.' + tc.tcolors.ENDC)

    def do_overwrite(self, yeeee):
        yo = Overwrite.Mystuff()
        yo.overwrite()

    def do_b64(self, passwd):
        riot = input('Input password to encrypt. :')
        woh = base64.b64encode(riot.encode('ascii'))
        print(tc.tcolors.SUCCESS + woh.decode() + tc.tcolors.ENDC)

    def do_decryptb64(self, decrypt):
        decode = input('Input password to decrypt. :')
        decrypt = base64.b64decode(decode.encode('ascii'))
        print(tc.tcolors.SUCCESS + decrypt.decode() + tc.tcolors.ENDC)

    def do_EOF(self, line):
        return True

    def do_exit(self, ex):
        ex = exit()

    def postloop(self):
        print()

if __name__ == '__main__':
    Vipercmd().cmdloop()
