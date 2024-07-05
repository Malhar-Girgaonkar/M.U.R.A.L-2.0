import streamlit as stl
from Module import Backend as bknd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'Website_images', 'AIvsHuman.jpg')

stl.set_page_config(page_title = "M.U.R.A.L",
                    page_icon=':tada:',
                    layout="wide",
                    initial_sidebar_state="expanded",
                    )

stl.title("M.U.R.A.L")
stl.subheader("Machine-aided Understanding and Recognition of Artistic Legacies")
stl.markdown("---")

# Sidebar / Left section for instructions
stl.sidebar.title('How to Use')
stl.sidebar.markdown('<hr>', unsafe_allow_html=True)
stl.sidebar.markdown('# Welcome to M.U.R.A.L!')
stl.sidebar.markdown('## Follow these steps:')
stl.sidebar.markdown('- Step 1: Read the summary')
stl.sidebar.markdown('- Step 2: Go to try M.U.R.A.L')
stl.sidebar.markdown('- Step 3: Click Upload Image button')
stl.sidebar.markdown('- Step 4: Get metadata for image ')
stl.sidebar.markdown('- Step 5: Click Predict')
stl.sidebar.markdown('- Step 6: View Result')
stl.sidebar.markdown('<hr>', unsafe_allow_html=True)
stl.sidebar.title('Contact Creator')
stl.sidebar.markdown('- Name : Malhar Girgaonkar')
stl.sidebar.markdown('- Email: [malhargirgaonkarr@gmail.com](malhargirgaonkarr@gmail.com)')
stl.sidebar.markdown('- Linkedin : [Malhar Girgaonkar](https://www.linkedin.com/in/malhar-girgaonkar-b9223a28a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)')
stl.sidebar.markdown('- Github : [Malhar Girgankar](https://github.com/Malhar-Girgaonkar)')

stl.subheader("Summary")
stl.write("M.U.R.A.L stands for Machine-aided Understanding and Recognition of Artistic Legacies. It is an application designed to identify artworks created by human artists and those generated by AI algorithms. This initiative aims to ensure proper credit for human artists and preserve the \"Human Essence of Art \" in the age of AI.")
stl.image(image_path, width= 1000)
stl.markdown("---")
stl.subheader("Try M.U.R.A.L")
# Button to upload image
uploaded_file = stl.file_uploader("Upload an image to make predictions", type=["jpg", "jpeg", "png"])
#print(uploaded_file)
# Check if a file is uploaded
if uploaded_file is not None:
    stl.image(uploaded_file, width= 500,caption="Uploaded Image")
    stl.markdown("---")
    stl.subheader('Image Metadata')
    stl.write("Image information can only be displayed if it was encoded when user took photo and in other cases it would not be possible to display image info..")
    if stl.button("Get Info"):
        image_info = bknd.Get_image_info(uploaded_file)
        if image_info is not None:
            stl.subheader("Image Information")
            for key, value in image_info.items():
                stl.write(f"- {key} : {value}")
        else:
            stl.write('No data available')
    # Button to trigger prediction
    stl.markdown("---")
    stl.subheader("Make Predictions")
    stl.write("Click Predict to see if image is AI made art or Human made Art")
    if stl.button("Predict"):
        # Call backend prediction function
        prediction_result = bknd.Predictions(uploaded_file)
        stl.markdown('---')
        # Display prediction result
        stl.subheader("Prediction Result")
        stl.write('Model predicted: ',prediction_result)
stl.markdown("---")
stl.subheader("About Author")
stl.markdown("This project, created by Malhar Girgaonkar, aims to support artists in receiving the credit they deserve and to combat the encroachment of AI in the art world. Modern advancements in generative AI have introduced a new challenge: artists often do not receive recognition for their work, which is used by large companies to train AI models without their consent. ")
stl.markdown("These models produce mass quantities of art that lack the human essence, soul, and dedication of real artists, yet are utilized by major media corporations in place of genuine art. This undermines the human essence of art, reducing it to a mere tool for capitalist profit. My project seeks to leverage AI against AI, providing artists with a platform to determine if an art piece they find online is AI-generated or created by a human artist")
stl.markdown("I have personally trained the Machine Learning model for this project and its documentation is given below")
stl.markdown("- Model Training code: [AI_Art_VS_Human_Art](https://malhar-girgaonkar.github.io/AI_Art_vs_Human_Art/)")
stl.markdown("- Primitive App: [M.U.R.A.L](https://malhar-girgaonkar.github.io/M.U.R.A.L/)")

