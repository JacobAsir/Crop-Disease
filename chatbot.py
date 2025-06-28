from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model_name="llama-3.1-8b-instant")

# Chatbot function with multilingual support
def chatbot(message, history, info, language="English"):
    # English prompt template
    prompt_template_en = """
    You are an expert agricultural advisor specializing in plant diseases. 
    Provide direct, actionable advice without unnecessary introductions.

    Disease: {info}

    Previous conversation: {history}

    Farmer's question: {message}

    Instructions:
    - Start your response directly with the answer
    - Be specific and practical
    - Include step-by-step guidance when relevant
    - Focus on actionable solutions
    - Don't mention "based on the information provided" or similar phrases
    - Don't use introductory phrases like "Here's a comprehensive guide" or "Let me help you"
    - Speak directly to the farmer as if in a consultation
    - Keep responses concise but complete
    """

    # Japanese prompt template
    prompt_template_ja = """
    あなたは植物病害の専門農業アドバイザーです。
    不要な前置きなしに、直接的で実行可能なアドバイスを提供してください。

    病害: {info}

    これまでの会話: {history}

    農家の質問: {message}

    指示:
    - 回答から直接始めてください
    - 具体的で実用的にしてください
    - 関連する場合は段階的なガイダンスを含めてください
    - 実行可能な解決策に焦点を当ててください
    - 「提供された情報に基づいて」などのフレーズは使用しないでください
    - 「包括的なガイドです」や「お手伝いさせてください」などの導入フレーズは使用しないでください
    - 相談のように農家に直接話しかけてください
    - 簡潔でありながら完全な回答を心がけてください
    - 必ず日本語で回答してください
    """

    # Select prompt based on language
    if language == "Japanese":
        prompt_template = prompt_template_ja
    else:
        prompt_template = prompt_template_en

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["info", "history", "message"]
    )

    chain = LLMChain(llm=llm, prompt=PROMPT)
    response = chain.predict(info=info, history=history, message=message)
    return response
