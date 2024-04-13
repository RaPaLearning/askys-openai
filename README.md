# Generate and Ask

Given a section (shloka) and a bunch of paragraphs (commentary), this program generates:
1. four questions to help focus on reading the text
1. an array of embeddings, one per paragraph

## To start

`python -m pip install -r requirements.txt`

`set OPENAI_API_KEY=`your_api_key

(py files are in trial still, execute them with python) 

## Samples

```  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a zen guru, framing short questions for a socratic session."},
    {"role": "user", "content": '''make a json array with five leading questions that have answers in the following paragraphs:...
```

The string comes in markdown

```json
{
  "questions": [
    {
      "q1": "What leads to bondage according to awareness?",
      "answer": "Attachment to things other than the Self."
    },
    {
      "q2": "What can help in getting rid of the thirst for various desires?",
      "answer": "Being aware and making a little effort from the intellect."
    },
    {
      "q3": "Why is bringing the mind under control essential for pursuing the Self?",
      "answer": "Without control of the mind, the pursuit of the Self is impossible."
    },
    {
      "q4": "How can a person persevere in bringing the mind under control?",
      "answer": "By working independent of desire to worship Me."
    },
    {
      "q5": "What abilities can one gain by practicing yoga and having control over the mind?",
      "answer": "The ability to practice yoga and to see everything with equanimity."
    }
  ]
}
```

Notice q3 and q4 have continuation

## Without Zen guru

```  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are framing short questions for a socratic session."},
    {"role": "user", "content": '''make a json array with five leading questions that have answers in the following paragraphs:...
```

the string comes in json

{
  "questions": [
    {
      "question": "What does attachment to things other than the Self lead to?",
      "answer": "Bondage."
    },
    {
      "question": "How can the thirst for various desires be eliminated?",
      "answer": "By becoming aware and getting rid of attachment to things other than the Self."
    },
    {
      "question": "What is necessary in order to pursue the Self effectively?",
      "answer": "Bringing the mind under control."
    },
    {
      "question": "What does one gain by persevering in bringing the mind under control?",
      "answer": "The ability to practice yoga and see everything with equanimity."
    },
    {
      "question": "How can the mind be brought under control?",
      "answer": "With awareness, effort from the intellect, and working independent of desire."
    }
  ]
}

## Repeat of the above

now gives markdown!!

```json
[
    {
        "question": "What leads to bondage according to the text?",
        "answer": "Attachment to things other than the Self leads to bondage."
    },
    {
        "question": "What is necessary to bring the mind under control?",
        "answer": "A little effort from the intellect is necessary to bring the mind under control."
    },
    {
        "question": "Why is pursuing the Self impossible without controlling the mind?",
        "answer": "The pursuit of the Self is impossible without controlling the mind, even with heavy effort."
    },
    {
        "question": "What does gaining the ability to practice yoga lead to?",
        "answer": "Gaining the ability to practice yoga leads to seeing everything with equanimity."
    },
    {
        "question": "How can one get rid of the thirst for various desires?",
        "answer": "One can get rid of the thirst for various desires with awareness and effort from the intellect."
    }
]
```

## GPT-4, with stricter json instruction

```  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are framing questions to help readers focus. Each question having less than seven words. Output as an array of strings in json"},
    {"role": "user", "content": '''frame four questions for the following text:
```

gives short stuff

```json
[
  "What leads to bondage?",
  "How can the mind be controlled?",
  "Why is self pursuit difficult?",
  "What ability is gained from yoga?"
]
```

## Best of the lot, input not sure

```json
{
  "questions": [
    "What does attachment to things other than the Self lead to?",
    "How can the mind be brought under control?",
    "What is necessary in order to pursue the Self?",
    "What ability does one gain through yoga practice?",
    "What can help a person see everything with equanimity?"
  ],
  "answers": [
    "Attachment to things other than the Self leads to bondage.",
    "The mind can be brought under control with 
awareness, effort from the intellect, and getting rid of the thirst for various desires.",
    "To pursue the Self, one needs to bring their mind under control 
by working independent of desire to worship.",
    "Through yoga practice, one gains the ability to see everything with equanimity.",
    "Bringing the mind under control can help a person see everything with equanimity."
  ]
}
```