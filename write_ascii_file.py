from settings import LIGHT_LEVELS, INVERSE_SHADING, PADDING, DIAGONAL_OFFSET
from datetime import datetime


def get_pixel_brightness(pixel):
    print(type(pixel), "efEFASEF@#FW")
    brightness_level = (pixel[0] + pixel[1] + pixel[2]) / 3  # Get average as brightness
    brightness_level = int((brightness_level * (1 / 255)) * len(LIGHT_LEVELS))  # Scale brightness to list len
    return brightness_level


def apply_pixel_brightness_settings(pixel_brightness):
    # Correct Index Errors
    pixel_brightness = 0 if pixel_brightness < 0 else pixel_brightness
    pixel_brightness = len(LIGHT_LEVELS) - 1 if pixel_brightness >= len(LIGHT_LEVELS) else pixel_brightness

    # INVERSE SHADING
    if INVERSE_SHADING:
        pixel_brightness = (pixel_brightness * -1) - 1

    return pixel_brightness


def write_ascii_file(data, img_width):
    # Start converting to ASCII
    diag_offset = DIAGONAL_OFFSET
    with open("ascii.txt", "w") as f:
        # Timekeeping
        start = datetime.now().now()
        for pixel in data:
            pixel_brightness = get_pixel_brightness(pixel)
            pixel_brightness = apply_pixel_brightness_settings(pixel_brightness)

            # Write to file
            try:
                f.write(PADDING + LIGHT_LEVELS[pixel_brightness])
            except IndexError:
                pause = input("Pause: ")

            # Iteration cleanup
            diag_offset += 1  # This is now acting as 'i'
            # Newline if at width limit
            if diag_offset == img_width:
                f.write(" \n")
                diag_offset = 0

        f.close()

    end = datetime.now().now()
    print(f"Start: {start}\nEnd: {end}\nElapsed: {end - start}")
