go\_games.py can be used to download all you game data from OGS. You run it with

  python go\_games.py \<user\_id\>

Where \<user\_id\> is the number that appears in the URL when you acces your profile page on OGS.

clean\_games.py filters out a bunch of irrelevan information from the raw data, and sorts the games by the start date. You run it with

  python clean\_games.py \<file\>

Where \<file\> is the file output by the previous command.

rank\_progression.py turns the JSON data into a CSV file you can import into a spreadsheet program for analysis. The CSV contains only your rating in one column and the date corresponding to that rating on the next colum. I'm also currently filtering out the ratings corresponding to unranked games and tournament games for my own purposes. You run it with

  python \<file\> \<username\>

Again, the \<file\> is the file spit out by the previous command, and unfortunately I couldn't find a nice way to avoid you having to put your username as well.
