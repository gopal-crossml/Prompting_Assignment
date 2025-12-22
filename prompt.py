# few shot prompting example:
prompt='''
 Classify the sentiment of the movie review as Positive or Negative.

 Review: "This movie was absolutely fantastic! A masterpiece!"
 Sentiment: Positive

 Review: "I fell asleep halfway through. Terrible plot."
 Sentiment: Negative

 Review: "It was okay, not great but not awful either."
 Sentiment: Negative

 Review: "The cinematography was stunning, but the story felt rushed."

 Sentiment:
 '''

# one shot prompting
prompt2 ='''
 Classify the sentiment of the following text as positive, negative, or neutral.
 Text: The product is terrible.
 Sentiment: Negative

 Text: I think the vacation was okay.
 Sentiment:
 '''

# role based prompting
prompt3='''
You are an experienced car dealer with 16 years of experience.
your goal is to help the customers to choose the right car according to their needs 

A customer says:
I need a car for daily travelling with good fuel efficiency"

Respond as a car dealer 
'''

# chain of thoughts prompting
prompt4 = '''
Solve the problem step by step.

If a phone costs $800 and is discounted by 25%, what is the final price?

'''
# Self consistency prompting
prompt5 ='''
If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

'''
# Tree of thoughts prompting
prompt6 ='''
Consider multiple possible solutions.
For each solution:
- Describe it briefly
- List one advantage
- List one drawback

Then select the best solution and explain why.

Question: How should I learn a new programming language quickly

'''
# Contextual prompting
prompt7 ='''
Context:
You are helping a beginner programmer who is new to Python.
They know how to print values but are confused about if–else statements.

Question:
Explain what an if–else statement is in Python with a simple real-life example.

'''

ALL_PROMPTS =[prompt]