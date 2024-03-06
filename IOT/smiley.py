import time
from grovepi import *
from grove_rgb_lcd import *

# Display smiley face on LCD
def display_smiley():
    setTextBytes([0xF0, 0x9F, 0x98, 0x8A])  # UTF-8 representation for smiley face

# Main function
def main():
    # Set the LCD to its normal mode (i.e., not in low-power mode)
    setRGB(0, 128, 64)
    # Display smiley face
    display_smiley()

# Run the main function
if __name__ == "__main__":
    main()
