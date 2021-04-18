**HeadsTailsRatio**: In a long string of heads and tails (h(s) & t(s)) find the substring with the largest percentage of heads or tails that is under 100%. Suboptimal, bruteforce solution.

**ImagesToPDF**:
I got access to an array of scanned images of an APUSH textbook and my job was to reformat these into readable PDFs. This script takes in many jpgs (or other image formats) and converts them into one single PDF. After I made PDFs of each chapter, I decided to OCR these for convenience (make the PDF recognize text as text so that copy/paste and search work). I found the amazing free tool OCRmyPDF (https://ocrmypdf.readthedocs.io/en/latest/), but unfortunately the package would absolutely not install on Windows 10. As a result, I had to get Windows subsystem Ubuntu (WSL, which basically allows you to use linux tools as a Windows user). The package installed perfectly on there and I made the script generate a command for command prompt so that the PDF gets OCRed through WSL.

**Motion**:
In The Office, there is a famous scene where everyone is looking at a TV screensaver of a DvD rectangle bouncing around waiting for it to hit a corner (https://www.youtube.com/watch?v=QOtuX0jL85Y&ab_channel=TheOffice). Inspired by this, I used pygame (basically a graphics library) to draw a box and have balls bouncing within it. Each time a ball hits a corner, the corner turns that ball's color. There are also collisions between balls which you can toggle by hitting (space). I must warn you that unfortunately, none of the collisions or motion follow the laws of physics.


https://user-images.githubusercontent.com/61990860/115143159-8233b800-9ffa-11eb-91c8-7a6bd5139532.mp4


https://user-images.githubusercontent.com/61990860/115143162-852ea880-9ffa-11eb-92a3-a61542ec4f47.mp4


**PiFromRNG**:
I saw this problem on Joma Tech's Youtube Channel (https://www.youtube.com/watch?v=pvimAM_SLic&t=284s&ab_channel=JomaTech) and I thought that the solution and the entire concept was absolutely fascinating. The problem is: Given a function which randomly generates uniform values from 0 to 1, estimate Pi.

Here are a write up I made of the solution and the results from the python code:

![image](https://user-images.githubusercontent.com/61990860/115143268-1bfb6500-9ffb-11eb-88c0-62418a041b36.png)

![image](https://user-images.githubusercontent.com/61990860/115143319-68df3b80-9ffb-11eb-87b9-b4fee51a9868.png)


**PublicBot**:
I encountered a real life problem when during the Covid-19 pandemic my grandmother's flight back to Russia (since she had been visiting the US) kept on getting delayed again and again. The Russian Government began offering return flights for stuck tourists, but these flights happened once a week and were difficult for people to book. An announcement would be posted in a public Telegram channel at a random time notifying that registration was open to book a flight. The seats on these flights would be all taken within 15 minutes of registration opening. The channel sending the messages also had many other notifications so it was impossible to respond to everything. I made this Telegram bot to monitor that channel and look for a specific message. Since the message could vary a bit, I used a fuzzy text matching library to evaluate whether the message matched the target. This bot then sent a new message to a specific channel which could have custom loud notifications turned on only for when registration was actually open. I had about a week for the entire project which gave me time to also implement logging and remote commands through Telegram messages. The bot was successful in booking a spot for my grandma and the channel eventually garnered around 600 subscribers with a couple thank you donations. Bot can be changed to look for other messages pretty easily, but the code is somewhat messy.
