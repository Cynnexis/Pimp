# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

import argparse
from PIL import Image, ImageEnhance
from typing import Optional, Union


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(prog="Pimp",
                                     description="Pimp is a Python-script that enhances multiple images from a single command line by changing their contrast and saturation level.")
    parser.add_argument("-i", "--image", nargs='+', required=True,
                        help="The images as input. All given images will be loaded, modified and then saved somewhere else. The original images will not be changed, unless the option -f (--force-overwrite) is given.")
    parser.add_argument("-o", "--output", default=None, type=Path,
                        help="The directory output. This option is compatible with -f (--force-overwrite), that will save the copy of the image in the given output folder and overwrite the original images. Note that this parameter is required, except in the case where -f is used, where it becomes optional.")
    parser.add_argument("-f", "--force-overwrite", dest="overwrite", default=False, action="store_true",
                        help="The given images will be overwritten.")
    parser.add_argument("-c", "--contrast", default=20, type=int,
                        help="The contrast level to apply to all images.")
    parser.add_argument("-s", "--saturation", default=1.2, type=float,
                        help="The saturation level to apply to all images.")
    args = parser.parse_args()

    # Validate arguments
    if not args.overwrite and args.output is None:
        parser.error("An output directory is required.")
    if args.output is not None and not args.output.exists():
        args.output.mkdir(parents=True, exist_ok=True)
    return args


def change_contrast(image: Union[str, Image.Image], contrast_level: Optional[int] = None) -> Image.Image:
    """Change the contrast of an image."""
    if isinstance(image, str):
        image = Image.open(image)
    if contrast_level is None:
        args = parse_args()
        contrast_level = args.contrast
    contrast_factor = (259 * (contrast_level + 255)) / (255 * (259 - contrast_level))

    def apply_contrast(c):
        return 128 + contrast_factor * (c - 128)

    return image.point(apply_contrast)


def change_saturation(image: Union[str, Image.Image], saturation_level: Optional[float] = None) -> Image.Image:
    """Change the saturation of an image."""
    if isinstance(image, str):
        image = Image.open(image)
    if saturation_level is None:
        args = parse_args()
        saturation_level = args.saturation
    converter = ImageEnhance.Color(image)
    return converter.enhance(saturation_level)


def main():
    args = parse_args()
    for image_path in args.image:
        with Image.open(image_path) as image:
            # Applying contrast
            contrasted_pil_img = change_contrast(image)

            # Applying saturation
            saturated_contrasted_pil_img = change_saturation(contrasted_pil_img)

            # Saving image
            if args.overwrite:
                output_path = Path(image_path)
            else:
                output_path = args.output / image_path.name
            saturated_contrasted_pil_img.save(output_path)


if __name__ == "__main__":
    main()