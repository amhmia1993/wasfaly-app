import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="وصفلي - توليد وصف منتجات تلقائي", layout="centered")

# CSS لتصميم احترافي شامل وخلفية موحدة وحركات خفيفة
st.markdown("""
    <style>
    html, body, .stApp {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
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
    .highlight-box {
        background-color: #fff9db;
        border: 2px dashed #f7c948;
        padding: 20px;
        font-size: 1.1em;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Hero Section
st.markdown("""
<div class="hero">
    <h1>وصفلي</h1>
    <p>📷 حوّل روابط صور منتجاتك إلى وصف عربي احترافي وجاهز للنشر ✨</p>
</div>
""", unsafe_allow_html=True)

# ✅ إدخال رابط واضح داخل صندوق مميز
st.markdown("""
<div class="highlight-box">
<b>🔗 الصق هنا رابط Google Sheet الخاص بك (يحتوي على عمود Image_URL):</b>
</div>
""", unsafe_allow_html=True)

sheet_url = st.text_input("مثال: https://docs.google.com/spreadsheets/d/...")

if st.button("✅ ابدأ التوليد الآن"):
    if sheet_url:
        try:
            csv_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
            df = pd.read_csv(csv_url)

            if "Image_URL" not in df.columns:
                st.error("لم يتم العثور على عمود Image_URL.")
            else:
                if len(df) > 20:
                    st.warning("⚠️ النسخة المجانية تدعم حتى 20 صورة فقط. سيتم استخدام أول 20.")
                    df = df.head(20)

                df["الوصف"] = df["Image_URL"].apply(lambda url: "مثال: منتج عصري بجودة عالية مناسب للبيع أونلاين.")

                st.success("🎉 تم توليد الأوصاف بنجاح!")
                st.dataframe(df)

                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button("⬇️ تحميل النتيجة بصيغة CSV", csv, "wasfaly_output.csv", "text/csv")

        except Exception as e:
            st.error(f"حدث خطأ: {e}")
    else:
        st.warning("⚠️ يرجى إدخال رابط الشيت أولاً.")

# ✅ شرح تفاعلي للمنصة بإيموجي
st.markdown("""
<div class="section">
<h3>🎯 ما هي وصفلي؟</h3>
<p>🔥 وصفلي هي أداة ذكية تساعدك في:</p>
<ul>
<li>✍️ توليد وصف جذاب وفوري لأي منتج</li>
<li>⚡ تسريع رفع المنتجات في متجرك</li>
<li>🎯 تحسين تجربة المستخدم والمبيعات</li>
<li>🌍 دعم اللغة العربية (الفصحى + لهجات)</li>
<li>🧠 تعمل تلقائيًا من صور المنتجات فقط!</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ✅ المميزات
st.markdown("""
<div class="section">
<h3>🚀 مميزات الأداة:</h3>
<ul>
<li>بدون كتابة يدوية ✍️</li>
<li>دعم CSV مباشر 📦</li>
<li>تجربة مجانية ✅</li>
<li>دعم لغوي متعدد 🇸🇦🇪🇬</li>
<li>تكامل سهل مع Shopify, Jumia, Noon 🛒</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ✅ خطوات الاستخدام
st.markdown("""
<div class="section">
<h3>🛠️ خطوات الاستخدام:</h3>
<div class='step-box'>
<b>1️⃣ جهّز ملف Google Sheet</b><br>
يحتوي على روابط صور المنتجات في عمود <code>Image_URL</code>.
</div>
<div class='step-box'>
<b>2️⃣ فعّل المشاركة</b><br>
اجعل صلاحية الوصول "Anyone with the link can view".
</div>
<div class='step-box'>
<b>3️⃣ الصق الرابط</b><br>
في الحقل بالأعلى.
</div>
<div class='step-box'>
<b>4️⃣ استمتع بالنتيجة</b><br>
CSV يحتوي على وصف احترافي جاهز.
</div>
</div>
""", unsafe_allow_html=True)

# ✅ خطط الأسعار
st.markdown("""
<div class="section">
<h3>💰 خطط الأسعار:</h3>
<ul>
<li>🆓 <b>الخطة المجانية:</b> حتى 20 منتج – بدون تسجيل</li>
<li>💼 <b>خطة المحترفين:</b> حتى 1000 منتج شهريًا – 39 دولار</li>
<li>🏢 <b>خطة الشركات:</b> تكامل API مخصص – تواصل معنا</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ✅ وسائل التواصل
st.markdown("""
<div class="section">
<h3>📞 تواصل معنا</h3>
<p>لو عندك استفسار أو محتاج مساعدة؟ نحن جاهزون!</p>
<div class="social-icons">
    <a href="https://wa.me/201091514582" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" alt="واتساب"></a>
    <a href="https://twitter.com" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="تويتر"></a>
    <a href="https://facebook.com" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="فيسبوك"></a>
</div>
</div>
""", unsafe_allow_html=True)

# ✅ Footer
st.markdown("""
<div class="footer">
<p>© 2025 وصفلي - جميع الحقوق محفوظة</p>
</div>
""", unsafe_allow_html=True)
