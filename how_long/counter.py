import datetime

from loguru import logger
from duration import duration # type: ignore

def counter_norm(video_path:list):
    fulltime = 0
    for path in video_path:
        fulltime += duration(path)

    fulltime = datetime.timedelta(seconds=fulltime) 
    print(f'Whole folder will be {fulltime}')


def counter_subdir(video_dict:dict):
    fulltime = 0
    for key in video_dict.keys():
        fulltime += video_dict.get(key)
        video_dict[key] = datetime.timedelta(seconds=video_dict.get(key))
    
    fulltime = datetime.timedelta(seconds=fulltime) 
    print("result of each folder:")
    for key in video_dict.keys():
        print(f'\t{key} will have {video_dict[key]}')
    print(f"In total: this root folder will be {fulltime}")