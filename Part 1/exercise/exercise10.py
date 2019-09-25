#%%
import sys


for i in range(1, 11):
    for j in range(i):
        sys.stdout.write(chr(219))
        sys.stdout.write(chr(219))
    sys.stdout.write("\n")


#%%
