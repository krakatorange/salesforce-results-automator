import webbrowser
import mechanize
import requests
import getpass
import Crypto
import json
import xlrd
import xlwt
import time
import os

#=========================================================
# Enter salesforce credentials and encrypt
#=========================================================
print('\n========================================================= '
	+ '\n Welcome to the Prometric Salesforce Results Automator'
	+ '\n========================================================='
	+ '\n\nEnter your Prometric credentials')
	
usr = raw_input('\nUsername: ')
pwd = getpass.getpass('Password: ')

from Crypto.Cipher import AES # AES password encryption
encryption_suite = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
decryption_suite  = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
cipher_text= encryption_suite.encrypt(pwd)

print('\nUser: ' + str(usr))
print('encrypted Password: ' + str(cipher_text))

decipher_text = decryption_suite.decrypt(cipher_text)

print('decrypted Password: Lol! You thought I\'d let you see this?!'
   # + 'decipher_text'
    + '\n')
	
#=========================================================
# Start Timer
#=========================================================
start = time.time()

#=========================================================
# Execute SQL Analyzer script and save to .xls file
#=========================================================
from subprocess import call
# call(["netstat", "-n"])

os.system('netstat -n > data.txt')

data = []
with open("data.txt") as f:
	for line in f:
		data.append([word for word in line.split("  ") if word])

wb = xlwt.Workbook()
sheet = wb.add_sheet("New Sheet")
for row_index in range(len(data)):
    for col_index in range(len(data[row_index])):
        sheet.write(row_index, col_index, data[row_index][col_index])

wb.save("Book1.xls")

#=========================================================
# Read from .xls file
#=========================================================
book = xlrd.open_workbook("Book1.xls")
print "The number of worksheets is", book.nsheets # test sheets
print "Worksheet name(s):", book.sheet_names() # test sheet names
sh = book.sheet_by_index(0)
print sh.name, sh.nrows, sh.ncols
foreign_ip = sh.cell_value(rowx = 4, colx = 2)
print "Element at cell B2 is ", foreign_ip # example get specific cell
# for rx in range(sh.nrows):
	# print(sh.row(rx))

'''
#=========================================================
# Search results by ID between 24 hrs and MAX hrs (searchform method)
#=========================================================
url = "https://pypi.python.org/pypi/simple-salesforce"
br = mechanize.Browser()
br.set_handle_robots(False) # ignore robots

# for loop for every record in results
for rx in range(4, 8):
	br.open(url)
	br.select_form(name = "searchform")
	br["term"] = sh.cell_value(rowx = rx, colx = 2)
	print(br["term"])
	res = br.submit()
	content = res.read()
	modcount = rx - 3
	with open("results" + str(modcount) + ".html", "w") as f:
		f.write(content)
	webbrowser.open("results" + str(modcount) + ".html")
# end for loop
'''

#=========================================================
# Search results by ID between 24 hrs and MAX hrs (REST API method)
#========================================================= 
url = 'http://jsonplaceholder.typicode.com/todos'
response = requests.request('GET', url)
data = json.loads(response.text)
# print(data)
	
#=========================================================
# End Timer
#=========================================================
end = time.time()
print('\nProgram runtime: ' + str(end - start))
