import Viper
import tc

print(tc.tcolors.WARNING +'/$/       //                         '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'\$\      //                          '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +' \$\    //  __                       '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'  \$\  //   ||  $$$$$  $$$$$  $$$$   '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'   \$\//    ||  $    $ $   $  $   $  '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'    \$/     ||  $    $ $ $$$  $      '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'            --  $$$$$  $      $      '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'                $       $$$$  $      '+ tc.tcolors.ENDC)
print(tc.tcolors.WARNING +'                $                    '+ tc.tcolors.ENDC)
print('\n')
print(tc.tcolors.SUCCESS +'Viper-CMD Alpha 1.0.0\n'
      'by B3nac'+ tc.tcolors.ENDC)
print(tc.tcolors.SYNTAX +'Welcome to Viper command terminal. Type help for list of commands.'+ tc.tcolors.ENDC)

class Command(object):

    def event_loop(self):
        self.cmd = input('(Viper-CMD)> ')
			
        if self.cmd == 'greet':
            Viper.Vipercmd().greet()
        elif self.cmd == 'help':
            Viper.Vipercmd().help()
        #elif self.cmd == 'playmusic':
            #self.playmusic() 
        elif self.cmd == 'portscan':
            Viper.Vipercmd().portscan()
        elif self.cmd == 'honeypot':
            Viper.Vipercmd().honeypot(self)
        elif self.cmd == 'netping':
            Viper.Vipercmd().netping()
        elif self.cmd == 'dl':
            Viper.Vipercmd().dl()
        elif self.cmd == 'runf':
            Viper.Vipercmd().runf()
        elif self.cmd == 'autocleanup':
            Viper.Vipercmd().autocleanup()
        elif self.cmd == 'clean_trash':
            Viper.Vipercmd().clean_trash()
        elif self.cmd == 'nautilus':
            Viper.Vipercmd().nautilus()
        elif self.cmd == 'listcd':
            Viper.Vipercmd().listcd()
        elif self.cmd == 'dirchange':
            Viper.Vipercmd().dirchange()
        elif self.cmd== 'listf':
            Viper.Vipercmd().listf()
        elif self.cmd == 'remf':
            Viper.Vipercmd().remf()
        elif self.cmd == 'remdir':
            Viper.Vipercmd().remdir()
        elif self.cmd == 'readf':
            Viper.Vipercmd().readf()
        elif self.cmd == 'overwrite':
            Viper.Vipercmd().overwrite()
        elif self.cmd == 'b64':
            Viper.Vipercmd().b64()
        elif self.cmd == 'b64decrypt':
            Viper.Vipercmd().decryptb64()
        elif self.cmd == 'connections':
            Viper.Vipercmd().connected()
        elif self.cmd == 'monitor':
            Viper.Vipercmd().keyboard_m()
        elif self.cmd == 'exit':
            Viper.Vipercmd().exit()
            
        else:
            print('Command does not exist,'
	          'try help for list of commands')
