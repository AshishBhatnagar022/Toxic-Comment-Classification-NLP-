import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import pandas as pd
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

dataset=pd.read_csv('train.csv')
# print(dataset.columms)
for col in dataset.columns: 
    print(col)

contractions = { 
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he's": "he is",
"how'd": "how did",
"how'll": "how will",
"how's": "how is",
"i'd": "i would",
"i'll": "i will",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'll": "it will",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"must've": "must have",
"mustn't": "must not",
"needn't": "need not",
"oughtn't": "ought not",
"shan't": "shall not",
"sha'n't": "shall not",
"she'd": "she would",
"she'll": "she will",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"that'd": "that would",
"that's": "that is",
"there'd": "there had",
"there's": "there is",
"they'd": "they would",
"they'll": "they will",
"they're": "they are",
"they've": "they have",
"wasn't": "was not",
"we'd": "we would",
"we'll": "we will",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"where'd": "where did",
"where's": "where is",
"who'll": "who will",
"who's": "who is",
"won't": "will not",
"wouldn't": "would not",
"you'd": "you would",
"you'll": "you will",
"you're": "you are"
}

def clean_text(text,remove_stopwords=True):
  
  text=text.lower()
  if True:
    text=text.split()
    new_text=[]
    for word in text:
      if word in contractions:
        new_text.append(contractions[word])
      else:
        new_text.append(word)
    text=" ".join(new_text)
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\<a href', ' ', text)
    text = re.sub(r'&amp;', '', text) 
    text = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', text)
    text = re.sub(r'<br />', ' ', text)
    text = re.sub(r'\'', ' ', text)
    
    if remove_stopwords:
        text = text.split()
        stops = set(stopwords.words("english"))
        text = [w for w in text if not w in stops]
        text = " ".join(text)
  return text

import nltk
nltk.download('stopwords')
import re
from nltk.corpus import stopwords
clean_comments=[]
for comment in dataset.comment_text:
  clean_comments.append(clean_text(comment))
print('Comments are complete')
dataset['comment_text']=clean_comments
dataset.drop(dataset[(dataset['insult']==0) & (dataset['toxic']==0) & (dataset['severe_toxic']==0) & (dataset['obscene']==0) & (dataset['threat']==0)& (dataset['insult']& (dataset['identity_hate']==0)==0)].index,inplace=True)

list_classes=['toxic','severe_toxic','obscene','threat','insult','identity_hate']
y=dataset[list_classes].values
list_sentence_train=dataset['comment_text']
# list_sentence_test=test['comment_text']
max_features=2000
tokenizer=Tokenizer(num_words=max_features)
tokenizer.fit_on_texts(list(list_sentence_train))
list_tokenizer_train=tokenizer.texts_to_sequences(list_sentence_train)
# list_tokenizer_test=tokenizer.texts_to_sequences(list_sentence_test)

maxlen=200
X_t=pad_sequences(list_tokenizer_train,maxlen=maxlen)

total_num_words=[len(one_comment) for one_comment in list_tokenizer_train]
from keras.layers import Dense,LSTM,Embedding,Dropout,Activation,GlobalMaxPooling1D
from keras.models import Sequential

total_num_words=[len(one_comment) for one_comment in list_tokenizer_train]
import os
embeddings_index = {}
	# f = open(os.path.join('', 'glove.6B.100d.txt'))
f = open('glove.6B.100d.txt', encoding="utf8")
for line in f:
	values = line.split()
	word = values[0]
	coefs = np.asarray(values[1:], dtype='float32')
	embeddings_index[word] = coefs
f.close()

from keras.layers import Embedding

EMBEDDING_DIM=100
embedding_matrix_x = np.zeros((len(tokenizer.word_index) + 1, EMBEDDING_DIM))
for word, i in tokenizer.word_index.items():
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix_x[i] = embedding_vector
        
embedding_layer = Embedding(len(tokenizer.word_index) + 1,
                            EMBEDDING_DIM,
                            weights=[embedding_matrix_x],
                            input_length=200,
                            trainable=False)
from keras.layers import Embedding

EMBEDDING_DIM=100
embedding_matrix_x = np.zeros((len(tokenizer.word_index) + 1, EMBEDDING_DIM))
for word, i in tokenizer.word_index.items():
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix_x[i] = embedding_vector
        
embedding_layer = Embedding(len(tokenizer.word_index) + 1,
                            EMBEDDING_DIM,
                            weights=[embedding_matrix_x],
                            input_length=200,
                            trainable=False)

embed_Size=128
model=Sequential()
model.add(embedding_layer)
# model.add(Embedding(max_features,embed_Size,input_length=200))
model.add(LSTM(60, name='lstm_layer'))

model.add(Dense(6,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=(['accuracy']))
from sklearn.model_selection import train_test_split
X_train,X_val,y_train,y_val=train_test_split(X_t,y,test_size=0.2)

model.fit(X_train,y_train,epochs=15,batch_size=16,validation_data=(X_val,y_val),verbose=2)
from sklearn.externals import joblib
joblib.dump(model,'mynewtoxic.pkl')
a=open('mynewtoxic.pkl','rb')
model=joblib.load(a)

