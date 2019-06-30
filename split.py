import os
for i in range(1,108):
    os.system("mkdir ./train/{}".format(i))
    os.system("mkdir ./test/{}".format(i))
    os.chdir("./data_norm/{}".format(i))
    flist = os.listdir(".")
    for j in range (5):
        os.system(" cp ./{} ../../train/{}".format(flist[j],i))
    for j in range(5,7):
        os.system(" cp ./{} ../../test/{}".format(flist[j],i))
    os.chdir("../../")