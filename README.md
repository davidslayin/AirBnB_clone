                        AirBnB clone: The Console

Description
  The airbnb clone project's goal is to deploy a simple copy of the airbnb website.Though, we will be tasked with building a command interpreter, the front-end, the database part and API for the whole project, we are focusing here on the back-end console( the command interpeter).

Storage
   Every time the backend is initialized, HolbertonBnB instantiates an instance of FileStorage called storage. The storage object is loaded/re-loaded from any class instances stored in the JSON file file.json. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.

Console
  It is a command line interpreter that allows the management of the backend of the airbnb clone. It can be used to handle and manipulate all classes utilized by the application.

How to use the Console

-To run the console in interactive mode, run the file console.py by itself:

	$ ./console.py
- When running in interactive mode , the console displays a prompt for input.
	$ ./console.py
	(hbnb)
- To quit the console, either enter the command quit or input EOF signal(ctrl-D)
	 $ ./console.py       or   $ ./console.py
         (hbnb) quit   		   (hbnb) EOF
	 $                         $

-And to run it in non-interactive mode, pipe any command into an execution of the file console.py at the command line. For example,

 	$ echo "help" | ./console.py
 	 (hbnb)
 	 Documented commands (type help <topic>):
	 ========================================
	 EOF  all  count  create  destroy  help  quit  show  update

	 (hbnb)
	 $
Console Commands
   The following commands are supported on the console.
