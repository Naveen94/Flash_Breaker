import os
import os.path
import re

i=0
a={}
local={}

# For finding all the .as files

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".as")]:
        a[i]=os.path.join(dirpath, filename)
        i+=1



j=0

#for removing the leadspaces in those .as files

while j<i:
    local[j]=a[j]+'_Stripped.txt' 
    f = open('%s' %local[j],'a+')
    with open (a[j], "r") as myfile:
        for line in myfile:
            cl = line.lstrip()
            if cl:
                f.write(cl)
    j +=1
    


count =0
c=0

#Finding Vulnerable Flash Methods

while c<i:
    g=open('%s_Match.txt' %a[count],'a+')
    with open('signatures.txt','r') as FlashSIG:
        for line1 in FlashSIG:
            inc =0 
            with open('%s' %local[count],'r') as FlashIP:
                for line2 in FlashIP:
                    if re.search(line1.rstrip(), line2.rstrip()):
                        g.write('Line %s - '%inc + line2)
                    inc +=1
    g.flush()
    g.close()
    count +=1
    c +=1