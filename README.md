---
title: "Codenames AI Assistant"
emoji: 🧠
colorFrom: blue
colorTo: red
sdk: streamlit
app_file: app.py
pinned: true
tags:
  - nlp
  - word2vec
  - strategy
  - ai
  - streamlit
  - game
license: mit
---

# 🧠 Codenames AI Assistant

Bu proje, **Codenames** oyununda hedef kelimelere en uygun **tek kelimelik ipucu**yu bulmaya çalışan bir yapay zeka strateji aracıdır.  
Word2Vec modeli ile anlamsal benzerlik hesaplanır, hedeflere yakın, yasaklara uzak en iyi kelime önerilir.

## 🔍 Kullanılan Teknikler

- Gensim ile önceden eğitilmiş `word2vec-google-news-300`
- Cosine benzerliği
- Stratejik kelime seçimi

## 🧩 Nasıl Çalışır?

- Hedef ve yasaklı kelimeleri gir
- AI, en alakalı ve güvenli kelimeyi önerir
- Model eğitimi yoktur (hazır embedding kullanılır)

## 🧠 Örnek

```python
hedefler = ["dog", "cat", "fish"]
yasaklar = ["bomb", "knife", "gun"]
ipucu = oner_ipucu(hedefler, yasaklar, model)
print(ipucu)  # animal gibi bir sonuç dönebilir
