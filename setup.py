import subprocess
import time
import os
os.system("sudo apt install python3-pyfiglet")
os.system("sudo apt install python3-colorama")
os.system("sudo apt install python3-requests")
import pyfiglet
import requests
from colorama import init, Fore

# Initialize Colorama
init()

def header():
    print('''
..................................................................................................................[41;33mXdl0NXXN[40;32m...........................................
..................................................................................................................[41;33mNxco0XXXXXXXXKN.N[40;32m..................................
............................................................................................................[41;33mN....N.0lcd0KXX0XXXXXXXXX[40;32m................................
............................................................................................................[41;33mNXXN.NNXdclOKXKx0.NNKxON.NN[40;32m..............................
.............................................................................................................[41;33mNX00XNXkclOKK0dkXXOdkXNNXKK0OkOKN[40;32m.......................
...............................................................................................................[41;33mN0kOK0dokKKOdk0xox0kxdolldk0XN[40;32m........................
...................................................................................................NNNNNNXXXXNNN[41;33mNKkoxOO0KXOk0kxOddk0XNNN[40;32m.............................
.............................................................................................NXXXXKXKOOO0000000KKX[41;33mKOxOKKXXKKKKKKKKXX00KXXNN[40;32m..........................
.......................................................................................NNXXXXKKKKKXX0kkxxddoooooxkOK[41;33mKKXXXNXXXXXKXXXXXXXXK0kdoodxkO0X[40;32m.................
.....................................................................................NXKKKXX00KKXXNNNNNNNXXKOkkxx[41;33mkO0KKKKXNNXXXKKKK0OkXXk00KKKN[40;32m.......................
..................................................................................NXXKKKKKXXKXNN...........[41;33mNNNXKOkxdxOKXXXXXXXKK000KKKKXN[40;32m............................
...............................................................................NXXKXK0KKXXN...........[41;33mNNNNNXXK0OkkkkO0KKKKXKKKKK0kxkOXN[40;32m..............................
.............................................................X0OkkxxddxxkOO0KXNKKKXXKKXN..........................[41;33mNNXKK00KKKK0kOXX00koccox0X[40;32m.........................
............................................................Kxoooooooooolllld0K0KKXXXN.........................[41;33mNXKKKKOdok0KKKKxldk00OXXkxolokKN[40;32m......................
........................................................NNXOdddooooooooc;.,d0NX0KK0xdxOX.....................[41;33mNXXKXXKxllxKXK0OOOollxKXXXXXXXKOkxkKN[40;32m...................
...............................................NK0kkxxxxddo:;clodddooool;,lO0N.XOlcoollldkX.................[41;33mNNNN.XOoldOKNNKK0xkkOkoONNXNNXXN[40;32m.........................
..........................................N0kxxdooodxxkkOOd;,:::lllodddoooddxkOOo;cooooc::lkN..................[41;33mNOdokKNNNNKOKNOod0N0x0[40;32m................................
......................................N0kxdoodkOOOkkkkkOOxc,,;::::::clloodddooollllllc::::ldK................[41;33mN0xk0N[40;32m..[41;33mKkOX.XdlO..XXN[40;32m..................................
...................................N0kdodxOOOkkkkkkkOkkOkdc;,;:::::::::::cclllllllllllloodddK................[41;33mK0X[40;32m....[41;33mXXN[40;32m...[41;33m0oO[40;32m........................................
................................N0kddxkOOkkkOkkkkkkkOkkkOxc;,,,;;;:::::::::::::::cccclllcc:dX.................................[41;33mNKX[40;32m....................................
..............................XOxdxkxxkkOkOkkkkkkkkkkkkkkkxc;,,,;;:::::::::::::::::::::::::dKX.......................................................................
............................XkddkkxxxkkOOOkkOOkkkkkkkkkOkkkxdl::::;;;;;::::::::::::::::::;cxkkOKN....................................................................
..........................XkddkOkxxkOkkkxxxkOOkOkkkkkkkOkkOkkkdoc:;,,,;;::;;;;::::;;;;:;;:oxkOkkkKN..................................................................
........................N0ddkOkkkkkkkkkkdodxxkkkkkkkkOOkkkkkkOkkxxdoc::::;;,,,;;;;,,,;:codxxxxkOkxkK.................................................................
.......................XkdxOkxkkOkkkkOkkkxxxkkkkOkkkOkkkOkkkkkkkkOkkkxxddollccccllllloxkkOkxkkxxkOkxOX...............................................................
......................KxxkkkkxkkkkkkOOkkkkkkkkxxxxkOkxxkkOOkkkkkkOOkkkkkkkkkkkxxkkkkkkkOkkOOkkkkxkOkxxK..............................................................
.....................KkkkkOkkkkkkkkkkkkkkkkkxxxxxkOOkkkkkkkkOkkkOOOkkOkkkkkkkkkkkkkkkkkkkOkkkkkOkkOkOxd0.............................................................
....................KxkOkkkOkkkkkkkkkkkOOkkkkkkkkkkOkkkkkkkkkkkOOOOOkkkddxxkkkkkkOkkkkkkkkkkkOkkkkkOOkxd0............................................................
...................NkxkkxxkkkkkkkkkkkkkkkkkkxxkkkkkOkkkkOkkkkkOkkOOkkxxxxxxkkkkkkkkkkkkkkkOkkxxkxololdkxdK...........................................................
..................NKxxOkddxkkkkkkkkkkkOkkkkkkkkkkkkkkkkkOkkOkkkkkkOOkkkkkkkkkkkkkkkkkkkOkkkxdxxl:loddllkdxX..........................................................
..................XdddkkkkkOkkxxdxxxxkkkkOkkkkkkkkkxkxxxxxdlcc:;;;;;;;;;;,;...;;:lddxkkOkkOkkkkkkkkkkkxkOdo0.N.......................................................
..................kdkkkxdkkdocccclloddxkkkkkkkkkOkxdddxdl:;,,,;:::c::;;,,,,.      ;lxkkkOkkOkkkkkkkkkxxkOdoK.........................................................
..................Kdxkkkkxl:;;:lc:;:cldxkOkOOOkkkkxddxo;,:c;:ldxollc:;;;,,,,.       ;xkxkOkkkkkkkOkkkxxOkldN.........................................................
...................koxdkx:;::lxxoc:;;;coxkOOOkkkkkddkl;;cc,:dxxdlccc:;;;,,,,;.       ;xkxkkkkkkkkkkxxxxOxlO..........................................................
...................Xdldxl,:;cddolc:;;,,,cdxxkkkkkxdkd,,cc,;odoollcc::;;;,,,,,.        ckxxxkOkkkxdxxdxkkloX..........................................................
....................koxd:,:,:llcc:;;;,;..cdxkkkkkkkOc;;c;;:cccccc::;;;;,,,,,,.        ,kxddxkkkOkxdodkOdl0...........................................................
...................Nxoxd:,;,,:::;;;;,,.  ;okkxdooxkOc;;c,;:cc:::;;;;;;,,,,,,;.        ,kkdddkOkkkdodkOxcxN...........................................................
..................Nkoxxxc;:,;;;;;;,,,;.  .:c:llllooxl;,c;;;;;;;;;;;;,,,,,,,,.         ;kxddxkkkkkxkkOkldX............................................................
..................kcoxkOo,;;.;,,,,,,;.    ;dxkkkOOxxx:;c:,,;;;;,,,,,,,,,,,;.         .dOdodkkkkkkkOOkooX.N...........................................................
..................x:lxkkkl,:;..;;...     .dOOxdxkOkkOx:,::,,,,,,,,,,,,,,;.          .oOxddkOkxxkkxddl:lx0............................................................
..................Nkloxddxl,;:;.        .lkxc..;lkkkkkxl;;::,;;,,,;;;...           ,dOkdxOOkdlcllloxxdo;;O...........................................................
...................Oloxddxkd:,;;,......,dOk:     ,odxkOkdc:;;,..                .,okOkdxkkkxddxxkOOkdc;.cK...........................................................
.................KdlokxdkkkOkdc:;;,,,;:cdOd.      .cooxxxkxocc;;..          ..,cdkkkkxxkOOkkxkkkkxl;;cd0N............................................................
.................dcxxkkkkkkkkkOkxddodkxcok;        .:dooooxOOxollllc:;;;::cldxkxxkkkOOOOkkkOOkxxo;.oX................................................................
.................KlcoddxxxkOkkkkkkkkkOo;dd.          ;ddddoooxxxkkkkkOOkkxxxddddxkkOkkOkkkkkOkdl..dN.................................................................
..................Ko:cloddxkkkkkkkOkkkccx;            ,dxkkxollllllllloxkkkkkxdxkkkkkOOkkkkkkkd..oN..................................................................
...................NOo:;cdkxdooodkkxxkxkd.             ,xkkkOOkxdollcloxkkkOkkkkOkkkkkkkxxxxxd; :X...................................................................
......................Kxlooodxxddlcldolxl.     .,.      cOkxxdllodddxxkOkxdxxkkkOkkkkkkxxxxxl. ,0....................................................................
.........................NN......Xd;odcco:.  .;xOo.    .lkxoc:oxkkOOkkkdooodxkkOOOOOOkxdxdl,. ,O.....................................................................
..................................X:;dxc;ddlldkkkkxc;,:okOd;:xxloxkxoclooddooooolllllcc::;,;cxX......................................................................
..................................k;oxxo:dOkkkkkkkkOOOOkkkc;dkolxOOo;dN.....NKK0000OOOOO0KN..........................................................................
.................................k:lkxxxxkkxxxkOxdkOOOkkkkdxdxOOOOOo;O...............................................................................................
................................O:odcldoocloodddddxdddxdddodxdolccoxlcK..............................................................................................
...............................Xlcd:oxxkl;okkOkxlclodxd::lllcccllc:;lll0.............................................................................................
...............................Kl;:okxkxccdxkkkOo:oxkOd;lkkOxclxkOOd;;:oX............................................................................................
................................k,:xOOOl;oxkkkkOl:dxxkd,lxxkOdcdOkkOxc,c0............................................................................................
.................................0olllc,:dkkOOOkc:dxOOx,:dxOkkclOOOOOk::K............................................................................................    
''')

def clear_screen():
    subprocess.run("clear" if os.name == "posix" else "cls")


def print_large_red(text):
    # Use pyfiglet to create large text
    large_text = pyfiglet.figlet_format(text)
    # Print in red
    print(Fore.RED + large_text + Fore.RESET, end="\r")

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # Print the timer in large red text
        clear_screen()
        header()
        print_large_red(timer)
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    clear_screen()
    print_large_red("BOMB SQUAD")  # Message after countdown finishes
    time.sleep(3)
    os.system("python3 ransom.py")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal before running
    countdown_timer(10)  # Start a countdown from 10 seconds
