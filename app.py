import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="وصفلي - توليد وصف منتجات تلقائي", layout="centered")

# CSS لتصميم احترافي شامل وخلفية موحدة وحركات خفيفة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri&display=swap');

    html, body, .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Amiri', serif;
        background-color: #f1f3f6;
    }
    .section {
        padding: 2em 1em;
        margin-bottom: 2em;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.07);
        transition: transform 0.2s ease;
    }
    .section:hover {
        transform: translateY(-3px);
    }
    .hero {
        text-align: center;
        padding: 3em 1em 2em;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.05);
        margin-bottom: 2em;
    }
    .hero h1 {
        font-size: 2.7em;
        color: #222;
    }
    .hero p {
        font-size: 1.2em;
        color: #666;
        margin-top: 0.5em;
    }
    .input-style label, .input-style input {
        font-size: 1.1em !important;
    }
    h3 {
        color: #004d7a;
    }
    ul li {
        color: #333;
        font-size: 1.05em;
    }
    .step-box {
        background-color: #e9eef4;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    a.social {
        text-decoration: none;
        margin: 0 10px;
        color: #ffffff;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        padding: 1em 0;
    }
    .social-icons {
        text-align: center;
        margin-top: 20px;
    }
    .social-icons img {
        width: 30px;
        margin: 0 10px;
        transition: transform 0.3s ease;
    }
    .social-icons img:hover {
        transform: scale(1.2);
    }
    .logo {
        width: 60px;
        display: block;
        margin: 0 auto 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Hero Section
st.markdown("""
<div class="hero">
    <img src="https://cdn-icons-png.flaticon.com/512/1006/1006540.png" class="logo" />
    <h1>وصفلي</h1>
    <p><span style='color:#004d7a;'>حوّل روابط صور منتجاتك</span> إلى وصف احترافي باللغة العربية في دقائق.</p>
</div>
""", unsafe_allow_html=True)

# ✅ تجربة الأداة المباشرة (CTA رئيسي)
st.markdown("### جرب الأداة مجانًا حتى 20 منتج")
with st.container():
    with st.form("wasfaly_form"):
        sheet_url = st.text_input("📄 أدخل رابط Google Sheet يحتوي على عمود Image_URL:", key="sheet_input")
        submitted = st.form_submit_button("ابدأ التوليد")

    if submitted:
        if sheet_url:
            try:
                csv_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
                df = pd.read_csv(csv_url)

                if "Image_URL" not in df.columns:
                    st.error("لم يتم العثور على عمود Image_URL.")
                else:
                    if len(df) > 20:
                        st.warning("النسخة المجانية تدعم حتى 20 صورة فقط. سيتم استخدام أول 20.")
                        df = df.head(20)

                    df["الوصف"] = df["Image_URL"].apply(lambda url: "مثال: منتج عصري بجودة عالية مناسب للبيع أونلاين.")

                    st.success("تم توليد الأوصاف بنجاح")
                    st.dataframe(df)

                    csv = df.to_csv(index=False).encode("utf-8")
                    st.download_button("تحميل النتيجة CSV", csv, "wasfaly_output.csv", "text/csv")

            except Exception as e:
                st.error(f"حدث خطأ: {e}")
        else:
            st.warning("يرجى إدخال رابط الشيت أولاً.")
