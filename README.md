SalesForce Results Automator
-------------------------------------

main.py - The main controller
re.py - The temporary folder clean up utility

This script displays the status of all results for tickets older than 24 hours. Executing this script submits search queries by ticket ID number through prometric.my.salesforce.com using the salesforce RESTful API. The final results are opened in your default web browser in individual tabs.

This script goes through 4 primary phases:
  1. Execution of the SQL analyzer using the appropriate SQL script after which an Excel (.xls) file is created.
  2. The ID numbers are read from the Excel (.xls) file and are used to build POST requests to send through the REST API.
  3. The API responses with a JSON format of the search results with the ticket status information and ticket URL.
  4. The URL is opened in the default web browser for every ticket ID that is passed through the API and responds successfully.

To use this script; download this repo, unzip it, and choose one of the options below:

Run in Command Prompt:
	
	1. If you don't have python installed, go to "https://www.python.org/downloads/"
	   and download the most recent version of python 2.7, if else skip to step 2
	2. Go to path
	3. Run "python main.py" in the command line

Run as executable:

	1. Go to "https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/"
	2. Download the correct version of py2exe
	3. Go into the directory of main.py
	4. Create file "setup.py" and copy/paste below code:
		
		from distutils.core import setup
		import py2exe

		setup(console=['main.py'])

	5. Run "python setup.py install" once to update required modules for the build
	6. Run "python setup.py py2exe" to build the distribution
	7. Go into the newly created dist directory and run "main.exe"
	8. You can now move the "dist" folder to any location you like (windows machines only)
     and run the application by double clicking on main.exe in the folder.

Tips:

	1. Make sure you don't name any other files in your pre-build folder the same as
	   the names of dependencies in the build folder or you will error out.
	2. Make sure you have all the correct modules installed and imported in your script
