This is the code to test video streaming from Pi Camera Rev 1.3 connected to Raspberry Pi 4B.
* I use vim editor on raspberry pi: 
  To install vim : sudo apt install vim
  To open file with vim: vi "filename" 
  >> Press I on keyboard for Insert mode and Escape followed by " :x " to save the file and quit.
  To check if your file content is saved , read the file on the shell : cat "filename" 

*NEVER save the file as picamera.py because it is librarys name!


Raspberry pi is hosting webserver to stream pi camera. To access camera , go to your browser and type "Your_Pi_IP":8000 . 

The code is taken from Randomnerdtutorials.com : https://randomnerdtutorials.com/video-streaming-with-raspberry-pi-camera/

Before accessing your camera , make sure the legacy camera support is enabled on your raspberry pi. Check or change through "sudo raspi-config" > Interface options > Enable legacy camera support > reboot your Pi.

Save the file as .py python file and to run on shell write : pythone3 "yourPyFileName".py
Then go to your browser on PC and do previous steps!

Common commands :  Before you start be sure you are in your "home" directory to create a file!
  
  raspistill -o test.jpg  : Pi camera takes a picture and saves it under name "test.jpg" in the currently located directory! 
  
  raspivid -o test.h624 -t 7000 : Creates a video recording of 7000 ms(7s). ".h624" is the format that pi uses to save video files.
  
  ls : to check if an image is created in the directory
  
  rm "filename" : to remove a file in the directory
  
  raspistill -o test.jpg -w xxx -h xxx : -w and -h to give an image custom width and height
  
Now to access the camera module , you must download "picamera" library on your raspberry pi.

   To install pip : sudo apt install python3-pip 
   
   To check pip version : pip3 --version
   
   To install "picamera" library : sudo apt-get install python3-picamera
   
