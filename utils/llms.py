import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
# api_key = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY= "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"

class LLMModel:
    def __init__(self, model_name="llama3-70b-8192"):
        if not model_name:
            raise ValueError("Model is not defined.")
        self.model_name = model_name
        self.openai_model=ChatGroq(model=self.model_name)
        
    def get_model(self):
        return self.openai_model

if __name__ == "__main__":
    llm_instance = LLMModel()  
    llm_model = llm_instance.get_model()
    response=llm_model.invoke("hi")

    print(response)