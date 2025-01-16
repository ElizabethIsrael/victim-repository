import sys

# Add the legitimate library's path to the Python environment
sys.path.append(r"D:\legitimate-library")

# Import the legitimate core module
from legitimate_library import core

# Overwrite the core module with the malicious component
from legitimate_library import malicious_library as core

# Victim's data to process
sensitive_data = "Linda"

# Call the malicious function
core.hello_world(sensitive_data)

# Process data using the malicious library
result = core.process_data(sensitive_data)


