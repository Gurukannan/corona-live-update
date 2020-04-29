import streamlit as st 
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import altair as alt
	
def sentiment_scores(sentence): 
	sid_obj = SentimentIntensityAnalyzer()
	sentiment_dict = sid_obj.polarity_scores(sentence)
	st.write("**_Overall sentiment dictionary is : _**", sentiment_dict)
	#st.write(pd.DataFrame(sentiment_dict, index=[0]))
	df2=pd.DataFrame(sentiment_dict, index=[0])
	st.write('**_Chart:_**')
	
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
	
	st.bar_chart(df2.T,width=0, height=0, use_container_width=True)
	st.write('**_Summary:_**')
	neg_score 
	neu_score
	pos_score
	comp_score
	st.write('**_Overall Rank : _**')
	if overall_rank == 'Positive':
		st.success(overall_rank)
	elif overall_rank == 'Negative':
		st.error(overall_rank)
	else:
		st.info(overall_rank)
	
	#st.write("sentence was rated as ", neg_score, "% Negative")
	#st.write("sentence was rated as ", neu_score, "% Neutral")
    	#st.write("sentence was rated as ", pos_score, "%ya")
 	#st.write("Sentence Overall Rated As", end = " ")
	
def main():
	""" A simple Text Analyzer App """

	st.title("Sentiment Analysis App")
	st.subheader("Designed By Guru.K")
	apply=st.sidebar.selectbox('Select Below',('Sentiment analysis', 'Use of SA', 'Examples of SA'))
	#st.info('information')
	if apply == 'Sentiment analysis':
		st.sidebar.markdown('**_Sentiment analysis_** is a text analysis method that detects polarity (e.g. a positive or negative opinion) within text, whether a whole document, 							paragraph, sentence, or	clause.\n\n Understanding people’s emotions is essential for businesses since customers are able to express their thoughts and feelings more openly than 			ever before.\n\n By automatically analyzing customer feedback,from survey responses to social media conversations, brands are able to listen attentively to their 					customers, and tailor products and services to meet their needs.')
	elif apply == 'Use of SA':
		st.sidebar.markdown('*Analyze tweets and/or facebook posts over a period of time to detect sentiment of a particular audience \n\n *Monitor social media mentions of your brand and automatically categorize by urgency \n\n *Automatically route social media mentions to team members best fit to respond \n\n *Automate any or all of these processes \n\n *Gain deep insights into what’s happening across your social media channels')
	else:
		st.sidebar.markdown('Negative: Death Racial discord was conceived, nurtured, refined & perpetuated by Americans incl realDonaldTrump’s father. Get real! \n\n Neutral: HillaryClinton will receive the first question at tonight’s presidential debate, according to CBSNews #ClintonVsTrump. \n\n Positive: Americans trust realDonaldTrump to Make our Economy Great Again! \n\n Positive: wcve it’s amazing how our city loves him and he really loves our city. HillaryClinton made a great choice for Vice President. timkaine.')
	sentence = st.text_area("Enter Text","Type Here ..")
	
	if st.button('Analyze'):
		result=sentence.title()
		#st.success(result)
		sentiment_scores(sentence)
	
if __name__ == '__main__':
	main()
