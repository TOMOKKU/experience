from picamera import PiCamera
from time import sleep

camera = PiCamera()

#--preview-------/
# camera.start_preview()
# sleep(5)
# camera.stop_preview()

#--rotate preview-------/
# camera = PiCamera()
# camera.rotation = 180

#--See through to monitoring error-------/
# camera.start_preview(alpha=200)

#--camera capture-------/
camera.start_previewa()
sleep(5)
camera.capture('/home/toki/Desktop/image.jpg')
camera.stop_preview()

#--roop camera capture-------/
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('home/toki/Desktop/image%s.jpg' % i)
camera.stop_preview()

#--video record-------/
# camera.start_preview()
# camera.start_recording()
# sleep(5)
# camera.stop_recording()
# camera.stop_preview()

#--picture config-------/
camera.resolution = (1920, 1080)
camera.framerate =15
camera.start_preview()
sleep(5)
camera.capture('/home/toki/Desktop/FullHD.jpg')
camera.stop_preview()
