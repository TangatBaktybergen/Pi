I am using Raspberry pi 4b with no desktop Raspbian OS.

3 LEDs are connected to pin 21, 13, and 7.
* Long leg of a LED(+) directly connects to the pin and short leg(-) connected to 470 Ohm resistor to the ground.

Enabling pins:
* Go to the directory: /sys/class/gpio/
* Create a control directory of the pin: echo 21 > export. This enables pin 21. 
* Now you should have a new directory named "gpio21".Enter the directory and set the pin to output: echo out > direction.

Repeat the steps for the other LEDs.
* Important: Every time you reboot your Pi, the setting of the pins goes to default.So, what you can do is to change "rc.local" file!

Raspberry pi runs rc.local every time it reboots.
* Go the location of the file and open it: /etc/rc.local
* Enter the following command lines before the line "#Print the IP adress"
    * Enabling the pin 21 : echo 21 > "/sys/class/gpio/export"
    * Setting the pin 21 to output: echo out > "/sys/class/gpio/gpio21/direction"
    
Repeat the same steps for the other pins! With these lines in rc.local , you will not have to enable pins manually every time!
* You should also make rc.local executable to avoid any problems,
  * Enter the command : chmod +x rc.local

You can do a quick test of your LEDs from the terminal if you want! Raspi-gpio command will help with that!
* Manual of raspi-gpio : raspi-gpio help
* To set the pin 21 to output and drive it high: raspi-gpio set 21 op dh
* To drive it low: raspi-gpio set 21 op dl
* To get the status of the pin: raspi-gpio get 21 
