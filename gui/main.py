import serial
import serial.tools.list_ports
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

BAUD_RATE = 9600

class SensorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sensor Monitor")

        self.ser = None
        self.running = False

        ttk.Label(master, text="Select COM Port:").grid(row=0, column=0, sticky="e")
        self.com_var = tk.StringVar()
        self.com_combo = ttk.Combobox(master, textvariable=self.com_var, values=self.list_com_ports(), state="readonly")
        self.com_combo.grid(row=0, column=1, sticky="w")

        self.connect_button = ttk.Button(master, text="Connect", command=self.connect_serial)
        self.connect_button.grid(row=0, column=2, padx=5)

        self.voltage_var = tk.StringVar(value="0 V")
        self.current_var = tk.StringVar(value="0 A")
        self.current2_var = tk.StringVar(value="0 A")

        ttk.Label(master, text="Voltage:").grid(row=1, column=0, sticky="e")
        ttk.Label(master, textvariable=self.voltage_var).grid(row=1, column=1, sticky="w")

        ttk.Label(master, text="Current 1:").grid(row=2, column=0, sticky="e")
        ttk.Label(master, textvariable=self.current_var).grid(row=2, column=1, sticky="w")

        ttk.Label(master, text="Current 2:").grid(row=3, column=0, sticky="e")
        ttk.Label(master, textvariable=self.current2_var).grid(row=3, column=1, sticky="w")

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def list_com_ports(self):
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def connect_serial(self):
        com_port = self.com_var.get()
        if not com_port:
            messagebox.showerror("Error", "Please select a COM port")
            return

        try:
            self.ser = serial.Serial(com_port, BAUD_RATE, timeout=1)
            self.running = True
            self.thread = threading.Thread(target=self.read_serial, daemon=True)
            self.thread.start()
            messagebox.showinfo("Connected", f"Connected to {com_port}")
            self.connect_button.config(state="disabled")
            self.com_combo.config(state="disabled")
        except serial.SerialException:
            messagebox.showerror("Error", f"Could not open {com_port}")

    def read_serial(self):
        while self.running:
            try:
                line = self.ser.readline().decode().strip()
                if line:
                    try:
                        voltage, current, current2 = map(float, line.split(","))
                        self.voltage_var.set(f"{voltage:.2f} V")
                        self.current_var.set(f"{current:.2f} A")
                        self.current2_var.set(f"{current2:.2f} A")
                    except ValueError:
                        pass  # Ignore malformed lines
            except serial.SerialException:
                break

    def on_close(self):
        self.running = False
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = SensorGUI(root)
    root.mainloop()
