# JaCircuitsNormal Sample Data

Small script meant to replicate data that Farmtek sends upon a car crossing the finish.
## Installation
Install the PySerial package
```bash
pip install -r requirements.txt
```
## Configuration
Edit the serial ports in use within the script as well as the time interval between finishes and minutes for script to run.
```python
serialPort = 'COM4' #serial where data is being sent from
timeToRun = 10 #minutes
sleepInterval = 30 #seconds between finishes
```
## Usage
Run as a python script using Python 3.5+
```bash
python generate-data.py
```
