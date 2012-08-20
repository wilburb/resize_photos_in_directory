Photo resizing script
=====================

Authors
-------
wilburb@wilburweb.com

Purpose
-------
Create multiple image sizes for all images in a directory.

Description
-----------
read through all photos in a directory (not recursively)
resizing each to the specified widths and storing in a
new directory with name corresponding to new widths.
(ie, photos run with sizes = [100, 200] becomes photos, 
     photos_100, and photos_200)
Aspect ratio is maintained, and the dimensions given in 
the sizes array/list are for width only.

Usage
-----
place the full path to your photo directory in 
read_directory('') and put all desired sizes in the 
sizes array/list
