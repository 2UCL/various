import os

file_names = [""]

for fn in file_names:
    print("Processing " + fn + "...")
    fsize = os.path.getsize(fn)

    with open(fn, "wb") as f:
        for i in range(fsize):
            f.write(bytes(1))
        f.flush()
    
    with open(fn, "wb") as f:
        for i in range(fsize):
            f.write(b"\xff")
        f.flush()
        

print("Done!\n")
