#Step1: Setup GROQ API key
import os
import streamlit as st
GROQ_API_KEY=st.secrets["GROQ_API_KEY"]

#Step2: Convert image to required format
import base64
def encode_image(image_file):   
   
    return base64.b64encode(image_file.read()).decode('utf-8')

#Step3: Setup Multimodal LLM 
from groq import Groq

#model = "meta-llama/llama-4-scout-17b-16e-instruct"
#model="llama-3.2-90b-vision-preview" #Deprecated


#query with image
def analyze_image_with_query(query, model, encoded_image):

    try:
        
        client=Groq()  
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": query
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}",
                        },
                    },
                ],
            }]
        chat_completion=client.chat.completions.create(
            messages=messages,
            model=model
        )

        return chat_completion.choices[0].message.content
    except:
        return "Service Unavailable"

#query without image
def analyze_image_without_query(query, model):
    try:
        client = Groq(
        api_key=st.secrets["GROQ_API_KEY"],
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                "role": "user",
                "content": query,
                }
            ],
        model=model,
        )

        return chat_completion.choices[0].message.content
    except:
        return "Service Unavailable"
