'''
Created on 2015-6-24

@author: songshunzhang
'''
#!/usr/bin/python  
# -*- coding=utf-8 -*-
import os
import zipfile
import fileinput
import shutil
import re
import xml.etree.ElementTree as ET
currentpath = "/Volumes/Macintosh_HD_E/decompile"
cputype = "armeabi"
orientation = "port"


oprators = {}

def generateop(type, path): 
    
    cocospay = "cocospay"
    oprators[cocospay] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/cocospay";
    if type == "gb":
        gb = "gb";
        oprators[gb] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/gb_20130"
    elif type == "mm":
        mm = "mm"
        oprators[mm] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/mm_3.1.3"
    elif type == "unicom":
        unicom = "uni_com"
        oprators[unicom] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/unipay_2.0.1_0509_report"
    elif type == "egame":
        egame = "egame"
        oprators[egame] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/egame_4.1.0"
        unicom = "uni_com";
        oprators[unicom] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/unipay_2.0.1_0509"    
        gb = "gb"
        oprators[gb] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/gb_20130"
    elif type == "common":
        egame = "egame"
        oprators[egame] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/egame_4.1.0"
        unicom = "uni_com";
        oprators[unicom] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/unipay_2.0.1_0509"    
        gb = "gb";
        oprators[gb] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/gb_20130"
        mm = "mm"
        oprators[mm] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/mm_3.1.3"
    else:
        oprators[cocospay] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/cocospay";    
        gb = "gb";
        oprators[gb] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/gb_20130";
        unicom = "uni_com";
        oprators[unicom] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/unipay_2.0.1_0509"
        mm = "mm"
        oprators[mm] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/mm_3.1.3"
        egame = "egame"
        oprators[egame] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/egame_4.1.0"
        egamelite = "egamelite"
        oprators[egamelite] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/egamelite"    
        pb = "pb"
        oprators[pb] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/pb_alipay"
        uni_com_sms = "uni_com_sms"
        oprators[uni_com_sms] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/unipaylite"
        hfb = "hfb"
        oprators[hfb] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/hfsw_2.0.0"
        mdo = "mdo"
        oprators[mdo] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/mdo"
        
    print oprators
    generateapkraw(type)       
    
    '''
    unicom = "uni_com";
    oprators[unicom] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/unipay_2.0.1_0509_report";
    '''
    '''
    mm = "mm"
    oprators[mm] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/mm_3.1.3"
    '''
    '''
    egame = "egame"
    oprators[egame] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/egame_4.1.0"
    unicom = "uni_com";
    oprators[unicom] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/unipay_2.0.1_0509"    
    gb = "gb";
    oprators[gb] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/gb_20130"
    mm = "mm"
    oprators[mm] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/mm_3.1.3"
    '''
    '''
    cocospay = "cocospay"
    oprators[cocospay] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/cocospay";    
    gb = "gb";
    oprators[gb] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/gb_20130";
    unicom = "uni_com";
    oprators[unicom] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/unipay_2.0.1_0509"
    mm = "mm"
    oprators[mm] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/mm_3.1.3"
    egame = "egame"
    oprators[egame] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/egame_4.1.0"
    egamelite = "egamelite"
    oprators[egamelite] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/egamelite"    
    pb = "pb"
    oprators[pb] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/pb_alipay"
    uni_com_sms = "uni_com_sms"
    oprators[uni_com_sms] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/unipaylite"
    hfb = "hfb"
    oprators[hfb] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/hfsw_2.0.0"
    mdo = "mdo"
    oprators[mdo] = "/Volumes/Macintosh_HD_E/decompile/CocopaySDK/SDKs/mdo"
    '''
 
