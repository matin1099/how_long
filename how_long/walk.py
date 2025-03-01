import os
from  loguru import logger
from .counter import counter_subdir, counter_norm
from .duration import duration


def subfolders_walk():
    abs_address = os.getcwd()
    logger.trace('Getting full address.')
    logger.info("Start walk!")
    pathes = []
    dir_list = {}
    logger.trace('Getting full address.')

    for dirpath, dirnames, filenames in os.walk("."):
        if dirnames != []:
            for name in dirnames:
                if dir_list.get(name, None) == None:
                    dir_list[name] = 0
        for filename in filenames:
            if filename.endswith(".mp4"):
        #         print(filename)
                pathes.append(abs_address+dirpath[1:]+'/'+filename)
                for name in dir_list.keys():
                    if dirpath.endswith(name):
                        dir_list[name] += duration(pathes[-1])

        
    return(pathes, dir_list)


def folder_walk(subfolder:str):
    if subfolder != './':
        logger.info(f"Start walk in {subfolder}!")

        Issub = True 
    else:
        logger.info("Start walk in root!")

        Issub = False

    abs_address = os.getcwd()
    logger.trace('Getting full address.')
    dir_files = os.listdir(subfolder)
    logger.trace('Getting folder files.')
    vids=[]
    
    logger.trace('Start to search for mp4s.')
    for file in dir_files:
        if file.endswith('.mp4') and Issub == True:
            vids.append(abs_address+'/'+subfolder+file)
        elif file.endswith('.mp4') and Issub == False:
            vids.append(abs_address+'/'+file)
    return(vids)


