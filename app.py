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
# from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
model = pickle.load(open('model1.pkl', 'rb'))
tokenizer=pickle.load(open('tranform1.pkl','rb'))
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
		    
		  
		return text   
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def predict():
	pred_type=[]
	pred_per=[]


	
	list_classes=['toxic','severe_toxic','obscene','threat','insult','identity_hate']


	if request.method == 'POST':

		comment = request.form['comment']
		
		test_samples=[comment]

		
		j=[]
		max_features=200
		maxlen=200
		# tokenizer=Tokenizer(num_words=max_features)
		test_sample_token=tokenizer.texts_to_sequences(test_samples)
		test_sample_tokens_pad=pad_sequences(test_sample_token,maxlen=maxlen)
		a=model.predict([test_sample_tokens_pad])
		
		# classes = np.array(da.columns[2:])
		top_3 = np.argsort(a[0])[:-4:-1]
		print(top_3)
		for i in range(3):
			top_3 = np.argsort(a[0])[:-4:-1]
			pred_type.append(list_classes[top_3[i]])
			pred_per.append(round(a[0][top_3[i]]*100,2))
		else:
			pass
			# pred_type=''
			# pred_per=''
	return render_template('index1.html',pred_type=pred_type,pred_per=pred_per) 
	
if __name__ == "__main__":
    app.run(debug=True)


