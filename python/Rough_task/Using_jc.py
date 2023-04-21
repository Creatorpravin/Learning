import subprocess
import jc

data = []

try:
 #  cmd_output = subprocess.check_output(['iptables','-t', 'nat' ,'-nvL'], text=True)
   cmd_output = subprocess.run(['iptables','-t', 'nat' ,'-nvL'],check=True, capture_output=True, text=True)
   print(cmd_output.stderr)
#   print(cmd_output.stderr)
   data = jc.parse('iptables', cmd_output.stdout)

except Exception as exception:
   print("Error while execute iptables command",exception)


print(data)

