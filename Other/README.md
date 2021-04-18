HeadsTailsRatio: In a long string of heads and tails (h(s) & t(s)) find the substring with the largest percentage of heads or tails that is under 100%. Suboptimal, bruteforce solution.

ImagesToPDF:
I got access to an array of scanned images of an APUSH textbook and my job was to reformat these into readable PDFs. This script takes in many jpgs (or other image formats) and converts them into one single PDF. After I made PDFs of each chapter, I decided to OCR these for convenience (make the PDF recognize text as text so that copy/paste and search work). I found the amazing free tool OCRmyPDF (https://ocrmypdf.readthedocs.io/en/latest/), but unfortunately the package would absolutely not install on Windows 10. As a result, I had to get Windows subsystem Ubuntu (WSL, which basically allows you to use linux tools as a Windows user). The package installed perfectly on there and I made the script generate a command for command prompt so that the PDF gets OCRed through WSL.

Motion:
In The Office, there is a famous scene where everyone is looking at a TV screensaver of a DvD rectangle bouncing around waiting for it to hit a corner (https://www.youtube.com/watch?v=QOtuX0jL85Y&ab_channel=TheOffice). Inspired by this, I used pygame (basically a graphics library) to draw a box and have balls bouncing within it. Each time a ball hits a corner, the corner turns that ball's color. There are also collisions between balls which you can toggle by hitting (space). I must warn you that unfortunately, none of the collisions or motion follow the laws of physics.


https://user-images.githubusercontent.com/61990860/115143159-8233b800-9ffa-11eb-91c8-7a6bd5139532.mp4


https://user-images.githubusercontent.com/61990860/115143162-852ea880-9ffa-11eb-92a3-a61542ec4f47.mp4

