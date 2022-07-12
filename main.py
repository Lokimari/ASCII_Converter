# Img To ASCII
# Takes an image, gets brightness of each pixel, converts to ASCII accordingly
# Lightness can be measured in ASCII on a simple scale like: [char for char in ".,`\'\"/;[@#"]\\]
# This list "light_levels" can be changed, inverted, etc to support more brightness levels. The program will scale to it

from datetime import datetime
from PIL import Image
import easygui

light_levels = [char for char in ".,':;^*!([%#"]  # Change this as you wish


def get_pixel_brightness(pixel):
    print(pixel)
    brightness_level = (pixel[0] + pixel[1] + pixel[2]) / 3  # Get average as brightness
    print(brightness_level)
    brightness_level = int((brightness_level * (1 / 255)) * len(light_levels))  # Scale brightness to list len
    print("Scaled brightness = ", brightness_level)
    return brightness_level


if __name__ == "__main__":
    # File selection menu
    print("File select:")
    image = easygui.fileopenbox()
    if image is not None:
        imgobj = Image.open(image)
        print("Image data:")
        print("Width:", imgobj.width)
        print("Height:", imgobj.height)

        # Prompt user to convert or not
        pixels = imgobj.convert('RGBA')
        data = imgobj.getdata()
        lofpixels = []
        PADDING = 1 * " "  # Padding between pixels

        start = datetime.now().now()

        # Start converting
        with open("ascii.txt", "w") as f:
            i = 1
            for pixel in data:
                lofpixels.extend(pixel)
                pixel_brightness = get_pixel_brightness(pixel)
                # print(pixel_brightness)
                f.write(PADDING + light_levels[pixel_brightness])
                i += 1
                # Newline if at width limit
                if i == imgobj.width:
                    f.write(" \n")
                    i = 1
            f.close()

        end = datetime.now().now()
        print(f"Start: {start}\nEnd: {end}\nElapsed: {end - start}")
