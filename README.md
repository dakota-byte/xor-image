# xor-image

A demonstration of using certain binary operations on an image.


```
usage: xor-image-tool [-h] [-a] [-o] [-x] [-b] [-s] filename

Perform binary operations on an image

positional arguments:
  filename

options:
  -h, --help          show this help message and exit
  -a, --binary_and    AND the image with a random bitstream
  -o, --binary_or     OR the image with a random bitstream
  -x, --binary_xor    XOR the image with a random bitstream
  -b, --binary_image  convert image to a simple binary image

You can supply any number of flags.
```

The key used is randomly generated on the fly.

The key is not saved anywhere so you cannot undo the operation. I plan
to create another tool in the future to do that.

Example usage:

```
python xor.py galaxy.png -x -a
$ Created and_galaxy.png
$ Created xor_galaxy.png
$ Done.
```