def generatefilter(path,type):
    if type == "gb":
        filepath = os.path.join(path, "assets/filter")
        open(filepath ,"wb").write("0")
                        
    elif type == "mm":
        filepath = os.path.join(path, "assets/filter")
        open(filepath ,"wb").write("1")
        folder_path_one = os.path.join(path, "assets/splash/480x320")
        if not os.path.exists(folder_path_one):
            os.makedirs(folder_path_one)
        splash_one = os.path.join(folder_path_one, "splash.png")
        if orientation == "port":
            splash_one_raw = os.path.join(currentpath, "splash/mm/port/480x320/splash.png")
        else:
            print "fucking ---------------"
            splash_one_raw = os.path.join(currentpath, "splash/mm/land/480x320/splash.png")            
         
        shutil.copy(splash_one_raw, splash_one)
        
        folder_path_two = os.path.join(path, "assets/splash/960x640")
        if not os.path.exists(folder_path_two):
            os.makedirs(folder_path_two)
        
        splash_two = os.path.join(folder_path_two, "splash.png")
        if orientation == "port":
            splash_two_raw = os.path.join(currentpath, "splash/mm/port/960x640/splash.png") 
        else:
            splash_two_raw = os.path.join(currentpath, "splash/mm/land/960x640/splash.png")            
        
        shutil.copy(splash_two_raw, splash_two)
             
    elif type == "unicom":
        filepath = os.path.join(path, "assets/filter")
        open(filepath ,"wb").write("103")    
                    
    elif type == "egame":
        filepath = os.path.join(path, "assets/filter")
        open(filepath ,"wb").write("201|0,103")  
          
        folder_path_one = os.path.join(path, "assets/splash/480x320")
        if not os.path.exists(folder_path_one):
            os.makedirs(folder_path_one)
        splash_one = os.path.join(folder_path_one, "splash.png")
        if orientation == "port":
            splash_one_raw = os.path.join(currentpath, "splash/egame/port/480x320/splash.png") 
        else:
            splash_one_raw = os.path.join(currentpath, "splash/egame/land/480x320/splash.png")        
         
        shutil.copy(splash_one_raw, splash_one)
        
        folder_path_two = os.path.join(path, "assets/splash/960x640")
        if not os.path.exists(folder_path_two):
            os.makedirs(folder_path_two)
        
        splash_two = os.path.join(folder_path_two, "splash.png")
        if orientation == "port":
            splash_two_raw = os.path.join(currentpath, "splash/egame/port/960x640/splash.png") 
        else:
            splash_two_raw = os.path.join(currentpath, "splash/egame/land/960x640/splash.png")
         
        shutil.copy(splash_two_raw, splash_two)
                   
    else:
        pass    
    
    
def generateapkraw(type):
    projectname = "TestDemo"
    output = currentpath + "/" + projectname
    if not os.path.exists(output):
        os.makedirs(output)
    sourceFile = os.path.join(currentpath,  "AndroidManifest.xml") 
    targetFile = os.path.join(output,  "AndroidManifest.xml")
    if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
        open(targetFile, "wb").write(open(sourceFile, "rb").read())        
    print "ko"
    androidcmd = "android update project --name " + projectname + " -t 1 -p " + output
    print androidcmd
    androidoutput = os.popen(androidcmd).readlines()
    print androidoutput
    androidsrc = output + "/src"
    if not os.path.exists(androidsrc):
        os.makedirs(androidsrc)
    copyfiles(projectname)
    egameHandle(output)
    generatefilter(output,type)
    apkcmd = "ant -buildfile " + output + "/build.xml " + "debug"
    print apkcmd
    apkoutput = os.popen(apkcmd).readlines()
    print apkoutput
    debugapk = output + "/bin/TestDemo-debug.apk" 
    apk_temp = currentpath + "/CocosPaySdk.apk" 
    finalapk = currentpath + "/com.cocospay.stub.dat"
    finalzip = zipfile.ZipFile(finalapk, 'w')
    debugzipraw = zipfile.ZipFile(debugapk)
    data_needed = debugzipraw.read("classes.dex")
    finalzip.writestr("classes.dex", data_needed)
    finalzip.close()
    debugzipraw.close()
    open(apk_temp, "wb").write(open(debugapk, "rb").read())
        
    
def egameHandle(path):
    egame_stand = os.path.join(path, "libs/cn.egame.terminal.paysdk.jar")
    print egame_stand
    egame_lite = os.path.join(path, "libs/EgamePayExt.jar")
    print egame_lite
    if os.path.exists(egame_stand) and os.path.exists(egame_lite):
        os.system("zip -d " + egame_stand + " cn/egame/terminal/paysdk/codec/Base64*.class")        
        os.system("zip -d " + egame_stand + " cn/egame/terminal/paysdk/codec/MD5.class")        
    pass
    
    
def copyFiles(sourceDir,  targetDir):
    for file in os.listdir(sourceDir):
        if str(file).startswith("AndroidManifest.activity") or str(file).startswith("AndroidManifest.permision"):
            continue
        print(file)
        sourceFile = os.path.join(sourceDir,  file) 
        targetFile = os.path.join(targetDir,  file) 
        if os.path.isfile(sourceFile): 
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
                                
        if os.path.isdir(sourceFile):
            copyFiles(sourceFile, targetFile)

