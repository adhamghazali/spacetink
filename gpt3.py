import os
from turtle import st
import openai

openai.api_key = os.getenv("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")


def quary_OAI(pr):

    response = openai.Completion.create(model="text-davinci-002",prompt=pr, temperature=0.7,max_tokens=256,top_p=1,frequency_penalty=0,presence_penalty=0)
    return response


def main(name='Dr.Peter', theme='fantasy'):
    start='Generate a non-player character for a game with the following settings.\nTheme: '+ theme+ '\ncharacter: Doctor \nName: ' +name
    print(start)
    prompt=quary_OAI(start)
    print(prompt)
    return prompt

main()
