import os

# Colors
class colors:
    reset = "\033[0m"
    red = "\033[1;31m"
    yellow = "\033[1;33m"

os.system("clear")

def bannerYoutube1():
    print (colors.yellow + "                                  ")
    print ("\n\t\t ░█░█░█▀█░█░█░▀█▀░█░█░█▀▄░█▀▀░░░░ ")
    print ("\t\t ░░█░░█░█░█░█░░█░░█░█░█▀▄░█▀▀░░░░ ")
    print ("\t\t ░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀░░▀▀▀░░░░ \n\n\n" + colors.reset)
    print (colors.red + "\t\t=================================== " + colors.reset)
    print ("\t\tPerintah dasar : ")
    print ("\t\t            exit = keluar")
    print ("\t\t            back = kembali\n\n")
    print (colors.red + "\t\t=================================== " + colors.reset)

if __name__=="__main__":
    bannerYoutube1()
