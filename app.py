import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import pandas as pd
import numpy as np
import nltk
	# nltk.download('stopwords')
import re
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
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

def clean_text(text):


  
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
		    
		   # if remove_stopwords:
		   #     text = text.split()
		   #     stops = set(stopwords.words("english"))
		   #     text = [w for w in text if not w in stops]
		   #     text = " ".join(text)
		return text   
app = Flask(__name__)
model = pickle.load(open('mynewtoxic.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index1.html')

# @app.route('/predict',methods=['POST'])
@app.route('/predict',methods=['GET','POST'])

# def predict():


	
# 	list_classes=['toxic','severe_toxic','obscene','threat','insult','identity_hate']


# 	if request.method == 'POST':

# 		comment = request.form['comment']
# 		print('hee')
# 		clean_comments=[]
# 		for com in comment:
# 		 clean_comments.append(clean_text(com))
# 		# commentify(model,comment,train)
# 		test_samples=[clean_comments]
# 		test_samples=[comment]

# 		print('TEST SAMPLES',test_samples)

		
# 		j=[]
# 		max_features=200
# 		maxlen=200
# 		tokenizer=Tokenizer(num_words=max_features)
# 		test_sample_token=tokenizer.texts_to_sequences(test_samples)
# 		test_sample_tokens_pad=pad_sequences(test_sample_token,maxlen=maxlen)
# 		a=model.predict([test_sample_tokens_pad])
# 		print('PREDICTION',a)

# 		# classes = np.array(da.columns[2:])
# 		top_3 = np.argsort(a[0])[:-4:-1]
# 		for i in range(3):
# 			top_3 = np.argsort(a[0])[:-4:-1]
# 			j.append(list_classes[top_3[i]])
# 			j.append(a[0][top_3[i]])
# 	return render_template('index1.html', prediction_text='Type of comment is \n $ {}'.format(j))



def predict():
	train=pd.read_csv('train.csv')

	
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
	def clean_text(text):


  
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
		    
		   # if remove_stopwords:
		   #     text = text.split()
		   #     stops = set(stopwords.words("english"))
		   #     text = [w for w in text if not w in stops]
		   #     text = " ".join(3text)
		return text   
	import nltk
	# nltk.download('stopwords')
	import re
    # from nltk.corpus import stopwords
	clean_comments=[]
	for comment in train.comment_text:
		 clean_comments.append(clean_text(comment))
		 print('Comments are complete')
	train['clean_comment_text']=	clean_comments 
	print('before',type(train['clean_comment_text']))
	# train.to_csv('abc1.csv')
	# clean_comments=pd.DataFrame(index=None)
	# clean_comments['clean_comments']=train['comment_text']
	# train['comment_text']=clean_comments
	# clean_comments.to_csv('clean_comments1.csv',index=None)
	# train=pd.read_csv('abc1.csv')
	# print('after',type(train['clean_comment_text']))

	# train.drop(train[(train['insult']==0) & (train['toxic']==0) & (train['severe_toxic']==0) & (train['obscene']==0) & (train['threat']==0)& (train['insult']& (train['identity_hate']==0)==0)].index,inplace=True)
	list_classes=['toxic','severe_toxic','obscene','threat','insult','identity_hate']
	# y=train[list_classes].values
	list_sentence_train=train['clean_comment_text']
	print('TYPE',type(list_sentence_train))
	# list_sentence_test=test['comment_text']
	max_features=2000
	tokenizer=Tokenizer(num_words=max_features)
	tokenizer.fit_on_texts(list_sentence_train)
	list_tokenizer_train=tokenizer.texts_to_sequences(list_sentence_train)
	print('lttt',list_tokenizer_train)
	# list_tokenizer_test=tokenizer.texts_to_sequences(list_sentence_test)
	maxlen=200
	X_t=pad_sequences(list_tokenizer_train,maxlen=maxlen)
	# X_tes=pad_sequences(list_tokenizer_test,maxlen=maxlen)
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
# tf.compat.v1.get_default_graph
	EMBEDDING_DIM=100
	embedding_matrix_x = np.zeros((len(tokenizer.word_index) + 1, EMBEDDING_DIM))
	for word, i in tokenizer.word_index.items():
		embedding_vector = embeddings_index.get(word)
		if embedding_vector is not None:
		 embedding_matrix_x[i] = embedding_vector

    		
    		

        # words not found in embedding index will be all-zeros.
        		
        
	embedding_layer = Embedding(len(tokenizer.word_index) + 1,
                            	EMBEDDING_DIM,
                            	weights=[embedding_matrix_x],
                            	input_length=200,
                            	trainable=False)
	embed_Size=128

# 	model=Sequential()
# 	model.add(embedding_layer)
# # model.add(Embedding(max_features,embed_Size,input_length=200))
# 	model.add(LSTM(60, name='lstm_layer'))

# 	model.add(Dense(6,activation='sigmoid'))
# 	model.compile(loss='binary_crossentropy',optimizer='adam',metrics=(['accuracy']))
# 		 # print('hellp')
# 	from sklearn.model_selection import train_test_split
# 	X_train,X_val,y_train,y_val=train_test_split(X_t,y,test_size=0.2)
# 	# model.fit(X_train,y_train,epochs=1,batch_size=64,validation_data=(X_val,y_val))
# 	from sklearn.externals import joblib
# 	# joblib.dump(model,'mynewtoxic.pkl')
# 	a=open('toxicity.pkl','rb')
# 	model=joblib.load(a)


				







	
	if request.method == 'POST':
		comment = request.form['comment']
		# commentify(model,comment,train)
		test_samples=[comment]
		j=[]
		# tokenizer=Tokenizer(num_words=max_features)
		test_sample_token=tokenizer.texts_to_sequences(test_samples)
		test_sample_tokens_pad=pad_sequences(test_sample_token,maxlen=maxlen)
		a=model.predict([test_sample_tokens_pad])
		classes = np.array(train.columns[2:])
		top_3 = np.argsort(a[0])[:-4:-1]
		for i in range(3):
			top_3 = np.argsort(a[0])[:-4:-1]
			j.append(classes[top_3[i]])
			j.append(a[0][top_3[i]])

		# data = [comment]
		# vect = cv.transform(data).toarray()
	return render_template('index1.html', prediction_text='Type of comment is :- \n  {} : {} \n {} : {} \n {} : {}'.format(j[0],round(j[1]*100, 2),j[2],round(j[3]*100, 2),j[4],round(j[5]*100, 2)))

	# return render_template('index1.html',prediction = j)



		# data = [comment]
		# vect = cv.transform(data).toarray()
	# return render_template('resultoxic.html',prediction = j)	# my_prediction = model.predict(vect)
# if __name__ == "__main__":

    # app.run(debug=True)	# return render_template('indtoxic.html',prediction = my_prediction)  
   
    # For rendering results on HTML GUI
   
    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)


