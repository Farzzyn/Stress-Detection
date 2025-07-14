
import streamlit as st
import pickle

# Load vectorizer and model
with open("vectorizer.pkl", "rb") as f:
    cv = pickle.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Set page config
st.set_page_config(page_title="Text Classifier", layout="centered")

def main():
    st.title("Stress Detection")

    # Text input
    user_input = st.text_area("Enter your text:", "")

    # When user clicks the button
    if st.button("Check Stress Level"):
        if user_input:
            data = cv.transform([user_input]).toarray()

            # Make prediction
            output = model.predict(data)

            # Display result
            if output[0].lower() == "no stress":
                st.success("Result: No Stress detected")
            else:
                st.warning("Result: Stress detected")
        else:
            st.info("Please enter some text to analyze")

if _name_ == "_main_":
    main()
