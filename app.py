import streamlit as st
import gensim.downloader as api
import numpy as np
import string
import re

# 🔹 AI ipucu önerici
def oner_ipucu(hedefler, yasaklar, model, aday_kelimeler=None):
    filtre = set(hedefler + yasaklar)
    if aday_kelimeler is None:
        aday_kelimeler = list(model.key_to_index.keys())

    en_iyi_ipucu = None
    en_iyi_skor = -float("inf")

    for kelime in aday_kelimeler:
        if kelime in filtre:
            continue
        try:
            hedef_skor = np.mean([model.similarity(kelime, h) for h in hedefler if h in model])
            yasak_skor = np.mean([model.similarity(kelime, y) for y in yasaklar if y in model])
            toplam_skor = hedef_skor - yasak_skor
            if toplam_skor > en_iyi_skor:
                en_iyi_skor = toplam_skor
                en_iyi_ipucu = kelime
        except KeyError:
            continue

    return en_iyi_ipucu

# 🧠 Word2Vec modeli yükle (ilk seferde indirir)
@st.cache_resource
def load_model():
    return api.load("word2vec-google-news-300")

model = load_model()

# 🎯 Uygulama Başlığı
st.title("🧠 Codenames AI Assistant")
st.subheader("💡 Yapay Zeka ile Stratejik İpucu Önerici")

# 🎯 Girdiler
hedef_input = st.text_input("🎯 Hedef kelimeler (virgülle ayırın)", "dog, cat, fish")
yasak_input = st.text_input("⛔ Yasaklı kelimeler (virgülle ayırın)", "bomb, knife, gun")

# Buton
if st.button("🔍 En iyi ipucuyu öner"):
    hedefler = [w.strip().lower() for w in hedef_input.split(",")]
    yasaklar = [w.strip().lower() for w in yasak_input.split(",")]

    ipucu = oner_ipucu(hedefler, yasaklar, model)
    if ipucu:
        st.success(f"🎯 Önerilen İpucu: **{ipucu}**")
    else:
        st.error("Uygun ipucu bulunamadı. Kelimeleri kontrol edin.")
