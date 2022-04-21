from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (720, 480)
camera.start_preview()
sleep(5)
i = 0
while True:
    try:
        i += 1
        camera.capture('/home/pi/toki/images1/image%s.jpg' % i)
        sleep(60)
    except KeyboardInterrupt:
        break
camera.stop_preview()
