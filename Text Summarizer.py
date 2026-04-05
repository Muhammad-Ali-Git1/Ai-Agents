import requests
import streamlit as st
Url='https://api.apyhub.com/ai/summarize-text'
Key='APY01qvfPrDxIlSthlHQshVZleOoNGwsufkypqUe6JLoghhByHFqxBv95FOH3RAntBGCXL2Ncp61i'
text=st.text_area('Enter to summarize: ')

if st.button('Summarize'):

    headers={
    'apy-token':Key,
    'Content-Type':'application/json'
    } 
    payload={
    'text':text

    }
    response=requests.post(Url,headers=headers,json=payload)

    if response.status_code==200:
        result=response.json()
        Summary=result['data']['summary']
        st.success("Summary: ")
        st.write(Summary)

    else:
        print({response.status_code})

