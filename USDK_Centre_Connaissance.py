# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:40:18 2021

@author: mathi
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px
import plotly.graph_objects as go
from PIL import Image

st.title('USDK Centre de connaissance')


image = Image.open(r'C:\Users\mathi\.spyder-py3\Images\2122.jpg')
st.image(image)

# import de données

DATA_URL = (r"C:\Users\mathi\.spyder-py3\source.csv")


@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv(DATA_URL, sep=";")
    return data

# Fin import de données

# affichage des données
df = load_data()

#Répondants
x = df.shape[0]
st.write("Le nombre de répondants est de ",x)
#
# Présentation de la civilité
st.subheader("Répartition des répondants par civilité")
count_civ = df["Civilite"].value_counts()
fig = px.bar(count_civ, y="Civilite", text="Civilite")
st.write(fig)
# fin de la présentation civilité

# Présentation de la code postal
st.subheader("Répartition des répondants par code postal")
count_cp = df["Code postal"].astype("string").str[:2].value_counts()
fig = px.bar(count_cp, y="Code postal",
             text="Code postal", color='Code postal')
st.write(fig)
# fin de la présentation code postal

# Présentation des dates de participation
st.subheader("Les participations dans le temps (numéro de mois de l'année)")
df["updateMoment"] = pd.to_datetime(df["updateMoment"])
count_tps = df["updateMoment"].dt.month.sort_values().value_counts()
fig = px.bar(count_tps, y="updateMoment",
             text="updateMoment", color='updateMoment')
st.write(fig)
# fin de la présentation des dates de participation

# Présentation de l'adversaire préféré
st.subheader("Répartition des répondants par adversaire favori")
count_adv = df["Adversaire prefere"].value_counts()
fig = px.bar(count_adv, y="Adversaire prefere",
             text="Adversaire prefere", color='Adversaire prefere')
st.write(fig)
# fin de la présentation adversaire préféré

# Présentation de l'adversaire préféré
st.subheader("Joueur préféré")
count_joueur = df["joueur"].value_counts()
fig = px.bar(count_joueur, y="joueur",
             text="joueur", color='joueur')
st.write(fig)
# fin de la présentation adversaire préféré

# Présentation des pratiquants
st.subheader("Pratiquants")
count_pratique = df["pratique"].value_counts()
fig = px.bar(count_pratique, y="pratique",
             text="pratique", color='pratique')
st.write(fig)
# fin de la présentation adversaire préféré

# Présentation de l'expérience
# split des variables
df['Experience'] = df["Experience"].fillna("").astype("string")
df['Enfant'] = df["Enfant"].fillna("").astype("string")
df['Offres'] = df["Offres"].fillna("").astype("string")
# fonctions

#EXPERIENCE
def copain(row):
    if "copain" in row:
        return 1
    else:
        return 0


def etudiant(row):
    if "tudiant" in row:
        return 1
    else:
        return 0


def premium(row):
    if "Premium" in row:
        return 1
    else:
        return 0


def jeu(row):
    if "quiz" in row:
        return 1
    else:
        return 0


def famille(row):
    if "famille" in row:
        return 1
    else:
        return 0


def garderie(row):
    if "garderie" in row:
        return 1
    else:
        return 0


def collegue(row):
    if "business" in row:
        return 1
    else:
        return 0

#Enfant
def evenement_spe(row):
    if "ciaux" in row:
        return 1
    else:
        return 0
    
def stage(row):
    if "Stage" in row:
        return 1
    else:
        return 0
    
def boutique_enf(row):
    if "boutique" in row:
        return 1
    else:
        return 0
    
def billetterie_enf(row):
    if "Billetterie" in row:
        return 1
    else:
        return 0
    

 # Fonctions Offres
def boutique_off(row):
    if "boutique" in row:
        return 1
    else:
        return 0
    
def abo_off(row):
    if "abonnement" in row:
        return 1
    else:
        return 0
    
def pack_off(row):
    if "pack" in row:
        return 1
    else:
        return 0
    
def entreprise_off(row):
    if "Entreprise" in row:
        return 1
    else:
        return 0

# fin des fonctions

    # Application des fonctions
    # Fonctions expériences
df["Experience_copain"] = df["Experience"].apply(lambda x: copain(x))
df["Experience_etudiant"] = df["Experience"].apply(lambda x: etudiant(x))
df["Experience_premium"] = df["Experience"].apply(lambda x: premium(x))
df["Experience_jeu"] = df["Experience"].apply(lambda x: jeu(x))
df["Experience_famille"] = df["Experience"].apply(lambda x: famille(x))
df["Experience_garderie"] = df["Experience"].apply(lambda x: garderie(x))
df["Experience_collègues"] = df["Experience"].apply(lambda x: collegue(x))

    # Fonctions Enfants
df["Enfant_Evspe"] = df["Enfant"].apply(lambda x: evenement_spe(x))
df["Enfant_stage"] = df["Enfant"].apply(lambda x: stage(x))
df["Enfant_boutique"] = df["Enfant"].apply(lambda x: boutique_enf(x))
df["Enfant_billetterie"] = df["Enfant"].apply(lambda x: billetterie_enf(x))

     # Fonctions Offres
df["boutique_off"] = df["Offres"].apply(lambda x: boutique_off(x))
df["abo_off"] = df["Offres"].apply(lambda x: abo_off(x))
df["pack_off"] = df["Offres"].apply(lambda x: pack_off(x))
df["entreprise_off"] = df["Offres"].apply(lambda x: entreprise_off(x))

# Fin Application des fonctions

# graph experiences
val = [df["Experience_copain"].sum(), 
       df["Experience_etudiant"].sum(),
       df["Experience_premium"].sum(),
       df["Experience_jeu"].sum(),
       df["Experience_famille"].sum(),
       df["Experience_garderie"].sum(),
       df["Experience_collègues"].sum()]

dfe = pd.DataFrame(val, index = ['Copains', 'Etudiant', 'Premium',
       'Jeu', 'Famille', 'Garderie', 'Collègues'], columns = ['Nb'])

st.subheader("Nombre de répondants intéressés par les expériences")
fig = px.bar(dfe, y="Nb", color='Nb')
st.write(fig)

# graph Enfant
val = [df["Enfant_Evspe"].sum(), 
       df["Enfant_stage"].sum(),
       df["Enfant_boutique"].sum(),
       df["Enfant_billetterie"].sum()]


dfe1 = pd.DataFrame(val, 
                    index = ['Evénements spéciaux', 'Stage', 'Boutique','Billetterie'], 
                    columns = ['Nb'])

st.subheader("Nombre de répondants intéressés par les produits enfants")
fig = px.bar(dfe1, y="Nb", color='Nb')
st.write(fig)
#fin graph enfant

# graph Offres
val = [df["boutique_off"].sum(), 
       df["abo_off"].sum(),
       df["pack_off"].sum(),
       df["entreprise_off"].sum()]


dfe2 = pd.DataFrame(val, 
                    index = ['Produits boutique', 'Abonnements', 'Packs de matchs','Offres Entreprises'], 
                    columns = ['Nb'])

st.subheader("Nombre de répondants intéressés par les différentes offres")
fig = px.bar(dfe2, y="Nb", color='Nb')
st.write(fig)
#fin graph enfant

