from transformers import pipeline
import streamlit as st

emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def analyze_emotion(text):
    """Analyze user's emotion and return top emotion and confidence."""
    try:
        result = emotion_classifier(text)
        if not result:
            return "neutral", 0.0  # If no emotion detected, return neutral
        top_emotion = max(result, key=lambda x: x['score'])
        return top_emotion['label'], top_emotion['score']
    except Exception as e:
        return "neutral", 0.0  # Fallback to neutral if detection fails




# Techniques for emotions
techniques = {
    "anger": "Try Cognitive Restructuring: Challenge negative thoughts by considering evidence that supports or contradicts your feelings. Practice deep breathing exercises to calm down.",
    "sadness": "Consider journaling your thoughts to process emotions more effectively. Engage in activities that bring you joy.",
    "joy": "Keep reinforcing positive behaviors with activities you find fulfilling. Share your joy with others to enhance your happiness.",
    "fear": "Try deep breathing or mindfulness exercises to reduce anxiety. Gradually expose yourself to the sources of your fear in a controlled manner.",
    "disgust": "Identify triggers of emotion and practice relaxation techniques. Challenge negative beliefs that may be contributing to your feelings.",
    "surprise": "Reflect on unexpected events through journaling. Consider how you can prepare for or embrace future surprises.",
    "neutral": "Take a moment to check in with yourself. Engage in a grounding exercise or simply enjoy a moment of calm."
}

# CBT techniques for mental health issues
cbt_techniques = {
    "Anxiety": [
        {"technique": "Cognitive Restructuring",
         "description": "Challenge irrational beliefs and replace them with realistic thoughts."},
        {"technique": "Breathing Exercises",
         "description": "Practice slow, deep breathing to reduce physical symptoms of anxiety."}
    ],
    "Sadness/Depression": [
        {"technique": "Behavioral Activation", "description": "Schedule positive activities to improve mood."},
        {"technique": "Cognitive Reframing", "description": "Identify and change negative thought patterns."}
    ],
    "Anger": [
        {"technique": "Progressive Muscle Relaxation", "description": "Relax your body to release tension."},
        {"technique": "Thought Stopping", "description": "Recognize and halt automatic anger-inducing thoughts."}
    ],
    "Guilt/Shame": [
        {"technique": "Self-Compassion", "description": "Practice kindness and understanding toward yourself."},
        {"technique": "Perspective Taking",
         "description": "Re-evaluate the situation with a less critical perspective."}
    ],
    "Stress": [
        {"technique": "Time Management",
         "description": "Create structured plans to manage tasks and reduce overwhelm."},
        {"technique": "Mindfulness", "description": "Stay in the present moment to reduce stress."}
    ]
}


def get_cbt_techniques(emotion_or_issue):
    # Check if the input is in the techniques dictionary


    if emotion_or_issue.lower() in techniques:
        return techniques[emotion_or_issue.lower()]

    # Check if the input is in the cbt_techniques dictionary
    elif emotion_or_issue in cbt_techniques:
        return "\n".join(
            [f"{entry['technique']}: {entry['description']}" for entry in cbt_techniques[emotion_or_issue]])

    else:
        return "Sorry, I don't have techniques for that emotion or issue."

# def get_cbt_techniques(emotion):
#     """Return CBT techniques based on emotion."""
#     techniques = {
#         "anger": "Try Cognitive Restructuring: Challenge negative thoughts by considering evidence that supports or contradicts your feelings.",
#         "sadness": "Consider journaling your thoughts to process emotions more effectively.",
#         "joy": "Keep reinforcing positive behaviors with activities you find fulfilling.",
#         "fear": "Try deep breathing or mindfulness exercises to reduce anxiety.",
#         "disgust": "Identify triggers of emotion and practice relaxation techniques.",
#         "surprise": "Reflect on unexpected events through journaling."
#     }
#     return techniques.get(emotion.lower(), "Let's explore some strategies for your emotions.")


# # Provide CBT techniques based on emotions
# def get_cbt_techniques(emotion, confidence, threshold=0.5):
#     """Get CBT techniques based on the detected emotion and confidence level."""
#     # Check if the confidence level meets the threshold
#     if confidence < threshold:
#         return "Emotion detection was uncertain. Consider practicing mindfulness or taking a break to assess your feelings."
#
#     techniques = {
#         "anger": "Try Cognitive Restructuring: Challenge negative thoughts by considering evidence that supports or contradicts your feelings. Practice deep breathing exercises to calm down.",
#         "sadness": "Consider journaling your thoughts to process emotions more effectively. Engage in activities that bring you joy.",
#         "joy": "Keep reinforcing positive behaviors with activities you find fulfilling. Share your joy with others to enhance your happiness.",
#         "fear": "Try deep breathing or mindfulness exercises to reduce anxiety. Gradually expose yourself to the sources of your fear in a controlled manner.",
#         "disgust": "Identify triggers of emotion and practice relaxation techniques. Challenge negative beliefs that may be contributing to your feelings.",
#         "surprise": "Reflect on unexpected events through journaling. Consider how you can prepare for or embrace future surprises.",
#         "neutral": "Take a moment to check in with yourself. Engage in a grounding exercise or simply enjoy a moment of calm."
#     }
#
#     return techniques.get(emotion.lower(), "Let's explore some strategies for your emotions.")
#
#
def get_default_cbt():
    """Provide a default fallback CBT technique if no specific emotion is detected."""
    return "It seems like you're feeling neutral. Try a mindfulness exercise or take a break to clear your thoughts."