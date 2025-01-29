# TERESA Mini Project Starter Code

The primary file you will need to edit is ```interface.py```

Note: The following instructions assume you're working in a Unix environment. Windows instructions may differ :(

## Dependencies
Make sure you have Python3 and Git installed!

## Set Up
1. Clone the repository however you'd like (command line, GitHub Desktop, etc.)
```
git clone git@github.com:Elegant-Mind-Club/teresa-starter-code.git
```

3. Navigate to the directory open it in a text editor of your choice
```
cd teresa-starter-code
code .
```

4. Create a virtual environment
   - Feel free to use whatever virtual environment manager you like (conda, venv, etc.)
   
 ```
 python3 -m venv venv
 source venv/bin/activate
 ```

6. Install dependencies
```
pip install -r requirements.txt
```

8. Start coding!
- modify ```interface.py``` and create any additional files you want/need to perform your data analysis


## Running the Simulation
```starter.py``` provides a convenient way to launch the simulated environment and the code that interfaces with it.

You can feel free to start each program independently, it doesn't matter which one you start first.


## Using a physical IMU
1. Plug one of the ESP32 boards into your computer. It should already have the necessary code running on the microcontroller. 
2. Find out which serial port the ESP32 is on for your computer. A quick Google search may help you if you don't know how to do this.
3. Modify ```interface.py``` to use an ```ArduinoIMU``` object instead of a ```SimulatedIMU```. You might have to import it if it isn't already imported.
```
from sensors.imu import ArduinoIMU
```
