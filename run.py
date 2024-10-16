from flask import Flask
from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
import os
import gradio as gr
from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.messages.concrete import SystemMessage
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation
load_dotenv()
API_KEY = os.getenv('API_KEY')
llm = GroqModel(api_key=API_KEY)
allowed_models = llm.allowed_models
conversation = MaxSystemContextConversation()
def loadmodel(selected_model):
    return GroqModel(api_key=API_KEY, name=selected_model)
def converse(input_text,histroy,system_context,model_name):
    print(f"system_context: {system_context}")
    print(f"model_name: {model_name}")
    llm = loadmodel(model_name)
    agent = SimpleConversationAgent(llm=llm, conversation=conversation)
    agent.conversation.system_context = SystemMessage(content=system_context)
    input_text = str(input_text)
    print(conversation.history)
    result = agent.exec(input_text)
    print(result,type(result))
    return str(result)
demo  = gr.ChatInterface(fn=converse, additional_inputs=[gr.Textbox(label="System Context"), gr.Dropdown( label="Model",choices=allowed_models, value=allowed_models[0])], title="Conversation Agent", description="Interact with Agent")
if __name__ == '__main__':
    demo.launch()

