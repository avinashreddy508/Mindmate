import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")
# Sample emotion classifier function (stub)
# Analyze user's emotion
def analyze_emotion(text):
    result = emotion_classifier(text)
    top_emotion = max(result, key=lambda x: x['score'])
    return top_emotion['label'], top_emotion['score']


# def analyze_emotion(text):
#     """
#     Analyze the user's emotion based on the input text and return the
#     most prominent emotion with the corresponding confidence score.
#     """
#     try:
#         # Call to the emotion classifier function
#         result = emotion_classifier(text)
#
#         if not result or len(result) == 0:
#             # Return 'neutral' if no emotion is detected
#             return "neutral", 0.0
#
#         # Find the emotion with the highest score
#         top_emotion = max(result, key=lambda x: x['score'])
#
#         return top_emotion['label'], top_emotion['score']
#
#     except Exception as e:
#         # Log the error if needed (print or logging)
#         print(f"Error in emotion analysis: {e}")
#
#         # Return 'neutral' and confidence 0.0 in case of error
#         return "neutral", 0.0


# Dictionary to map emotions to CBT techniques
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

# Streamlit App
st.title("Emotion-Aware Chat Assistant for CBT with Emotion Tracking")

# Initialize the session state for emotion history if not already set
if 'emotion_history' not in st.session_state:
    st.session_state.emotion_history = []

# Input text from the user
user_input = st.text_area("How are you feeling today? Describe your thoughts and emotions.", "")

# Button to analyze emotion
if st.button("Analyze Emotion"):
    if user_input:
        # Analyze the emotion from the input text
        emotion, confidence = analyze_emotion(user_input)

        # Display the detected emotion and confidence score
        st.write(f"**Detected Emotion**: {emotion} (Confidence: {confidence:.2f})")

        # Save the detected emotion to the session state
        st.session_state.emotion_history.append(emotion)

        # Display relevant CBT techniques if the emotion is known
        if emotion in cbt_techniques:
            st.subheader(f"CBT Techniques for {emotion}")
            for technique in cbt_techniques[emotion]:
                st.markdown(f"**{technique['technique']}**: {technique['description']}")
        else:
            st.write("No specific CBT techniques available for this emotion.")
    else:
        st.warning("Please enter some text for emotion analysis.")

# Optionally allow the user to take notes or reflect on the suggestions
with st.expander("Reflection"):
    reflection = st.text_area("Write down your thoughts or how you might apply these techniques.")

# Submit reflection button
if st.button("Submit Reflection"):
    st.success("Thank you for sharing your thoughts!")

# --- Emotion Graphs Section ---
st.subheader("Emotion Tracking Graph")

# If emotion history is available, visualize the emotions
if len(st.session_state.emotion_history) > 0:
    # Count occurrences of each emotion
    emotion_counts = Counter(st.session_state.emotion_history)

    # Create a bar plot of the emotions over time
    fig, ax = plt.subplots()
    ax.bar(emotion_counts.keys(), emotion_counts.values())
    ax.set_xlabel("Emotions")
    ax.set_ylabel("Occurrences")
    ax.set_title("Emotion Distribution Over Time")

    # Display the plot in Streamlit
    st.pyplot(fig)
else:
    st.write("No emotions detected yet. Start by analyzing your first emotion!")
