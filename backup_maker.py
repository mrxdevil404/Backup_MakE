from socket import socket , AF_INET , SOCK_STREAM , gethostbyname , gaierror
from os import walk , listdir , getcwd , getlogin , system , remove
from os.path import isfile , isdir , getsize , basename , expanduser
from random import _urandom , choice
from subprocess import PIPE , Popen
from platform import system as iden
from colorama import Fore
from shutil import copy
from time import sleep
from mega import Mega
from gtts import gTTS
w = Fore.WHITE
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
c = Fore.CYAN
if iden() == 'Windows':
  paths_tool = [f'C:\\Users\\{getlogin()}\\AppData\\Roaming\\Done.txt' , f'C:\\Users\\{getlogin()}\\AppData\\Roaming\\check.txt' , f'C:\\Users\\{getlogin()}\\AppData\\Roaming\\Done_ext.txt']
elif iden() == 'Linux':
  if not Popen('uname -o',shell=True,stdout=PIPE).communicate()[0].decode() == 'Android':
   paths_tool = ['/home/.done.txt', '/home/.check.txt' , '/home/.done_ext.txt']
  else:
   paths_tool = ['/sdcard/.done.txt', '/sdcard/.check.txt' , '/sdcard/.done_ext.txt']
colors = [w ,r, g, b , c]
voice = int(open("voice.txt" , 'r').readlines()[0])
def banner():
    print(f"""{choice(colors)}
                 ____        _                 __  __       _             
                |  _ \      | |               |  \/  |     | |            
                | |_) | __ _| | ___   _ _ __  | \  / | __ _| | _____ _ __ 
                |  _ < / _` | |/ / | | | '_ \ | |\/| |/ _` | |/ / _ \ '__|
                | |_) | (_| |   <| |_| | |_) || |  | | (_| |   <  __/ |   
                |____/ \__,_|_|\_\\__,_| .__/ |_|  |_|\__,_|_|\_\___|_|   
                                        | |______                          
                                        |_|______|                         

                    
                                Coded By : Ali Mansour
""")
def start_up():
    name = basename(__file__).split('.')[0]
    pathN = getcwd() + f'//{name}'
    if iden() == 'Windows':
        name += '.exe'
        pathN += '.exe'
        if not isfile(f'C:\\\\Users\\\\{getlogin()}\\\\AppData\\\\Roaming\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup\\\\{name}'):copy(pathN,f'C:\\\\Users\\\\{getlogin()}\\\\AppData\\\\Roaming\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup')
    elif iden() == 'Linux':
        name += '.py'
        pathN += '.py'
        if not isfile(expanduser("~") + '//.startup.txt'):
          with open(expanduser('~') + '//.bashrc' , 'a')as f:
            f.write(f"python3 {pathN}")
          copy("voice.txt" , expanduser('~'))
          with open(expanduser("~") + '//.startup.txt' , 'w')as f:f.write("Done")
def check():
    data = _urandom(65000)
    s = socket(AF_INET,SOCK_STREAM)
    try:
        ip = gethostbyname('www.google.com')
        s.connect((ip,80))
        s.sendto(data,(ip,80))
        s.close()
    except gaierror:
        sleep(1)
        check()
def SpeakDone(num):
    language = "ar"
    if str(num).isnumeric():
        num = f"مرحبا لقد تم رفع {str(num)} ملفات بنجاح"
    myobj = gTTS(text=num, lang=language, slow=False)
    myobj.save("welcome.mp3")
    if iden() == 'Windows':
      system("start welcome.mp3")
      sleep(5)
    #else:system("nvlc welcome.mp3")
    remove("welcome.mp3")
def finish( n ):
  if isfile(paths_tool[int(n)]):
      try:
        remove(paths_tool[int(n)])
      except:print (f'{w}[{g}!{w}] Delete {paths_tool[0]} To Uploader Work')
def spec( email , password , path ):
    check()
    if isdir( path ):
        num = 0
        for dir,dirs,files in walk(path):
            for file in files:
                pathF = dir + '/' + file
                if isfile(r"{}".format(pathF)):
                    try:
                       m.upload( pathF )
                       num += 1
                       print (f"{w}[{c}+{w}] {pathF.split('/')[-1]} Success Upload")
                    except Exception as e:
                      print (e)
                      continue
        if not voice == 1:SpeakDone(num)
        else:print (f'{w}[{b}+{w}] {str(num)} Files Successfully Uploaded')
def All(email , password , ext):
    check()
    if ext:n = 2
    else:n = 0
    pathf = get_paths()
    if not isfile(r"{}".format(paths_tool[n])):
     h = open(r"{}".format(paths_tool[n]) , 'a')
     for depart in pathf:
      depart = depart.rstrip()
      for dir,dirs,files in walk(depart):
       for file in files:
        pathF = dir + '/' + file
        if pathF[-4:] == '.lnk' or pathF[-4:] == '.ini':continue
        else:
            try:
                if ext:
                    if ('.' + pathF.split('\\')[-1].split('.')[-1]) in ext:
                        h.write(pathF + '\n')
                else:
                    h.write(pathF  + '\n')
            except UnicodeEncodeError:continue
     h.close()
    ff = open(r"{}".format(paths_tool[n]) , 'r')
    num = 0
    ff_l = ff.readlines()
    x = []
    for pathff in ff_l:
        pathff = pathff.rstrip()
        if isfile(r"{}".format(pathff)):
           m.upload(pathff)
           x.append(pathff)
           num += 1
           if ext:
            f2 = open(r"{}".format(paths_tool[n]) , 'w')
           else:
            f2 = open(r"{}".format(paths_tool[n]) , 'w')
           for o in ff_l:
            if o.rstrip() != pathff:
             if o.rstrip() not in x:
               f2.write(o)
           f2.close()
           print (f"{w}[{b}+{w}] SUCCESS UPLOAD {pathff.split('/')[-1]}")
    ff.close()
    if not voice == 1:SpeakDone(num)
    else:print (f'{w}[{b}+{w}] {str(num)} Files Successfully Uploaded')
    finish(n)
