import streamlit as st 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence): 
	sid_obj = SentimentIntensityAnalyzer()
	sentiment_dict = sid_obj.polarity_scores(sentence)
	st.write("Overall sentiment dictionary is : ", sentiment_dict)
	
def main():
	""" A simple Iris EDA App """

	st.title("Iris EDA App with streamlit")
	st.subheader("Streamlit is Cool")
	sentence = st.text_area("Enter Text","Type Here ..")
	if st.button('Analyze'):
		#sid_obj = SentimentIntensityAnalyzer()
		#sentiment_dict = sid_obj.polarity_scores(sentence)
		#st.write("Overall sentiment dictionary is : ", sentiment_dict)
		sentiment_scores(sentence)
if __name__ == '__main__':
	main()
