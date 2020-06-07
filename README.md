#<b> Toxic-Comment-Classification-NLP</b>


It is a multi-headed model that’s capable of detecting different types of toxicity like
threats, obscenity, insults, and identity-based hate better than Perspective’s current models. 

<h2> Data </h2>

We have a large number of Wikipedia Comments which have been labeled by human raters for toxic behaviour. The types of toxicity are
:
* Toxic

* Severe_toxic

* Obscene

* Threat

* Insult

* Identity_hate


<h2>Description</h2>
This is a model which could able to predict the toxicity of the comments. It is deployed through flask framework in which for a given comment the model able to predict the toxicity of the comment.
LSTM is used to build the above model with some data preprocessing techniques. 
You must create a model which predicts a probability of each type of toxicity for each comment.



![pcc](https://user-images.githubusercontent.com/50323194/83974971-9f91f300-a90e-11ea-9b36-a30983881ab6.PNG)

<h2> Results </h2>

The model is now able to predict the toxicity ofthe comments sucessfully.

Test Accuracy Acieved: 95.95%

<b>Comment :-</b>


![pcc1](https://user-images.githubusercontent.com/50323194/83975040-0ca58880-a90f-11ea-92e6-8d699bcb6142.PNG)

<b>Prediction :-</b>

![pcc2](https://user-images.githubusercontent.com/50323194/83975042-13cc9680-a90f-11ea-9038-17b12a00363f.PNG)
