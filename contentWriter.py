# https://beta.openai.com/playground


import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write code in css to display multiple html pages in horizontal tabs",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response["choices"][0].get("text"))
