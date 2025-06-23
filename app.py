import streamlit as st
from responder import my_gpt

st.title("Humanize your text")

user_input = st.text_area("Paste your Arabic text:", height=200)


if st.button("Adapt"):
    if user_input.strip() == "":
        st.warning("Please enter your text.")
    
    else:
        prompt = f"""
Your task is to rewrite the text between the brackets in a simple written style using only Classical Standard Arabic (Fus'ha).
You must never use Arabic dialect like Egyptian, Levantine (Syrian, Lebanese, Palestinian, Jordanian), Gulf, Iraqi,
Maghrebi (Moroccan, Algerian, Tunisian, Libyan), Sudanese, Yemeni, or any other spoken variant.
You must never use any dialectal expression (e.g., 'بيكون', 'مو', 'صار', 'عشان', etc.).

You must rewrite the text as if it were written by a high school student with average academic skills — not advanced, not polished.
Do not use complex language. Use short, simple sentences and basic vocabulary that a student might use.
Include minor grammar issues or awkward phrasing, as long as the meaning is clear and the Arabic remains classical, meaning written Arabic and not spoken.

Do not summarize, do not shorten, and do not remove or merge any idea. Every sentence and idea from the original must appear in the rewritten version.
You are not allowed to ignore or compress content. Your task is to rewrite it, not to improve or clean it.
The text between brackets is:
[{user_input}]
"""

        answer = my_gpt(prompt)

        st.markdown("### Answer:")
        st.markdown(
    f"<div dir='rtl' style='text-align: right; font-size: 20px;'>{answer}</div>",
    unsafe_allow_html=True
)
        st.markdown("---")