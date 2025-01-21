import openai

def ask_question(prompt):
    openai.api_key = "proj_NNLJ1e3oL6Nj5WA0LyF7tXJv"
    response = openai.ChatCompletion.create(
        engine="gpt-4",
        prompt = prompt,
        max_tokens=100
    )
    print(response)
    return response.choices[0].text.strip()