def redownload(email , password , ext):
 check()
 pathf = get_paths()
 if not isfile(paths_tool[1]):
  f = open(paths_tool[1] , 'a')
  for depart in pathf:
   depart = depart.rstrip()
   for dir,dirs,files in walk(depart):
    for file in files:
     pathF = dir + '/' + file
     if pathF[-4:] == '.lnk' or pathF[-4:] == '.ini':continue
     else:
      if ext == pathF.split('.')[-1]:
       m.upload(pathF)
       f.write(pathF + ',' + str(getsize(pathF)) + '\n')
  f.close()
 for depart in pathf:
   depart = depart.rstrip()
   for dir,dirs,files in walk(depart):
    for file in files:
     pathF = dir + '/' + file
     if pathF[-4:] == '.lnk' or pathF[-4:] == '.ini':continue
     else:
      if ext == pathF.split('.')[-1]:
       with open(paths_tool[1] , 'r')as f:
        for data in f.readlines():
         name , size = data.rstrip().split(',')
         if name == pathF:
          if int(size) == getsize(pathF):
           print (name , size)
          else:
           result = m.find(name.split('/')[-1])
           if result:
            m.delete(result[0])
            m.upload(name)
            print (c, name , size , " UPLOAD " , str(getsize(pathF)))
def check_m(*ask):
 global mega , m
 ask_ = ''
 for i in ask:ask_ += i
 try:
   email = input(f"{w}[{c}+{w}] Enter Email Mega >> ")
   password = input(f"[{w}{c}+{w}] Enter Password Mega >> ")
   mega = Mega()
   m = mega.login(email , password)
   if ask_ == 'All':All( email , password , [] )
   elif ask_ == 'spec':
     path = input(f"{w}[{c}+{w}] Enter Path Dir >> ")
     if not isdir(path):
      if not voice == 1:SpeakDone("عذرا المسار غير متاح")
      else:print (f"{w}[{r}!{w}] Path InValid")
     else:spec(email , password , path)
   elif ask_ == 'specifi_ext':
     ext = []
     while True:
      ask_ext = input(f"{c} Enter Extention [ start with . ] >> ")
      if ask_ext.lower() == 'stop':
            if not voice == 1:SpeakDone("لقد تم حفظ صيغ الملفات جاري فحصهم")
            else:print (f'{w}[{b}+{w}] Extenstions Are Saved Uploader Will Work Now On Them')
            break
      elif not ask_ext.startswith("."):
        ext.append("." + ask_ext)
      else:
        ext.append(ask_ext)
     print (ext)
     All(email , password , ext)
   elif ask_ == 'redownload':
     ext = input(f"{g} Enter Extention [ Don't Start With . ] >> ")
     if ext.startswith("."):
      ext = ext[1:]
     redownload(email , password , ext)
 except Exception as e:
   print (e)
   if not voice == 1:SpeakDone("الاميل او الباسورد غير صحيح")
   else:print (f"{w}[{r}!{w}] Email Or Password Is Incorrect")
def get_paths():
 if iden() == 'Windows':
    pathf = []
    for i in range(65,91):
      if isdir(f'{chr(i)}:\\') and chr(i) != "C":
          xx = chr(i) + ':\\'
          xx += '\\'
          pathf.append(xx)
    pathf.append(f'C:\\Users\\{getlogin()}\\Desktop')
 elif iden() == 'Linux':
   if not Popen('uname -o',shell=True,stdout=PIPE).communicate()[0].decode() == 'Android':pathf = ['/home']
   else:pathf = ['/sdcard']
 return pathf
def Inter():
 banner()
 while True:
  SpeakDone("صلي علي محمد")
  print (f"""{choice(colors)}
                            1 - Upload Specific files in Dir
                            2 - Upload All Files In Pc
                            3 - Upload Specific Extention In Pc
                            4 - Check Upgrades In Specific Extention
                            5 - Fix Problems Related To Errors
                            q - Quit
  """)
  number = str(input(f"{w}[{c}+{w}] Choose Number >> "))
  if number == "1":check_m("spec")
  elif number == "2":check_m("All")
  elif number == "3":check_m("specifi_ext")
  elif number == "4":check_m("redownload")
  elif number == '5':
   if iden() == 'Windows':system(f"del {paths_tool[0]} && del {paths_tool[1]}")
   elif iden() == 'Linux':system(f"rm {paths_tool[0]} {paths_tool[1]}")
   if not voice == 1:SpeakDone("تم حل جميع المشاكل")
   else:print (f"[{w}{b}+{w}] All Problems Were Solved")
  elif number == "q":exit()
  else:
   if not voice == 1:SpeakDone("الاختيار غير صحيح")
   else:print(f"{w}[{r}!{w}] InValid Choice")
if __name__ == "__main__":
     while True:
        check()
        start_up()
        Inter()
