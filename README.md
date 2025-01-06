# open_colorimeter_plus_firmware  

![alt text](/images/flourimeter_prototype.png)

Development firmware (circuitpython) for a fluorimeter based on our open colorimeter (in development). 

## Requirements (see requirements.txt)

* circuitpython = 9.1.1
* adafruit_tsl2591==1.3.13
* adafruit_ticks==1.1.1
* adafruit_tca9548a==0.7.4
* adafruit_bus_device==5.2.10
* adafruit_itertools==2.1.2
* adafruit_bitmap_font==2.1.3
* adafruit_display_text==3.2.0
* adafruit_display_shapes==2.10.0


## Installation

* Copy the code.py and all the .py files in src file to the CIRCUITPY drive associated with
your feather development board. 

* Copy assets folder to the CIRCUITPY drive

* Copy the required libraries from the circuitpython bundle to CIRCUITPY/lib. Note, this can be done 
most easily using the [circup](https://github.com/adafruit/circup) tool. 

```bash
circup install -r requirements.txt

```

  

