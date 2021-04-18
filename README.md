# Personal-Project-Collection
A small collection of personal projects

I apologize in advance as some of the projects have spahgetti code and/or zero to few comments. I hope to have the time to fix that in the future.

Here is an overview of all the projects:

**15-Puzzle-Game**: A pygame version of the 15 Puzzle

**Benfords-Law**: A dataset of US City Populations [https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population] analyzed for Benford's Law.

**Bulls-and-Cows**: The game bulls and cows with option to guess versus computer or for computer to guess versus you where computer uses bruteforce algorithm to win.

**Cube-Puzzle-Solver**: Imagine a 3D 3x3x3 cube made of little cubes. Now this cube is cut up into figures of cubes and the figures are glued together. Code takes input of figures and assembles them back into large cube.

**Infection-Simulation**: See Repo https://github.com/FedyaS/Estimating-Active-Cases-in-an-Epidemic-Model

**RankerBot**: Discord Bot which utilizes commands to create events, record people who react, and remind participants to attend via a ping. See Repo https://github.com/FedyaS/RankerBot

**Other:**

**-HeadsTailsRatio**: In a long string of heads and tails (h(s) & t(s)) find the substring with the largest percentage of heads or tails that is under 100%. Suboptimal, bruteforce solution.

**-ImagesToPDF**: Script assembles a collection of Images and turns them into a PDF, then provides a Windows Subsystem Linux command to OCR this PDF using OCRmyPDF package.
-Motion: Pygame balls bounce inside of a box. If they touch a corner the corner turns the color of the ball. Turn on ball to ball collisions by hitting SPACE. (Inspired by The Office DVD Logo bouncing.)

**-PiFromRNG**: Given a function which randomly generates numbers between 0 and 1, estimate Pi. This problem / solution was not invented by me, but this is a simple python implementation I coded.

**-PublicBot**: A Telegram Bot which scans a chat for messages similar to a prior message. Sends alert to different chat when said message is found. Includes logging system and commands to remotely test/operate the bot through Telegram.




Almost all of the packages used are builtins except for:

-pygame (Used in multiple projects)

-pygame-gui (only Infection-Simulation)

-Pillow (only ImagesToPDF)

-telegram (only PublicBot)

-telethon (only PublicBot)

-fuzzywuzzy (only PublicBot)

For projects with multiple files, you will need all the files to be in the same directory for the code to work.
