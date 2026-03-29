from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key=os.environ["AZURE_API_KEY"],
    azure_endpoint=os.environ["AZURE_ENDPOINT"],
    api_version="2024-02-01-preview",
)

def translate(sentence: str, language: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional translator. "
                    "Return only the translated text, no explanation, "
                    "no quotation marks, no preamble."
                )
            },
            {
                "role": "user",
                "content": f"Translate this to {language}: {sentence}"
            }
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    sentence = "Good morning, I hope you have a wonderful day"
    languages = ["French", "Spanish", "German", "Italian", "Arabic", "Japanese", "Portuguese"]

    for language in languages:
        print(f"=== {language} ===")
        print(translate(sentence, language))
        print()