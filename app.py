import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image

def main():
	""" A simple Text Analyzer App """
	st.header('Sample Analytical App on COVID19 - Guru.K')
	st.subheader('Last Updated - Today')
	image = Image.open('corona_image.png')
	st.image(image, use_column_width=True)
	st.subheader('_Statewise - Update_')


	st.sidebar.header('Want to know more about COVID-19?')
	st.sidebar.text('Yeah, Lets go!')
	st.sidebar.subheader('Overview')
	st.sidebar.markdown('''* Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.\n\n * Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.\n\n* Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.''')
	
	st.sidebar.subheader('Symptoms')
	st.sidebar.markdown('''Common symptoms:
* fever
* tiredness
* dry cough
\n 
Some people may experience:
* aches and pains.
* nasal congestion.
* runny nose.
* sore throat.
* diarrhoea.
\n
On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.
People with mild symptoms who are otherwise healthy should self-isolate. Seek medical attention if you have a fever, a cough, and difficulty breathing. Call ahead.''')
	st.sidebar.subheader('Prevention')
	st.sidebar.markdown(''' STAY HOME.SAVE LIVES.
\n
Help stop coronavirus
* 1STAY home
* 2KEEP a safe distance
* 3WASH hands often
* 4COVER your cough
* 5SICK? Call the helpline''')

	st.sidebar.subheader('Overview')
	st.sidebar.markdown('''Self-care
\n
* If you feel sick you should rest, drink plenty of fluid, and eat nutritious food. Stay in a separate room from other family members, and use a dedicated bathroom if possible. \n 
* Clean and disinfect frequently touched surfaces.
\n 
* Everyone should keep a healthy lifestyle at home. Maintain a healthy diet, sleep, stay active, and make social contact with loved ones through the phone or internet. \n 
* Children need extra love and attention from adults during difficult times. Keep to regular routines and schedules as much as possible.
\n
* It is normal to feel sad, stressed, or confused during a crisis. Talking to people you trust, such as friends and family, can help. If you feel overwhelmed, talk to a health worker or counsellor.

Medical treatments \n
* If you have mild symptoms and are otherwise healthy, self-isolate and contact your medical provider or a COVID-19 information line for advice.\n
* Seek medical care if you have a fever, a cough, and difficulty breathing. Call in advance. ''')


	df=pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')
	df= df.iloc[:,:7]
	st.dataframe(df)
	df=df.drop(df.index[0])
	df=df.replace(0,np.NaN)
	confirmed_largest=df[['State','Confirmed']].nlargest(7,'Confirmed')
	confirmed_largest_plus=df[['State','Confirmed','Recovered','Deaths']].nlargest(7,'Confirmed')
	recovered_largest=df[['State','Recovered']].nlargest(7,'Recovered')
	fatality_largest=df[['State','Deaths']].nlargest(7,'Deaths')
	confirmed_smallest=df[['State','Confirmed']].nsmallest(7,'Confirmed')
	confirmed_smallest_plus=df[['State','Confirmed','Recovered','Deaths']].nsmallest(7,'Confirmed')
	recovered_smallest=df[['State','Recovered']].nsmallest(7,'Recovered')
	fatality_smallest=df[['State','Deaths']].nsmallest(7,'Deaths')
	
	#To make charts sorted in order:
	confirmed_largest=confirmed_largest.sort_values('Confirmed')
	confirmed_largest_plus=confirmed_largest_plus.sort_values('Confirmed')
	recovered_largest=recovered_largest.sort_values('Recovered')
	fatality_largest=fatality_largest.sort_values('Deaths')
	
	
	
	agree1 = st.checkbox('States with High Confirmed Numbers')
	if agree1:
		ax = confirmed_largest.plot.barh(x='State', y='Confirmed', rot=0)
		plt.tight_layout()
		st.pyplot()

	agree7=st.checkbox('States with High Confirmed Numbers(With Death & Recovery Comparision)')
	if agree7:
		ax = confirmed_largest_plus.plot.barh(x='State', y=['Confirmed','Recovered','Deaths'], rot=0)
		plt.tight_layout()
		st.pyplot()

	agree2 = st.checkbox('States with High Recovery Numbers')
	if agree2:
		ax = recovered_largest.plot.barh(x='State', y='Recovered', rot=0)
		plt.tight_layout()
		st.pyplot()

	agree3=st.checkbox('States with high Fatality Numbers')
	if agree3:
		ax = fatality_largest.plot.barh(x='State',y='Deaths',rot=0)
		plt.tight_layout()
		st.pyplot()
	agree4=st.checkbox('States with Low Confirmed Numbers')
	if agree4:
		ax = confirmed_smallest.plot.barh(x='State', y='Confirmed', rot=0)
		plt.tight_layout()
		st.pyplot()
	
	agree8=st.checkbox('States with Low Confirmed Numbers(With Death & Recovery Comparision)')
	if agree8:
		ax = confirmed_smallest_plus.plot.barh(x='State', y=['Confirmed','Recovered','Deaths'], rot=0)
		plt.tight_layout()
		st.pyplot()

	#agree5 = st.checkbox('States with Low Recovery Numbers')
	#if agree5:
		#ax = recovered_smallest.plot.barh(x='State', y='Recovered', rot=0)
		#plt.tight_layout()
		#st.pyplot()

	agree6=st.checkbox('States with Low Fatality')
	if agree6:
		ax = fatality_smallest.plot.barh(x='State',y='Deaths',rot=0)
		plt.tight_layout()
		st.pyplot()

	conf_nil=df.loc[df['Confirmed'].isnull()]
	rec_nil=df.loc[df['Recovered'].isnull()]
	fat_nil=df.loc[df['Deaths'].isnull()]

	#selectbox9
	agree9 = st.checkbox('States with Nil Confirmed')
	if agree9:
		conf_nil.iloc[:,0]

	#selectbox10
	#agree10 = st.checkbox('States with Nil Recovery')
	#if agree10:
		#rec_nil.iloc[:,1]

	#selectbox9
	agree11 = st.checkbox('States with Nil Death')
	if agree11:
		fat_nil.iloc[:,0]


	
	st.subheader('Time Series Analysis')
	df2=pd.read_csv('https://api.covid19india.org/csv/latest/case_time_series.csv')
	st.dataframe(df2)

	# plot data
	df2=pd.read_csv('https://api.covid19india.org/csv/latest/case_time_series.csv')
	df2[['Day','Month']] = df2.Date.apply(lambda x: pd.Series(str(x).split()))
	data=df2.groupby(['Month'])['Daily Confirmed','Daily Recovered','Daily Deceased'].sum()
	new_order = ['January', 'February', 'March', 'April', 'May']
	df1 = data.reindex(new_order, axis=0)
	df1.plot(kind='line')
	df1
	st.pyplot()
	

	st.subheader('_Districtwise - Update_')
	df3=pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
	df3=df3[['State','District','Confirmed','Active','Recovered','Deceased']]
	#st.dataframe(df3)

	#Getting Unique States & User Selection:
	unique_states=df3['State'].unique()
	unique_states.sort()
	option = st.selectbox('Select a State',unique_states)
	filt=df3['State']==option
	state_selected=df3.loc[filt]
	#converting 0 to Nan for treemap
	state_selected['Confirmed']=state_selected['Confirmed'].replace(0,np.nan)
	#sorting volume :
	state_selected=state_selected.sort_values(['Confirmed'],ascending=False)
	df5= pd.DataFrame(state_selected)
	st.dataframe(df5)
		
	if df5['Confirmed'].isnull().all() == True:
		st.write('Selected State contains Zero Confirmed Case')
			 	
	else:
		state_selected=state_selected.nlargest(14,'Confirmed')
		state_selected.sort_values(by='Confirmed',inplace=True)
		#state_selected
		ax = state_selected.plot.barh(x='District', y='Confirmed', rot=0)
		plt.tight_layout()
		plt.legend(loc=4)
		st.pyplot()
		
		ax = state_selected.plot.barh(x='District', y=['Confirmed','Active','Recovered','Deceased'], rot=0)
		plt.tight_layout()
		plt.legend(loc=4)
		st.pyplot()
		

	st.markdown('**_Source - api.covid19india.org_**')

	
	
	age = st.slider('Please feel free to rate this app', 1, 5, 1)
	if st.button('Submit'):
		st.write('Feedback Recieved at 8667722919 & mukhthakannan@gmail.com.\n Thank you for the feedback.')

	image2 = Image.open('guru_image.jpg')
	st.image(image2, use_column_width=False)
	
if __name__ == '__main__':
	main()
