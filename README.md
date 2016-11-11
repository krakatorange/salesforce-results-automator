SalesForce Results Automator

test.py - The controller

This script displays the status of all results for tickets older than 24 hours. Executing this script submits search queries by ticket ID number through prometric.my.salesforce.com using the salesforce RESTful API. The final results are opened in your default web browser in individual tabs.

This script goes through 4 primary phases:
  1. Execution of the SQL analyzer using the appropriate SQL script after which an Excel (.xls) file is created.
  2. The ID numbers are read from the Excel (.xls) file and are used to build POST requests to send through the REST API.
  3. The API responses with a JSON format of the search results with the ticket status information and ticket URL.
  4. The URL is opened in the default web browser for every ticket ID that is passed through the API and responds successfully.

To use this script; download this repo, unzip it, and launch "test.py".
