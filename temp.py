#-------- Old Version----------------



# #All necessary imports
# import streamlit as st

# from pvoice import transcribe_with_groq
# from brain import analyze_image_with_query,analyze_image_without_query,encode_image
# import os

# from voice_of_doctor import speak

# #Tittle and Caption
# st.title("AI Doctor")
# st.caption("Note That This ChatBot Provides General Medical Informations And It Is Not A Substitute For Professional Medical Advicers")


# #Creating 2rows for clean layout
# row2=st.container()
# row3=st.container()
# #row3 includes multiple columns for better audio input placement
# with row3:
#     col1,col2,col3,col4=st.columns(4,vertical_alignment="bottom")

# #Some flags and global veriables
# cflag=False
# rflag=False
# uploaded_file=False
# text=False
# doctor_response=None

# #This prompt is for image
# system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
#             What's in this image?. Do you find anything wrong with it medically? 
#             If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
#             your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Donot say 'In the image I see' but say 'With what I see, I think you have ....'
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
#             Keep your answer concise . No preamble, start your answer right away please"""
# #This promt is for plain text
# system_prompt_txt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
#              Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
#             Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
#             Keep your answer concise . No preamble, start your answer right away please"""

# #row2 will include chats
# with row2:
#     with st.chat_message(name="ai",avatar="👨‍⚕️"):
#         st.write("Hello ,what brings you in today?")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "ai", "content": "Let's start chatting! 👇"}]

# with col4:
#     audio_value = st.audio_input("Record a voice message",label_visibility="collapsed")

#     if audio_value:
#         speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
#                                                     audio_filepath=audio_value,
#                                                     stt_model="whisper-large-v3")
#         rflag=True

# #Here our prompt starts
# if prompt := st.chat_input("What is up?",disabled=cflag,accept_file=True ):            
#             #text is taken from audio input
#             if rflag:
#                 prompt.text=speech_to_text_output

#             with row2:
#                 # Display user message in chat message container including image if any
#                 with st.chat_message("user"):
#                     if prompt and prompt.text:                        
#                         st.markdown(prompt.text)
#                         text=prompt.text
#                     if prompt and prompt["files"]:
#                         uploaded_file=prompt["files"][0]
#                         st.image(prompt["files"][0])
                
#                 #text and image both
#                 if text and uploaded_file :
#                     #encoding image
#                     input=encode_image(uploaded_file)
#                     #fetching response
#                     doctor_response = analyze_image_with_query(query=system_prompt+text, model="meta-llama/llama-4-scout-17b-16e-instruct", encoded_image=input)
#                     #speak function to play audio response
#                     speak(doctor_response)
#                     with st.chat_message(name="ai",avatar="👨‍⚕️"):
#                         st.write(doctor_response)
#                 #text only
#                 elif text :
#                     #fetching response
#                     doctor_response=analyze_image_without_query(system_prompt_txt+text, model="gemma2-9b-it")
#                     #speak function to play audio response
#                     speak(doctor_response)
#                     with st.chat_message(name="ai",avatar="👨‍⚕️"):
#                         st.write(doctor_response)

#                 #image only
#                 elif uploaded_file:
#                     input=encode_image(uploaded_file)
#                     doctor_response = analyze_image_with_query(query=system_prompt, model="meta-llama/llama-4-scout-17b-16e-instruct", encoded_image=input)
#                     speak(doctor_response)
#                     with st.chat_message(name="ai",avatar="👨‍⚕️"):
#                         st.write(doctor_response)
# #withou chat input
# else:
#     #if user have recorded any message
#     if rflag:
#          with row2:
#             with st.chat_message("user"):
#                  st.write(speech_to_text_output)
#             #checking if image is attached 
#             # with image     
#             if uploaded_file:
#                 uploaded_file=prompt["files"][0]
#                 st.image(prompt["files"][0])
#                 #encoding image
#                 input=encode_image(uploaded_file)
#                 #fetching response
#                 doctor_response=analyze_image_with_query(system_prompt+speech_to_text_output, model="meta-llama/llama-4-scout-17b-16e-instruct",encoded_image=input)
#                 #speak function to play audio response
#                 speak(doctor_response)
#                 with st.chat_message(name="ai",avatar="👨‍⚕️"):
#                     st.write(doctor_response)
#             #without image        
#             else:    
#                 #fetching response
#                 doctor_response = analyze_image_without_query(query=system_prompt_txt+speech_to_text_output, model="gemma2-9b-it")
#                 #speak function to play audio response
#                 speak(doctor_response)
#                 with st.chat_message(name="ai",avatar="👨‍⚕️"):
#                     st.write(doctor_response)

