import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="وصفلي - توليد وصف منتجات تلقائي", layout="centered")

# CSS لتصميم احترافي وخطوط متناسقة
st.markdown("""
    <style>
    html, body, .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
        background-color: #f9f9f9;
    }
    .section {
        padding: 2em 1em;
        margin-bottom: 2em;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .hero {
        text-align: center;
        padding: 3em 1em 2em;
    }
    .hero h1 {
        font-size: 2.5em;
        color: #333;
    }
    .hero p {
        font-size: 1.2em;
        color: #666;
        margin-top: 0.5em;
    }
    .step-box {
        background-color: #f1f1f1;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Hero Section
st.markdown("""
<div class="hero">
    <h1>وصفلي</h1>
    <p>حوّل روابط صور منتجاتك إلى وصف احترافي باللغة العربية في دقائق.</p>
</div>
""", unsafe_allow_html=True)

# ✅ تجربة الأداة المباشرة (CTA رئيسي)
st.markdown("### جرب الأداة مجانًا حتى 20 منتج")
sheet_url = st.text_input("رابط Google Sheet يحتوي على عمود Image_URL:")

if st.button("ابدأ التوليد"):
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

# ✅ ما هو وصفلي؟
st.markdown("""
<div class="section">
<h3>ما هي وصفلي؟</h3>
<p>وصفلي هي أداة ذكية تساعدك على توليد وصف منتجات عربي تلقائي بالاعتماد على الصور فقط، لتوفير وقتك وجهدك في كتابة المحتوى.</p>
</div>
""", unsafe_allow_html=True)

# ✅ المميزات
st.markdown("""
<div class="section">
<h3>مميزات الأداة:</h3>
<ul>
<li>وصف احترافي باللغة العربية</li>
<li>لا حاجة لكتابة أي شيء يدويًا</li>
<li>دعم للفصحى ولهجات السوق الخليجي والمصري</li>
<li>نتائج فورية بصيغة CSV</li>
<li>نسخة تجريبية مجانية حتى 20 منتج</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ✅ خطوات الاستخدام
st.markdown("""
<div class="section">
<h3>خطوات الاستخدام:</h3>
<div class='step-box'>
<b>1. جهّز ملف Google Sheet</b><br>
ضع فيه روابط صور المنتجات في عمود باسم <code>Image_URL</code>.
</div>
<div class='step-box'>
<b>2. فعّل المشاركة العامة</b><br>
اضبط الشيت على "Anyone with the link can view".
</div>
<div class='step-box'>
<b>3. الصق الرابط في الأعلى</b><br>
وأضغط على "ابدأ التوليد".
</div>
<div class='step-box'>
<b>4. حمّل الملف الناتج</b><br>
CSV يحتوي على وصف تلقائي لكل منتج.
</div>
</div>
""", unsafe_allow_html=True)

# ✅ CTA إضافي
st.markdown("""
<div class="section" style="text-align: center;">
<p>هل تريد توليد أوصاف لأكثر من 20 منتج؟ أو دمج الأداة مع متجرك؟</p>
<a href="#" style="color: #0066cc; font-weight: bold;">تواصل معنا</a>
</div>
""", unsafe_allow_html=True)
