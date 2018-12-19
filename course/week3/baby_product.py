import pandas as pd 
from nltk import RegexpTokenizer
from collections import Counter


# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/amazon_baby.csv
def baby_prod():
    data = pd.read_csv("course/week3/data/amazon_baby.csv")
    selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']
    data['word_count'] = data['review'].apply(get_word_count)
    for word in selected_words:
        data[word] = data['word_count'].apply(lambda word_count: word_count[word])
    
    for word in selected_words:
        print(word, data[word].sum())


def get_word_count(senetence):
    
    try :
        tokens = RegexpTokenizer(r'\w+').tokenize(senetence)
        word_counts = Counter(tokens)
        return word_counts
    except:  
        return Counter("")
 

if __name__ == "__main__":
    baby_prod()