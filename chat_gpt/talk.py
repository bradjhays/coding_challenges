"""Using the OpenAI api, talk to chatGPT."""
import openai

# Use the OpenAI API key
openai.api_key = "your_openai_api_key"


def talk_to_gpt(prompt="hi, how are you?"):
    """Generate a response from the model."""
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the first response from the generated completions
    response_text = response["choices"][0]["text"]

    # Print the response
    print("Response: ", response_text)

    # Record the response to a file
    with open("chatgpt_response.txt", "w", encoding="utf-8") as file:
        file.write(response_text)


if __name__ == "__main__":
    talk_to_gpt()
