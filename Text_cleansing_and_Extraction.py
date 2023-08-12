import nltk
import os
#tokenization-converts text into individual tokens they can be words or punctations
base_file =open(os.getcwd()+ "\Spark-Course-Description.txt",'rt')
raw_text = base_file.read()
print(raw_text)
base_file.close()
token_list =nltk.word_tokenize(raw_text)
print(token_list)
print(len(token_list))
####Text Cleansing##############
#this involves convertion of languages removal of punctations,dates etc case convertion (lowr case upper case )
#Remove abbreviations hashtags and urls are necessary
#to remove punctations
token_list2=list(filter(lambda token:nltk.tokenize.punkt.PunktToken(token).is_non_punct,token_list))
print("Length of list after tokenization is :" ,len(token_list2))
#to print every word starting with a cap letter
#to print every word starting with a lower case use first_lower
token_list_first_upper=list(filter(lambda  token: nltk.tokenize.punkt.PunktToken(token).first_upper,token_list2))
print(token_list_first_upper)
#to convert every letter to lower case
token_list_to_lower =[word.lower() for word in token_list2]
print("the list after converting to lower case:",token_list_to_lower)
print("the length after converting to lower case:", len(token_list_to_lower) )
##Stop word removal
#they dont carry any meaning as alone example "in and which etc "
nltk.download("stopwords") #loading list of pre defined stopword list
from nltk.corpus import stopwords
#removing stop words
token_list_ohne_stopword=list(filter(lambda token:token not in stopwords.words('english'),token_list_to_lower))
print("The list after removing stopwors: ",token_list_ohne_stopword)
print("The list without stopwords has a length of:", len(token_list_ohne_stopword))

###Stemming____stem is a base part of a word ex combine is the stem for combined combaining etc .....####
#stemming converts the word to its stem word
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
token_list_stem =[stemmer.stem(word) for word in token_list_ohne_stopword]
print("the token list after stemming:",token_list_stem)
print("the length of the stemmed tokenlist:",len(token_list_stem))
#the number of words dosen't change after stemming but every word will be coverted to the root word
#lemmetization
#simialr to lemmetization but produces lemmetized version of the word for exaMPLE
#COMBINE IS THE lemmetized version of the word combined, combining etc ..
#it uses a dictonary to match so its expencive
nltk.download("wordnet")
from nltk.stem import WordNetLemmatizer
Lemmatizer=WordNetLemmatizer()
token_list_lemmatized =[Lemmatizer.lemmatize(word) for word in token_list_ohne_stopword]
print("the token list after Lemmatizing:",token_list_lemmatized)
print("the length of the Lemmatized tokenlist:",len(token_list_lemmatized))
