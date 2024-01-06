import openai

openai.api_key = "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"

response = openai.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Hello"}
  ]
)

temp = response.choices[0].message.content
temp_index = temp.find(":")
message = temp[temp_index+3:-2]
print(message)