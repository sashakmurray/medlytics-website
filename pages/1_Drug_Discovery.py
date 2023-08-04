import streamlit as st
import numpy as np
import pandas as pd
import joblib
import subprocess
from keras.models import load_model

def predict(model, df):
    file = f"tools/model_CHEMBL{model}.joblib"
    rf = joblib.load(file)
    return round(10 ** (-rf.predict(df)[0]), 3)

st.title("Drug Discovery for Autism")

"""We created models to predict the antagonistic action of compounds on 5-hydroxytryptamine (5-HT) receptors which are associated with irritability, aggression, temper-outburst and self-injurious
behavior. 

We focused on 5-HT1AR, 5-HT1DR, 5-HT2AR, 5-HT2CR, and 5-HT7R. Drugs like Risperidone have been used to prevent the effects of these 5-HTs."""


smile = st.text_input("Please enter the molecular smile of your molecule. The model may take some time to load.")
print(smile)

if smile is not None and smile != "":
    df = pd.DataFrame([[smile]])
    df.to_csv('molecule.smi', sep='\t', index=False, header=False)
    subprocess.run(["cat", "molecule.smi"])
    subprocess.run(["cat", "padel.sh"])
    subprocess.run(["bash", "padel.sh"])
    df_X = pd.read_csv("descriptors_output.csv")
    df_X = np.array(df_X)[:, 1:]
    st.write("Below are the half-maximal inhibitory concentrations (IC50) of this molecule for each 5-HT receptor. This value measures what concentration of the molecule will inhibit 50% of the 5-HT receptor.")
    for model, molecule in zip([214, 224, 1983, 225, 3155], ["5-HT1AR", "5-HT1DR", "5-HT2AR", "5-HT2CR", "5-HT7R"]):
        if model == 225:
            m = load_model("tools/model_CHEMBL225.h5")
            prediction = round(10 ** (-m.predict(df_X.astype(np.float32))[0][0]), 3)
        else:
            prediction = predict(model, df_X)
        st.write(f"{molecule}: {prediction} nM")

