# NSFW Image Detector And Organizer

This repository contains scripts to classify, rename, and reset image file names based on specific criteria.

## Install
`pip install nudenet`

`pip install tqdm` -- for progress indicator

### 1. Rename Low-Res and High-Res Images
Run the following command to rename low-resolution and high-resolution images based on the threshold defined in the settings file:

`python size.py`

##

### 2. Classify Nude Images
Run the following command to rename nude-detected images as defined in the settings file:

`python classifier.py`
##

### 3. Reset File Names
Run the following command to reset file names to their original format:

`python reset.py`
##

## Settings
The `settings.py` file contains the following configuration options:

### 1. Commit Changes: 
Control whether changes are applied to files. Set to False to run in "dry run" mode without modifying files.

`COMMITCHANGES = False`   Set to True to commit changes to files
##
### 2. Define Paths
`SCANPATH = 'G:/'` Base folder path

`TEMPPATH = SCANPATH + 'Zz_temp/'` Temporary folder path for processing

##
### 3.Preset File Name Tags
`ISNUDE = '_processed_'`

`ISNOTNUDE = '_filtered_'`

`ISCORRUPT = '_corrupt_'`

`ISLOWRES = '_lowres_'`

`ISHIGHRES = '_highres_'`

##
Processed files are not moved but renamed with the above presets.
#
Please configure the `settings.py` before running above commands.

