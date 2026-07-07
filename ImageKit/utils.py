from PIL import Image
import numpy as np
import os, sys


# the simple one channel gray scale image read [0-255]
def LoadImageGrayScaleAuto(img_path):
    """
    load an image and judge if it is grayscale or not, if not will remind and force the image to convert to grayscale
    return as numpy array [height, width] with values in [0, 255] type uint8
    """
    try:
        img = Image.open(img_path)
    except Exception as e:
        raise RuntimeError(f"Failed to load image: {img_path}. Error: {str(e)}")

    width, height = img.size  # Pillow scales images as (width, height)
    print(f"Input image size: {width} x {height} (width x height)")

    original_mode = img.mode
    grayscale_modes = {"1", "L", "LA"}

    if original_mode not in grayscale_modes:
        print(f"Warning: Input image is not grayscale (current mode: {original_mode}). "
              f"Converting to 8-bit grayscale automatically.")
        img_gray = img.convert("L")
    else:
        img_gray = img

    gray_array = np.array(img_gray, dtype=np.uint8)

    return gray_array # return as numpy array 

# Image read color
def LoadImageColorAuto(img_path):
    """
    Load an image and automatically unify it to standard 8-bit RGB format.
    If the input is not standard RGB (e.g. RGBA, CMYK, grayscale, palette),
    it will print a reminder and force conversion.
    Returns:
        numpy.ndarray: RGB image array with shape (height, width, 3),
                       dtype uint8, pixel values in [0, 255], channel order: R, G, B
    """
    try:
        img = Image.open(img_path)
    except Exception as e:
        raise RuntimeError(f"Failed to load image: {img_path}. Error: {str(e)}")

    width, height = img.size # Pillow scales images as (width, height)
    print(f"Input image size: {width} x {height} (width x height)")

    original_mode = img.mode

    if original_mode == "RGB":
        img_rgb = img
    else:
        grayscale_modes = {"1", "L", "LA"}
        if original_mode in grayscale_modes:
            print(f"Warning: Input is a grayscale image (mode: {original_mode}). "
                  f"Converting to 3-channel RGB automatically.")
        else:
            print(f"Warning: Input image is not standard RGB (current mode: {original_mode}). "
                  f"Converting to 8-bit RGB automatically.")
        img_rgb = img.convert("RGB")
    
    rgb_array = np.array(img_rgb, dtype=np.uint8)
    # If use OpenCV, the channel order will be BGR, but here we keep it as RGB for consistency. " bgr_array = rgb_array[:, :, ::-1]  # RGB → BGR "

    return rgb_array