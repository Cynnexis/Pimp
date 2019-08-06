# -*- coding: utf-8 -*-

import os
import sys
import ntpath

import argparse
from PIL import Image
from PIL import ImageEnhance
from typing import *
from typeguard import typechecked

# Parse the arguments
p = argparse.ArgumentParser(prog="Pimp", description="Pimp is a Python-script that enhance multiple images from a single command line by changing their contrast and saturation level.")
p.add_argument("-i", "--image", nargs='+', required=True, help="The images as input. All given images will be loaded, modified and then saved somewhere else. The original images will not be changed, unless the option -f (--force-overwrite) is given.")
p.add_argument("-o", "--output", default=None, type=str, help="The directory output. This option is compatible with -f (--force-overwrite), that will save the copy of the image in the given output folder and overwrite the original images. Note that this parameter is required, except in the case where -f is used, where it becomes optional.")
p.add_argument("-f", "--force-overwrite", dest="overwrite", default=False, action="store_true", help="The given images will be overwritten.")
p.add_argument("-c", "--contrast", default=20, type=int, help="The contrast level to apply to all images.")
p.add_argument("-s", "--saturation", default=1.2, help="The saturation level to apply to all images.")
args = p.parse_args()

if not args.overwrite and args.output is None:
	# TODO: If there is only one image to treat, then args.output = "pimped-" + image.name, and continue the program
	print("Error: An output directory is required.")
	sys.exit(-1)

if args.output is not None:
	if not os.path.exists(args.output):
		os.mkdir(args.output)
	if os.sep == "\\":
		args.output.replace("\\", '/')
	if not args.output.endswith('/'):
		args.output += os.sep

args.saturation = float(args.saturation)

@typechecked
def change_contrast(image: Union[str, Image.Image], contrast_level: Optional[int] = None) -> Image:
	if isinstance(image, str):
		image = Image.open(image)
		image.load()
	
	if contrast_level is None:
		global args
		contrast_level = args.contrast
	
	contrast_factor = (259 * (contrast_level + 255)) / (255 * (259 - contrast_level))
	
	def apply_contrast(c):
		return 128 + contrast_factor * (c - 128)
	
	return image.point(apply_contrast)


def change_saturation(image: Union[str, Image.Image], saturation_level: Optional[Union[int, float]] = None) -> Image:
	if isinstance(image, str):
		image = Image.open(image)
		image.load()
	
	if saturation_level is None:
		global args
		saturation_level = args.saturation
	
	converter = ImageEnhance.Color(image)
	return converter.enhance(saturation_level)


for image_name in args.image:
	# Applying contrast
	contrasted_pil_img = change_contrast(image_name)
	
	# Applying saturation
	saturated_contrasted_pil_img = change_saturation(contrasted_pil_img)
	
	# Saving image
	if args.output is not None:
		saturated_contrasted_pil_img.save(args.output + ntpath.basename(image_name))
	if args.overwrite:
		saturated_contrasted_pil_img.save(image_name)
