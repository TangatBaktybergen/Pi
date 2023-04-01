This is the code to test video streaming from Pi Camera Rev 1.3 connected to Raspberry Pi 4B.

Raspberry pi is hosting webserver to stream pi camera. To access camera , go to your browser and type "Your_Pi_IP":8000 . 

The code is taken from Randomnerdtutorials.com : https://randomnerdtutorials.com/video-streaming-with-raspberry-pi-camera/

Before accessing your camera , make sure the legacy camera support is enabled on your raspberry pi. Check or change through "sudo raspi-config" > Interface options > Enable legacy camera support > reboot your Pi.

Save the file as .py python file and to run on shell write : pythone3 "yourPyFileName".py
Then go to your browser on PC and do previous steps!
