#!/usr/bin/python
#coding=utf-8
import os,shutil

def moveFileToPath(extName,sourcePath,targetPath):
	folder = os.path.exists(targetPath)
	if not folder:
		os.mkdir(targetPath)
		print("文件夹不存在，创建文件夹\t"+targetPath)
	else:
		print("文件夹"+targetPath+"存在")
	print("开始搜索:"+sourcePath)
	for root,dirs,files in os.walk(sourcePath,topdown=True):
		print("fafafee:\t"+root)
		for file in files:
			print(file)
			if os.path.splitext(file)[-1] == extName:
				current_path = root+'/'+file
				print("当前路径1:\t"+current_path)
				print("是后缀名为"+extName+"的文件")
				shutil.move(current_path, targetPath+'/'+file)
					

if __name__ == "__main__":
	ext_name = ".mkv";
	target_path = "/Users/heboyce/Downloads/guike"
	path_list = [];
	path_list.append("/Users/heboyce/Downloads/www.tskscn.com33")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(1).com5")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(2).com6")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(2).com7")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(3).com8")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(3).com9")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(4).com10")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(4).com11")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(5).com12")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(6).com13")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(7).com14")
	path_list.append("/Users/heboyce/Downloads/www.tskscn(8).com15")
	path_list.append("/Users/heboyce/Downloads/www.tskscn.com1")
	path_list.append("/Users/heboyce/Downloads/www.tskscn.com12")
	path_list.append("/Users/heboyce/Downloads/www.tskscn.com2")
	
	for path in path_list:
		moveFileToPath(ext_name,path,target_path)
		
	
		