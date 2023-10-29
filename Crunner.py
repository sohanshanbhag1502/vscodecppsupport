from subprocess import run
from sys import argv
from os import remove

f=open(r"C:\Windows\Temp\tep.txt", 'w')
run(["g++", argv[2], argv[3], argv[4]], shell=True)
try:
    run([argv[4]], stderr=f, shell=True)
    remove(argv[4])
except:
    exit(0)
finally:
    f.close()