# HentCLI
A python command-line tool to show random images from Rule34 in a command line.


As of right now, the install script is Windows only! (It doesn't work very well...)

This requires a terminal, that supports colored escape characters - conhost (the default windows terminal) won't do!
I suggest you use Windows Terminal

# Installation
Just download and start the install_windows.bat script! It **does not** require Admin privileges, and if you run it as admin it won't work on your default user!

# Manual installation
In the likely event of the install script not working do the following:

1. Create a folder named HentCLI in your home directory (for instance: C:/users/juje/HentCLI)
2. Create a folder named images in that new folder
3. Add the folder to the PATH and PYTHONPATH system (or user) variables
4. Put all of the files from this repo (except for install_windows.bat, and ofcourse readme.md) into **the HentCLI folder**
5. Install the dependencies using `pip install timg rule34`
6. Restart your shell
7. Enjoy!
8. Open an issue when it fails

# Usage
If you installed it correctly, just write `hentcli (tags)` into your shell!

The tags are space seperated. For example, if you want to get an image with the tags `darling_in_the_franxx` and `krokotritralalakikirikokodakamaronij` you would write `hentcli darling_in_the_franxx krokotritralalakikirikokodakamaronij`
