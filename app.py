
import streamlit as st
from sklearn.naive_bayes import BernoulliNB

# Set page config
st.set_page_config(page_title="Text Classifier", layout="centered")

def main():
    st.title("Stress Detection")
    
    # Text input
    user_input = st.text_area("Enter your text:", "")
    
    # When user clicks the button
    if st.button("Check Stress Level"):
        if user_input:
            # Preprocess the input (replace with your actual preprocessing)
            data = cv.transform([user_input]).toarray()
            
            # Make prediction
            output = model.predict(data)
            
            # Display result
            if output[0] == "No Stress":
                st.success("Result: No Stress detected")
            else:
                st.warning("Result: Stress detected")
        else:
            st.info("Please enter some text to analyze")

if __name__ == "__main__":
    # Load your trained model (you'll need to load this properly)
    model = BernoulliNB()  # Replace with your actual model loading code
    # You'll also need to load your CountVectorizer (cv) here
    
    main()

