import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": f"Bearer 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"}

def explain_sentence(sentence: str) -> str:
    prompt = f"Explain the following legal sentence in layman's terms:\n\n{sentence}"
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()

        # Extract the generated explanation and remove the prompt part
        explanation = result[0]["generated_text"]

        # Remove the prompt part from the explanation
        explanation = explanation.replace(prompt, "").strip()

        return explanation
    else:
        return f"Error {response.status_code}: {response.text}"

