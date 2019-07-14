# import subprocess
# subprocess.run('cd seleniumtest-master/seleniumtest/ && python sele.py', shell=True)
import subprocess
sub = subprocess.Popen("ls", cwd='seleniumtest-master/seleniumtest/',stdout=subprocess.PIPE)
out = sub.stdout.read()
print(str(out, encoding='utf-8'))
print(bytes.decode(out))