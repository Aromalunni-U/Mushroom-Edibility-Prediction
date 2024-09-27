import pickle
import streamlit as st

def predict():
    model = pickle.load(open('model.sav', 'rb'))
    scaler = pickle.load(open('scaler.sav', 'rb'))

    #LabelEncoders
    capshape_encoder = pickle.load(open('cap-shape_encoder.sav', 'rb'))
    season_encoder = pickle.load(open('season_encoder.sav', 'rb'))
    gill_attachment_encoder = pickle.load(open('gill-attachment_encoder.sav', 'rb'))
    bruise_or_bleed_encoder = pickle.load(open('does-bruise-or-bleed_encoder.sav', 'rb'))
    stem_color_encoder = pickle.load(open('stem-color_encoder.sav', 'rb'))
    cap_color_encoder = pickle.load(open('cap-color_encoder.sav', 'rb'))

    capshape_mapping = {
        "bell": "b", 
        "conical": "c", 
        "convex": "x", 
        "flat": "f", 
        "sunken": "s", 
        "spherical": "p", 
        "others": "o"
    }
    season_map = {
        'spring': 's', 'summer': 'u', 'autumn': 'a', 'winter': 'w'
    }
    gill_attachment_map = {
        'adnate': 'a', 'adnexed': 'x', 'decurrent': 'd', 'free': 'e',
        'sinuate': 's', 'pores': 'p', 'other': 'f'
    }
    bruise_or_bleed_map = {
        'Yes': 't', 
        'No': 'f'
    }
    stem_color_map = {
        'brown': 'n', 'buff': 'b', 'gray': 'g', 'green': 'r', 'pink': 'p',
        'purple': 'u', 'red': 'e', 'white': 'w', 'yellow': 'y', 'blue': 'l',
        'orange': 'o', 'black': 'k', 'other': 'f'
    }
    cap_color_map = {
        'brown': 'n', 'buff': 'b', 'gray': 'g', 'green': 'r', 'pink': 'p',
        'purple': 'u', 'red': 'e', 'white': 'w', 'yellow': 'y', 'blue': 'l',
        'orange': 'o', 'black': 'k'
    }

    # User input
    cap = st.number_input("Cap Diameter")
    stem_height = st.number_input("Stem Height")
    stem_width = st.number_input("Stem Width")
    
    # Select boxes
    capshape = st.selectbox("Cap Shape", list(capshape_mapping.keys()))
    gill_attachment_input = st.selectbox('Gill Attachment', list(gill_attachment_map.keys()))
    bruise_or_bleed_input = st.selectbox('Does Bruise or Bleed?', list(bruise_or_bleed_map.keys()))
    stem_color_input = st.selectbox('Stem Color', list(stem_color_map.keys()))
    cap_color_input = st.selectbox('Cap Color', list(cap_color_map.keys()))
    season_input = st.selectbox('Season', list(season_map.keys()))


    try:
        cap = float(cap)
        stem_height = float(stem_height)
        stem_width = float(stem_width)
    except ValueError:
        st.write("Please enter valid numbers for Cap Diameter, Stem Height, and Stem Width.")
        return

    capshape_value = capshape_mapping[capshape]
    capshape_value_encoded = capshape_encoder.transform([capshape_value])[0]

    gill_attach = gill_attachment_map[gill_attachment_input]
    gill_attach_encoded = gill_attachment_encoder.transform([gill_attach])[0]

    bruise_or_bleed = bruise_or_bleed_map[bruise_or_bleed_input]
    bruise_or_bleed_encoded = bruise_or_bleed_encoder.transform([bruise_or_bleed])[0]

    stem_color = stem_color_map[stem_color_input]
    stem_color_encoded = stem_color_encoder.transform([stem_color])[0]

    cap_color = stem_color_map[cap_color_input]
    cap_color_encoded = cap_color_encoder.transform([cap_color])[0]

    season = season_map[season_input]
    season_encoded = season_encoder.transform([season])[0]

    features = [cap, capshape_value_encoded, cap_color_encoded, bruise_or_bleed_encoded,gill_attach_encoded, stem_height, stem_width, stem_color_encoded, season_encoded]

    pred = st.button("PREDICT")
    if pred:
        try:
            scaled_features = scaler.transform([features])
            result = model.predict(scaled_features)
            if result == 0:
                st.write("### The mushroom is **:green[Edible]** ✅")
            else:
                st.write("### The mushroom is **:red[Poisonous]**! ☠️")
        except Exception as e:
            st.write(f"An error occurred: {e}")
