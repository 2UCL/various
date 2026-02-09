import os

file_names = [""]

for fn in file_names:
    fsize = os.path.getsize(fn)

    with open(fn, "wb") as f:
        for i in range(fsize):
            f.write(bytes(1))
        f.flush()