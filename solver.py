#!usr/bin/env python

encrypted = open('encrypted', 'r').readline()
known = "GamaCTF{"

while True:
	for i in range(0,256):
		flag = known+chr(i)+""

		cipher = ""
		for x in range(len(flag)):
			for y in range(x):
				for z in range(y):
					cipher += str(ord(flag[z]) + ord(flag[x]) - ord(flag[y]))
					
		if cipher[:len(cipher)] == encrypted[:len(cipher)]:
			known += chr(i)
			print known


