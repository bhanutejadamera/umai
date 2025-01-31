# demos/demo_umai.py
import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.umai_framework import UMAI

if __name__ == "__main__":
    # Create an instance of the UMAI framework
    umai = UMAI()

    # Run the UMAI framework
    umai.run()