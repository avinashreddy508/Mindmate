import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import streamlit as st

def plot_emotion_distribution(messages):
    """Plot the emotion distribution if it hasn't been generated already."""
    # Check if the plot already exists in session state

    if len(st.session_state.emotion_history) > 0:
        # Count occurrences of each emotion
        emotion_counts = Counter(st.session_state.emotion_history)
    # #if "emotion_plot" not in st.session_state or st.session_state.emotion_data_changed:
    #     emotion_data = [msg.get("emotion", "neutral") for msg in messages]
    #     emotion_counts = Counter(emotion_data)
        #emotion_counts = pd.Series(emotion_data).value_counts()

        # Create a bar plot of the emotions over time
        fig, ax = plt.subplots()
        ax.bar(emotion_counts.keys(), emotion_counts.values())
        ax.set_xlabel("Emotions")
        ax.set_ylabel("Occurrences")
        ax.set_title("Emotion Distribution Over Time")

        # Store the plot in session state
        #st.session_state.emotion_plot = fig
        #st.session_state.emotion_data_changed = False  # Reset the flag after plotting

    # Display the plot from session state
        st.pyplot(fig)
    else:
        st.write("No emotions detected yet. Start by analyzing your first emotion!")