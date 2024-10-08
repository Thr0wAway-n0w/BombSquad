import os
import subprocess
import math
import webbrowser
import time
from time import sleep
os.system("sudo apt install python3-requests")

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

def rainbow_gradient_text(text):
    for i, char in enumerate(text):
        r = int((i / len(text)) * 255)
        g = int((1 - (i / len(text))) * 255)
        color = f"\033[38;2;{r};{g};0m"
        print(f"{color}{char}\033[0m", end="")
    print()

def main_menu():
    print("\033[93mBOMB SQUAD")
    print(" ")
    print("", end="", flush=True)
    for char in " \033[95mA curated collection of Ransomware decryption tools. Select from the list below to recover your files":
        print(char, end="", flush=True)
        time.sleep(0.04)
    time.sleep(3)
    print(" ")
    rainbow_gradient_text("1. 777 Ransom")
    rainbow_gradient_text("2. AES_NI Ransom")
    rainbow_gradient_text("3. Agent.iih Ransom")
    rainbow_gradient_text("4. Akira Ransom")
    rainbow_gradient_text("5. Alcatraz Ransom")
    rainbow_gradient_text("6. Alpha Ransom")
    rainbow_gradient_text("7. Amnesia Ransom")
    rainbow_gradient_text("8. Amnesia2 Ransom")
    rainbow_gradient_text("9. Annabelle Ransom")
    rainbow_gradient_text("10. AstraLocker Ransom")
    rainbow_gradient_text("11. AtomSilo Ransom")
    rainbow_gradient_text("12. Aura Ransom")
    rainbow_gradient_text("13. Aurora Ransom")
    rainbow_gradient_text("14. AutoIt Ransom")
    rainbow_gradient_text("15. AutoLocky Ransom")
    rainbow_gradient_text("16. Avaddon Ransom")
    rainbow_gradient_text("17. Avest Ransom")
    rainbow_gradient_text("18. BTCWare Ransom")
    rainbow_gradient_text("19. Babuk Ransom")
    rainbow_gradient_text("20. BadBlock Ransom")
    rainbow_gradient_text("21. BarRax Ransom")
    rainbow_gradient_text("22. Bart Ransom")
    rainbow_gradient_text("23. Bianlian Ransom")
    rainbow_gradient_text("24. BigBobRoss Ransom")
    rainbow_gradient_text("25. Bitcryptor Ransom")
    rainbow_gradient_text("26. BlackBasta Ransom")
    rainbow_gradient_text("27. CERBER V1 Ransom")
    rainbow_gradient_text("28. Chaos Ransom")
    rainbow_gradient_text("29. CheckMail7 Ransom")
    rainbow_gradient_text("30. Chernolocker Ransom")
    rainbow_gradient_text("31. Chimera Ransom")
    rainbow_gradient_text("32. Coinvault Ransom")
    rainbow_gradient_text("33. Cry128 Ransom")
    rainbow_gradient_text("34. Cry9 Ransom")
    rainbow_gradient_text("35. CryCryptor Ransom")
    rainbow_gradient_text("36. CrySIS Ransom")
    rainbow_gradient_text("37. Cryakl Ransom")
    rainbow_gradient_text("38. Crybola Ransom")
    rainbow_gradient_text("39. Crypt32 Ransom")
    rainbow_gradient_text("40. Crypt888 Ransom")
    rainbow_gradient_text("41. CryptON Ransom")
    rainbow_gradient_text("42. CryptXXX V1 Ransom")
    rainbow_gradient_text("43. CryptXXX V2 Ransom")
    rainbow_gradient_text("44. CryptXXX V3 Ransom")
    rainbow_gradient_text("45. CryptXXX V4 Ransom")
    rainbow_gradient_text("46. CryptXXX V5 Ransom")
    rainbow_gradient_text("47. CryptoMix Ransom")
    rainbow_gradient_text("48. Cryptokluchen Ransom")
    rainbow_gradient_text("49. Cyborg Ransom")
    rainbow_gradient_text("50. DXXD Ransom")
    rainbow_gradient_text("51. Daivol ransomware Ransom")
    rainbow_gradient_text("52. Damage Ransom")
    rainbow_gradient_text("53. Darkside Ransom")
    rainbow_gradient_text("54. Democry Ransom")
    rainbow_gradient_text("55. Derialock Ransom")
    rainbow_gradient_text("56. Dharma Ransom")
    rainbow_gradient_text("57. DoNex Ransom")
    rainbow_gradient_text("58. DragonCyber Ransom")
    rainbow_gradient_text("59. ElvisPresley Ransom")
    rainbow_gradient_text("60. EncrypTile Ransom")
    rainbow_gradient_text("61. Everbe 1.0 Ransom")
    rainbow_gradient_text("62. FONIX Ransom")
    rainbow_gradient_text("63. FenixLocker Ransom")
    rainbow_gradient_text("64. FilesLocker v1 and v2 Ransom")
    rainbow_gradient_text("65. FortuneCrypt Ransom")
    rainbow_gradient_text("66. Fury Ransom")
    rainbow_gradient_text("67. GalactiCryper Ransom")
    rainbow_gradient_text("68. GandCrab (V1, V4 and V5 up to V5.2 versions) Ransom")
    rainbow_gradient_text("69. GetCrypt Ransom")
    rainbow_gradient_text("70. Globe Ransom")
    rainbow_gradient_text("71. Globe/Purge Ransom")
    rainbow_gradient_text("72. Globe2 Ransom")
    rainbow_gradient_text("73. Globe3 Ransom")
    rainbow_gradient_text("74. GlobeImposter Ransom")
    rainbow_gradient_text("75. GoGoogle Ransom")
    rainbow_gradient_text("76. Gomasom Ransom")
    rainbow_gradient_text("77. HKCrypt Ransom")
    rainbow_gradient_text("78. Hakbit Ransom")
    rainbow_gradient_text("79. HermeticRansom Ransom")
    rainbow_gradient_text("80. HiddenTear Ransom")
    rainbow_gradient_text("81. HildaCrypt Ransom")
    rainbow_gradient_text("82. Hive (v1 to v4) Ransom")
    rainbow_gradient_text("83. HomuWitch Ransom")
    rainbow_gradient_text("84. Iams00rry Ransom")
    rainbow_gradient_text("85. InsaneCrypt Ransom")
    rainbow_gradient_text("86. Iwanttits Ransom")
    rainbow_gradient_text("87. JSWorm 2.0 Ransom")
    rainbow_gradient_text("88. JSWorm 4.0 Ransom")
    rainbow_gradient_text("89. Jaff Ransom")
    rainbow_gradient_text("90. JavaLocker Ransom")
    rainbow_gradient_text("91. Jigsaw Ransom")
    rainbow_gradient_text("92. Judge Ransom")
    rainbow_gradient_text("93. Kokokrypt Ransom")
    rainbow_gradient_text("94. LECHIFFRE Ransom")
    rainbow_gradient_text("95. LambdaLocker Ransom")
    rainbow_gradient_text("96. Lamer Ransom")
    rainbow_gradient_text("97. Linux.Encoder.1 Ransom")
    rainbow_gradient_text("98. .Encoder.3 Ransom")
    rainbow_gradient_text("99. LockFile Ransom")
    rainbow_gradient_text("100. Lockbit 3.0 Ransom")
    rainbow_gradient_text("101. LockerGoga Ransom")
    rainbow_gradient_text("102. Loocipher Ransom")
    rainbow_gradient_text("103. Lorenz Ransom")
    rainbow_gradient_text("104. Lortok Ransom")
    rainbow_gradient_text("105. MacRansom Ransom")
    rainbow_gradient_text("106. MafiaWare666 Ransom")
    rainbow_gradient_text("107. Magniber Ransom")
    rainbow_gradient_text("108. Mapo Ransom")
    rainbow_gradient_text("109. Marlboro Ransom")
    rainbow_gradient_text("110. Marsjoke aka Polyglot Ransom")
    rainbow_gradient_text("111. Maze / Sekhmet / Egregor Ransom")
    rainbow_gradient_text("112. MegaCortex Ransom")
    rainbow_gradient_text("113. MegaLocker Ransom")
    rainbow_gradient_text("114. Merry X-Mas Ransom")
    rainbow_gradient_text("115. MirCop Ransom")
    rainbow_gradient_text("116. Mira Ransom")
    rainbow_gradient_text("117. Mole Ransom")
    rainbow_gradient_text("118. Muhstik Ransom")
    rainbow_gradient_text("119. Nemty Ransom")
    rainbow_gradient_text("120. Nemucod Ransom")
    rainbow_gradient_text("121. NemucodAES Ransom")
    rainbow_gradient_text("122. Nmoreira Ransom")
    rainbow_gradient_text("123. NoWay Ransom")
    rainbow_gradient_text("124. Noobcrypt Ransom")
    rainbow_gradient_text("125. Onyx2 Ransom")
    rainbow_gradient_text("126. Ouroboros Ransom")
    rainbow_gradient_text("127. Ozozalocker Ransom")
    rainbow_gradient_text("128. Paradise Ransom")
    rainbow_gradient_text("129. Pewcrypt Ransom")
    rainbow_gradient_text("130. Philadelphia Ransom")
    rainbow_gradient_text("131. Planetary Ransom")
    rainbow_gradient_text("132. Pletor Ransom")
    rainbow_gradient_text("133. Plutocrypt Ransom")
    rainbow_gradient_text("134. Popcorn Ransom")
    rainbow_gradient_text("135. Professeur Ransom")
    rainbow_gradient_text("136. Prometheus Ransom")
    rainbow_gradient_text("137. Puma Ransom")
    rainbow_gradient_text("138. Pylocky Ransom")
    rainbow_gradient_text("139. RAGNAROK Ransom")
    rainbow_gradient_text("140. REvil/Sodinokibi Ransom")
    rainbow_gradient_text("141. Ragnar Ransom")
    rainbow_gradient_text("142. Rakhni Ransom")
    rainbow_gradient_text("143. RanHassan Ransom")
    rainbow_gradient_text("144. Rannoh Ransom")
    rainbow_gradient_text("145. Ransomwared Ransom")
    rainbow_gradient_text("146. RedRum Ransom")
    rainbow_gradient_text("147. Rhysida Ransom")
    rainbow_gradient_text("148. Rotor Ransom")
    rainbow_gradient_text("149. SNSLocker Ransom")
    rainbow_gradient_text("150. Shade Ransom")
    rainbow_gradient_text("151. SimpleLocker Ransom")
    rainbow_gradient_text("152. Simplocker Ransom")
    rainbow_gradient_text("153. Solidbit Ransom")
    rainbow_gradient_text("154. SpartCrypt Ransom")
    rainbow_gradient_text("155. Stampado Ransom")
    rainbow_gradient_text("156. SynAck Ransom")
    rainbow_gradient_text("157. Syrk Ransom")
    rainbow_gradient_text("158. TargetCompany Ransom")
    rainbow_gradient_text("159. Tarrak ransomware Ransom")
    rainbow_gradient_text("160. Teamxrat/Xpan Ransom")
    rainbow_gradient_text("161. TeslaCrypt V1 Ransom")
    rainbow_gradient_text("162. TeslaCrypt V2 Ransom")
    rainbow_gradient_text("163. TeslaCrypt V3 Ransom")
    rainbow_gradient_text("164. TeslaCrypt V4 Ransom")
    rainbow_gradient_text("165. Thanatos Ransom")
    rainbow_gradient_text("166. ThunderX Ransom")
    rainbow_gradient_text("167. Trustezeb Ransom")
    rainbow_gradient_text("168. TurkStatic Ransom")
    rainbow_gradient_text("169. VCRYPTOR Ransom")
    rainbow_gradient_text("170. WannaCryFake Ransom")
    rainbow_gradient_text("171. Wildfire Ransom")
    rainbow_gradient_text("172. XData Ransom")
    rainbow_gradient_text("173. XORBAT Ransom")
    rainbow_gradient_text("174. XORIST Ransom")
    rainbow_gradient_text("175. Yatron Ransom")
    rainbow_gradient_text("176. ZQ Ransom")
    rainbow_gradient_text("177. ZeroFucks Ransom")
    rainbow_gradient_text("178. Ziggy Ransom")
    rainbow_gradient_text("179. Zorab Ransom")
    rainbow_gradient_text("180. djvu Ransom")
    choice = input("Select Decryption Tool: ")

    if choice == "1":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "2":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_aes_ni.exe")
    elif choice == "3":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "4":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_akira64.exe")

    elif choice == "5":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_alcatrazlocker.exe")
    elif choice == "6":
        webbrowser.open("https://www.bleepingcomputer.com/download/alphadecrypter/dl/329/")
    elif choice == "7":
        webbrowser.open("https://decrypter.emsisoft.com/download/amnesia")
    elif choice == "8":
        webbrowser.open("https://decrypter.emsisoft.com/download/amnesia2")
    elif choice == "9":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDAnnabelleDecryptTool.exe")
    elif choice == "10":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/astralocker")
    elif choice == "11":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_atomsilo.exe")
    elif choice == "12":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "13":
        webbrowser.open("https://www.bleepingcomputer.com/download/auroradecrypter/dl/379/")
    elif choice == "14":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip")

    elif choice == "15":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "16":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDAvaddonDecryptor.exe")
    elif choice == "17":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/avest")
    elif choice == "18":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_btcware.exe")
    elif choice == "19":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_babuk.exe")
    elif choice == "20":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "21":
        webbrowser.open("https://blog.checkpoint.com/wp-content/uploads/2017/03/BarRaxDecryptor.zip")
    elif choice == "22":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDBartDecryptor.exe")
    elif choice == "23":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_bianlian.exe")
    elif choice == "24":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/bigbobross")

    elif choice == "25":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/CoinVaultDecryptor.zip")
    elif choice == "26":
        webbrowser.open("https://github.com/srlabs/black-basta-buster/archive/refs/heads/master.zip")
    elif choice == "27":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "28":
        webbrowser.open("https://github.com/Truesec/TSDecryptors/releases/download/v1.0.0.0/Truesec.Decryptors-1.0.0.0.zip")
    elif choice == "29":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/checkmail7")
    elif choice == "30":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/chernolocker")
    elif choice == "31":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "32":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/CoinVaultDecryptor.zip")
    elif choice == "33":
        webbrowser.open("https://decrypter.emsisoft.com/download/cry128")
    elif choice == "34":
        webbrowser.open("https://decrypter.emsisoft.com/download/cry9")

    elif choice == "35":
        webbrowser.open("https://github.com/eset/cry-decryptor/releases/download/v1.0/CryDecryptor.apk")
    elif choice == "36":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "37":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "38":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip")
    elif choice == "39":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/crypt32")
    elif choice == "40":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_crypt888.exe")
    elif choice == "41":
        webbrowser.open("https://decrypter.emsisoft.com/download/crypton")
    elif choice == "42":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "43":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "44":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")

    elif choice == "45":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "46":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "47":
        webbrowser.open("https://nomoreransom.cert.pl/static/cryptomix_decryptor.exe")
    elif choice == "48":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "49":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/cyborg")
    elif choice == "50":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "51":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/diavol")
    elif choice == "52":
        webbrowser.open("https://decrypter.emsisoft.com/download/damage")
    elif choice == "53":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDDarkSideDecryptor.exe")
    elif choice == "54":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")

    elif choice == "55":
        webbrowser.open("https://www.bleepingcomputer.com/download/stupiddecryptor/dl/351/")
    elif choice == "56":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    if choice == "57":
        webbrowser.open("https://sector7.computest.nl/downloads/DoNexDecrypt.zip")
    elif choice == "58":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/jigsaw")
    elif choice == "59":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/jigsaw")
    elif choice == "60":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_encryptile.exe")
    elif choice == "61":
        webbrowser.open("https://www.bleepingcomputer.com/download/insanecrypt-desucrypt-decrypter/dl/369/")
    elif choice == "62":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDFONIXDecryptor.exe")
    elif choice == "63":
        webbrowser.open("https://decrypter.emsisoft.com/download/fenixlocker")
    elif choice == "64":
        webbrowser.open("https://www.bleepingcomputer.com/download/fileslockerdecrypter/dl/378/")

    elif choice == "65":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "66":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip")
    elif choice == "67":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/galacticrypter")
    elif choice == "68":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDGandCrabDecryptTool.exe")
    elif choice == "69":
        webbrowser.open("https://www.emsisoft.com/decrypter/download/getcrypt")
    elif choice == "70":
        webbrowser.open("https://decrypter.emsisoft.com/download/globe")
    elif choice == "71":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "72":
        webbrowser.open("https://decrypter.emsisoft.com/download/globe2")
    elif choice == "73":
        webbrowser.open("https://decrypter.emsisoft.com/download/globe3")
    elif choice == "74":
        webbrowser.open("https://decrypter.emsisoft.com/download/globeimposter")
    elif choice == "75":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDGoGoogleDecryptor.exe")
    elif choice == "76":
        webbrowser.open("https://decrypter.emsisoft.com/download/gomasom")
    elif choice == "77":
        webbrowser.open("https://decrypter.emsisoft.com/download/hkcrypt")
    elif choice == "78":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/hakbit")
    elif choice == "79":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_hermeticransom.exe")
    elif choice == "80":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_hiddentear.exe")
    elif choice == "81":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/hildacrypt")
    elif choice == "82":
        webbrowser.open("https://seed.kisa.or.kr/kisa/Board/133/detailView.do")
    elif choice == "83":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_homuwitch.exe")
    elif choice == "84":
        webbrowser.open("https://www.emsisoft.com/decrypter/ims00rry")
    elif choice == "85":
        webbrowser.open("https://www.bleepingcomputer.com/download/insanecrypt-desucrypt-decrypter/dl/369/")
    elif choice == "86":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/ransomwared")
    elif choice == "87":
        webbrowser.open("https://www.emsisoft.com/decrypter/download/jsworm-20")
    elif choice == "88":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/jsworm-40")
    elif choice == "89":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "90":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/javalocker")
    elif choice == "91":
        webbrowser.open("https://www.bleepingcomputer.com/download/stupiddecryptor/dl/351/")
    elif choice == "92":
        webbrowser.open("https://mdsassets.blob.core.windows.net/downloads/Judge-Decryptor.exe")
    elif choice == "93":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/kokokrypt")
    elif choice == "94":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "95":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_lambdalocker.exe")
    elif choice == "96":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "97":
        webbrowser.open("https://labs.bitdefender.com/wp-content/plugins/download-monitor/download.php?id=Decrypter_0-1.3.zip")
    elif choice == "98":
        webbrowser.open("https://labs.bitdefender.com/wp-content/plugins/download-monitor/download.php?id=encoder_3_decrypter.zip")
    elif choice == "99":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_atomsilo.exe")
    elif choice == "100":
        webbrowser.open("https://www.nomoreransom.org/uploads/check_decryption_id_manual.zip")
    elif choice == "101":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDLockerGogaDecryptTool.exe")
    elif choice == "102":
        webbrowser.open("https://www.emsisoft.com/decrypter/loocipher")
    elif choice == "103":
        webbrowser.open("https://mdsassets.blob.core.windows.net/downloads/Lorenz-Decryptor.exe")
    elif choice == "104":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "105":
        webbrowser.open("https://esupport.trendmicro.com/media/13801530/Trend%20Micro%20Ransomware%20Decryptor_V1.0.1.zip")
    elif choice == "106":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_mafiaware666.exe")
    elif choice == "107":
        webbrowser.open("https://seed.kisa.or.kr/kisa/Board/56/detailView.do")
    elif choice == "108":
        webbrowser.open("https://nomoreransom.cert.pl/static/mapo_decryptor.exe")
    elif choice == "109":
        webbrowser.open("https://decrypter.emsisoft.com/download/marlboro")
    elif choice == "110":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip")
    elif choice == "111":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "112":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDMegaCortexDecryptTool.exe")
    elif choice == "113":
        webbrowser.open("https://www.emsisoft.com/decrypter/download/megalocker")
    elif choice == "114":
        webbrowser.open("https://blog.checkpoint.com/wp-content/uploads/2017/03/MXM_Decryptor-3.7z")
    elif choice == "115":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "116":
        webbrowser.open("https://download.f-secure.com/support/tools/Mira-decryptor/Mira%20Ransomware%20Decryptor.zip")
    elif choice == "117":
        webbrowser.open("https://nomoreransom.cert.pl/static/mole_decryptor.exe")
    elif choice == "118":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/muhstik")
    elif choice == "119":
        webbrowser.open("https://mdsassets.blob.core.windows.net/downloads/NemtyDecryptor.exe")
    elif choice == "120":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "121":
        webbrowser.open("https://decrypter.emsisoft.com/download/nemucodaes")
    elif choice == "122":
        webbrowser.open("https://decrypter.emsisoft.com/download/nmoreira")
    elif choice == "123":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/noway")
    elif choice == "124":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_noobcrypt.exe")
    elif choice == "125":
        webbrowser.open("https://github.com/Truesec/TSDecryptors/releases/download/v1.0.0.0/Truesec.Decryptors-1.0.0.0.zip")
    elif choice == "126":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDOuroborosDecryptTool.exe")
    elif choice == "127":
        webbrowser.open("https://decrypter.emsisoft.com/download/ozozalocker")
    elif choice == "128":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/paradise")
    elif choice == "129":
        webbrowser.open("https://decrypter.emsisoft.com/download/pewcrypt")
    elif choice == "130":
        webbrowser.open("https://decrypter.emsisoft.com/download/philadelphia")
    elif choice == "131":
        webbrowser.open("https://decrypter.emsisoft.com/download/planetary")
    elif choice == "132":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "133":
        webbrowser.open("https://github.com/prodaft/malware-ioc/raw/master/PlutoCrypt/plutocrypt_decryptor.exe")
    elif choice == "134":
        webbrowser.open("https://www.elevenpaths.com/innovation-labs/technologies/recover-popcorn#eulaModal")
    elif choice == "135":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/jigsaw")
    elif choice == "136":
        webbrowser.open("https://github.com/cycraft-corp/Prometheus-Decryptor/releases/download/1.2/prometheus_decryptor.zip")
    elif choice == "137":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/stop-puma")
    elif choice == "138":
        webbrowser.open("https://github.com/Cisco-Talos/pylocky_decryptor")
    elif choice == "139":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/ragnarok")
    elif choice == "140":
        webbrowser.open("http://download.bitdefender.com/am/malware_removal/BDREvilDecryptor.exe")
    elif choice == "141":
        webbrowser.open("https://seed.kisa.or.kr/async/MultiFile/download.do?FS_KEYNO=FS_0000000415&amp;MNK=MN_0000001279")
    elif choice == "142":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "143":
        webbrowser.open("https://download.bitdefender.com/am/malware_removal/BDRanHassanDecryptTool.exe")
    elif choice == "144":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip")
    elif choice == "145":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/ransomwared")
    elif choice == "146":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/redrum")
    elif choice == "147":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_rhysida.exe")
    elif choice == "148":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "149":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "150":
        webbrowser.open("https://www.mcafee.com/us/downloads/free-tools/shadedecrypt.aspx")
    elif choice == "151":
        webbrowser.open("https://seed.kisa.or.kr/kisa/Board/57/detailView.do")
    elif choice == "152":
        webbrowser.open("https://download.eset.com/com/eset/tools/decryptors/simplocker/latest/eset-simplocker-decryptor.apk")
    elif choice == "153":
        webbrowser.open("https://github.com/Truesec/TSDecryptors/releases/download/v1.0.0.0/Truesec.Decryptors-1.0.0.0.zip")
    elif choice == "154":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/spartcrypt")
    elif choice == "155":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "156":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/synack")
    elif choice == "157":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/syrk")
    elif choice == "158":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_targetcompany64.exe")
    elif choice == "159":
        webbrowser.open("https://files.avast.com/files/decryptor/avast_decryptor_tarrak64.exe")
    elif choice == "160":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "161":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "162":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "163":
        webbrowser.open("https://www.mcafee.com/us/downloads/free-tools/tesladecrypt.aspx")
    elif choice == "164":
        webbrowser.open("https://github.com/Cisco-Talos/TeslaDecrypt")
    elif choice == "165":
        webbrowser.open("https://github.com/Cisco-Talos/ThanatosDecryptor")
    elif choice == "166":
        webbrowser.open("https://mdsassets.blob.core.windows.net/downloads/ThunderX-Decryptor.exe")
    elif choice == "167":
        webbrowser.open("https://download.eset.com/com/eset/tools/decryptors/trustezeb_a/latest/esettrustezebadecoder.exe")
    elif choice == "168":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/turkstatik")
    elif choice == "169":
        webbrowser.open("https://www.elevenpaths.com/downloads/vcrypt_decryptor.zip")
    elif choice == "170":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/wannacryfake")
    elif choice == "171":
        webbrowser.open("https://www.mcafee.com/us/downloads/free-tools/wildfiredecrypt.aspx")
    elif choice == "172":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "173":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "174":
        webbrowser.open("https://powerbox-na-file.trend.org/SFDC/DownloadFile_iv.php?jsonInfo=%7b%22Query%22%3a%22jn1XVHnvtwlVGuZ9XTrPudWOVgKHfE1fVf4mh9XXETPsT4jEX1DzaXiIio6niXlTxEHkXvbf%2fag68Dmuv%2fz0adD%2f3a4rmG1FhFP7q1cJhqLLyvO8VuBr65fUerKjrrzMQWzRT86MuUneIx7%2b%2bi8LufENTYCTK1vakiJw0ij34qulyJRwqAHlBbxuMm5Zy%2b5BmueD%2bfAyd%2bJceSs3oSW6q3VL9gl11LWas2jPQvUCZM9D9UDepgprqnQtF%2fU7D7%2bon%2b3OSp8OdBwED8qp9RgXb53hqzal2kXNlyntYczTaOo%3d%22%2c%22iv%22%3a%22db0d918f007fe97830d4cbc2e44b4cd2%22%7d")
    elif choice == "175":
        webbrowser.open("https://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip")
    elif choice == "176":
        webbrowser.open("https://www.emsisoft.com/decrypter/download/zq")
    elif choice == "177":
        webbrowser.open("https://www.emsisoft.com/decrypter/zerofucks")
    elif choice == "178":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/ziggy")
    elif choice == "179":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/zorab")
    elif choice == "180":
        webbrowser.open("https://www.emsisoft.com/ransomware-decryption-tools/download/stop-djvu")
    else:
        rainbow_gradient_text("Invalid choice.")
        main_menu()

if __name__ == "__main__":
    main_menu()
