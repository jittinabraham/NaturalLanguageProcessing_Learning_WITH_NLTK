
#######Load FILE To Corpus#############
import nltk
import os
nltk.download('punkt')
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpus=PlaintextCorpusReader(os.getcwd(),"Spark-Course-Description.txt")
print(corpus.raw())
####Print list of file ID#############
#extract file ID#####
print("files in ths corpus",corpus.fileids())
#Extract paragraphs from the file
print("the paragraphs in this corpus ",len(corpus.paras()))

#corpus.paras() will extract a  words list from the plain text
#extract sentences from corpus
print("the sentences in this corpus are ",len(corpus.sents()))
sentence=corpus.sents()
print(sentence[0])
#extract words from corpus
print("the words in this corpus are",len(corpus.words()))
#Analysis of words using NLTK
freq_dist = nltk.FreqDist(corpus.words())
print("the most repated words are ",freq_dist.most_common(10))
#find distribution of specific word
print("the distribution of the word technologies in the text is:",freq_dist.get("technologies"))
print("the distribution of the word technology in the text is:",freq_dist.get("technology"))
