import os


os.system("clear")

# Color

class colors:
    reset = "\033[0m" # Reset Warna
    red = "\033[1;31m" # Merah
    green = "\033[32m" # Hijau
    yellow = "\033[1;93m" # Kuning
    cian = "\033[1;36m" # Cyan
    biru = "\033[1;35m" # Biru

def usingBanner():
    print (colors.yellow + "\t ╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━" + colors.reset)
    print (colors.red + "\t      ╺┳┓┏━┓╻ ╻┏┓╻╻  ┏━┓┏━┓╺┳┓┏━╸┏━┓        ")
    print ("\t       ┃┃┃ ┃┃╻┃┃┗┫┃  ┃ ┃┣━┫ ┃┃┣╸ ┣┳┛        ")
    print ("\t      ╺┻┛┗━┛┗┻┛╹ ╹┗━╸┗━┛╹ ╹╺┻┛┗━╸╹┗╸•••   " + colors.reset)
    print (colors.cian + "\t      [ Social Media Downloader v1.0 ]      " + colors.reset)
    print (colors.biru + "\t             ► Coding Night ◄      " + colors.reset)
    print (colors.yellow + "\t ╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━╺━" + colors.reset)

if __name__=='__main__':
    usingBanner()
