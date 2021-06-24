import cv2
import dropbox
import time
import random

start_time=time.time()
def take_snapshot():
    video_capture_object=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=video_capture_object.read()
        img_name="img"+str(random.randint(0,100))+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshot taken")
    video_capture_object.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="A7ca9-5Hm6IAAAAAAAAAAdHCKLMQNl1bJ5rHCUPmGHZfU1kYkrgGTanoUsQ9UJY2"
    file_from=img_name
    file_to="/hoho/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
 
    with open (file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name =take_snapshot()
            upload_file(name)

main()
        

