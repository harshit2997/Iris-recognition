from torchvision import transforms, datasets, models
import torch
from torch import optim, cuda
from torch.autograd import Variable
from torch.utils.data import DataLoader, sampler
import torch.nn as nn
import pickle as pk

datadir = './'
traindir = datadir + 'train/'
testdir = datadir + 'test/'

batch_size = 535

trans = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


# Datasets from each folder
data = {
    'train':
    datasets.ImageFolder(root=traindir, transform=trans),
    #'test':
    #datasets.ImageFolder(root=testdir, transform=trans)
}

# Dataloader iterators
dataloaders = {
    'train': DataLoader(data['train'], batch_size=batch_size, shuffle=True),
    #'test': DataLoader(data['test'], batch_size=batch_size, shuffle=True)
}


model = models.resnet18(pretrained=True)
model.eval()


l1= list(model.children())
#now, bilding custom model i.e. uptil some layer of the original network. WIll be done differently for differen networks and different layer numbers
l2 = list(list(l1[6].children())[0].children())
m2 = nn.Sequential(*l1[:6])
model_cur=m2
for param in model_cur.parameters():
    param.requires_grad = False
#model_cur = model_cur.to('cuda')
inputs, labels = next(iter(dataloaders['train']))
inputs, labels = Variable(inputs), Variable(labels)

print "Data Loaded"
outputs = model_cur(inputs)
print "Outputs calculated"
print str(inputs.data.shape)
print str(outputs.data.shape)

outputs = outputs.cpu().numpy()
labels = labels.cpu().numpy()

#res in filenames is for resnet

f_out = open ("f_out_res","wb+")
f_lab = open ("f_lab_res","wb+")

pk.dump(outputs,f_out)
pk.dump(labels,f_lab)

f_out.close()
f_lab.close()
