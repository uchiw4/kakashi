import os
import ctypes

try:
    import requests
except:
    os.system("python3 -m pip install requests")
try:
    from pyfade import Fade, Colors
except:
    os.system("python3 -m pip install pyfade")

try:
    from pycenter import center
except:
    os.system("python3 -m pip install pycenter")
try:
    from colorama import Fore
except:
    os.system("python3 -m pip install colorama")


ctypes.windll.kernel32.SetConsoleTitleW("kakashi by uchiw4")

mangadl = """  
                                                      
:::    :::     :::     :::    :::     :::      ::::::::  :::    ::: ::::::::::: 
:+:   :+:    :+: :+:   :+:   :+:    :+: :+:   :+:    :+: :+:    :+:     :+:     
+:+  +:+    +:+   +:+  +:+  +:+    +:+   +:+  +:+        +:+    +:+     +:+     
+#++:++    +#++:++#++: +#++:++    +#++:++#++: +#++:++#++ +#++:++#++     +#+     
+#+  +#+   +#+     +#+ +#+  +#+   +#+     +#+        +#+ +#+    +#+     +#+     
#+#   #+#  #+#     #+# #+#   #+#  #+#     #+# #+#    #+# #+#    #+#     #+#     
###    ### ###     ### ###    ### ###     ###  ########  ###    ### ########### 
                                                                                                      
"""


print(Fade.Vertical(Colors.red_to_yellow, center(mangadl)))

i = str(1)

while True:
    manga = input("\033[33m Manga (remplacer les espaces par des tirets) >  ")
    chapitre = input("\033[33m Chapitre >  ")

    path = manga+"/"+chapitre
    try:
        os.mkdir(manga)
    except:
        pass
    try:
        os.mkdir(path)
    except:
        pass


    re = requests.get("https://scansmangas.xyz")
    while re.status_code != 404:    

        re = requests.get("https://scansmangas.xyz/scans/"+manga+"/"+chapitre+"/"+i+".jpg")
        if re.status_code == 404:
            pass
        else:
            with open(manga+"/"+chapitre+"/"+manga+"_"+i+".jpg","wb")as f:
                    f.write(re.content)  
            i = str(int(i)+1)
        
    print("\033[33m Chapitre "+chapitre+"\033[33m de "+manga+"\033[33m téléchargé mon reuf !"+Fore.RESET)


    restart = input("\033[33m On continue ? [o/n] ")

    if restart == "o":
        os.system("cls")
        print(Fade.Vertical(Colors.red_to_yellow, center(mangadl)))
        i = str(1)
    else:
        break


