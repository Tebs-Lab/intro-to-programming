# Coding Essentials Outline

This class is a one-day workshop designed for students with little-to-no programming experience to gain familiarity programming concepts, software ecosystems, and ultimately learn to write a little bit of code themselves. However, the goals of this class are more about fostering empathy and understanding between less-technical people and engineers than they are about making the students into programmers.

_Note to instuctors_: in this lesson plan anything in **bold** is meant to be a question posed to your students. Anything in _italics_ is either a further instruction to you or the answer to a **question**. Everything else is something you might say out loud to the class.

**Remember: This is a one-day workshop, you can only do so much. Work the clock and use students' time efficently as much as possible.** 

## Objectives

*   Students can describe the main components of modern software infrastructure, and how they are connected. Especially the following:
    *   Point of Sale Systems
    *   Databases & Data Warehouses
    *   Web servers (their own and 3rd party APIs)
    *   Browsers
    *   Heavy Compute Machines (e.g. for data science workloads)
    *   Cloud Compute Infrastructure generally.  

*   Students can describe the main infrastructural components software development & deployment. Especially:
    *   Developers’ Local environment vs staging vs production
    *   Version control repositories
    *   Deployment infrastructure (CI/CD such as Jenkins, AWS role, “dev ops”)
    *   Monitoring infrastructure  

*   **(Less Important, skippable):** Students can describe that different languages are used for different tasks, and a little bit about why. Especially:
    *   Python (almost everything, “2nd best language for every task”)
    *   JavaScript (Websites, but increasingly a little more)
    *   Java / C# (Web infrastructure, games, enterprise)
    *   C / C++ (Systems, low level)
    *   SQL (totally different, just for getting data from a database!)  

*   Students can identify and define fundamental building blocks of code
    *   Print and the importance of the console
    *   Data types & collections (lists & dictionaries)
    *   If/else
    *   Loops
    *   Basic math
    *   Functions
    *   Errors & debugging   

*   Students can read basic python scripts.   

*   Students can solve simple problems with Python:
    *   Finding duplicates in two lists.
    *   Detecting if a word is a palindrome.
    *   Detecting if two words are anagrams of each other.
    *   Finding the most and least common elements in a list.
    *   **Bonus:** writing a simple text-based rock paper scissors game. 

# Lesson Plan:

Before starting the lesson write a broad version of the objectives somewhere that will remain visible to students throughout the day. Roughly:

*   Describe the software ecosystem/architecture of enterprise scale companies. 
*   Describe the process of software development and the software lifecycle.
*   Describe why there are so many different programming languages, frameworks, and tools.
*   Define core programming concepts that appear in most programming languages (using Python as an example).
*   Write simple Python programs. 

_The goal in the morning is to get students talking and thinking about the big picture of programming, both in general and within the context of their company. Focus on asking questions and facilitating a discussion rather than leading a presentation. Your knowledge and ability to connect ideas will be more valuable than a list of important concepts. Said another way; focus on diagraming what the students tell you about and pushing them for more information, rather than hitting every little topic mentioned in the outline below._

## Introductions (5-10 minutes)

Try to be quick, encourage the students to be quick also. Ask every student to answer these questions, **starting with the instructor.**

1. What is your name.
2. What do you do here at SomeCompany.
3. What is one thing you hope to learn in this class.

Make sure to tell people if they _will_ learn the thing they want to learn, especially if you don’t think it’s on the curriculum. **This is your best chance to set expectations.**

**Try to memorize their names as well.**


## Set The Agenda and Atmosphere (5-10 minutes):

*   This is a class with a lot of different levels of experience, and a lot of beginners.
    *   Please don’t belittle anyone for not already knowing something.
    *   In general please be kind and compassionate in class.   

*   Please ask lots of questions, and expect me to ask you a lot of questions.
    *   I will be facilitating group discussions, pair shares, exercises, and maybe even cold calling you!
    *   Don’t be afraid of being wrong, guessing then getting feedback is a great way to learn. 
    *   I love going on tangents, and I have a pretty strong breadth of knowledge. This class is meant to be valuable to _you_ so get your questions answered. 
    *   I may punt on some questions if we get TOOOOOO far afield.   

*   The more you engage, the more you will learn. 
    *   If you wanted to come to class and passively absorb some tidbits from a slideshow, I am going to disappoint you, just a heads up   

*   **Questions? Concerns? Thoughts?** 

In broad strokes, go over the agenda for the day. Use the objectives you wrote on the board somewhere as a guide for this. Here they are again:

*   Describe the software ecosystem/architecture of enterprise scale companies. 
*   Describe the process of software development and the software lifecycle.
*   Describe why there are so many different programming languages, frameworks, and tools.
*   Define core programming concepts that appear in most programming languages (using Python as an example).
*   Write simple Python programs. 
*   **Questions?**

