#!/usr/bin/python
#!
#!批量创建OC类
import os
import shutil
 


def createHFile():
	for index in range(0,120):
		fp = open("TestLoad"+str(index)+".h","w")
		fp.write("#import <Foundation/Foundation.h>\n")
		fp.write("@interface TestLoad"+str(index)+" : NSObject\n")
		fp.write("@end")
		fp.flush()
		fp.close()
		
		
def createMFile():
	for index in range(0,120):
		fp = open("TestLoad"+str(index)+".m","w")
		fp.write("#import \"TestLoad"+str(index)+".h\"\n")
		fp.write("#import \"ViewController.h\"\n")
		fp.write("@implementation TestLoad"+str(index)+"\n")
		fp.write("+ (void)load{\n")
		fp.write("static dispatch_once_t onceToken;\n")
		fp.write("dispatch_once(&onceToken, ^{\n")
		fp.write("[ViewController setViewController:NSStringFromClass(self) forViewModel:NSStringFromClass(self)];\n")
		fp.write("});\n")
		fp.write("}\n")
		fp.write("@end")
		fp.flush()
		fp.close()
		
		
createHFile()
createMFile()

		
	
	
	