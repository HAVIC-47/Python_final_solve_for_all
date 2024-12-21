import string

def countWords(text):
     text =text.translate(str.maketrans("",'',string.punctuation))
     words = text.split() 

     word_count={}
     for word in words:
          word=word.lower()
          word_count[word]=word_count.get(word,0)+1

     return word_count   

text = "Hello, world! Hello Python. Python is great."
print(countWords(text))