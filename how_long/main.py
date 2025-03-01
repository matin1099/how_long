import argparse

from loguru import logger
from .walk import folder_walk, subfolders_walk
from .counter import counter_norm, counter_subdir

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--folder", help=" Search in specific folder.example: how_long -f parentDir/childDir",
                        action='store')
    parser.add_argument("-s","--subdirs", help="Going for all subdirs in parent dirs", action="store_true")
    #parser.add_argument("-v", "--verbose", help="Return video lenght of each subdir sepratly.", action="store_true")


    args = parser.parse_args()

    if args.folder != None and args.subdirs == False:
        logger.info("Single Dir Search ACTIVATED")
        insubdir = str(args.folder)
        if not insubdir.endswith('/'):
            insubdir = insubdir+'/'
        vid_list = folder_walk(insubdir)
        counter_norm(video_path=vid_list)

    elif args.folder == None and args.subdirs == True:
        logger.info("Full Dirs Search ACTIVATED")

        _ ,video_dict = subfolders_walk()
        counter_subdir(video_dict = video_dict)
        
    elif args.folder == None and args.subdirs == False:
        logger.info("Root Dir Search ACTIVATED")
        justrootdir = "./"
        vid_list = folder_walk(justrootdir)
        counter_norm(video_path=vid_list)

    else:
        logger.critical("MISS USED FLAGS!")
        logger.info("Use -h or --help for instractions")
        logger.info("$ how-long -h")
        