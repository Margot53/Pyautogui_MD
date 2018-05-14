name = "Margot"
subjects = ["English","Spanish","Math","Science","History"]

print("My name is " + name)

#print(subjects)

for i in subjects:
    print("One of my classes is " + i)

characters = ["Ted Mosby","Lily Aldren","Marshall Ericson","Barney Stinson","Robin Scherbatsky"]

for i in characters:
    if i == "Ted Mosby":
        print(i + " is a desperate guy trying to find love")
    elif i == "Lily Aldren":
        print(i + " is a kindergarden teacher who is married to Marshall")
    elif i == "Marshall Ericson":
        print(i + " is a laywer who wants to save the world from global warming and is married to Lily")
    elif i == "Barney Stinson":
        print(i + " is a crazy man who makes everyday legen wait for it dary!")
    elif i == "Robin Scherbatsky":
        print(i + " puts her job infornt of everything and is from Canada")


tvshows =[]

while True:
    print("What are your favorite tvshows? 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        tvshows.append(answer)

for i in tvshows:
    print("One of your favorite tvshows is " + i)

    
   
