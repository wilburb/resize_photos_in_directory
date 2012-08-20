'''
Photo resizing script
@author wilburb@wilburweb.com

Purpose: Create multiple image sizes for all images in a directory.

Description: read through all photos in a directory (not recursively)
			 resizing each to the specified widths and storing in a
			 new directory with name corresponding to new widths.
			 (ie, photos run with sizes = [100, 200] becomes photos, 
			 	  photos_100, and photos_200)
			 Aspect ratio is maintained, and the dimensions given in 
			 the sizes array/list are for width only.
Usage: place the full path to your photo directory in 
       read_directory('') and put all desired sizes
       in the sizes array/list
'''

import os, sys
import Image

sizes = [100, 200, 300]

def read_directory(path):
    # create new directories to store resized photos
    for size in sizes:
        size_dir = path+'_'+str(size)
        if not os.path.exists(size_dir):
            os.makedirs(size_dir)
    for dirname, dirs, files in os.walk(path):
        for infile in files:
            for size in sizes:
                outfile = os.path.join(path+'_'+str(size), infile)
                infile_full = os.path.join(dirname, infile)
                resize_photo(infile_full, outfile, size)

def resize_photo(original_photo, new_photo, size):
    try:
        photo = Image.open(original_photo)
        photo.thumbnail((size,size), Image.ANTIALIAS)
        photo.save(new_photo, "JPEG")
    except IOError:
        print "cannot create thumbnail for '%s'" % original_photo

read_directory('')