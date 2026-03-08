from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Connect to Foundry
myEndpoint = "https://eliasabdo718-1008-resource.services.ai.azure.com/api/projects/eliasabdo718-1008"

project_client = AIProjectClient(
    endpoint=myEndpoint,
    credential=DefaultAzureCredential(),
)

myAgent = "Elias-language-Translator"
myVersion = "3"
openai_client = project_client.get_openai_client()

# Reusable function
def ask_agent(prompt):
    response = openai_client.responses.create(
        model="gpt-4.1",
        input=[{"role": "user", "content": prompt}],
        extra_body={"agent_reference": {"name": myAgent, "version": myVersion, "type": "agent_reference"}},
    )
    return response.output_text

# The sentence we are testing
sentence = "Good morning, I hope you have a wonderful day"

# List of languages to translate into
languages = ["French", "Spanish", "German", "Italian", "Arabic", "Japanese", "Portuguese"]

# Loop through each language and print the translation
for language in languages:
    print(f"=== {language} ===")
    print(ask_agent(f"Translate this to {language}: '{sentence}'"))
    print()

