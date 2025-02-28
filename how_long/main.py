import argparse

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--folder", help=" Search in specific folder.\n\texample: how_long -f parentDir/childDir",
                        action='store')
    parser.add_argument("-s","--subdirs", help="Going for all subdirs in parent dirs", action="store_true")



    args = parser.parse_args()

    if args.folder != None:
        abcd = args.folder
        print(type(abcd))
        print(abcd)
    else:
        print('dosent work!')

run()
'''
    term_args = sys.argv[:]
    try:
        subfolder = term_args[1]+'/'
    except IndexError:
        subfolder='./'
    vid_list = filefinder(subfolder)
    counter(video_path=vid_list)
'''

'''parser = argparse.ArgumentParser()
parser.add_argument("-m", "--meoww", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.meoww:
    print("meow meow!")
'''