def copyfiles(targetDir):
    for key in oprators.keys():
        print key, ":", oprators[key]
        copyFiles(oprators[key], os.path.join(currentpath, targetDir))
        
        
def getApkName(path):
    name = str(path).split("/")
    length = len(name)
    print name[length-1]
    return name[length-1]

def decompileapk(apkpath, output):    
    #apkpath = currentpath + ("/Home-release.apk") 
    apkname = getApkName(apkpath)   
    tempfile = currentpath + "/temp"
    decompilecmd = "apktool d -s " + apkpath + " -o " + tempfile
    os.popen(decompilecmd).readlines()
    for key in oprators.keys():
        print key, ":", oprators[key]
        formFile = os.path.join(oprators[key], "res")
        if os.path.exists(formFile):
            toFile = os.path.join(tempfile, "res")
            copyFiles(formFile, toFile)            
        else:
            continue        
    print "Gooo...."
    modifyManifest(currentpath, "temp")
    recompilecmd = "apktool b " + tempfile
    os.popen(recompilecmd).readlines()
    tmp_apk = tempfile + "/dist/" + apkname
    cpapkzip = zipfile.ZipFile(tmp_apk, 'a')
    payapkzip = zipfile.ZipFile(currentpath + "/CocosPaySdk.apk")
    cpapkrawzip = zipfile.ZipFile(apkpath)
    for name in payapkzip.namelist():
        if str(name).startswith("AndroidManifest.xml"):
            continue
        if str(name).startswith("classes.dex"):
            continue
        if str(name).startswith("META-INF/"):
            continue
        
        if str(name).startswith("res/"):
            continue
        if str(name).startswith("resources.arsc"):
            continue
        if str(name).startswith("lib/"):
            if (cputype == "armeabi"):
                if str(name).startswith("lib/armeabi-v7a/") or str(name).startswith("lib/x86/"):
                    continue
            elif (cputype == "armeabi-v7a"):
                if str(name).startswith("lib/armeabi/") or str(name).startswith("lib/x86/"):    
                    continue
            elif (cputype == "x86"):
                if str(name).startswith("lib/armeabi/") or str(name).startswith("lib/armeabi-v7a/"):
                    continue   
            elif (cputype == "armeabi-both"):
                if str(name).startswith("lib/x86/"):
                    continue                    
        data = payapkzip.read(name)
        cpapkzip.writestr(name, data)
        print name
    for name2 in cpapkrawzip.namelist():
        if str(name2).startswith("AndroidManifest.xml"):
            continue
        if str(name2).startswith("classes.dex"):
            continue
        if str(name2).startswith("META-INF/"):
            continue        
        if str(name2).startswith("res/"):
            continue
        if str(name2).startswith("resources.arsc"):
            continue
        if str(name2).startswith("assets/"):
            continue
        if str(name2).startswith("lib/"):
            continue
        data = cpapkrawzip.read(name2)
        cpapkzip.writestr(name2, data)
        print name2
    cpapkzip.write(currentpath + "/com.cocospay.stub.dat", "assets/com.cocospay.stub.dat", zipfile.ZIP_DEFLATED)
    cpapkrawzip.close()    
    cpapkzip.close()
    payapkzip.close()
    release_path =  os.path.join(currentpath, "realeaseversion")
    if not os.path.exists(release_path):
        os.mkdir(release_path)
    apk_output_release = os.path.join(release_path, output)
    resign(tmp_apk, apk_output_release)
    deletetempfile()

def deletetempfile():
    path_dat = os.path.join(currentpath, "com.cocospay.stub.dat")
    if os.path.exists(path_dat):
        os.remove(path_dat)
    path_sdk = os.path.join(currentpath, "CocosPaySdk.apk")
    if os.path.exists(path_sdk):
        os.remove(path_sdk)
    path_temp = os.path.join(currentpath, "temp")
    if os.path.exists(path_temp):
        shutil.rmtree(path_temp)
    path_demo = os.path.join(currentpath, "TestDemo")
    if os.path.exists(path_demo):
        shutil.rmtree(path_demo)
    pass
        

