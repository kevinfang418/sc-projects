"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_dist = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0
    total_green = 0
    total_blue = 0

    for i in range(len(pixels)):
        pixel_red = pixels[i].red
        total_red += pixel_red
        pixel_green = pixels[i].green
        total_green += pixel_green
        pixel_blue = pixels[i].blue
        total_blue += pixel_blue
    average = [total_red//len(pixels), total_green//len(pixels), total_blue//len(pixels)]
    return average


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    best_pixel = pixels[0]
    average = get_average(pixels)
    color_dist = get_pixel_dist(pixels[0], average[0], average[1], average[2])
    best = color_dist
    for i in range(len(pixels)):
        color_dist = get_pixel_dist(pixels[i], average[0], average[1], average[2])
        if color_dist < best:
            best = color_dist
            best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # assign list to store best pixel from get_best_pixel function
    best = []
    # assign list to store all pixels from each image
    new_pixel = []
    # read same (x, y) from each image then append to new_pixel list
    for x in range(images[0].width):
        for y in range(images[0].height):
            for i in range(len(images)):
                new_pixel.append(images[i].get_pixel(x, y))

    # get the numbers of pixel from each image
    for j in range(len(new_pixel)//len(images)):
        # input pixels from each images to get best pixel function then append to best
        best.append(get_best_pixel(new_pixel[j*len(images):j*len(images)+len(images)]))

    # assign variable k and fill best pixel to result
    k = 0
    for x in range(result.width):
        for y in range(result.height):
            new_img = result.get_pixel(x, y)
            new_img.red = best[k].red
            new_img.green = best[k].green
            new_img.blue = best[k].blue
            k += 1
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
