import streamlit as st 
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#def sentiment_scores(sentence): 
	#sid_obj = SentimentIntensityAnalyzer()
	#sentiment_dict = sid_obj.polarity_scores(sentence)
	#st.write("Overall sentiment dictionary is : ", sentiment_dict)
	
def sentiment_scores(sentence): 
	sid_obj = SentimentIntensityAnalyzer()
	sentiment_dict = sid_obj.polarity_scores(sentence)
	st.write("**_Overall sentiment dictionary is : _**", sentiment_dict)
	#st.write(pd.DataFrame(sentiment_dict, index=[0]))
	df2=pd.DataFrame(sentiment_dict, index=[0])
	st.write('**_Summary:_**')
	
	neg_score= df2.loc[0,'neg']
	neu_score= df2.loc[0,'neu']
	pos_score= df2.loc[0,'pos']
	comp_score= df2.loc[0,'compound']
	
	neg_score = round(neg_score*100,2)
	neu_score= round(neu_score*100,2)
	pos_score= round(pos_score*100,2)
	comp_score= round(comp_score*100,2)
	overall_rank=1
	if comp_score >= 0.5:
		overall_rank = 'Positive'
	elif comp_score <=-0.5:
		overall_rank = 'Negative'
	else:
		overall_rank = 'Neutral' 

	neg_score = "1.Rated Negative Score is" + " " + str(neg_score) + '%'
	neu_score = "2.Rated Neautral Score is" + " " + str(neu_score)+ '%'
	pos_score= "3.Rated Positive Score is" + " " + str(pos_score)+ '%'
	comp_score= "4.Rated Compound Score is" + " " + str(comp_score)+ '%'
	
	neg_score 
	neu_score
	pos_score
	comp_score
	st.write('**_Overall Rank is _**',overall_rank)
	#st.write("sentence was rated as ", neg_score, "% Negative")
	#st.write("sentence was rated as ", neu_score, "% Neutral")
    	#st.write("sentence was rated as ", pos_score, "%ya")
 	#st.write("Sentence Overall Rated As", end = " ")
	
def main():
	""" A simple Iris EDA App """

	st.title("Sentiment Analysis App")
	st.subheader("Designed By Guru.K")
	sentence = st.text_area("Enter Text","Type Here ..")
	if st.button('Analyze'):
		#sid_obj = SentimentIntensityAnalyzer()
		#sentiment_dict = sid_obj.polarity_scores(sentence)
		#st.write("Overall sentiment dictionary is : ", sentiment_dict)
		sentiment_scores(sentence)
if __name__ == '__main__':
	main()
