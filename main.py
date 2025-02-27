import os
import cv2 
import datetime 
from loguru import logger

def filefinder():
    abs_address = os.getcwd()
    logger.info('Getting full address.')
    dir_files = os.listdir()
    logger.info('Getting folder files.')
    vids=[]
    
    logger.debug('Start to search for mp4s.')
    for file in dir_files:
        if file[-3:] == 'mp4':
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

if __name__=='__main__':
    vid_list = filefinder()
    counter(video_path=vid_list)
