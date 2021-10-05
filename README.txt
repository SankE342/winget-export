winget-export

A series of Batch and Python scripts that export a list of all programs (with proper winget packages available) currently installed and then creates a console script to automatically install those programs through winget. Useful when doing a clean install, or to bring your workframe with you in an USB.


Requirements and how to use:

To run this script, you'll need to have winget installed on both your current system and the one you'll want to install the packages on. You can download the latest version of winget (https://github.com/microsoft/winget-cli) on GitHub.

This script also requires Python. If you don't have Python installed, run 'export_packages.bat' to install it (through winget) and create the batch installer automatically. If you have Python, just run 'batch builder.py' through a console or terminal.

Once the program finishes, you'll get the list of packages exported from winget as 'winget_packages.json' and 'package_installer.bat'. To install all your programs on the new PC/OS, run the latter. Alternatively, you can load the json file with the 'winget import' command through the console.


Notes:

Different programs may have different instalations processes, so be sure to accept admin rights and other prompts when needed. Default installation settings are assumed when using winget, so if you need to tinker with some programs, it may be preferable to do a manual installation for those.

You can also open the batch installer with a text editor and delete the lines corresponding to the programs you may not want in your new OS.

Lastly, winget may not always install the latest version of a package. Sometimes developers take some time to enroll their latest version in the list of winget packages. Use the 'winget upgrade --all' command through the console to keep your programs up to date.


Recent changelog:

(03-Oct-2021): Translating comments and such to english. Will upload files when done.

(03-Oct-2021): Translation done. Testing program in preparation for first release.

(04-Oct-2021): RELEASE v1.0 - Temporary unpackaged release. Added 'README.txt' for easier reading.
