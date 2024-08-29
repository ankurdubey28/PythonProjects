with open('story.txt','r') as f:
    mylist=set()
    for line in f.readlines():
        words=line.split()
        for word in words:
            if word.startswith("<") and word.endswith(">"):
                mylist.add(word)



answers=dict()

for word in mylist:
    answer=input("Enter a word for "+ word+": ")
    answers[word]=answer

with open("story.txt") as f:
    story=f.read()


for word in mylist:
   story=story.replace(word,answers[word])

print(story)