# single_file_projects

A sortiment of single-file projects that aren't worth their own repo.

Most if not all of them stem from the Jetbrains Academy Python course, which I highly recommend.

The projects have been minimally edited so it's not a complete freakshow (I mostly just got rid of global variables), but I've absolutely tried my best to keep their original 'spirit' from the time I originally wrote them alive.

If you still want to see the full, unadultered versions including the learning process, head over to my gists:

https://gist.github.com/ms85py

Anyway, if the names of the files isn't enough of a clue, I've got you covered:

## Coffee Machine
is a simple (text-)ui-guided coffee machine.

It's the very first python project I've done and works just like you'd think:

the machine has a set amount of water/milk/beans/cups/money.

Buying drinks will reduce the water/milk/... and add the cost of the type of coffee to the machines money.

While there's enough resources, you get your coffee. If there's not enough of any resource, the machine tells you what's missing.

You can also supply the machine by filling it up, take the money from it or simply display how much of each resource is left.

**Libraries/Modules used:** None.


## To-Do-List
is the first project I've done involving SQLite3 + the Python ORM SQLAlchemy.

It is, as the name suggests, a to-do-list.

You can see todays tasks, show all tasks for the week, show missed tasks and add/delete tasks.

I'm not using classes extensively here, because I'm not sure how it'd benefit from them.

I'm also not exactly happy with how I query things, but I couldn't think of a way to implement DRY (don't repeat yourself) without making the queries pretty obscure for everyone trying to understand what's going on, so I guess this way is "fine" for now.

**Libraries/Modules used:** SQLAlchemy, datetime.


## Simple Banking System
my third project in Python is a simple Banking system.

After using an SQLite3 DB and SQLAlchemy in the previous project, I now wanted to get to know 'raw' SQL more, so this was the perfect project.

It creates another SQLite3 DB, but this time I'm using it without an ORM and instead use SQL-queries for everything.

Upon running the program you'll at first see a simple menu with just 2 options, log-in to and existing account with your card number and pin - or create a new account.

Creating a new account will give you a card number and a PIN.

The card number is created via the 'random' module and then checked for validity by a checksum test that's using the Luhn-Algorithm.

https://en.wikipedia.org/wiki/Luhn_algorithm

After loggin in to an existing account you'll see another menu that'll let you do the usual banking stuff:

- View your balance
- Add income to the account
- Transfer funds to another account (with check if account is valid!)
- Close the account
- Log out
- Exit the program

I'm surely juggling things between functions too much here and there's absolutely room for improvement, but I think for the third project I've managed well.

**Libaries/Modules used:** random, sqlite3



## Rock, Paper, Scissors
with a highscore system & the option to use your own imaginary deck.

The fourth project centers around working with files and a small algorithm and a tiny bit of logic to handle the game, even when players choose to use their own deck.

When running the file (be aware you need a 'rating.txt' in the same directory!), you're asked to enter a name. This name will be used to read your score from the .txt file if you already played, or later save it to the .txt when you're done playing.

After entering the name you're then asked if you wish to play with the normal deck (rock, paper, scissors) or if you want to use your own deck, e.g. rock, paper, scissors, lizard, spock.

It's using a neat little algorithm to process the deck in a way that we're left with a 'gets_beaten' (great choice of variable name, I know~) list that contains every choice the users choice will get beaten by.

What's left is just checking if:

- PC choice = users choice -> draw

- PC choice in 'gets_beaten' -> pc won

- else -> player wins

Each draw adds 50 points to your score, each win adds 100. You can view your current rating by typing "!rating" and quit the game with "!exit".

All in all this project isn't anything special or impressive. But it's neat and taught me how to work with files and work my way around some things I wasn't aware of before - so I think it's done an excellent job.

Here, too, I'm sure there's better ways to do it by using more classes, but as soon as I thought about splitting it in classes for game/player/ai and so son, I was left wondering if that really would make things easier - which, in the end, I found not to be the case.

**Libraries/Modules used:** random



## Text Based Browser (simple)
is a very simple text based browser

Almost daily I read about people doing webscraping with Python by using BeautifulSoup or Scrappy on the pydis.com Python Discord.

I wanted to get in on the fun, too, so I thought this project would be a good first step.


It's also the first project I've tried command line arguments with, so starting this project is done by starting it via cmd and giving it a directory name as the first and only arugment.

If the directory already exists, it will tell you just that - if it doesn't, it creates the directory which will be used to store the visited websites in respective .txt files, as a kind of 'cache'.


The browser also observes the visited sites and current site via lists that act as stacks.

This is needed because the browser has a 'back' functionality, which works without having to re-load the page; it will be read from the .txt if there is one.

That means that the site will only be written to the file on the first visit - and loaded from that file on every visit after that.

To distinguish links from every other content, I used the Colorama module to print them in blue - it's more of me playing around than anything else though.


The browser is far from perfect in general, I'm really disliking the way I handled the 'back' functionality.

Even worse is the input handling - if I had to do it again, I'd use regex, but...urgh. I really don't like regex.

Now thinking about it, I guess even just splitting at the dots and taking the website name part would've worked way better~

But as I said, I'm trying to keep the 'spirit' from back when the files were originally written alive, so I'm not going to re-write them just to look good.

It's a learning process - and I like to see how far I've come by taking a look at my earlier shortcomings from time to time.

In the end I still think it was a nice way to get my feet wet in the world of scraping; but I don't think it's for me.

**Libraries/Modules used:** os, sys, requests, bs4, colorama



## Socket Bruteforcer (not all too malicious)
with mockup socket server to test out!

Readme for that one to be done. It's quite a bit and every time I start writing it, it ends in a big fucking wall of text~
