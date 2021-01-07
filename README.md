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
