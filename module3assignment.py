# Module 3 assignment
# Maggie Cloos

myfile = open("question.txt","r+")

myquestion = myfile.read()

myresponse = input(myquestion)

myfile.write(myresponse)

myfile.close()