## The Software Ecosystem (30-40 minutes)

**During this exercise, you should be drawing on the whiteboard _constantly_.** The goal of this section is helping students understand the breadth and complexity of modern software ecosystems. Most importantly, helping them understand the parts of the business that THEY interact with, which is why you want to **continuously probe the students for more:** “What else does SomeCompany use? What would this connect to? Who uses this, where are they in the diagram?

At a minimum, the following will probably come up so know how to put them on the board:

*   Websevers
*   DNS
*   Databases
*   Point of Sale Systems
*   Data Science / Machine Learning tools (data and compute)
*   Business Intelligence tools (e.g. Tableau)
*   “APIs” (they’re just other websevers!)

**Okay Here’s the actual discussion walkthrough:**

*   Over the next 30-40 minutes we’re going to build a big picture of software, how it works, and the physical infrastructure involved.
*   We’re going to talk about a lot of things that basically every business does with software, and we’ll try and get some of the specifics of SomeCompany with your help.
*   We’re going to diagram as much as we can on the whiteboard.
*   Let’s start off simple: How does a user get to SomeCompany’s website?
    *   User (phone/computer/tablet) makes types [www.SomeCompany.com](www.starbucks.com) into their browser
    *   HTTP request gets sent it to SomeCompany webserver
    *   Webserver responds, also using HTTP.
    *   **Boom? Have we left anything out (all of networking)? Ask follow ups if no one answers:**
        *   _How did the HTTP request know where to go? From [www.SomeCompany.com](www.starbucks.com) to this particular webserver?_
        *   _What if the user wants to log in? Would this be different? How?_
        *   _Are customers the only users of SomeCompany’ web systems?_   
	
*   **DNS**: The URL has to become an IP address, and SomeCompany probably operates their own DNS infrastructure. Possible they pay someone else (Cloudflare, NS1…)
    *   At a minimum, SomeCompany has to have their IP addresses in DNS servers.
    *   Those DNS servers communicate with other DNS infrastructure, mention ISP run, and other resolvers (maybe put them on the board in a different color)
    *   _DNS is a whole big ecosystem, don’t get into TOO much depth_.   

*   **Login:**
    *   User needs to send data.
    *   Server needs to… check that data against a database!
    *   _So add the database to our diagram._
    *   **Most of the time, we stay logged in… how does this work?**
        *   _Cookies (lots of tangents possible here, if you have time. Tracking cookies are always fun.)_   

*   **Databases & Data Warehouses:**
    *   So, the website needs a database for users and other website data. 
    *   Other teams and departments probably need data too… 
    *   Often times DB’s will be separated by task.
    *   Data warehouses for long term storage.
    *   Analytics databases for common use. 
    *   ...
    *   The data might be in very different formats in these databases for a variety of reasons like space efficiency or access speed.   

*   **What about for internal tools? We all know a lot is hidden to a user of your website…**
    *   _B.I. Tools probably come up here._
        *   _And/or some way for people to actually QUERY the databases._
    *   _Email maybe._
    *   _Point of Sales systems._
    *   _Encourage them to say more!!_   

*   **What about “Web APIs”? What are these?**
    *   _Mostly just 3rd party web servers. You an add one._    

*   **What about data scientists? Where is there code running here?**
    *   _Highlight the difference between something like fraud detection (live, always running) and report generation / data analysis._
    *   _Compute to train the model on AWS vs the running version of the trained model (webserver)_
    *   _Compute to train the models and crunch the numbers vs slide deck, charts, etc that is the deliverable for many data scientists._    

*   **Where the heck does all this data come from?**
    *   _Point of sale._
    *   _Purchased data._
    *   _Painstaking data collection (forms, surveys, consumer research…)_
    *   _Website monitoring / tracking._
    *   _And… all this has to be run through software that converts it to a schema that your database can handle, so that it can be useful!_   

*   **What about “The Cloud”, how does that fit into all this?**
    *   _Most of the services on the board are probably running on AWS or Azure, or something similar._
    *   _There might be one or several instances, possibly even one of more providers._
    *   _E.g. DNS might be with one “cloud provider” and your web servers might be on a separate cloud provider._

**This is a good time to give the students a quick break. Take 5-10. It should be about ~10:30am by now.**

## The Software Development Lifecycle (10-15 minutes)

**In this section we’ll be expanding the diagram we already made, hopefully there is room. If not, try to leave some of the more critical things on the board. For example, the Web Servers.**

