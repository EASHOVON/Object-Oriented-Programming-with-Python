""" 
    Object Processor Program
    Project From Lab class
    Instractor: Minhaj Sir
    
    Practiced this project: MD. ASRAFUZZAMAN SUVON
"""

# import glob,shutil,os,time
# destination_path = "../destination"
# source_path = "../source/*"
# postfix = [1,2,3]

# while True:
#     source_object = glob.glob(source_path)
#     if len(source_object)>0:
#         object_path = source_object[-1]
#         shutil.copy(object_path,'.')

#         object_name = object_path.split('\\')[-1].split('.')
#         prefix = object_name[0]
#         postfix2 = object_name[1]

#         for item in postfix:
#             file_name = prefix + "_" + str(item) + "." + postfix2
#             shutil.copy(object_path,f"{destination_path}/{file_name}")

#         os.remove(object_path)
#         os.remove(object_path.split('\\')[-1])


import glob, shutil, os, time

destination_path = "../destination"
source_path = "../source/*"
server_path = "./*"

postfix = [1,2,3]

while True:
    source_object = glob.glob(source_path)
    server_object = glob.glob(server_path)
    if len(source_object)>0:
        source_object_path = source_object[0]
        shutil.copy(source_object_path,'./')
    server_object_path = ""
    if len(server_object)>1:
        for item in source_object:
            for itemT in server_object:
                if item.split("\\")[-1] in itemT:
                    server_object_path = itemT
        server_object_name = server_object_path.split("\\")[-1].split(".")
        for i in postfix:
            file_name = server_object_name[0] + "_" + str(i) + "."+ server_object_name[1]
            shutil.copy(server_object_path,f"{destination_path}/{file_name}")
        
        time.sleep(5)
        os.remove(source_object_path)
        os.remove(server_object_path)
           

    

        

