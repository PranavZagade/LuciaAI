# Display System Information
# This script gathers and displays detailed system information using `platform` and `wmi` modules.

import platform  # For cross-platform system information
import wmi  # For Windows Management Instrumentation (WMI)

# Display general system information using the `platform` module
print("=" * 40, "System Information", "=" * 40)
uname = platform.uname()
print(f"System: {uname.system}")  # Operating system name
print(f"Node Name: {uname.node}")  # Hostname
print(f"Release: {uname.release}")  # OS release version
print(f"Version: {uname.version}")  # OS version
print(f"Machine: {uname.machine}")  # Machine type (e.g., 'AMD64')
print(f"Processor: {uname.processor}")  # Processor type

# Additional system details using the `wmi` module
c = wmi.WMI()  # Initialize the WMI client
my_system = c.Win32_ComputerSystem()[0]  # Access system information

# Print detailed hardware and system configuration
print(f"Manufacturer: {my_system.Manufacturer}")  # Manufacturer of the computer (e.g., Dell, HP)
print(f"Model: {my_system.Model}")  # Model of the computer
print(f"Name: {my_system.Name}")  # System name
print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")  # Number of processors
print(f"SystemType: {my_system.SystemType}")  # System architecture (e.g., 'x64-based PC')
print(f"SystemFamily: {my_system.SystemFamily}")  # System family (e.g., 'ThinkPad Family')
