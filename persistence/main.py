import traceback
import os
import time
"""
Why do we not dump data directly into files ?
Persistence
If process to write to a file crashes : 
1) File can lose last write
2) File can be half-written with new data
3) More corruption

Database recovers to usable state after unexpected shutdown

Achieving persistence without databases implemented below
--> 1) Write data to file temp.txt 
--> 2) fsync temp.txt
--> 3) rename temp.txt to data.txt
"""




def save_file(data:str) -> None:
    try:
        fd_path = os.path.join(os.getcwd(), 'temp.txt')
        rename_path = os.path.join(os.getcwd(), 'data.txt')
        fd =  os.open(fd_path, os.O_RDWR | os.O_CREAT)
        encoded_data = str.encode(data)
        os.write(fd, encoded_data)
        os.fsync(fd)
        os.rename(fd_path, rename_path)
        os.close(fd)
    except:
        print(traceback.format_exc())
    return

if __name__ == "__main__":
    save_file('capture this data')
    time.sleep(5)
    save_file('captured save after 5 seconds')