
import streamlit as st
import pickle

# Load the trained vectorizer
with open("vectorizer.pkl", "rb") as f:
    cv = pickle.load(f)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit page configuration
st.set_page_config(page_title="Stress Detection", layout="centered")

def main():
    st.markdown(
    """
    <style>
    body {
        background-color: #ADD8E6; /* Light blue background */
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    st.title("🧠 Stress Detection")

    # Input box
    user_input = st.text_area("Enter your text:")

    # Button
    if st.button("Check Stress Level"):
        if user_input:
            data = cv.transform([user_input]).toarray()
            output = model.predict(data)

            if output[0].lower() == "no stress":
                st.success("Result: No Stress detected")
            else:
                st.warning("Result: Stress detected")
        else:
            st.info("Please enter some text")

if __name__ == "__main__":
    main()
