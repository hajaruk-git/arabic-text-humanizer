import streamlit as st
from responder import my_gpt

st.title("Humanize your text")

user_input = st.text_area("Paste your Arabic text:", height=200)


if st.button("Adapt"):
    if user_input.strip() == "":
        st.warning("Please enter your text.")
    
    else:
        prompt = f"""
أعد صياغة النص الموجود بين القوسين بأسلوب طالب في المرحلة الثانوية، مستواه عادي وليس ممتازًا.

اكتب فقط باللغة العربية الفصحى البسيطة والواضحة. لا تستخدم أي لهجة محكية أو كلمات غير فصيحة.

تجنب الأسلوب الأكاديمي أو اللغة المعقدة. استخدم جُملاً قصيرة وكلمات مألوفة لطلاب المدارس.

لا تكتب النص بشكل مثالي. اجعله يبدو كأنه كُتب من طرف طالب عادي: يُسمح بوجود بعض التراكيب البسيطة أو التعابير غير المتقنة، ما دام المعنى واضحًا.

لا تختصر ولا تحذف أي فكرة من النص الأصلي. فقط أعد كتابته بأسلوب أقل رسمية، أبسط، وأقرب لما يكتبه الطلاب فعلاً.

ولا تستخدم أبدًا كلمات أو تعابير من اللهجات، حتى وإن كانت شائعة.

النص بين القوسين هو:
[{user_input}]
"""




        answer = my_gpt(prompt)

        st.markdown("### Answer:")
        st.markdown(
    f"<div dir='rtl' style='text-align: right; font-size: 20px;'>{answer}</div>",
    unsafe_allow_html=True
)