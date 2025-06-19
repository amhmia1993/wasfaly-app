import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="وصفلي - توليد وصف منتجات", layout="wide")

# 💅 CSS للتصميم الداكن والكتابة من اليمين لليسار
st.markdown("""
    <style>
    html, body, .stApp {
        direction: rtl;
        text-align: right;
        background-color: #111;
        color: #eee;
        font-family: 'Cairo', sans-serif;
    }
    h1, h2, h3, h4, h5, h6, p, label {
        color: #eee !important;
    }
    .step-box {
        background-color: #1a1a1a;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 12px;
        border: 1px solid #333;
    }
    .stTextInput > div > div > input {
        background-color: #222;
        color: #eee;
    }
    .stDownloadButton > button {
        background-color: #333;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان التطبيق
st.title("وصفلي")
st.subheader("توليد وصف منتجات عربي تلقائي من الصور")

# 🧱 خطوات الاستخدام
st.markdown("## خطوات الاستخدام")
st.markdown("""
<div class='step-box'>
<b>1. إعداد الصور:</b>  
ارفع صور منتجاتك على الإنترنت، وضع روابطها في ملف Google Sheet داخل عمود اسمه <code>Image_URL</code>.
</div>

<div class='step-box'>
<b>2. مشاركة الشيت:</b>  
اجعل صلاحية الشيت "Anyone with the link can view"، ثم انسخ الرابط.
</div>

<div class='step-box'>
<b>3. إدخال الرابط:</b>  
الصق رابط الشيت هنا داخل الأداة، وسيتم توليد أوصاف تلقائية لأول 20 منتج.
</div>

<div class='step-box'>
<b>4. تحميل النتيجة:</b>  
بعد التوليد، يمكنك تحميل ملف CSV يحتوي على الأوصاف بصيغة جاهزة للنسخ أو الاستخدام في متجرك.
</div>
""", unsafe_allow_html=True)

# 💡 نموذج تجربة
st.markdown("## تجربة الأداة")

sheet_url = st.text_input("رابط Google Sheet (يحتوي على عمود Image_URL):")

if st.button("ابدأ التوليد"):
    if sheet_url:
        try:
            csv_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
            df = pd.read_csv(csv_url)

            if "Image_URL" not in df.columns:
                st.error("الملف لا يحتوي على عمود باسم 'Image_URL'.")
            else:
                if len(df) > 20:
                    st.warning("النسخة التجريبية تدعم حتى 20 صورة فقط. تم معالجة أول 20.")
                    df = df.head(20)

                df["الوصف"] = df["Image_URL"].apply(
                    lambda url: "مثال: منتج عالي الجودة بتصميم عصري وملائم للتجارة الإلكترونية."
                )

                st.success("تم التوليد بنجاح.")
                st.dataframe(df)

                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="تحميل ملف CSV",
                    data=csv,
                    file_name='wasfaly_output.csv',
                    mime='text/csv',
                )

        except Exception as e:
            st.error(f"حدث خطأ أثناء قراءة الملف: {e}")
    else:
        st.warning("يرجى إدخال رابط Google Sheet أولاً.")

# ✅ مميزات الخدمة
st.markdown("## مميزات وصفلي")
st.markdown("""
- توليد وصف عربي احترافي مباشرة من الصور
- لا حاجة لخبرة في الكتابة أو المحتوى
- دعم للمتاجر على Shopify, WooCommerce, Jumia, Noon
- نتائج فورية جاهزة للنشر
- تجربة مجانية حتى 20 منتج
""")