*   Version control is one of the most foundational pieces of infrastructure in software development. 
*   **What is version control? Does anyone use it?**
    *   Describe git, and github:
        *   Git is VC software, github is a service built on that software to host code.
        *   Keeping old versions, enabling rollback in case of bugs, enabling audits of old code.
        *   It also has collaboration tools like branching so that many people can work on the same (large) codebase at once while stepping on eachother’s toes a bit less.    

    *   In their daily work, an engineer will typically start by pulling down any new code.
    *   Then make changes locally.
    *   Test it, code review, other process can happen.
    *   Then push the code up to the repo.    

*   **Does this mean the code on the webserver has changed?** (no)
    *   When we push the code to GitHub, there still has to be a process to move that new code onto the servers where it will be executed.
    *   This is “DevOps” and for a lot of companies this is mostly automated now—that automation is ITSELF software, which makes this kind of recursive and weird but bare with me... 
    *   Code gets pushed to github, a hook detects that push, that hook takes the code, and moves it to the web server, where it can now be executed.    

*   Describe the differences between: Production / Staging / Dev /  Test / Local
    *   **Has anyone heard these terms used?**
    *   **What do they mean?**   

    *   There are usually several different “environments” that this code runs through during a deployment.    

    *   Local: the programmers computer. Might have lots of differences between the production hardware, OS, and more.    

    *   Dev / Test: Available to programmers & QA engineers, closer to production hardware but at a much smaller scale. Used for devs to test things out, or possibly give demos of new features.   

    *   Staging: Typically not available to the public, but mirrors the production setup very closely at a smaller scale. Typically this is used for running automated tests just before deployment.    

## The Purpose of Different Languages, and Different Kinds of Programming (20-30 minutes)

**This section is to get students thinking about the breadth of software, but it is also to elucidate the fact that all these different subdomains share a lot in common. We’re going to be focused on learning those key foundational aspects of programming after lunch.**

*   **What IS a programming language?**
    *   _You’ll get some interesting answers here…_
    *   _Help students see that it is more or less: text with special rules on how it must be formatted._
    *   _Rules help the “compiler” or “interpreter” understand and execute the code._
    *   _But most programs are also made with humans in mind: Other programmers must be able to read your code!!_   

*   **Who here speaks a programming language, even just a little?**
    *   **Which one?**
    *   **What do you use it for?**   

*   **What languages have you heard of, besides the ones you’ve used?**
    *   **What do you think it’s used for?**   

*   _Be prepared here to discuss the different languages and their purpose. At a minimum you should expect the following to come up:_   

    *   _Python (almost everything, “2nd best language for every task”)_
    *   _JavaScript (Websites, but increasingly a little more)_
    *   _Java / C# (Web infrastructure, games, enterprise)_
    *   _C / C++ (Systems, low level)_
    *   _SQL (totally different, just for getting data from a database!)_
    *   _HTML/CSS_   

*   _Bring up a few more than the students guess, unless they collectively get a lot._
    *   _The point is: There are about a zillion different kinds of programming languages._    

*   **Why are there so many different programming languages?**
    *   _Different languages for different specialties within programming._
    *   _Which means: when someone says they are a “programmer” it can mean a ton of different things, from application engineering to systems engineering the daily work can be vastly different._    

*   Describe the difference between “declarative” languages, and “imperative” languages. 
    *   SQL, HTML, and CSS are all declarative: you describe what you want and the computer makes it happen, but the process of how it happens is invisible to you.
    *   C. JS, Python are all imperative: You describe the steps that the computer will take to fetch or process the data.
    *   It’s not always a clean hard-line distinction, some programs have aspects of both depending on where your abstractions start. E.g. JS almost feels declarative when you consider that the real executing code is Machine Code.    

*   After lunch, we’re going to learn to write and execute simple programs in Python. 
*   **Questions?**


## Environment Setup Help (Till Lunch)

Students SHOULD have VS code setup, but that might not be the case. Make sure everyone has it, and direct them to install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) if it is not already installed. Give the students a goal, execute this very simple program from within VS Code:

```
print(“hello world”)
```

**As a backup students can use repl.it instead. Not as ideal, since they won’t have their own work saved on their machine to take away from the class, but if firewall issues or something like that comes up, it’s better than nothing.**

# Lunch Break

_After lunch your goal should be getting out of lecture mode as fast as possible. There are both code reading and code writing exercises designed to help students learn these fundamental concepts without you just telling them. This content is utterly uninteresting as a lecture about rules and syntax and the differences between ‘expressions’, ‘statements’, and all that stuff._

_Tell them the absolute basics, then push them off the cliff. They’ll learn to fly or they’ll ask you for help and both are better than a boring lecture._


## Programming Fundamentals (5-10 minutes)

