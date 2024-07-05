import streamlit as stl
from Module import Backend as bknd

def main():
    stl.set_page_config(
        page_title="M.U.R.A.L",
        page_icon=':tada:',
        layout="wide",
        initial_sidebar_state="expanded",
    )

    display_header()

    stl.subheader("Summary")
    stl.write("M.U.R.A.L stands for Machine-aided Understanding and Recognition of Artistic Legacies...")

    stl.image("Website_images/AIvsHuman.jpg", width=1000)
    stl.markdown("---")

    display_instructions()

    stl.subheader("Try M.U.R.A.L")
    uploaded_file = stl.file_uploader("Upload an image to make predictions", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        display_uploaded_image(uploaded_file)

        if stl.button("Get Info"):
            display_image_info(uploaded_file)

        if stl.button("Predict"):
            display_prediction_result(uploaded_file)

    stl.markdown("---")
    display_about_author()

def display_header():
    stl.title("M.U.R.A.L")
    stl.subheader("Machine-aided Understanding and Recognition of Artistic Legacies")
    stl.markdown("---")

def display_instructions():
    stl.sidebar.title('How to Use')
    stl.sidebar.markdown('<hr>', unsafe_allow_html=True)
    stl.sidebar.markdown('# Welcome to M.U.R.A.L!')
    stl.sidebar.markdown('## Follow these steps:')
    steps = [
        "Step 1: Read the summary",
        "Step 2: Go to try M.U.R.A.L",
        "Step 3: Click Upload Image button",
        "Step 4: Get metadata for image",
        "Step 5: Click Predict",
        "Step 6: View Result"
    ]
    for step in steps:
        stl.sidebar.markdown(step)
    stl.sidebar.markdown('<hr>', unsafe_allow_html=True)
    stl.sidebar.title('Contact Creator')
    stl.sidebar.markdown('- Name : Malhar Girgaonkar')
    stl.sidebar.markdown('- Email: [malhargirgaonkarr@gmail.com](malhargirgaonkarr@gmail.com)')
    stl.sidebar.markdown('- Linkedin : [Malhar Girgaonkar](https://www.linkedin.com/in/malhar-girgaonkar-b9223a28a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)')
    stl.sidebar.markdown('- Github : [Malhar Girgankar](https://github.com/Malhar-Girgaonkar)')

def display_uploaded_image(uploaded_file):
    stl.image(uploaded_file, width=500, caption="Uploaded Image")
    stl.markdown("---")
    stl.subheader('Image Metadata')
    stl.write("Image information can only be displayed if it was encoded when user took photo and in other cases it would not be possible to display image info..")

def display_image_info(uploaded_file):
    image_info = bknd.Get_image_info(uploaded_file)
    if image_info is not None:
        stl.subheader("Image Information")
        for key, value in image_info.items():
            stl.write(f"- {key} : {value}")
    else:
        stl.write('No data available')

def display_prediction_result(uploaded_file):
    prediction_result = bknd.Predictions(uploaded_file)
    stl.subheader("Prediction Result")
    stl.write('Model predicted: ', prediction_result)

def display_about_author():
    stl.markdown("---")
    stl.subheader("About Author")
    stl.markdown("This project, created by Malhar Girgaonkar, aims to support artists in receiving the credit they deserve...")
    stl.markdown("- Model Training code: [AI_Art_VS_Human_Art](https://malhar-girgaonkar.github.io/AI_Art_vs_Human_Art/)")
    stl.markdown("- Primitive App: [M.U.R.A.L](https://malhar-girgaonkar.github.io/M.U.R.A.L/)")

if __name__ == "__main__":
    main()
