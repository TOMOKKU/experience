from picamera import PiCamera
from time import sleep
import cv2
from mine import colors as  col
import os
camera = PiCamera()

camera.resolution = (720, 480)
cc=0
sec=60
i = 0
c=0
try:
   while True:

    key = chr(cv2.waitKey(1)&0xff)
    print("フォルダ名を")
    f_name=str(input())
    path=f_name+"/"

    path_tf=os.path.exists(f_name)
    if str(path_tf)=="True":
       col.c_print("エラー:保存先のフォルダがすでに存在しています",[col.bg_red,col.bold,col.white])
    else:
            os.mkdir(f_name)
            col.c_print("保存先フォルダ: "+f_name+" を作成しました",[col.bg_white,col.blue])
            camera.start_preview()

            col.c_print("確認:準備ができたら「r」を",[col.bold,col.white])
            key = str(input())

            if key=="r":

                break

   while True:

        c=c+1
        f_c=str(str(c)+"枚目 "+str(sec)+"秒周期.jpg")

        camera.capture('/home/pi/onisi/physics/'+str(path)+str(f_c))

        mes_c=str((str(c)+"枚目 "+str(sec)+"秒周期で保存"))
        col.c_print(mes_c,[col.bg_green,col.bold,col.white])

        sleep(sec)
except KeyboardInterrupt:
        camera.stop_preview()
