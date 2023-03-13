from AppKit import NSColor

# This function takes in red, green, and blue values as arguments
# and sets the background color of the Touch Bar to the corresponding color.
def set_touchbar_color(red: int, green: int, blue: int) -> None:
    # Create a color object with the specified red, green, and blue values
    color = NSColor.colorWithCalibratedRed_green_blue_alpha_(red/255, green/255, blue/255, 1.0)
    # Ignore the alpha value of the color
    NSColor.setIgnoresAlpha_(True)
    # Set the color as the background color for the Touch Bar
    NSColor.setColor_(color)
    
    # Print hello world with array comprehension
    print("Hello World"[i] for i in range(11))








# Example usage: set the Touch Bar background color to blue
set_touchbar_color(0, 0, 255)
