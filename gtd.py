import sys, os
import fnmatch

gtd_files = ['1_in', '2_next_actions', '3_waiting_for', '4_someday_maybe']

if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except IndexError:
        path = """/Users/mbottom/Desktop/projects""" 
        print("No path specified, using default: "+path)
    list_of_files = {}
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename in gtd_files:
                with open(os.path.join(dirpath, filename), 'r') as f:
                    file_contents = f.read()
                    if len(file_contents)>3:
                        print(dirpath.center(80, '#'))
                        print(filename.center(80, '#'))
                        print(file_contents)
                        print("\n")
                #list_of_files[filename] = os.sep.join([dirpath, filename])
