# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the 
# greatest number of mail messages. The program looks for 'From ' lines and takes the second 
# word of those lines as the person who sent the mail. The program creates a Python dictionary 
# that maps the sender's mail address to a count of the number of times they appear in the 
# file. After the dictionary is produced, the program reads through the dictionary using a 
# maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()

for line in handle:
    if line.startswith("From "):
        emails[line.split(" ")[1]] = emails.get(line.split(" ")[1], 0) + 1

bigCount = 0
bigEmail = 0

for key,value in emails.items():
    if bigCount is None or value > bigCount:
        bigEmail = key
        bigCount = value

print bigEmail, bigCount