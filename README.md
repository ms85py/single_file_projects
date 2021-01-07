# single_file_projects

A sortiment of single-file projects that aren't worth their own repo.

Most if not all of them stem from the Jetbrains Academy Python course, which I highly recommend.

The projects have been (slightly) re-written so I won't have to be ashamed putting 'em on github. :P

If you want to see the full, unadultered versions including the learning process, head over to my gists, but be warned: it's 'global' hell:

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
