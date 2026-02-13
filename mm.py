import os
import sys
import builtins

path = "/data/user/0/ru.iiec.pyahmed/files/aarch64-linux-android/lib64/python3.11"

code = r'''import sys, os, builtins
def jack_exit(*args, **kwargs):
    return None  
sys.exit = jack_exit
os._exit = jack_exit
builtins.exit = jack_exit
builtins.quit = jack_exit
'''

filename = "sitecustomize.py"
file = os.path.join(path, filename)

try:
    os.makedirs(path, exist_ok=True)
    with open(file, "w", encoding="utf-8") as f:
        f.write(code)
    print('تم التحويل بنجاح ⚜️')    
except PermissionError:
    print("[!] راسلني مطور الاداة  @C_WC2.")
