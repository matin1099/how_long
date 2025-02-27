import os 
def get_files(url:str)-> str:
        """get path of folder--> return list of video files

        Args:
            url (str): path of folder with videos

        Returns:
            str: list contain FULL video path
        """
        print(os.listdir(url))

get_files("/home/matin-uni/Downloads/Videos")
# import module 
import cv2 
import datetime 

# create video capture object 
data = cv2.VideoCapture('/home/matin-uni/Downloads/Videos/Despicable Me 4.[SS][720][AioFilm.com].mkv') 

# count the number of frames 
frames = data.get(cv2.CAP_PROP_FRAME_COUNT) 
fps = data.get(cv2.CAP_PROP_FPS) 

# calculate duration of the video 
seconds = round(frames / fps) 
video_time = datetime.timedelta(seconds=seconds) 
print(f"duration in seconds: {seconds}") 
print(f"video time: {video_time}") 