# @app.route('/predict_api',methods=['POST'])
# def predict_api():

   
    # For direct API calls trought request
    
    # data = request.get_json(force=True)
    # prediction = model.predict([np.array(list(data.values()))])

    # output = prediction[0]
    # return jsonify(output)

if __name__ == "__main__":
    app.run(debug=False,threaded='False')


# test_samples=[test_sample1]
  # test_sample_token=tokenizer.texts_to_sequences(test_samples)
  # test_sample_tokens_pad=pad_sequences(test_sample_token,maxlen=maxlen)
  # a=model.predict([test_sample_tokens_pad])
  
  # classes = np.array(train.columns[2:])

  # top_3 = np.argsort(a[0])[:-4:-1]

#   # for i in range(3):
#       # top_3 = np.argsort(a[0])[:-4:-1]

#       # print("{}".format(classes[top_3[i]])+" ({:.3})".format(a[0][top_3[i]])


#       contractions = { 

# 	"ain't": "am not",
# 	"aren't": "are not",
# 	"can't": "cannot",
# 	"can't've": "cannot have",
# 	"'cause": "because",
# 	"could've": "could have",
# 	"couldn't": "could not",
# 	"couldn't've": "could not have",
# 	"didn't": "did not",
# 	"doesn't": "does not",
# 	"don't": "do not",
# 	"hadn't": "had not",
# 	"hadn't've": "had not have",
# 	"hasn't": "has not",
# 	"haven't": "have not",
# 	"he'd": "he would",
# 	"he'd've": "he would have",
# 	"he'll": "he will",
# 	"he's": "he is",
# 	"how'd": "how did",
# 	"how'll": "how will",
# 	"how's": "how is",
# 	"i'd": "i would",
# 	"i'll": "i will",
# 	"i'm": "i am",
# 	"i've": "i have",
# 	"isn't": "is not",
# 	"it'd": "it would",
# 	"it'll": "it will",
# 	"it's": "it is",
# 	"let's": "let us",
# 	"ma'am": "madam",
# 	"mayn't": "may not",
# 	"might've": "might have",
# 	"mightn't": "might not",
# 	"must've": "must have",
# 	"mustn't": "must not",
# 	"needn't": "need not",
# 	"oughtn't": "ought not",
# 	"shan't": "shall not",
# 	"sha'n't": "shall not",
# 	"she'd": "she would",
# 	"she'll": "she will",
# 	"she's": "she is",
# 	"should've": "should have",
# 	"shouldn't": "should not",
# 	"that'd": "that would",
# 	"that's": "that is",
# 	"there'd": "there had",
# 	"there's": "there is",
# 	"they'd": "they would",
# 	"they'll": "they will",
# 	"they're": "they are",
# 	"they've": "they have",
# 	"wasn't": "was not",
# 	"we'd": "we would",
# 	"we'll": "we will",
# 	"we're": "we are",
# 	"we've": "we have",
# 	"weren't": "were not",
# 	"what'll": "what will",
# 	"what're": "what are",
# 	"what's": "what is",
# 	"what've": "what have",
# 	"where'd": "where did",
# 	"where's": "where is",
# 	"who'll": "who will",
# 	"who's": "who is",
# 	"won't": "will not",
# 	"wouldn't": "would not",
# 	"you'd": "you would",
# 	"you'll": "you will",
# 	"you're": "you are"
# 	}
# 	def clean_text(text):


  
# 		text=text.lower()
# 		if True:
# 		   text=text.split()
# 		   new_text=[]
# 		   for word in text:
# 		     if word in contractions:
# 		       new_text.append(contractions[word])
# 		     else:
# 		       new_text.append(word)
# 		   text=" ".join(new_text)
# 		   text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
# 		   text = re.sub(r'\<a href', ' ', text)
# 		   text = re.sub(r'&amp;', '', text) 
# 		   text = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', text)
# 		   text = re.sub(r'<br />', ' ', text)
# 		   text = re.sub(r'\'', ' ', text)
		    
