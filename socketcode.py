import socket as s

class so():
	def __init__(sd, target):
		sd.target_ip = target
	def scan_port(sd):
		print("Open ports:")
		for port in range(1,1024):
			sd.s1 = s.socket(s.AF_INET, s.SOCK_STREAM)
			sd.result = sd.s1.connect_ex((sd.target_ip, port))
			sd.s1.settimeout(0.5)
			if sd.result == 0:
				print(f"{port}")
			sd.s1.close()

t = input("What is the target ip or domain name:")
try:
	t_ip = s.gethostbyname(t)
except:
	print("Ip address or hostname is unknown")
	exit()
print(f"scan started on {t_ip}")
scanstart = so(t_ip)
scanstart.scan_port()
print("scan completed")

