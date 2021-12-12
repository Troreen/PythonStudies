'''
# Q1
# plus# Topic: List Comprehensions
# Write out the following code without using a list comprehension:
# plus_thirteen = [number + 13 for number in range(1,11)]
plus_thirteen = []
for number in range(1,11):
    new_number = number + 13
    plus_thirteen.append(new_number)


# Q2
# Topic: List Comprehensions
# Using a list comprehension, create a list of the even indexed
# characters of every word in the strings below:
# "The quick brown fox jumps over the lazy dog."
# "My name is Inigo Montoya. You killed my father. Prepare to die."
# "Luke, I am your father"
sentence = "The quick brown fox jumps over the lazy dog."
sentence_ls = list(sentence)
even_indexed = [charecter for charecter in sentence_ls[::2]]

princess_bride = "My name is Inigo Montoya. You killed my father. Prepare to die."
princess_bride_ls = list(princess_bride)
even_indexed_pb = [charecter for charecter in princess_bride_ls[::2]]

star_wars = "Luke, I am your father"
star_wars_ls = list(star_wars)
even_indexed_sw = [charecter for charecter in star_wars_ls[::2]]

# Q3
# Topic: String Manipulation
# Write a program that finds all the words that starts with the letter
# 'd' in the following strings:
# "A day without sunshine is like, you know, not a day."
# "Dreams come true. Without a dream, nothing happens."
# "Dry day in a drought."
# "Dance or die. The choice is dreadfully simple."
a_day= "A day without sunshine is like, you know, not a day."
d_index = a_day.find("d")
print(a_day[d_index:d_index+3])
d_index_end = a_day.rfind("d")
print(a_day[d_index_end:d_index_end+3])

# Q4
# Topic: String Manipulation
# Change all the cat's to dog's in the following strings:
# "My cat is my best friend."
# "This cat is outrageous."
# "We have a cat problem."
sentence1 = "My cat is my best friend."
print(sentence1.replace("cat", "dog"))
sentence2 = "This cat is outrageous."
print(sentence2.replace("cat", "dog"))
sentence3 = "We have a cat problem."
print(sentence3.replace("cat", "dog")) 

# Q5
# Topic: String Manipulation
# Store a sentence in a variable. Using slices, print out
# the first five characters, any five consecutive characters
# from the middle of the sentence, and the last five characters
# of the sentence.

# Q6
# Topic: String Manipulation
# A string is simply an ordered collection of symbols selected
# from some alphabet and formed into a word; the length of a string
# is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the
# symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective
# number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# Source: https://rosalind.info/problems/dna/
s = "ATGCTTCAGAAAGGTCTTACG"
chars = "ACGT"
for char in chars:
    print(s.count(char))

# Q7
# Topic: String Manipulation
# An RNA string is a string formed from the alphabet containing 'A', 
# 'C', 'G', and 'U'.

# Given a DNA string t corresponding to a coding strand, its transcribed
# RNA string u is formed by replacing all occurrences of 'T' in t with 'U'
# in u.

# Given: A DNA string t having length at most 1000 nt.

# Return: The transcribed RNA string of t.

# source: https://rosalind.info/problems/rna/
t = "GATGGAACTTGACTACGTAAATT"
u = t.replace("T", "U")
print(u)
'''
# Q8
# Topic: String Manipulation
# In DNA strings, symbols 'A' and 'T' are complements of each other,
# as are 'C' and 'G'.

# The reverse complement of a DNA string s is the string sc formed by
# reversing the symbols of s, then taking the complement of each symbol
# (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.

# Return: The reverse complement sc of s.

# source: https://rosalind.info/problems/revc/
s = "ATGCTTCAGAAAGGTCTTACG"
sc = s[::-1]
chars1 = "TACG"
chars2 = "ATGC"
index = 0
print(sc)
for char in chars1:
    print(index, char, chars2[index])
    sc = sc.replace(char, chars2[index])
    index +=1
print(sc)

# Q9
# Topic: General
# - Make a list of the most important words you have 
#   learned in programming so far. You should have terms such as list,
# - Make a corresponding list of definitions. Fill your list with 'definition'.
# - Use a for loop to print out each word and its corresponding definition.
# - Maintain this program until you get to the section on Python's Dictionaries.
important_words = ["list", "function", "string", "integer", "float", "index", "loop", "range"]
definitions = ["A variable containing multiple items.", "It performs specific tasks that are easy to manipulate.", "Characters that aren't functioning as integers.", "A number.", "A decimal.", "Every character has its own place that is numbered as an index, starting at 0 going up.", "To make something run over and over again.", "Run within a range, using minimum, maximum and the size of the steps between."]
#for i in range(len(important_words)):
 #   print(important_words[i].title(), "=", definitions[i])

# Q10
# Topic: Functions
# - Many songs follow a familiar variation of the pattern of verse, 
#   refrain, verse, refrain. The verses are the parts of the song 
#   that tell a story - they are not repeated in the song. The refrain
#   is the part of the song that is repeated throughout the song.
# - Find the lyrics to a song you like that follows this pattern. 
#   Write a program that prints out the lyrics to this song, 
#   using as few lines of Python code as possible.  