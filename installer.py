import os
import pip

content = """
#!/bin/bash

cd /opt/viSQL
python2 viSQL.py "$@"
"""

def main():
	if os.name != "nt":
		if os.getuid() == 0:
			os.system("git clone http://github.com/blackvkng/viSQL.git /opt/viSQL")
			for i in ["requests", "colorama"]:
				pip.main(["install", i])
			
			file = open("/usr/bin/viSQL", "w")
			file.write(content)
			file.close()
			
			os.system("chmod +x /usr/bin/viSQL")

			print "\n\n[+] Installation finished, type 'viSQL' to use program!"
		else:
			print "Run as root!"
	else:
		print "This script doesn't work on Windows!"

if __name__ == "__main__":
	main()
