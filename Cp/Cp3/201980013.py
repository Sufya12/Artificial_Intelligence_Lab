# INSTRUCTIONS

# Class Participation 03

# 1. File name should be "Your_ID.py" e.g "18802585.py".
# 2. You don't need to create a new file. Edit this file and add your answer.
# 3. Finally, submit this file with your answers.
# 4. If you've any additional files like "story.txt" / "student.csv", don't submit them.
# 5. Only SUBMIT this "Your_ID.py" file with your answers.
# 6. Don't edit or remove any line or comment.


# Exercise-01
# Write a function in python to count the number of lines from a text file “story.txt” which is not
# starting with an alphabet “T”.
# Example: If the file “story.txt” contains the following lines;
# A boy is playing there. There is a playground. An aeroplane is in the sky. The sky is pink.
# Alphabets and numbers are allowed in the password.
# Create story.txt file manually first, add above lines.
# 
# 
# Answer Task1  

def line_count():
    fill = open("story.txt","r")
    count1=0
    for line in fill:
        if line[0] not in 't':
            count1= count1+1
    fill.close()
    print("Total Num of the  lines not start with The  't'=",count1)

line_count()


# 
# 
# Exercise-02
# Write a function display_words() in python to read lines from a text file “story.txt”, and display
# those words, which are less than 4 characters.
# 
# 
#
Answer Task 02


def display_words() :
    fill = open("story.txt", "r")
    l = fill.readlines()
    for a in l :
        word = a.split()
        for b in word :
            if len( b ) < 4 :
                print( b )
    fill.close()

print(" The Word are length smaller than the  3 :- \n")
display_words()




# 
# 
# Exercise-03
# Write a function in Python to count words in a text file those are ending with alphabet “e”.
# 
# 
#

Answer Task 03

def counts1_word():
    fill = open("story.txt","r")
    count1 = 0
    d = fill.read()
    word1 = d.split()
    for word2 in word1:
        if word2[-1] == 'e':
            count1+=1
    print("The  ending with alphabet “e” is =",count1)
    fill.close()

counts1_word()



# 
# 
# Exercise-04
# Create a “student.csv” file with dummy students data having fields ID, Name, Dept, CGPA,
# Semester, Marks. Write a program to read all content of “student.csv” and display records of
# only those students who scored more than 80 marks. Records stored in students is in format : ID,
# Name, Marks
# 
# 
# write your answer here... .. .
# 
# 
########################END########################