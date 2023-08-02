import streamlit as st
st.set_page_config(page_title="My Page Title", page_icon="👋")

def main():
    st.title("AutiVisi∞n")

    st.subheader("Please upload an image of a face below:")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        st.write("The image above is an example of a lemniscate.")

main()
