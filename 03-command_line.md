# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

Core Commands:
	pwd -> print working directory
	ls -> list of files in directory
	cd -> change directory
		.. -> navigate one layer up
		../.. -> navigate two layers up
	mkdir -> create new directory
	touch -> create new file


Option Modifications:
	-a -> list all content (includes hidden files)
	-l -> list all contents in long format
		1. Access Rights
		2. Number of files under that file
		3. Username
		4. Owner of file
		5. Size of file in bytes
		6. Date/Time of modification
		7. Name of file
	-t -> order files by time they were last modified
	-alt -> combines 3 above commands

File Commands:
	cp <file> <destination>/ -> copy file to a destination
		* --> wildcard
	mv <file> <destination>/ -> move file to a destination
	mv <file name> <new file name> -> rename file
	rm <file> -> remove a file
	rm -r <folder> -> remove folder


Redirection:
	echo <input> > <output file> -> echo is a standard input
	cat <file> -> displays output of file
		cat <file> > <file2> -> take output of left file and redirect into right file
		cat <file> >> <file2> -> take output of left file and append into right file
		cat < <file> -> take input from file on right and input into file on left
	
	uniq <file> -> filters out duplicates of adjacent lines
		sort <file> | uniq -> sorts file then filters out any duplicates
	sort <file> -> sort file contents
	grep <regex statement> <file> -> search for regex statement in the file
		grep -i -> case insensitive
		grep -R -> search files in a directory and output filenames and lines containing matched results.
			grep -Rl -> only outputs files (no lines)
	sed 's/<word to find>/<word to replace with>/g(global)' <file> -> accepts a standard input and modifies it on an expression (essentially find and replace)
		s -> substitution
		g -> global 
	Misc:
		| -> standard output on left and "pipes" it as standard input to the command on right
	Properties:
		stdin -> standard input (information inputted into terminal)
		stdout -> standard output (information outputted from a process)
		stderr -> standard error (error message outputted by failed process)


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls -> list of files in directory
ls -a -> list all content (including hidden files)
ls -l -> list all content in long format
ls -lh -> list content in long format with human readable sizes
ls -lah -> list content in long format (including hidden files) with human readable sizes
ls -t -> orders files by last modification date
ls -Glp -> list of files in long format, appends a "/" after the directories, and highlights the directories in blue
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

-t
-1
-R
-F
-p
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

