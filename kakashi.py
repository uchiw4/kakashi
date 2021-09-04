import os
from sys import platform
try:
    import requests
except:
    os.system("python3 -m pip install requests")
    import requests
try:
    from pyfade import Fade, Colors
except:
    os.system("python3 -m pip install pyfade")
    from pyfade import Fade, Colors    

try:
    from pycenter import center
except:
    os.system("python3 -m pip install pycenter")
    from pycenter import center



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

page = str(1)
while True:
    manga = input("\033[33m Manga (remplacer les espaces par des tirets) >  ")
    quantity = input("\n\033[33m Souhaites-tu télécharger plusieurs chapitres en même temps ?  [o/n] >  ")
    if quantity == "o":

        chapter_a = int(input("\033[33m Du chapitre >  "))
        chapter_b = int(input("\033[33m Au chapitre >  "))
        print(f"\n\033[33m Tu vas télécharger les scans du manga : {manga} du chapitre {chapter_a} au {chapter_b}.")

        try:
            os.mkdir(manga)
        except:
            pass
        for i in range(chapter_a, chapter_b+1):
            try:
                os.mkdir(f"{manga}/{i}")
            except:
                pass

        for i in range(chapter_a, chapter_b+1):
            while True:
                i = str(i)
                re = requests.get(f"https://scansmangas.xyz/scans/{manga}/{i}/{page}.jpg")
                if re.status_code != 404:
                    with open(f"{manga}/{i}/{manga}_{page}.jpg","wb")as f:
                        f.write(re.content)  
                    if platform == "win32":
                        os.system("cls")
                    else:
                        os.system("clear")

                    print(Fade.Vertical(Colors.red_to_yellow, center(mangadl)))
                    print(f"\n\033[33m Page {page}, chapitre {i} téléchargée !")
                    page = str(int(page)+1)
                else:
                    page = str(1)
                    print(f"\n\033[33m Chapitre {i} de {manga} téléchargé !")
                    break

    


    else:
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

        while True:    

            re = requests.get(f"https://scansmangas.xyz/scans/{manga}/{chapitre}/{page}.jpg")
            if re.status_code != 404:
                with open(f"{manga}/{chapitre}/{manga}_{page}.jpg","wb")as f:
                    f.write(re.content)  
                if platform == "win32":
                    os.system("cls")
                else:
                    os.system("clear")


                print(Fade.Vertical(Colors.red_to_yellow, center(mangadl)))
                print(f"\n\033[33m Page {page} téléchargée !")
                page = str(int(page)+1)
            else:
                break

        print(f"\n\033[33m Chapitre {chapitre} de {manga} téléchargé !")


    restart = input("\n\033[33m On continue ? [o/n] ")

    if restart == "o":
        if platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
        print(Fade.Vertical(Colors.red_to_yellow, center(mangadl)))
        page = str(1)
    else:
        break
