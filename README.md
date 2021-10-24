# **winget-export**
An executable (written in Python) that export a list of all programs (with proper winget packages available) currently installed and then creates a console script to automatically install those programs through winget. Useful when doing a clean install, or to bring your workframe with you in an USB.

## Requirements and how to use:
To run this program, you'll need to have winget installed on both your current system and the one you'll want to install the packages on. You can download the [latest version of winget](https://github.com/microsoft/winget-cli) on GitHub.

This script doesn't require Python. If it's the first time that you're using winget, the Microsoft Store may ask you to accept some sort of ToS before proceeding. In that case just write and enter `Y`.

Once the program finishes, you'll get the list of packages exported from winget as `winget_packages.json` and the batch file `package_installer.bat`. To install all your programs on the new PC/OS, transfer and run the batch file. Alternatively, you can load the json file with the `winget import` command through the console.

## Notes:

Different programs may have different instalations processes, so be sure to accept admin rights and other prompts when needed. Default installation settings are assumed when using winget, so if you need to tinker with some programs, it may be preferable to do a manual installation for those.

You can also open the batch installer with a text editor and delete the lines corresponding to the programs you may not want in your new PC/OS.

Lastly, winget may not always install the latest version of a package. Sometimes developers take some time to enroll their latest version in the list of winget packages. Use the `winget upgrade --all` command through the console to keep your programs up to date.

## Recent changelog:

(03-Oct-2021): Translating comments and such to english. Will upload files when done.

(03-Oct-2021): Translation done. Testing program in preparation for first release.

(04-Oct-2021): `RELEASE v1.0` - Temporary unpackaged release. Added `README.txt` for easier reading.

(13-Oct-2021): `RELEASE v2.0` - Source code packaged into a single executable file. Added more text prompts for higher clarity.

(24-Oct-2021): Made some slight changes to make the python script easier to read.