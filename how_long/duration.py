import cv2
from loguru import logger

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

