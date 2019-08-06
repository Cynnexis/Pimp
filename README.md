# Pimp

![language: python][shield-language] ![license: GPL][shield-license] ![python: 3.7][shield-python-version]

Pimp is a Python-script that enhance multiple images from a single
command line by changing their contrast and saturation level.

## Getting Started

This instructions will give you a copy of the source code of the
software, as well as its minimal configuration to run it properly.

### Prerequisites

*This section is still in progress*

You need [Python 3.7][python 3.7] to execute this script.

Here is a list of Python package to install to make this program
works:

```bash
pip install typeguard
pip install pillow
```

if you use Anaconda, use the following commands:

*On Unix:*

```bash
source activate <env>
pip install typeguard
pip install pillow
```

*On Windows:*

```bash
activate <env>
pip install typeguard
pip install pillow
```

### Installing

To install this script, simply download the [script](https://raw.githubusercontent.com/Cynnexis/Pimp/master/pimp.py),
or clone this repo:

```bash
git clone https://github.com/Cynnexis/Pimp.git
```

### Running the script

To run the script, use the following commands:

```bash
cd pimp/
python pimp.py -i images/* -o pimped-images/ -c 20 -s 1.2
```

This will take all images in the folder `images/`, process them and save the results
in `pimped-images/`. The contrast level is **20**, and the saturation level is
**1.2**.

The following is the list of all parameters:

* `-i`/`--images`: The images. All given images will be loaded, modified and
then saved somewhere else. The original images will not be changed, unless the
option `-f` (`--force-overwrite`) is given.

* `-o`/`--output`: The directory output. This option is compatible with `-f`
(`--force-overwrite`), that will save the copy of the image in the given
output folder and overwrite the original images. Note that this parameter is
required, except in the case where `-f` is used, where it becomes optional.

* `-f`/`--force-overwrite`: The given images will be overwritten. Be very
careful using this option.

* `-c`/`--contrast`: The contrast level to apply to all images.

* `-s`/`--saturation`:The saturation level to apply to all images.

## Built With

* [Python 3.7][python 3.7]
* [typeguard][typeguard]
* [PIL][pil]

## Contributing

No contribution system for this repo.

## Versionning

This project is controlled by [Git][git] and [GitHub][github].

## Author

* **Valentin Berger ([Cynnexis](https://github.com/Cynnexis)):** developer

## License

This project is under the GNU Affero General Public License v3.0.
Please see the [LICENSE.txt](https://github.com/Cynnexis/Pimp/blob/master/LICENSE.txt)
file for more detail (it's a really fascinating story written in
there!)

## Acknowledgments

* [Håken Lid](https://stackoverflow.com/users/1977847/h%c3%a5ken-lid)
from "[StackOverflow - Change contrast of image in PIL](https://stackoverflow.com/a/42054155/7347145)"
* [abarnert](https://stackoverflow.com/users/908494/abarnert) from
"[StackOverflow - Change saturation with Imagekit, PIL or Pillow?](https://stackoverflow.com/a/16070333/7347145)"
* [PurpleBooth](https://gist.github.com/PurpleBooth) for giving an
[open-source template for README files](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).

[git]: https://git-scm.com/
[github]: https://github.com/
[python 3.7]: https://www.python.org/downloads/release/python-374/
[typeguard]: https://pypi.org/project/typeguard/
[pil]: https://pillow.readthedocs.io/en/stable/
[shield-language]: https://img.shields.io/badge/language-python-yellow.svg
[shield-license]: https://img.shields.io/badge/license-GPL-blue.svg
[shield-python-version]: https://img.shields.io/badge/python-3.7-yellow.svg