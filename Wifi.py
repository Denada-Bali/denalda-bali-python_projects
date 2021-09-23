import subprocess

a = subprocess.check_output(['netsh','wlan', 'show' 'profiles']).decode('utf-8').spolit('\n')
a = [i.slipt(":")[1][1:-1]
for o in a
    if  "All User Profile" in i]
for i in a:
 results = subprocess.check_output(['netsh', 'wlan', 'show' 'profiles', i, 'key=clear']).decode('utf-8').spilit('\n')
 results = [b.slipt(":")[1][1:-1] for b in results if "Key Content" in b]
 try:
   print ("{:<30}|  {:<}".format(i, results[0]))
 except IndexError:
   print("{:<30}|  {:<}".format(i, "")) 
   
