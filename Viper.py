import cmd
import os
import sys
import subprocess
import socket
import shutil
import urllib
import base64
import Overwrite
from os import listdir
from os.path import isfile, join
#from passlib.hash import pbkdf2_sha256

print('/$/       //                         ')
print('\$\      //                          ')
print(' \$\    //  __                       ')
print('  \$\  //   ||  $$$$$  $$$$$  $$$$   ')
print('   \$\//    ||  $    $ $   $  $   $  ')
print('    \$/     ||  $    $ $ $$$  $      ')
print('            --  $$$$$  $      $      ')
print('                $       $$$$  $      ')
print('                $                    ')
print('\n')
print('Viper Alpha 0.0.5\n'
      'by B3nac')
print ('Welcome to Viper command terminal. Type help for list of commands.')
#I had to use Python 2.7 becuase some of the modules weren't cross compatable.

class tcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    
class Vipercmd(cmd.Cmd):
    #Command example

    def do_greet(self, person):
        if person:
            print(tcolors.WARNING + "hi" ,person + tcolors.ENDC)
        else:
            print(tcolors.WARNING + "hi" + tcolors.ENDC)
            
    def do_help(self, commands):
        print('Current list of commands: greet, portscan, honeypot,'
              ' listcd, dirchange, dl, listf, remf, remdir, readf, runf, sechash, b64, exit')

    #Security Functions.
    #---------------------------------------------------------------------
    def do_portscan(server_address, self):
        server_address = raw_input("Enter a remote host :")
        remoteconnectionIP = socket.gethostbyname(server_address)

        try:
            for port in range(1,1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteconnectionIP, port))
                if result == 0:
                    print "Port {}: \t Open".format(port)
                    sock.close()
                    return
        except socket.error:
            print "Couldn't connect to server"

    def do_honeypot(sock, server_address):

       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       server_address = ('', 443)
       try:
           sock.bind(server_address)
       except socket.error:
           print("Socket error, sudo run Viper or change ports.")
       else:
           while True:
               print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
               sock.listen(1)
               print >>sys.stderr, 'waiting for a connection from sneaky mofackles.'
               connection, client_address = sock.accept()
               compname = socket.gethostname()
               try:
                   print >>sys.stderr, 'client connected:', client_address
                   print >>sys.stderr, 'Computer name:', compname
                   while True:
                       data = connection.recv(16)
                       print >>sys.stderr, 'recieved "%s"' % data
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
       print('Downloads file to Viper directory.')
       try:
           web = raw_input('What is the url?')
           files = raw_input('What file?')
           #IOError
           urllib.urlretrieve(web,files)
       except IOError:
           print('File does not exist or url.')
       else:
           print('File downloaded!')

    def do_runf(self, f):
        print('If executing C or C++ program put ./ for Bash or Perl sh in front of file name.')
        #C and Bash work so far.
        f = subprocess.call(raw_input("Which file would you like to run? :"), shell=True)

    def do_autocleanup(self, clean):
       print("Only works on Debian Linux type distros.")
       clean = 'sh ./Cleanup.sh'
       try:
           subprocess.call(clean, shell = True)
           print("Finished system cleanup!")
       except:
       	   print("Not a Debian Linux distro?")

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
        F = raw_input("What file would you like to remove? :")
        try:
            os.remove(F)
        except OSError:
            print('File does not exist.')
        else:
            print('File removed!')

    def do_remdir(self, F):
        print('WARNING: This command deletes the whole directory and contents.')
        F = raw_input("What directory would you like to remove? :")
        try:
            shutil.rmtree(F)
        except OSError:
            print('Directory does not exist')
        else:
            print('Entire directory removed!')

    def do_readf(self, yeeee):
        yeeee = raw_input('What file do you want to read? :')
        try:
            f = open(yeeee)
            print f.readlines()
        except IOError:
            print('File not found.')
        #IOError

    def do_overwrite(self, yeeee):
        #Shred function in the works.
        yo = Overwrite.Mystuff()
        yo.overwrite()

    def do_sechash(self, passwd):
        riot = raw_input('Input password. :')
        passwd = pbkdf2_sha256.encrypt(riot, rounds=200000, salt_size = 16)
        print(passwd)
        valid = pbkdf2_sha256.verify(riot, passwd)
        print(valid)
        #False?
        f = open("passwd.txt", "a")
        f.write(str(passwd))

	    #ValueError: Empty mode string.
    def do_b64(self, passwd):
        riot = raw_input('Input password to encrypt. :')
        woh = base64.b64encode(riot)
        print(woh)

    def do_decryptb64(self, decrypt):
        decode = raw_input('Input password to decrypt. :')
        decrypt = base64.b64decode(decode)
        print(decrypt)

    def do_EOF(self, line):
        return True

    def do_exit(self, ex):
        ex = exit()

    def postloop(self):
        print()

if __name__ == '__main__':
    Vipercmd().cmdloop()
