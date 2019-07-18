#!/usr/bin/python2.7

#"<span style=""font-family:Arial;font-size:18px;"">"
#"<span style=""font-size:18px;"">"
#"<span style=""font-size:18px;"">"
import os
def IsSubString(SubStrList,Str):
    flag=True
    for substr in SubStrList:
        if not(substr in Str):
            flag=False
    return flag
#scan file
def GetFileList(FindPath,FlagStr=[]):
    FileList=[]
    FileNames=os.listdir(FindPath)
    if len(FileNames)>0:
        for fn in FileNames:
            if len(FlagStr)>0:
                if IsSubString(FlagStr,fn):
                    fullfilename=os.path.join(FindPath,fn)
                    FileList.append(fullfilename)
            else:
                fullfilename=os.path.join(FindPath,fn)
                FileList.append(fullfilename)
    if len(FileList)>0:
        FileList.sort()
    return FileList

#train dataset code
train_txt=open('train.txt','w')
#create label data, if airplane, setting label to 0, if car, setting label to 1, if horse ,setting label to 2
imgfile=GetFileList('train/train_car')
for img in imgfile:
    str1=img+' '+'1'+'\n' 
    train_txt.writelines(str1)

imgfile=GetFileList('train/train_airplane')
for img in imgfile:
    str2=img+' '+'0'+'\n'
    train_txt.writelines(str2)

imgfile=GetFileList('train/train_horse')
for img in imgfile:
    str3=img+' '+'2'+'\n' 
    train_txt.writelines(str3)
train_txt.close()

#test dataset list
test_txt=open('val.txt','w')
imgfile=GetFileList('val/val_car')
for img in imgfile:
    str4=img+' '+'1'+'\n'
    test_txt.writelines(str4)

imgfile=GetFileList('val/val_airplane')
for img in imgfile:
    str5=img+' '+'0'+'\n'
    test_txt.writelines(str5)

imgfile=GetFileList('val/val_horse')
for img in imgfile:
    str6=img+' '+'2'+'\n'
    test_txt.writelines(str6)
test_txt.close()
print("Creating successful")
