import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="🚀 وصفلي - توليد وصف منتجات تلقائي", layout="centered")

# CSS لتنسيق RTL وخط جميل
st.markdown("""
    <style>
    body, .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
        background-color: #F9FAFC;
    }
    .step {
        background-color: #ffffff;
        padding: 1.2em;
        border-radius: 10px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
        margin-bottom: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان جذاب
st.title("🧠 وصفلي - توليد وصف المنتجات تلقائيًا من الصور")
st.markdown("### ✨ جرب الأداة مجانًا لأول 20 منتج")

# ✅ قسم شرح الفكرة بخطوات بصريّة
st.markdown("## 📋 كيف تعمل وصفلي؟")

st.markdown("""
<div class="step">
<h4>📸 1. جهّز الصور</h4>
<p>ضع روابط صور منتجاتك في Google Sheet في عمود اسمه <code>Image_URL</code>.</p>
</div>
<div class="step">
<h4>🔗 2. انسخ رابط الشيت</h4>
<p>افتح Google Sheet واختر <strong>Anyone with the link can view</strong> وانسخ الرابط.</p>
</div>
<div class="step">
<h4>⚙️ 3. لصق الرابط هنا</h4>
<p>الصق الرابط في الحقل أدناه، وسيتم توليد وصف عربي احترافي تلقائيًا.</p>
</div>
<div class="step">
<h4>📥 4. تحميل النتيجة</h4>
<p>نمنحك ملف CSV يحتوي على الأوصاف الجاهزة للنشر على متجرك.</p>
</div>
""", unsafe_allow_html=True)

# ✅ المميزات داخل expander
with st.expander("🛠 مميزات وصفلي"):
    st.markdown("""
- توليد وصف تلقائي من الصور 🎯  
- دعم اللغة العربية الفصحى واللهجات ✍️  
- جاهز للتكامل مع Shopify وWooCommerce وJumia ونون ⚡️  
- لا يتطلب تسجيل أو بطاقة ائتمان 🔒  
- نسخة تجريبية حتى 20 منتج ✅  
    """)

# 🧪 تجربة الأداة
st.markdown("## 🚀 جربها الآن (نسخة تجريبية)")

sheet_url = st.text_input("📎 الصق هنا رابط Google Sheet (يحتوي على عمود Image_URL):")

if st.button("✅ توليد الأوصاف"):
    if sheet_url:
        try:
            # تحويل للرابط القابل للتنزيل
            csv_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
            df = pd.read_csv(csv_url)

            if "Image_URL" not in df.columns:
                st.error("❌ لم يتم العثور على العمود 'Image_URL' في الشيت.")
            else:
                if len(df) > 20:
                    st.warning("⚠️ النسخة المجانية تدعم حتى 20 صورة فقط. سيتم توليد أوصاف لأول 20.")
                    df = df.head(20)

                st.info("⏳ جاري توليد أوصاف تجريبية...")

                # توليد وصف وهمي (تجريبي)
                df["الوصف"] = df["Image_URL"].apply(lambda url: "مثال: منتج فاخر بتصميم عصري وجودة عالية.")

                st.success("✅ تم توليد الأوصاف بنجاح!")
                st.dataframe(df)

                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="📥 تحميل ملف CSV",
                    data=csv,
                    file_name='wasfaly_sample.csv',
                    mime='text/csv',
                )

        except Exception as e:
            st.error(f"❌ حدث خطأ أثناء معالجة الرابط: {e}")
    else:
        st.warning("⚠️ الرجاء إدخال الرابط أولاً.")
