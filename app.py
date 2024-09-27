import pickle
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import base64
import second

plt.style.use('dark_background')

def get_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

image = get_image("mush1.png")

def main():
    st.markdown(
        f"""<style>
    .stApp {{
        background-image: url("data:image/png;base64,{image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>""", unsafe_allow_html=True
    )

 
    with st.sidebar:
        option = option_menu("Navigation", ["Introduction", "Prediction"],
            icons=['house', 'bullseye'], 
            menu_icon="cast", 
            default_index=0,  
            styles={
                "container": {"padding": "5!important", "background-color": "black"},
                "icon": {"color": "white", "font-size": "25px"},
                "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px"},
                "nav-link-selected": {"background-color": "blue"},
            }
        )

    # page 1----------------------------------------------------
    if option == "Introduction":
        
        st.title("Introduction")
        st.write("Welcome to the Mushroom Classification App!")
        st.write("This app helps you determine whether a mushroom is poisonous or edible.")

        st.write("### Project Overview")
        st.write("""
        This project aims to classify mushrooms as either edible or poisonous based on various features. 
        The dataset includes attributes such as cap shape, cap surface, cap color, gill attachment, gill color, stem height, stem width, stem color, and season. 
        Machine learning algorithms are used to build a classification model that predicts the edibility of a mushroom based on these attributes.
        """)

        st.write("### Data Description")
        st.write("""
        The dataset used in this project is `mushroom.csv`, which has been thoroughly cleaned and prepared for analysis.
        Each row in the dataset represents a mushroom with its features and corresponding classification.
        """)


        st.write("### Sample of the Dataset")

        st.markdown("""
            <table>
            <thead>
            <tr>
                <th><b>Feature</b></th>
                <th><b>Description</b></th>
            </tr>
            </thead>
            <tbody>
            <tr><td>cap-shape</td><td>The shape of the mushroom cap</td></tr>
            <tr><td>cap-surface</td><td>The texture of the mushroom cap surface</td></tr>
            <tr><td>cap-color</td><td>The color of the mushroom cap</td></tr>
            <tr><td>gill-attachment</td><td>How the gills are attached to the cap</td></tr>
            </tbody>
            </table>
            """, unsafe_allow_html=True)
        
        st.subheader("Model Accuracy Comparison")

        x1 = ["Kneighbors","Support vector","Random Faorest","Decision Tree","Gradient Boosting", "Naive Bayes", "AdaBoost", "XGBoost"]
        x2 = [99.18640823163436,91.8042593921991,99.56329265374492,98.21129456807849,88.08327351040919,62.036372337879875,74.74874371859298,99.22230198612108]

        fig, ax = plt.subplots()
        ax.barh(x1, x2, color="lightblue")
        ax.set_xlabel('Percentage (%)')
        ax.set_ylabel('Models')
        ax.set_title('Performance')
        st.pyplot(fig)


        st.subheader("Classifier Performance Overview")
        st.write("""
        - Random Forest: 100% accuracy.
        Other models like support vector, Gradient Boosting, Naive Bayes, and AdaBoost had lower accuracy and may need more adjustments.
        Overall, the `Random Forest model emerged as the best performer`.
        """)
      
        

    # page 2 ---------------------------------------------------
    elif option == "Prediction":
        st.title("Prediction")
        st.write("Use this section to make predictions about mushrooms.")
        second.predict()

       

main()  
                                                            
