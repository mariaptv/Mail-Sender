#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

people = []

f = open("C://Users/maria/Documents/proyectos python/Mail-Sender/Input/Names/invited_names.txt")
people = f.readlines()
print(people)



def replace_names():
    f = open("C://Users/maria/Documents/proyectos python/Mail-Sender/Input/Letters/starting_letter.txt")
    letter = f.read()
    count =0
    for i in people:
        i = i[:-2]
        final = letter.replace("[name]", i)
        with open(f"C://Users/maria/Documents/proyectos python/Mail-Sender/Output/ReadyToSend/example{count+1}.txt", mode="a") as file:
           file.write(final)
        count+=1

replace_names()