# Imports
from PIL import Image
import argparse, random,  io

# For the purposes of making the tool easy to use
parser = argparse.ArgumentParser(
    prog='xor-image-tool',
    description='Perform binary operations on an image',
    epilog='You can supply any number of flags.'
)
parser.add_argument('filename')
parser.add_argument('-a', '--binary_and', action='store_true', help="AND the image with a random bitstream")
parser.add_argument('-o', '--binary_or', action='store_true', help="OR the image with a random bitstream")
parser.add_argument('-x', '--binary_xor', action='store_true', help="XOR the image with a random bitstream")
parser.add_argument('-b', '--binary_image', action='store_true', help="convert image to a simple binary image")
args = parser.parse_args()

# Helper: Converts (r,g,b) -> int
def rgbtoint(rgb):
    color = 0
    for v in rgb[::-1]:
        color = (color<<8) + v
    return color

# Stumbled across this on accident, looks cool
def binary_image(IMAGE_FILENAME):
    # Load image
    img = Image.open(IMAGE_FILENAME)
    width, height = img.size
    pixels = img.load()

    # The int value of #FFFFFF
    MAX_COLOR = rgbtoint((255,255,255))

    for i in range(width):
        for j in range(height):
            r,g,b = pixels[i,j]
            color = rgbtoint((r,g,b))
            if (color > MAX_COLOR/2):
                pixels[i,j] = MAX_COLOR
            else:
                pixels[i,j] = (0,0,0)

    filename = f"binary_img_{IMAGE_FILENAME}"
    img.save(filename)
    print(f"Created {filename}")
    img.close()

# Generate a key the length of the image to perform AND, OR, XOR operations on.
# Except I'm not actually gonna do that. The key will be generated on the fly
# and I'm not sure how cryptographically secure that is.

def _and(IMAGE_FILENAME):
    # Load image
    img = Image.open(IMAGE_FILENAME)
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            r,g,b = pixels[i,j]
            color = rgbtoint((r,g,b))
            pixels[i,j] = color & random.getrandbits(24)

    filename = f"and_{IMAGE_FILENAME}"
    img.save(filename)
    print(f"Created {filename}")
    img.close()

def _or(IMAGE_FILENAME):
    # Load image
    img = Image.open(IMAGE_FILENAME)
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            r,g,b = pixels[i,j]
            color = rgbtoint((r,g,b))
            pixels[i,j] = color | random.getrandbits(24)

    filename = f"or_{IMAGE_FILENAME}"
    img.save(filename)
    print(f"Created {filename}")
    img.close()

def _xor(IMAGE_FILENAME):
    # Load image
    img = Image.open(IMAGE_FILENAME)
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            r,g,b = pixels[i,j]
            color = rgbtoint((r,g,b))
            pixels[i,j] = color ^ random.getrandbits(24)

    filename = f"xor_{IMAGE_FILENAME}"
    img.save(filename)
    print(f"Created {filename}")
    img.close()

# Handle command-line arguments
if (args.binary_and):
    _and(args.filename)
if (args.binary_or):
    _or(args.filename)
if (args.binary_xor):
    _xor(args.filename)
if (args.binary_image):
    binary_image(args.filename)

print("Done.")
