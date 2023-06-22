import streamlit as st
import pandas

st.set_page_config(page_title="Tehran", layout="wide")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("")
    st.write("")
    st.image("images/Tehran_01.jpg", width=800)
    st.write("")
    st.write("")
    st.image("images/Tehran_02.jpg", width=800)

Tehran_Introduction ='''Tehran Province (Persian: استان تهران Ostān-e Tehrān) is one of the 31 provinces of Iran. It covers an area of 18,814 square kilometers (7,264 sq mi) and is located to the north of the central plateau of Iran. At the time of the National Census of 2006, the province had a population of 13,281,858 in 3,729,010 households. The following census in 2011 counted 12,183,391 people in 3,731,480 households, by which time Karaj, Nazarabad, and Savojbolagh Counties had been separated from the province to become Alborz province. The province was made a part of the First Region with its secretariat located in Tehran, upon the division of the provinces into 5 regions, solely for coordination and development purposes on June 22, 2014. According to the latest census in 2016, the population of the province had increased to 13,267,637 in 4,288,563 households. Tehran province borders Mazandaran province in the north, Qom province in the south, Semnan province in the east, Alborz province in the west and Markazi province in the southwest. The metropolis of Tehran is the capital city of the province and of Iran. Tehran province is the richest in Iran, as it contributes approximately 29% of the country's GDP. Furthermore, it houses approximately 18% of the country's population and is the most industrialized province in Iran, with nearly 94% of its residents living in the cities as of 2016. The province gained importance when Tehran was claimed the capital by the Qajar dynasty in 1778. Today, Tehran, with a population of 8 million, is ranked amongst the 40 most populous metropolitan cities of the world.'''

with col2:
    st.header("Tehran Province")
    st.write(f"<h20>{Tehran_Introduction}</h20>", unsafe_allow_html=True)

df = pandas.read_csv('Tehran.csv')

col3, spaceCol, col4 = st.columns([1.5, 1, 1.5])

with col3:

    for index, row in df.iloc[:35].iterrows():
        st.title(row['name'])
        st.image('images/' + row['image'])

with col4:

    for index, row in df.iloc[35:].iterrows():
        st.title(row['name'])
        st.image('images/' + row['image'])
