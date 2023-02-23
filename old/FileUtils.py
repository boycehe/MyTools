
import os
import copy
import shutil

#替换特定地字符串
def replace_specify_name(fileDirs,oldName,replaceName):
    allFileNames = os.listdir(fileDirs)
    for fName in allFileNames:
        (path,fileName) = os.path.split(fName)
        tmpOldName = copy.deepcopy(fileName)
        fileName = fileName.replace(oldName,replaceName)
        rename_file(fileDirs,tmpOldName,fileDirs,fileName)
#重命名
def rename_file(srcDir,srcName,dstDir,dstName):
    src = os.path.join(srcDir, srcName)
    dst = os.path.join(dstDir, dstName)
    os.rename(src,dst)


##将特定字符串移动到文件名地最前
def rename_File_Case1(fileDirs,moveHeadName):
    allFileNames = os.listdir(fileDirs)
    for fName in allFileNames:
        (path,fileName) = os.path.split(fName)
        if moveHeadName in fileName:
            oldName = copy.deepcopy(fileName)
            fileName = fileName.replace("small_weather_","")
            fileName = moveHeadName + fileName
            rename_file(fileDirs,oldName,fileDirs,fileName)

##将含有特定字符串地文件移动到指定地目录
def move_contain_specifiy_name_to_another_dir(oldFileDir,specifyName,newFileDir):
    allFileNames = os.listdir(oldFileDir)
    for fName in allFileNames:
        if specifyName in fName:
            src = os.path.join(oldFileDir, fName)
            dst = os.path.join(newFileDir, fName)
            shutil.move(src, dst)



if __name__=="__main__":
    move_contain_specifiy_name_to_another_dir("C:\\Users\\Administrator\\Downloads\\data","weather_","C:\\Users\\Administrator\\Downloads\\data\\normal")
    replace_specify_name("C:\\Users\\Administrator\\Downloads\\data\\normal","weather_.",".")