import os
if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
else:
    print("no existe")