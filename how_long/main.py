import os
import sys
import cv2 
import datetime 

from loguru import logger


def filefinder(subfolder:str):
    if subfolder != './':
        Issub = True 
    else:
        Issub = False

    abs_address = os.getcwd()
    logger.info('Getting full address.')
    dir_files = os.listdir(subfolder)
    logger.info('Getting folder files.')
    vids=[]
    
    logger.debug('Start to search for mp4s.')
    for file in dir_files:
        if file[-3:] == 'mp4' and Issub == True:
            vids.append(abs_address+'/'+subfolder+file)
        elif file[-3:] == 'mp4' and Issub == True:
            vids.append(abs_address+'/'+file)

    return(vids)

def duration(pathtofile:str):
    data = cv2.VideoCapture(pathtofile)
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT) 
    fps = data.get(cv2.CAP_PROP_FPS)
    logger.trace(f'is open:\t{data.isOpened()}') 
    logger.trace(f'path:\t{pathtofile}') 
    logger.trace(f'fps:\t{fps}') 
    logger.trace(f'frames:\t{frames}') 

    seconds = round(frames / fps) 
    return seconds


def counter(video_path:list):
    fulltime = 0
    for path in video_path:
        fulltime += duration(path)

    folder_time = datetime.timedelta(seconds=fulltime) 
    print(f'Whole folder will be {folder_time}')


def run():
    term_args = sys.argv[:]
    try:
        subfolder = term_args[1]+'/'
    except IndexError:
        subfolder='./'
    vid_list = filefinder(subfolder)
    counter(video_path=vid_list)