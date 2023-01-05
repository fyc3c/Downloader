import os
from tools import bannerSaya
from tools.youtube import main

os.system("clear")

bannerSaya.usingBanner()

def daftar():
    print ("\n\t [1] YouTube")
    print ("\t [2] Facebook")
    print ("\t [3] Instagram")

    choice = int(input("\n\t Input ▶ "))

    if choice == 1:
        os.system("clear")
        bannerSaya.usingBanner()
        main.mainMenu()

    elif choice == 2:
        print ("Facebook")

    elif choice == 3:
        print ("Instagram")

if __name__=="__main__":
    daftar()
