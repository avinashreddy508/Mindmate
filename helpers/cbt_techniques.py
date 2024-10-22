# Define a broader range of CBT techniques
def cbt_techniques(technique_name):
    techniques = {
        "thought_challenging": "Try to challenge your thoughts by asking yourself: What evidence do I have that supports this thought? What evidence do I have against this thought?",
        "reframing": "Can you think of a more balanced or alternative way to view this situation? What positive aspects can you focus on?",
        "behavioral_activation": "Is there something small you can do to reduce your stress or anxiety? Sometimes, taking one small action can help you feel more in control.",
        "coping_statements": "Repeat positive coping statements like: 'I can handle this' or 'I’ve dealt with similar situations before, and I came through.'",
        "mindfulness": "Try to bring your attention to the present moment. Focus on your breath and the sensations around you. Let your thoughts come and go without judgment.",
        "exposure_therapy": "Gradually expose yourself to situations that cause anxiety in a controlled way. Start small, and over time, you’ll reduce the power that these situations have over you.",
        "journaling": "Write down your thoughts and feelings in a journal. Sometimes, putting your emotions on paper can help you process and understand them better.",
        "problem_solving": "Focus on specific, actionable steps that you can take to solve the problem you're facing. Break it down into smaller steps, and tackle them one at a time."
    }
    return techniques.get(technique_name, "No technique available for this response.")


# Function to identify the situation based on user input
def identify_situation(user_input):
    user_input = user_input.lower()
    if "stress" in user_input or "overwhelmed" in user_input:
        return "stress_at_work"
    elif "guilt" in user_input or "argument" in user_input:
        return "guilt_after_argument"
    elif "anxiety" in user_input or "future" in user_input:
        return "anxiety_about_future"
    elif "body image" in user_input or "self-esteem" in user_input:
        return "negative_body_image"
    elif "social" in user_input or "shy" in user_input:
        return "social_anxiety"
    elif "focus" in user_input or "concentration" in user_input:
        return "difficulty_focusing"
    elif "overwhelmed" in user_input:
        return "feeling_overwhelmed"
    elif "sleep" in user_input or "insomnia" in user_input:
        return "trouble_sleeping"
    else:
        return "unknown"


# Sample situations the chatbot can respond to
def ask_cbt_questions(situation):
    if situation == "stress_at_work":
        return "It sounds like you're feeling overwhelmed at work. That's a common experience when we have a lot on our plate. What thoughts are coming to your mind when you feel like you can’t catch up?" \
               "\nCBT Technique: " + cbt_techniques("thought_challenging")

    elif situation == "guilt_after_argument":
        return "It seems like you're feeling guilty about the argument with your friend. It's tough to feel that way, but you're already reflecting on it." \
               "\nWhat part of the argument is making you feel the most guilty?" \
               "\nCBT Technique: " + cbt_techniques("reframing")

    elif situation == "anxiety_about_future":
        return "I understand that you're feeling anxious about the future. It's normal to feel that way when there's a lot of uncertainty." \
               "\nWhat specific thoughts are causing you to feel this way about the future?" \
               "\nCBT Technique: " + cbt_techniques("behavioral_activation")

    elif situation == "negative_body_image":
        return "It sounds like you're struggling with how you see yourself right now. That's really hard, and I'm here to help you through it." \
               "\nWhat thoughts do you have when you look at yourself in the mirror?" \
               "\nCBT Technique: " + cbt_techniques("coping_statements")

    elif situation == "social_anxiety":
        return "It seems like social situations are making you feel anxious. I can understand how intimidating that can be." \
               "\nWhat thoughts or feelings come up when you think about these situations?" \
               "\nCBT Technique: " + cbt_techniques("exposure_therapy")

    elif situation == "difficulty_focusing":
        return "It sounds like you’re having a hard time focusing. That can be frustrating, especially when you have a lot to do." \
               "\nWhat do you think might be making it difficult to focus right now?" \
               "\nCBT Technique: " + cbt_techniques("mindfulness")

    elif situation == "feeling_overwhelmed":
        return "It sounds like you’re feeling overwhelmed by everything going on. That’s a really tough place to be." \
               "\nWhat’s the first thing that comes to mind when you think about what’s overwhelming you?" \
               "\nCBT Technique: " + cbt_techniques("problem_solving")

    elif situation == "trouble_sleeping":
        return "It sounds like you’re having trouble sleeping. That can have a big impact on how you feel during the day." \
               "\nWhat thoughts tend to keep you up at night?" \
               "\nCBT Technique: " + cbt_techniques("journaling")

    else:
        return "I'm sorry, I don't have a specific response for that situation right now."


# # Simulating user input and chatbot response
# def simulate_cbt_chat():
#     print("Welcome to your Cognitive Behavioral Therapy (CBT) assistant!")
#
#     # Get user input
#     user_input = input("\nPlease describe a situation or emotion you'd like help with: ")
#
#     # Identify the situation based on user input
#     situation = identify_situation(user_input)
#
#     # Get appropriate response based on identified situation
#     response = ask_cbt_questions(situation)
#
#     print("\nChatbot Response: ", response)
#
#
# # Run the chatbot simulation
# simulate_cbt_chat()