def resign(input, output):    
    cmd = "d2j-apk-sign.sh -f " + input + " -o " + output
    result = os.popen(cmd).read()
    print result          
        
    
def modifyManifest(currpath, tmp):
    activityname = "AndroidManifest.activity.txt"
    permissionname = "AndroidManifest.permission.txt"
    manifestraw = os.path.join(currpath, tmp) + ("/AndroidManifest.xml")
    ET.register_namespace('', "http://java.sun.com/xml/ns/javaee")
    ET.register_namespace('android', "http://schemas.android.com/apk/res/android")
    treeraw = read_xml(manifestraw)
    
    #testfile = os.path.join(currpath, "TestXml.xml")
    #treetest = read_xml(testfile)
        
    testroot = treeraw.getroot()
    print testroot.get("package")
    packagename = testroot.get("package")
    print testroot.tag
    for key in oprators.keys():
        print key, ":", oprators[key]
        activity = os.path.join(oprators[key],activityname)
        print activity
        permission = os.path.join(oprators[key],permissionname)
        if os.path.exists(activity):
            treeactivity = read_xml(activity)
            application = find_node(testroot, "application")           
            for node in treeactivity.getroot():
                print node.tag
                application.append(node)
            write_xml(treeraw, manifestraw)
        if os.path.exists(permission):
            print "has permission"
            treepermission = read_xml(permission)
            print treepermission.getroot().tag
            #permission_list = find_nodes(treepermission.getroot(), "./uses-permission")
            for node in treepermission.getroot().findall("uses-permission"):
            #for node in permission_list:
                print node.tag
                testroot.append(node)
            write_xml(treeraw, manifestraw)
            
    replaceInFile(manifestraw, "PACKAGE_NAME_ABC", packagename)
    mainentry = getGameMainEntry(manifestraw)
    modifygstring(currpath, mainentry)
    modifyUnicomEntry(manifestraw, mainentry)

def getGameMainEntry(path):
    manifest = read_xml(path)
    mainentry = find_node(manifest.getroot(), "application/activity//meta-data[@{http://schemas.android.com/apk/res/android}name='dest_activity']")
    return mainentry.get('{http://schemas.android.com/apk/res/android}value')     
    
def modifygstring(currpath, packagename):       
    gstringpath = os.path.join(currpath, "temp/res/values/g_strings.xml")
    if os.path.exists(gstringpath):        
        gstringtree = read_xml(gstringpath)        
        gclassname = find_node(gstringtree, "string[@name='g_class_name']")        
        replaceInFile(gstringpath, str(gclassname.text), packagename) 
        
def modifyUnicomEntry(path, entry):
    manifest = read_xml(path)
    try:
       mainentry = find_node(manifest.getroot(), "application/activity//meta-data[@{http://schemas.android.com/apk/res/android}name='UNICOM_DIST_ACTIVITY']")       
       mainentry.set('{http://schemas.android.com/apk/res/android}value', entry)
       write_xml(manifest, path)
    except Exception, ex:        
        pass    
    pass
    
    
def replaceInFile(filename, strFrom, strTo):  
    lines = fileinput.input(filename, inplace=1)
    for line in lines:         
        if re.search(strFrom, line):  
            line = line.replace(strFrom, strTo)  
        print line,
    fileinput.close()          
   
def read_xml(in_path):         
    tree = ET.parse(in_path)    
    return tree  
  
def write_xml(tree, out_path):       
    tree.write(out_path, encoding="utf-8",xml_declaration=True)  
  
def if_match(node, kv_map):     
    for key in kv_map:  
        if node.get(key) != kv_map.get(key):  
            return False  
    return True  
    
def find_node(tree, path):    
    return tree.find(path)  

def find_nodes(tree, path):    
    return tree.findall(path) 
  
  
def get_node_by_keyvalue(nodelist, kv_map):    
    result_nodes = []  
    for node in nodelist:  
        if if_match(node, kv_map):  
            result_nodes.append(node)  
    return result_nodes 
          
def add_child_node(nodelist, element):     
    for node in nodelist:  
        node.append(element)  


if __name__ == '__main__':
    apkpath = os.sys.argv[1]    
    apkoutput = os.sys.argv[2]
    outputtype = os.sys.argv[3]
    if len(os.sys.argv) == 5:
        orientation = os.sys.argv[4]
        print orientation
        
    generateop(outputtype, "adc")   
    decompileapk(apkpath, apkoutput)   
    pass