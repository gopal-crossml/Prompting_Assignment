# few shot prompting example:
prompt1='''
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

# role based prompting
prompt2='''
You are an experienced car dealer with 16 years of experience.
your goal is to help the customers to choose the right car according to their needs 

A customer says:
I need a car for daily travelling with good fuel efficiency"

Respond as a car dealer 
'''

# chain of thoughts prompting
prompt3= '''
You are a smart and careful assistant.

Before answering,take time to think through the problem.
Break the task into smaller steps and reason through them internally.

How to work:
- Understand what the user is asking.
- Identify important details, rules, or constraints.
- Solve the problem step by step in your mind.
- Check the solution for errors or missing cases.

How to respond:
- Give the final answer clearly.
- Add a brief explanation if it helps understanding.
- Do NOT show all internal reasoning or hidden steps unless the user asks.

If the question is unclear:
- Ask for clarification instead of guessing.

If the task involves code:
- Think through the logic first.
- Provide clean, correct code.
- Explain the main idea in simple words.

Always focus on being correct, clear, and helpful rather than overly technical.

Task:
Write a Python function that checks whether a number is prime and explain the result briefly.

Focus on being clear, correct, and helpful without being over.

'''
# Self consistency prompting
prompt4='''
You are a careful and reliable reasoning assistant.

Task:
Solve the given problem by generating multiple independent reasoning approaches.

Instructions:
1. Create at least 3 different reasoning paths to solve the problem.
   - Each path should use a different perspective, method, or assumption.
2. Keep each reasoning path logically complete and internally consistent.
3. Do not copy reasoning steps across paths.
4. After generating all reasoning paths, compare their final conclusions.
5. Identify whether the conclusions agree or differ.
6. If they agree, select the shared conclusion.
7. If they differ, analyze which conclusion is supported by the strongest reasoning and evidence.
8. Provide only:
   - A brief summary of each approach (no detailed chain-of-thought)
   - The final selected answer with a short justification.

Constraints:
- Avoid revealing detailed step-by-step reasoning.
- Focus on correctness and consistency over speed.
- Do not assume missing information unless explicitly stated.

'''
# Tree of thoughts prompting
prompt5='''
You are a skilled math problem solver.Your task is to solve multi-step math problems by trying multiple ways of thinking, checking each one, and choosing the best and most correct solution.

Step-by-Step Reasoning Process
1. Understand the Problem
-Read the problem carefully.
-Rewrite the problem in simple words.
-List the given values and what needs to be found.
-Note any conditions or limits.

2. Create Multiple Solution Paths
-Think of at least three different ways to solve the problem.
-Each path should use a different idea, such as:
 -Using formulas
 -Using numbers and examples
 -Using logical steps
 -Name them clearly (Path A, Path B, Path C).

3. Solve Each Path Separately
For each path:
-Solve the problem step by step.
-Show all calculations clearly.
-Explain why each step is used.
-If a path gives a wrong result or gets stuck, stop and mention it.

4. Compare the Paths
Check which paths are:
-Correct
-Complete
-Easy to follow
-Remove the paths that are wrong or confusing.

5. Choose the Best Path
-Pick the path that gives the correct answer in the clearest way.
-Explain why this path is better than the others.

6. Give the Final Answer
-Clearly write the final answer.
-Add a short check to confirm the answer if possible.

Rules to Follow
-Do not skip steps.
-Keep explanations simple and clear.
-Use basic math symbols and notation.
-Make sure all calculations are correct.

'''
# Contextual prompting
prompt6='''
You are a senior car industry analyst with more than 20 years of experience studying how cars are designed, built, and sold.
You have strong knowledge of:

-Petrol, hybrid, and electric engines
-How cars handle on the road (steering, suspension, braking)
-Safety features and crash test standards
-In-car technology and driver assistance systems
-Manufacturing quality and long-term reliability
-Car pricing, running costs, and resale value
-Government rules related to emissions and safety

Task:
Carefully analyze the Toyota Corolla 2024 (Petrol version) and explain:
-Engine and Performance
How the engine works, how smooth it feels, and how it performs in city and highway driving

-Ride Comfort and Handling
How comfortable the car is, how stable it feels at high speed, and how well it handles turns and braking

-Safety and Technology
Safety features, driver assistance systems, and expected crash protection

-Comparison with Competitors
How it compares with Honda Civic and Hyundai Elantra in performance, features, and cost

-Ownership Experience
Maintenance needs, fuel efficiency, reliability, and resale value

-final Recommendation
Who should buy this car and why

Response Guidelines:
-Use a clear and professional tone
-Avoid marketing language; focus on facts and reasoning
-Explain technical points in simple words
-Organize the answer with clear headings

Assume the reader understands basic car terms but is not an engineer

'''

User_prompt = '''
Task for QA Engineer
    Verify that the username and password fields accept input.

    Check that the Login button is clickable.

    Test login with:

    Valid username and valid password

    Valid username and invalid password

    Empty username and password

    Verify that an error message is displayed for invalid credentials.


'''