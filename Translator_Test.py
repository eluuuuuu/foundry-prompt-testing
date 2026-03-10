from openai import AzureOpenAI
import os

openai_client = AzureOpenAI(
    api_key=os.environ["AZURE_API_KEY"],
    azure_endpoint="https://eliasabdo718-1008-resource.services.ai.azure.com",
    api_version="2025-01-01-preview",
)

myAgent = "Elias-language-Translator"
myVersion = "3"

def ask_agent(prompt):
    response = openai_client.responses.create(
        model="gpt-4.1",
        input=[{"role": "user", "content": prompt}],
        extra_body={"agent_reference": {"name": myAgent, "version": myVersion, "type": "agent_reference"}},
    )
    return response.output_text

sentence = "Good morning, I hope you have a wonderful day"
languages = ["French", "Spanish", "German", "Italian", "Arabic", "Japanese", "Portuguese"]

for language in languages:
    print(f"=== {language} ===")
    print(ask_agent(f"Translate this to {language}: '{sentence}'"))
    print()
