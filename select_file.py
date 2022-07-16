import easygui
from PIL import Image
from write_ascii_file import write_ascii_file


def select_file():
    # File selection menu
    print("File select:")
    image = easygui.fileopenbox()
    if image is not None:
        # Image data output
        imgobj = Image.open(image)
        print("Image data:")
        print("Width:", imgobj.width)
        print("Height:", imgobj.height)

        data = imgobj.getdata()
        write_ascii_file(data, imgobj.width)
