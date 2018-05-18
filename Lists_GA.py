name = "Greer"

subjects = [" English", " Math", " Science"," Chinese", " History"]

print("Hello " +  name)

for i in subjects:
    print("One of my classes is " + i)
    
characters = ["Rachel", "Joey", "Monica", "Ross", "Chandler"]
for i in characters:
    if i == "Ross":
        print(i+ " is the annoying one")
    elif i == "Monica":
        print( i+ " is a chef")
    else:
        print ("One of the characters in friends is " +i)
        
movie = []
while True:
    print("What's your favorite movie? Type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("one of your favoite movies is" + i) 
    
