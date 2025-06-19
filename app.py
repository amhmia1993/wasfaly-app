import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="وصفلي - توليد وصف منتجات", layout="centered")

# تنسيق CSS للواجهة
st.markdown("""
    <style>
    html, body, .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
        background-color: #f9f9f9;
    }
    .step-box {
        background-color: #ffffff;
        padding: 18px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ العنوان الرئيسي في الأعلى
st.title("🧠 وصفلي - توليد وصف منتجات تلقائي")

st.caption("جرب الأداة مجانًا حتى 20 صورة منتج")

# ✅ خانة إدخال الرابط في الأعلى
sheet_url = st.text_input("📎 أدخل رابط Google Sheet (يحتوي على عمود Image_URL):")

# ✅ زر التنفيذ
if st.button("ابدأ التوليد"):
    if sheet_url:
        try:
            csv_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
            df = pd.read_csv(csv_url)

            if "Image_URL" not in df.columns:
                st.error("لم يتم العثور على عمود Image_URL في الملف.")
            else:
                if len(df) > 20:
                    st.warning("النسخة المجانية تدعم حتى 20 صورة. سيتم استخدام أول 20.")
                    df = df.head(20)

                # توليد وصف مؤقت تجريبي
                df["الوصف"] = df["Image_URL"].apply(lambda url: "مثال: منتج عصري بجودة عالية ومناسب للبيع أونلاين.")

                st.success("تم توليد الأوصاف بنجاح")
                st.dataframe(df)

                # تحميل الملف
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button("تحميل الملف بصيغة CSV", csv, "wasfaly_output.csv", "text/csv")

        except Exception as e:
            st.error(f"حدث خطأ أثناء قراءة الملف: {e}")
    else:
        st.warning("يرجى إدخال رابط صحيح.")

# ⬇️ الشرح التفصيلي بعد الأداة
st.markdown("## خطوات الاستخدام")

st.markdown("""
<div class='step-box'>
<b>1. إعداد الصور:</b>  
أنشئ ملف Google Sheet يحتوي على عمود باسم <code>Image_URL</code> يتضمن روابط الصور.
</div>

<div class='step-box'>
<b>2. ضبط المشاركة:</b>  
غيّر إعدادات المشاركة في Google Sheet إلى "Anyone with the link can view".
</div>

<div class='step-box'>
<b>3. الصق الرابط هنا:</b>  
ضع رابط الشيت في الحقل بالأعلى واضغط "ابدأ التوليد".
</div>

<div class='step-box'>
<b>4. تحميل النتائج:</b>  
يمكنك تحميل الملف الناتج بصيغة CSV لاستخدامه مباشرة في متجرك.
</div>
""", unsafe_allow_html=True)

# ✅ المميزات
with st.expander("عرض مميزات الأداة"):
    st.markdown("""
- توليد وصف عربي احترافي مباشرة من صور المنتجات
- نسخة مجانية حتى 20 منتج لتجربة الأداة
- يدعم صيغة CSV الجاهزة للنشر
- لا حاجة لتسجيل أو بطاقة
- قابل للتكامل مع متاجر WooCommerce, Shopify, Jumia, Noon
    """)
