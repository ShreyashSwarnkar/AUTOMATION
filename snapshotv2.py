import time,cv2,dropbox,random

start_time = time.time()

def take_snapshot():
    numbers = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(numbers)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_images(img_name):
        access_token = 'sl.BAqY5tp-CCgu0Uj3in5B9Grlr5EFqOczUya1dLky3RtpVlsS1nWaQ_TLfCyvWTkWakv5QAm2-tQulRFwSW5mgF1El2OTziAF-3J2xSbOl-JhVdcj19YJXSpVuaeNnLLQJRR4FjJPJKtM'
        file = img_name
        file_from = file
        file_to = '/Img/'+ (img_name)
        dbx = dropbox.dropbox(access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
            print("files uploaded")

def main():
    while(True):
        if((time.time()-start_time) >=5):
            name = take_snapshot()
            upload_images(name)

main()