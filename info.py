"""
#  https://www.geeksforgeeks.org/get-video-duration-using-python-opencv/
# import module 
import cv2 
import datetime 

# create video capture object 
data = cv2.VideoCapture('C:/Users/Asus/Documents/videoDuration.mp4') 

# count the number of frames 
frames = data.get(cv2.CAP_PROP_FRAME_COUNT) 
fps = data.get(cv2.CAP_PROP_FPS) 

# calculate duration of the video 
seconds = round(frames / fps) 
video_time = datetime.timedelta(seconds=seconds) 
print(f"duration in seconds: {seconds}") 
print(f"video time: {video_time}") 
"""
def get_files(url:str)-> str:
    """get path of folder--> return list of video files

    Args:
        url (str): path of folder with videos

    Returns:
        str: list contain FULL video path
    """
    pass 
def swing(name:str)->str:
    """swing full pass to video names

    Args:
        name (str): video names

    Returns:
        str: full path name
    """
    pass