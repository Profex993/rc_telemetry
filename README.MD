# RC Racing Car Telemetry Project

This repository contains a complete telemetry solution for RC racing cars using Arduino and Python.  
It allows monitoring key parameters such as battery voltage and motor currents in real-time, both on the RC car and from a PC.

This is **our full RC telemetry project**, but it can also serve as inspiration for others looking to build similar systems. The repository includes **all Arduino code** and a **Python GUI** for displaying telemetry data.

## Project Components

### 1. Arduino Transmitter (On the RC Car)
- Reads sensors such as voltage and motor currents.
- Sends telemetry data wirelessly (using RF24 or another module) in CSV format:
    ```
    voltage,current,current2
    12.34,1.23,0.45
    ```
- Can be used directly or modified for additional sensors.

### 2. Arduino Receiver (Connected to PC)
- Receives telemetry data from the car.
- Outputs the data via Serial to the Python GUI.

### 3. Python GUI
- Connects to the Arduino receiver via a selectable COM port.
- Displays Voltage, Current 1, and Current 2 in real-time.
- Lightweight and simple interface for telemetry monitoring.

## Setup

### Arduino
1. Upload the **transmitter code** to the Arduino on the RC car.
2. Upload the **receiver code** to the Arduino connected to your PC.
3. Ensure the transmitter sends CSV-formatted telemetry data as shown above.

### Python
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the Python GUI from console:
    ```bash
    python main.py
    ```
   or double-click `gui/dist/main.exe` in your file explorer.

3. Select the correct COM port for the Arduino receiver and start monitoring.

## Dependencies
- Python 3.12

- pyserial
- tkinter (usually included with Python)