*   Programming is always about data.
    *   Fetching data.
    *   Transforming data.
    *   Processing & combining data.
    *   Saving data. 
    *   _And that’s about it._
    *   **But what does data even mean? What kinds of data are there?**
        *   _As long as students say something that has ever been on a computer… they are correct! Videos are data, images are data, text is data, numbers are data…._   

*   It sounds simple and in a way it is. Even very complex programs are made by combining simple building blocks.
    *   Legos are a great metaphor, the game Minecraft is another good one:
    *   From simple rules and simple atomic units (bricks) you can build huge and elegant masterworks.    

*   All programming languages have ways to handle data and different data types.
*   Nearly all programming languages have the following:
    *   Variables, control flow, functions.
    *   _I say nearly because there are languages like CSS/HTML (no control flow, no variables) as well as languages like Prolog (no control flow, variables are… different)_   

*   We’re now going to examine these fundamentals in the context of Python. 
    *   Different languages have different syntax, different restrictions, and sometimes  different data types.
    *   But much of what we learn today will be the same in other languages, just like learning “grammar” is helpful in learning other human languages.

## Syntax and Basics By Example (30-40 minutes)

_Work through the code-examples folder with the students. Encourage students to ask a lot of questions, live code changes that they request and run the samples. Ideally this shouldn’t take too long, so try to keep things moving._

_Tell the students we’re going to look at more realistic examples very soon, and focus on the syntax—this is like learning the alphabet before we read. “A makes the sounds ‘uhh’, ‘ay’ … etc.” This part can be painful, but we have to crawl before we can walk._

_The purpose of these examples is to:_

*   Introduce syntax fundamentals
    *   **Especially scope and whitespace, which so important in python!**
*   Introduce the idea of data types
*   Introduce variables
*   Describe how computers are absurdly “pedantic”
    *   case sensitivity, 
    *   no ability to infer,
    *   “the computer does exactly what you told it, not what you THINK you told it”
*   Introduce lists and dictionaries
    *   A few builtin functions (append, get, len…)
    *   Point students towards documentation for more
*   Introduce loops
*   Introduce if/elif/else
*   Introduce functions
*   **Quick break, ~5 minutes try not to lose too much momentum, but let students catch their breath.**


## Reading Code Exercises (~60 minutes)

_Work through the reading-exercises folder with the students. Work through each code file one by one and:_

*   **Work the clock**: set a reasonable amount of time and put a timer on the projector for students to see (5-10 minutes should be enough)
*   **Work in pairs or groups**: students need to practice explaining code to each other!
*   **Let them lead:** when time is up ask if anyone wants to describe the code.
    *   Then ask for answers to the questions in the comments.
    *   If everyone is confused, help them out by describing the code.

**Take a longer break now, the students have earned it!**


## Writing Code Exercises (until there are 30-40 minutes left in class)

_The class finishes with a lot of time for students to practice writing code. Have students work through the exercises in writing-exercises one by one. The order is frankly arbitrary, and if students want to work on them out of order based on their interest, that’s totally fine. Similarly, most students will probably not finish all 5 exercises and that’s also fine. If some students DO finish all the exercises before class ends you can set them up with harder problems on leetcode.com, codewars.com, hackerrank.com or something similar._

_Unlike the reading exercises, I suggest allowing students to have this block largely uninterrupted. If a handful of students are encountering a similar problem, bring the class together to look at a solution, then let them go back to work._

_Encourage students to work alone or in pairs, but not in groups of 3 or more. Before you unleash the class on the exercises, spend 5-10 minutes describing a good strategy for approaching these coding problems (more or less this is [Polya’s Method](https://math.berkeley.edu/~gmelvin/polya.pdf))_:

*   Step 1: Understand the problem.
    *   Define the input and output carefully
    *   Create examples / test cases
    *   Give names to important concepts if necessary
*   Step 2: Make a plan
    *   Use comments, or pseudocode on a whiteboard or paper
    *   Make a diagram
    *   Work backwards
    *   Guess and check
*   Step 3: Enact the plan
    *   Take your plan and translate it into code
    *   This step is the easiest for folks who have already mastered their programming language
    *   But it is hardest the first few times, since you’re learning the language
    *   This is the part where the computers irritating pedanticness is felt most heavily.
*   Step 4: Revise and revisit
    *   Did your plan work? 
    *   What specifically worked? What didn’t?
    *   Ask yourself if you can break your code, are there edge cases you haven’t yet considered?
    *   Ask how you can make it better (faster? more readable?)

## Review Two (or more) Solutions (with the last 30-40 minutes of class)

*   _Quickly poll the class to see who solved which problems_
*   _Pick two of the problems such that a majority of the class solved at least one of them_
    *   _(most likely the first two problems!)_
*   _Ask a student to demonstrate their solution_
    *   _Then you demonstrate the sample solution_
*   _Thank the students, and release them back into the wild._