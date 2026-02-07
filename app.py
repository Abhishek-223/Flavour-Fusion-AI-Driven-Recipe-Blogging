from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
import random

# ================================
# Configure Gemini API Key
# ================================
load_dotenv() 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# ================================
# Model Generation Configuration
# ================================
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 2048,
}


# ================================
# Initialize Gemini Model
# ================================
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config
)




# ================================
# Joke Generation Function
# ================================
def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the programmer quit his job? Because he didn't get arrays!",
        "How many programmers does it take to change a light bulb? None. It's a hardware problem!",
        "Why do Java developers wear glasses? Because they don't see sharp!",
        "Why was the computer cold? Because it forgot to close its Windows!",
        "There are only 10 types of people in the world: those who understand binary and those who don't.",
        "Why did the programmer go broke? Because he used up all his cache!",
        "Debugging: Being the detective in a crime movie where you are also the murderer."
    ]
    return random.choice(jokes)


# ================================
# Recipe Generation Function
# ================================
def recipe_generation(user_input, word_count):
    """
    Generates a recipe blog using Gemini AI
    """

    # Show loading message
    st.write("### ⏳ Generating your recipe blog...")
    st.write(f"💡 Here's a programmer joke while you wait:\n\n**{get_joke()}**")

    # Prompt for Gemini
    prompt = f"""
    Write a detailed and engaging recipe blog about: {user_input}.

    Requirements:
    - Word count: approximately {word_count} words
    - Include:
        • Introduction
        • Ingredients list
        • Step-by-step instructions
        • Cooking tips
        • Variations (optional)
        • Conclusion

    Make it friendly, engaging, and suitable for a food blog.
    """

    try:
        response = model.generate_content(prompt)
        st.success("✅ Your recipe blog is ready!")
        return response.text

    except Exception as e:
        st.error(f"❌ Error generating blog: {e}")
        return None


# ================================
# Streamlit User Interface
# ================================

# Page title
st.title("🍽️ Flavour Fusion: AI-Driven Recipe Blogging")

# Description
st.write("Generate creative and detailed recipe blogs using Gemini AI.")


# User input
topic = st.text_input("Enter Recipe Topic:", placeholder="Example: Vegan Chocolate Cake")

word_count = st.number_input(
    "Enter Word Count:",
    min_value=100,
    max_value=2000,
    value=500,
    step=100
)


# Generate button
if st.button("Generate Recipe Blog"):

    if topic.strip() == "":
        st.warning("⚠️ Please enter a recipe topic.")

    else:
        blog = recipe_generation(topic, word_count)

        if blog:
            st.write("## 📖 Generated Recipe Blog")
            st.write(blog)


# Footer
st.write("---")
st.write("Made with ❤️ using Streamlit and Gemini API")
