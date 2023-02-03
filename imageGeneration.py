import openai

openai.api_key = "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"


response = openai.Image.create(
  prompt="a cat working on a laptop with laptop screen showing steps to defeat a dog",
  n=1,
  size="256x256"
)
image_url = response['data'][0]['url']
print(image_url)
