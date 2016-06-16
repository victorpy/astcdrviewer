## astcdrviewer

## Synopsis

Simple Asterisk 12.8.1 CDR Viewer and CDR Rating engine made with Django Framework.

## Motivation

This project was created to show the asterisk CDR in the web, with user authenticacion support. Also CDR Rating was included in the project.

## Description
This project use Django Framework to implement a asterisk web CDR viewer. 
It uses the Django Auth for user authentication
It uses Django Admin to manage the users CRUD.
It has Accounts, the account has a credit and is associated with an asterisk accountcode and extension.
It has Rategroups and Rates for selected destinations, for one account.
It could Rate the CDR based on the Rates associated with the account.

In cron folder, there is a php file with the procedure to rate the CDR.
The original asterisk CDR are copied by trigger to a new table cdrtmp, before rating them.
In the sql folder is the db structure. Warning, the correct info should be added to the accounts and others tables, or the application will not work correctly. Right now, i will not add info on how the data should be added to the tables, but you could work around just by looking at the tables columns.

## Installation

Install Django
Download the files from the github repo
Create the database
Load the needed info on the tables with djando admin.
Login the system runing the Django web server.

## Contributors

victorpy@gmail.com

## License
released under the http://opensource.org/licenses/MIT  MIT License.

