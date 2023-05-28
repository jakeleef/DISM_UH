# DISM_UH
This tool is programmed in Python and generated as an .exe with PyInstaller. The purpose is to make the DISM command prompt tool easier to use by giving the user a list of packages that can be uninstalled so they don't have to enter each package manually, and can instead enter only their index on the list and the program takes care of the rest.

To use this tool, you can either run the .exe as an admin, or run the python file as an admin in an IDE or using command prompt with admin privlages.

Once started, it runs DISM /Online /Get-ProvisionedAppxPackages | select-string Packagename and extracts all the resulting PackageNames.

It prints these names to a list and allows the user to select the index of each one individually or by entering multiple selections separated by a comma.

Once the user has entered a selection(s), it runs DISM /Online /Remove-ProvisionedAppxPackage /PackageName:PACKAGENAME on each packagename that is pointed to by the entered indecies.

There is almost no exception handling, partly because the program is VERY simple, and partly because there is an assumption of a certain level of computer literacy if you are using this script.

The .exe is located int he dist folder. 
