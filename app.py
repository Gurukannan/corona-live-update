import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
	
def main():
	""" A simple Text Analyzer App """

	st.header('India - Live Coronavirus Update - Guru.K')
	st.subheader('_Statewise - Live Corona Update_')
	df=pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')
	df= df.iloc[:,:7]
	st.dataframe(df)
	df=df.drop(df.index[0])
	confirmed_largest=df[['State','Confirmed']].nlargest(7,'Confirmed')
	#st.table(confirmed_largest)
	#plt.bar(confirmed_largest['State'],confirmed_largest#['Confirmed'],color=['g','y','b','r'])

	agree = st.checkbox('States with high numbers')
	if agree:
		plot= sns.barplot(x=confirmed_largest['Confirmed'], y=confirmed_largest['State'],data=confirmed_largest)
		plt.tight_layout()
		st.pyplot()

	st.subheader('_Time Series - Live Corona Update_')
	df2=pd.read_csv('https://api.covid19india.org/csv/latest/case_time_series.csv')
	st.dataframe(df2)

	st.subheader('_Districtwise - Live Corona Update_')
	df3=pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
	df3=df3[['State','District','Confirmed','Active','Recovered','Deceased']]
	st.dataframe(df3)

	#plot TreeMap
	unique_states=df3['State'].unique()
	option = st.selectbox('Select a State',unique_states)
	filt=df3['State']==option
	state_selected=df3.loc[filt]
	st.dataframe(state_selected)
	#converting 0 to Nan for treemap
	state_selected['Confirmed']=state_selected['Confirmed'].replace(0,np.nan)
	#sorting volume :
	state_selected=state_selected.sort_values(['Confirmed'],ascending=False)

	state_selected=state_selected.nlargest(7,'Confirmed')
	volume=state_selected['Confirmed']
	labels=state_selected['District']
	ax= sns.barplot(x=volume, y=labels,data=state_selected,label='small')
	st.pyplot()
	df6=state_selected[['District','Confirmed']]
	#pd.melt(df6,id_vars=['District'],value_vars=['Confirmed'])
	#df6.set_index('District',inplace=True)
	#df6
	#st.bar_chart(state_selected['District'],state_selected['Confirmed'])

	#plt.autoscale()
	#plt.tight_layout()
	#df6.plot.barh()
	#st.pyplot()

	st.markdown('**_Source - api.covid19india.org_**')

	age = st.slider('Please feel free to rate this app', 1, 5, 1)
	if st.button('Submit'):
		st.write('Thank you for the feedback')
	
if __name__ == '__main__':
	main()
