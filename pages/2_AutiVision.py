from PIL import Image
import streamlit as st
import keras
import numpy as np

st.set_page_config(page_title="My Page Title", page_icon="👋")

def main():
    st.title("AutiVisi∞n")

    st.subheader("Please upload an image of a face below:")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    st.write("The model may take a few minutes to run.")

    if uploaded_file is not None:
        # st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        image = Image.open(uploaded_file).resize((300, 300))
        image = np.array(image)
        image = image[:, :, :3]
        image = np.reshape(image, (1, 300, 300, 3))
        image = image.astype(np.float32) / 255.0
        model = keras.models.load_model("tools/model_V2/")
        predictions = model.predict(image)
        st.write(f"Our model predicts a {round(predictions[0][0] * 100, 4)}% chance of autism in this photo.")


main()
