import os
for pind in range (1,109):
    os.chdir ("./data_norm")
    os.system("mkdir {}".format(pind))
    os.chdir("../data/{}".format(pind))
    flist = os.listdir(".")
    for fname in flist:
        os.system("wine /home/harshit/Downloads/USITv2.4.2/bin/caht.exe -i {} -o ../../data_norm/{}/{} -s 224 224".format(fname,pind,fname))
    os.chdir ("../..")
