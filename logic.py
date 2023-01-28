import openai


def ai_response(user_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_text,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=1,
    )
    generated = response.choices[0].text
    return generated