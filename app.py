import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
	
def main():
	""" A simple Text Analyzer App """

	st.header('India - Live Coronavirus Update - Guru.K')
	st.subheader('_Statewise - Live Corona Update_')

	url='https://api.covid19india.org/csv/latest/state_wise.csv'
	df=pd.read_csv(url,index_col='State')
	df= df.iloc[:,:6]
	df=df.replace(0,np.NaN)
	st.dataframe(df)
	#Drop Total Row:
	df=df.drop('Total')

	conf_larg=df.nlargest(7,'Confirmed')
	rec_larg=df.nlargest(7,'Recovered')
	fat_larg=df.nlargest(7,'Deaths')

	#selectbox1
	agree1 = st.checkbox('States with High Confirmed Numbers')
	if agree1:
		plot= sns.barplot(x='Confirmed',y=conf_larg.index,data=conf_larg)
		plt.tight_layout()
		st.pyplot()

	#selectbox10
	agree10 = st.checkbox('States with High Confirmed Numbers(With Recovery Comparision)')
	if agree10:
		xpos=np.arange(len(conf_larg.index))
		plt.yticks(xpos,conf_larg.index)
		plt.barh(xpos,conf_larg['Confirmed'],label=conf_larg['Confirmed'])
		plt.barh(xpos,conf_larg['Recovered'],label=conf_larg['Recovered'])
		#plt.barh(xpos,conf_larg['Recovered'],label=conf_larg['Deaths'])
		plt.tight_layout()
		labels=['Confirmed','Recovered']
		plt.legend(labels)
		st.pyplot()

	#selectbox11
	agree11 = st.checkbox('States with High Confirmed Numbers(With Fatality Comparision)')
	if agree11:
		xpos=np.arange(len(conf_larg.index))
		plt.yticks(xpos,conf_larg.index)
		plt.barh(xpos,conf_larg['Confirmed'],label=conf_larg['Confirmed'])
		#plt.barh(xpos,conf_larg['Recovered'],label=conf_larg['Recovered'])
		plt.barh(xpos,conf_larg['Deaths'],label=conf_larg['Deaths'])
		plt.tight_layout()
		labels=['Confirmed','Deaths']
		plt.legend(labels)
		st.pyplot()

	#selectbox2
	agree2 = st.checkbox('States with High Recovery Numbers')
	if agree2:
		plot= sns.barplot(x='Recovered',y=rec_larg.index,data=rec_larg)
		plt.tight_layout()
		st.pyplot()
	#selectbox3
	agree3 = st.checkbox('States with high Fatality Numbers')
	if agree3:
		plot= sns.barplot(x='Deaths',y=fat_larg.index,data=fat_larg)
		plt.tight_layout()
		st.pyplot()


	conf_smal=df.nsmallest(7,'Confirmed')
	rec_smal=df.nsmallest(7,'Recovered')
	fat_smal=df.nsmallest(7,'Deaths')

	#selectbox4
	agree4 = st.checkbox('States with Low Confirmed Numbers')
	if agree4:
		plot= sns.barplot(x='Confirmed',y=conf_smal.index,data=conf_smal)
		plt.tight_layout()
		st.pyplot()
	#selectbox5
	#agree5 = st.checkbox('States with Low Recovery Numbers')
	#if agree5:
		#plot= sns.barplot(x='Recovered',y=rec_smal.index,data=rec_smal)
		#plt.tight_layout()
		#st.pyplot()
	#selectbox6
	agree6 = st.checkbox('States with Low Fatality Numbers')
	if agree6:
		plot= sns.barplot(x='Deaths',y=fat_smal.index,data=fat_smal)
		plt.tight_layout()
		st.pyplot()

	conf_nil=df.loc[df['Confirmed'].isnull()]
	rec_nil=df.loc[df['Recovered'].isnull()]
	fat_nil=df.loc[df['Deaths'].isnull()]

	#selectbox7
	agree7 = st.checkbox('States with Nil Confirmed')
	if agree7:
		conf_nil.iloc[:,0]

	#selectbox8
	agree8 = st.checkbox('States with Nil Recovery')
	if agree8:
		rec_nil.iloc[:,1]

	#selectbox9
	agree9 = st.checkbox('States with Nil Death')
	if agree9:
		fat_nil.iloc[:,2]


	st.subheader('_Time Series - Live Corona Update_')
	url2='https://api.covid19india.org/csv/latest/case_time_series.csv'
	df2=pd.read_csv(url2)
	st.dataframe(df2)
	#Chart:
	df2[['Day','Month']] = df2.Date.apply(lambda x: pd.Series(str(x).split()))
	graph1=df2.groupby('Month')['Daily Confirmed','Daily Recovered','Daily Deceased'].sum()
	new_order = ['January', 'February', 'March', 'April', 'May']
	graph1 = graph1.reindex(new_order, axis=0)
	graph1

	x = graph1.index
	y1 = graph1['Daily Confirmed']
	y2 = graph1['Daily Recovered']
	y3 = graph1['Daily Deceased']

	plt.plot(x, y1, "-b", label="Confrimed")
	plt.plot(x, y2, "-r", label="Recovered")
	plt.plot(x,y3,'-y',label='Deceased')
	plt.legend(loc="upper left")
	#plt.ylim(-1.5, 2.0)
	plt.show()
	st.pyplot()


	st.subheader('_Districtwise - Live Corona Update_')
	df3=pd.read_csv('https://api.covid19india.org/csv/latest/district_wise.csv')
	df3=df3[['State','District','Confirmed','Active','Recovered','Deceased']]
	#st.dataframe(df3)

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
	ax= sns.barplot(x=volume, y=labels,data=state_selected)
	st.pyplot()
		
	st.markdown('**_Source - api.covid19india.org_**')

	age = st.slider('Please feel free to Numbers this app', 1, 5, 1)
	if st.button('Submit'):
		st.write('Thank you for the feedback')
if __name__ == '__main__':
	main()
