from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
while True:
    try:
        camera.capture('home/pi/toki/images1/image%s.jpg' % i)
        sleep(60)
    except KeyboardInterrupt:
        camera.stop_preview()
