import json

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are framing questions to help readers focus. Each question having less than seven words. Output as an array of strings in json"},
    {"role": "user", "content": '''frame four questions for the following text:
Moreover, attachment to things other than the Self leads to bondage. With this awareness, we get rid of the thirst for various desires. With this and a little effort from the intellect, the mind can be brought under our grip.
The pursuit of the Self is indeed impossible - even with very heavy effort - if the mind is not under control. A person needs to bring his mind under control, persevering by working independent of desire to worship Me.
With this, he gains the ability to practice yoga . He gains the ability to see everything with equanimity.'''}
  ]
)

print(completion.choices[0].message.content)

askys = json.loads(completion.choices[0].message.content)
for question in askys:
    print(f'Q: {question}')
