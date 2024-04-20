import os
import openai

personality = [
    {"role": "system", "content": "You are a well mannered english butler who can pleasantly answer any questions"}
]

print("\nGood afternoon sir or madam, My name is Jeeves, How can I be of assistance?")

i = -1

while (i < 1):

  userInput = input("\n") 
  print("\n")

  question = [
      {"role": "system", "content": "You are a well mannered english butler named Jeeves who can pleasantly answer any questions asked of him. Jeeves never breaks character so when responding to questions always take on the personality of Jeeves."},
      {"role": "user", "content": userInput}
  ]

  messages = personality.append(question)

  completion = openai.chat.completions.create(messages=question, model="gpt-3.5-turbo" )


  #better format for larger quereys, not currently working
  #completion = openai.chatCompletions.create(
  #  model="gpt-3.5-turbo",
  #  messages=messages
  #)

  textBlock = completion.choices[0].message.content
  print(textBlock)
