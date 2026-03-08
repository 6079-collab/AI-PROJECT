import google.generativeai as genai

genai.configure(api_key="AIzaSyB7pM4TxJjkaG2imh-ZaUX6nnm1xplWCtg")

models = genai.list_models()

for m in models:
    if "generateContent" in m.supported_generation_methods:
        print(m.name)