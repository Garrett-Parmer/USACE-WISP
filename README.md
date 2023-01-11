# USACE-WISP
Website for US Army Corps of Engineers Water Information Sharing Program to share water data with the public


You must have node.js installed to compile and run SCSS files. To install required dependencies for development, please open the command line and navigate to the project root folder. Once there, you will run 'npm install'. This will install all required dependencies listed in the package.json file.


SCSS is a CSS pre-processor that allows the usage of variables, functions, and various other features in CSS that are not otherwise available and this makes life all the more easier. To compile SCSS files into the CSS style sheet after making changes, use the command line to navigate to the program root folder and run the command 'npm run compile:sass'. Then open another command box and navigate to the root folder, where you will now run 'live-server'. This will allow you to make changes to the SCSS files and see the changes happen on the page in real time once you have saved the SCSS files.

The compile:sass script is a continuous script, meaning it will run until the command line is closed. The same goes for the live-server functionality.