# 		   # if remove_stopwords:
# 		   #     text = text.split()
# 		   #     stops = set(stopwords.words("english"))
# 		   #     text = [w for w in text if not w in stops]
# 		   #     text = " ".join(text)
# 		return text   
# 	import nltk
# 	# nltk.download('stopwords')
# 	import re
# 	# from nltk.corpus import stopwords
# 	clean_comments=[]
# 	for comment in train.comment_text:
# 		 clean_comments.append(clean_text(comment))
# 		 print('Comments are complete')
# 	train['comment_text']=clean_comments
# 	train.drop(train[(train['insult']==0) & (train['toxic']==0) & (train['severe_toxic']==0) & (train['obscene']==0) & (train['threat']==0)& (train['insult']& (train['identity_hate']==0)==0)].index,inplace=True)
# 	list_classes=['toxic','severe_toxic','obscene','threat','insult','identity_hate']
# 	y=train[list_classes].values
# 	list_sentence_train=train['comment_text']
# 	# list_sentence_test=test['comment_text']
# 	max_features=2000
# 	tokenizer=Tokenizer(num_words=max_features)
# 	tokenizer.fit_on_texts(list(list_sentence_train))
# 	list_tokenizer_train=tokenizer.texts_to_sequences(list_sentence_train)
# 	# list_tokenizer_test=tokenizer.texts_to_sequences(list_sentence_test)
# 	maxlen=200
# 	X_t=pad_sequences(list_tokenizer_train,maxlen=maxlen)
# 	# X_tes=pad_sequences(list_tokenizer_test,maxlen=maxlen)
# 	total_num_words=[len(one_comment) for one_comment in list_tokenizer_train]
# 	import os
# 	embeddings_index = {}
# 	# f = open(os.path.join('', 'glove.6B.100d.txt'))
# 	f = open('glove.6B.100d.txt', encoding="utf8")
# 	for line in f:

# 		  values = line.split()
# 		  word = values[0]
# 		  coefs = np.asarray(values[1:], dtype='float32')
# 		  embeddings_index[word] = coefs
# 	f.close()
# 	from keras.layers import Embedding
# # tf.compat.v1.get_default_graph
# 	EMBEDDING_DIM=100
# 	embedding_matrix_x = np.zeros((len(tokenizer.word_index) + 1, EMBEDDING_DIM))
# 	for word, i in tokenizer.word_index.items():
# 		embedding_vector = embeddings_index.get(word)
# 		if embedding_vector is not None:
# 		 embedding_matrix_x[i] = embedding_vector

    		
    		

        # words not found in embedding index will be all-zeros.
        		
        
	# embedding_layer = Embedding(len(tokenizer.word_index) + 1,
 #                            	EMBEDDING_DIM,
 #                            	weights=[embedding_matrix_x],
 #                            	input_length=200,
 #                            	trainable=False)
	# embed_Size=128