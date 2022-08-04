
from cgi import print_form
import prompt_toolkit
from requests import session
import streamlit as st
import time
import os
from turtle import st as trt
import openai




def open_ai_query(pr):
 
    openai.api_key ="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"

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=pr,#"The following is a conversation with an intelligent fictional character. The character's race is Dragonborn. he/she is a Barbarian with an Acolyte background.\n\nHuman: Hello, who are you? Tell me about yourself, what's your history, traits, and favorite sport?\n\n",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
    
    return response

def my_widget(key):
    st.subheader('Hello there!')
    return st.button("Click me " + key)


        
        #if len(question)!=0:
        #    print("inside", counter)
        #    "wht happened?"
        #    counter+=1
        #    prompt=prompt+resp+question
        #    print("I got here")
        #    ask_question(counter)
            


st.markdown("### Welcome to Spacetink® Character Generator")
st.markdown('choose your characeter attributes')

name=st.text_input("Enter the name of your Characrer")
characterRaces = ("Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling", "Orc of Exandria", "Leonin", "Satyr", "Fairy", "Harengon", "Owlin", "Aarakocra", "Genasi", "Goliath", "Aasimar", "Bugbear", "Firbolg", "Goblin", "Hobgoblin", "Kenku", "Kobold", "Lizardfolk", "Orc", "Tabaxi", "Triton", "Yuan-ti Pureblood", "Feral Tiefling", "Tortle", "Changeling", "Kalashtar", "Orc of Eberron", "Shifter", "Warforged", "Gith", "Centaur", "Loxodon", "Minotaur", "Simic Hybrid", "Vedalken", "Verdan", "Locathah", "Grung")

characterClasses = ("Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer", "Blood Hunter")
characterBackgrounds = ("Acolyte", "Acolyte - Baldur's Gate", "Acolyte (Luxonborn)", "Anthropologist", "Archaeologist", "Athlete", "Azorius", "Functionary", "Boros Legionnaire", "Celebrity Adventurer’s Scion", "Charlatan", "Charlatan - Baldur’s Gate", "City Watch / Investigator", "Clan Crafter", "Cloistered Scholar", "Courtier", "Criminal - Baldur’s Gate", "Criminal (Myriad Operative)", "Criminal / Spy", "Dimir Operative", "Entertainer", "Entertainer - Baldur’s Gate", "Faceless", "Faction Agent", "Failed Merchant", "Far Traveler", "Feylost", "Fisher", "Folk Hero", "Folk Hero - Baldur’s Gate", "Gambler", "Gladiator", "Golgari Agent", "Grinner", "Gruul Anarch", "Guild Artisan - Baldur’s Gate", "Guild Artisan / Guild Merchant", "Haunted One", "Hermit", "Hermit - Baldur’s Gate", "House Agent (Cannith)", "House Agent (Deneith)", "House Agent (Ghallanda)", "House Agent (Jorasco)", "House Agent (Kundarak)", "House Agent (Lyrandar)", "House Agent (Medani)", "House Agent (Orien)", "House Agent (Orien)", "House Agent (Orien)", "House Agent (Tharashk)", "House Agent (Thuranni)", "House Agent (Vadalis)", "Inheritor", "Investigator", "Izzet Engineer", "Knight", "Knight of the Order", "Lorehold Student", "Marine", "Mercenary Veteran", "Noble", "Noble - Baldur’s Gate", "Orzhov Representative", "Outlander", "Outlander - Baldur’s Gate", "Pirate", "Plaintiff", "Prismari Student", "Quandrix Student", "Rakdos Cultist", "Rival Intern", "Sage", "Sage - Baldur’s Gate", "Sage (Cobalt Scholar)", "Sailor", "Sailor - Baldur’s Gate", "Sailor (Revelry Pirate)", "Selesnya Initiate", "Shipwright", "Silverquill Student", "Simic Scientist", "Smuggler", "Soldier", "Soldier - Baldur’s Gate", "Spy (Augen Trust)", "Urban Bounty Hunter", "Urchin", "Urchin - Baldur’s Gate", "Uthgardt Tribe Member", "Volstrucker Agent", "Waterdhavian Noble", "Witchlight Hand", "Witherbloom Student")

race=st.selectbox('Race',characterRaces)
klass=st.selectbox('Class',characterClasses)
background=st.selectbox('Background',characterBackgrounds)
st.write(st.session_state)


if 'count' not in st.session_state:
	st.session_state.count = 0

global gen_char
gen_char=st.button("Generate Character",key=772)
if name:
    prompt="The following is a conversation with an intelligent fictional character, thier name is "+name+". The character's race is "+ race+".he/she is a " + klass+" with an "+background+"background.\n\nHuman: Hello, who are you? Tell me about yourself, what's your history, traits, and favorite sport?\n\n",
    prompt=prompt[0]
else:
    "Please insert character name!"
    st.stop()

if gen_char:
    
    
    with st.spinner('Wait for it...'):
        generated_response=open_ai_query(prompt)
    #global resp        
    resp=str(generated_response['choices'][0]['text'])
    st.session_state.count += 1
    os.remove("demofile2.txt")
    f = open("demofile2.txt", "a")
    f.write(resp)
    f.close()

f = open("demofile2.txt", "r")

resp=f.read()
f.close()
st.markdown(resp)

#clicked=st.button("Ask me a question")
if 'counter' not in st.session_state:
	st.session_state.counter = 0
def ask_questiton():
    st.session_state.counter+=1

    text=st.text_input("add a new question",key=st.session_state.counter)
    st.markdown(text)
    clicked=st.button("Ask me a question",key=st.session_state.counter)
    if clicked:
        ask_questiton()
    
ask_questiton()




   
    


# option = st.selectbox("",('Human', 'Robot', 'Vehicle' , 'Animal'))

# text=st.text_input('describe your Character: ')

# clicked=st.button('Generate 3D model')

# if clicked and text:
#     with st.spinner('Wait for it...'):
#         time.sleep(10)
#     video_file = open('./images/donkey_final_crop.mp4', 'rb')
#     data = video_file.read()
#     st.video(data, format="video/mp4", start_time=0)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
