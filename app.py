#Necessary imports
import streamlit as st
import nltk
import pandas as pd
from matplotlib import pyplot as plt
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
from gensim.summarization.summarizer import summarize 

import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()


from collections import Counter




#Headings for Web Application
st.title("Natural Language Processing Web Application Name Entity Recognition")
st.subheader("What type of NLP service would you like to use?")

#Picking what NLP task you want to do
option = st.selectbox('NLP Service',('Entity Extraction','None')) #option is stored in this variable

#Textbox for text user is entering
st.subheader("Enter the text you'd like to analyze.")
text = st.text_input('Enter text') #text is stored in this variable

#Display results of the NLP task
st.header("Results")

#Function to take in dictionary of entities, type of entity, and returns specific entities of specific type
def entRecognizer(entDict, typeEnt):
    entList = [ent for ent in entDict if entDict[ent] == typeEnt]
    return entList




  

#Named Entity Recognition
if option == 'Entity Extraction':

    #Getting Entity and type of Entity
    entities = []
    entityLabels = []
    doc = nlp(text)
    for ent in doc.ents:
        entities.append(ent.text)
        entityLabels.append(ent.label_)
    entDict = dict(zip(entities, entityLabels)) #Creating dictionary with entity and entity types

    #Using function to create lists of entities of each type
    entOrg = entRecognizer(entDict, "ORG")
    entCardinal = entRecognizer(entDict, "CARDINAL")
    entPerson = entRecognizer(entDict, "PERSON")
    entDate = entRecognizer(entDict, "DATE")
    entGPE = entRecognizer(entDict, "GPE")

    #Displaying entities of each type
    st.write("Organization Entities: " + str(entOrg))
    st.write("Cardinal Entities: " + str(entCardinal))
    st.write("Personal Entities: " + str(entPerson))
    st.write("Date Entities: " + str(entDate))
    st.write("GPE Entities: " + str(entGPE))





st.text("")
st.text("")
st.text("")
st.markdown("***")
#---------------------------------#
# About
expander_bar = st.expander("About")
expander_bar.markdown("""
Kartikey Sharma, Student, Department of Computer Engineering
""")
