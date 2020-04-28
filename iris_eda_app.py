import streamlit as st 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def main():
	""" A simple Iris EDA App """

	st.title("Iris EDA App with streamlit")
	st.subheader("Streamlit is Cool")
	sentence = st.text_area("Enter Text","Type Here ..")
	if st.button('Analyze'):
		sid_obj = SentimentIntensityAnalyzer()
		sentiment_dict = sid_obj.polarity_scores(sentence)
		st.write("Overall sentiment dictionary is : ", sentiment_dict)

if __name__ == '__main__':
	main()
