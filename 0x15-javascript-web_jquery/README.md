0x15. JavaScript - Web jQuery
Front-end
JavaScript

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
How to select HTML elements in JavaScript
How to select HTML elements with JQuery
What are differences between ID, class and tag name selectors
How to modify an HTML element style
How to get and update an HTML element content
How to modify the DOM
How to make a GET request with JQuery Ajax
How to make a POST request with JQuery Ajax
How to listen/bind to DOM events
- How to listen/bind to user events
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Chrome (version 57.0)
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should be semistandard compliant with the flag --global $: semistandard *.js --global $
You must use JQuery version 3.x
You are not allowed to use var
HTML should not reload for each action: DOM manipulation, update values, fetch data…


Tasks
0. No JQuery
mandatory
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

You must use document.querySelector to select the HTML tag
You can’t use the JQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 


