from together import Together

client = Together(api_key="67f4b43be85bc61720e44a42d4c5b6cf26904245e11f85a9bffba0c4506d113a") # auth defaults to os.environ.get("TOGETHER_API_KEY")

response = client.chat.completions.create(
    model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=[{"role": "user", "content": "What are some fun things to do in New York?"}]
)
print(response.choices[0].message.content)

