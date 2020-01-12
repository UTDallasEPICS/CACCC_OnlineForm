# CACCC_OnlineForm
UTD EPICS Children's Advocacy Center Online From Project

## Getting Started
Also remember to switch apache server to port 81 in bitnami windows manager.

There are 4 files in this folder.

First off use the bitnami wordpress file to install bitnami. 
	Click next till create admin account page.
		remember login and password as it will be needed later.
			one time thing.
	Click next till Deploy wordpress to the cloud page 
		Deselect the checkbox.
	Finish the installation.

A website should open up in your browser on the localhost.
	* To open this up again you have to:
		Make a shortcut to manager-windows.exe
		This file is where you installed bitnami under
		the wordpress5.3.2 folder.

The opened website should have Access WordPress written there.
	Click those words.
	New page should have Meta section with Log in button
	Click Log in under Meta.

Login in using the user and password you set during installation.


Click the plugins section in the browser tab 

Click Upload Plugin button.
	Select all-in-one-wp-migration-extension.zip file to upload
	from this folder.
	Press Activate Plugin button.

Then check the boxes for that plugin in the list of plugins shown.
	Both the All-in-One WP Migration and 
		 All-in-One WP Migration File Extension ones.

	and activate both if any of them are deactivated.

Then under plugin section you'll see new section called All-in-One WP Migration
Go there and select import.

Import from file or drag the localhost-wordpress-20191217-171628-113 wordpress file
to upload the website.

This will lof you out and make you sign in with new credentials:
	Username: epicsonlineclientform@gmail.com
	Password: kindlekindle

This will conclude setup for the site.


-----------------------------------------------------------------------------------------


For working on the pdf converter.

All the files are in Page-Flowables.zip file
Take this file unzip it.
go to repl.it and make a new python Repl.
Copy files from the file to the new repl. 
	* Just drag all those files into the repl.


-----------------------------------------------------------------------------------------



Things to do website:
	1. Final checks.
	2. Make the website work at CACCC. Start doing this right after setup.
		*Should be able to access website from tablet at site. 
		*Idea is to use 'computer ip':81/wordpress. Is how to get to the website 
		from the same network. It should work if:
			1. Both tablet and computer/server is on same (wifi)network.
			2. from tablet url type 'computer ip':81 and it should take you to
			website.
	3. .bat file to restart server if power goes down.
		*Ask Advisor for 2 and 3.
		*Get Started soon after setting up.
	4. Need to write some php code to make submit button send form csv directly to 
	python converter and making that automatic.

Things to do for converter:
	1. Need to make forms save in a pdf folder with a threshold of 150. Then it starts
	deleting oldest file for each new one added.
	2. In this 'def answer(element):' method you need to:
		1. make it so that if a string is too long then change font to half its size
		   write half string half abouve line and half below line to get more space 
		   for string.
		2. You can look into using flowables from reportlab flowables.
			*just search reportlab pdf and search for flowables in that doc.
		* these are two ways to solve the problem of string that are too long and 
		  overlap with the other text in the pdf.
	
	3. Make sure files are saved as 'lastname-firstname-date_submitted'

	4. make better comments and make a document for client to use.
		We want this part to be automatic.
	


## Built With
N/A
## Versioning
N/A
## LMASK
Team member:
  * **Sarah Nicole**    - Project Liason
  * **Luiz Astorga**    - Project Web Master
  * **Kira**            - Project Financial Officer
  * **Aditi**           - Project Manager
  * **Muhammad Salman** - Project Document Manager

## Acknowledgments
Previous EPICS groups that have worked on this project.
