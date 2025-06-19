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
    </style>
""", unsafe_allow_html=True)

# ✅ Hero Section
st.markdown("""
<div class="hero">
    <h1>وصفلي</h1>
    <p><span style='color:#004d7a;'>حوّل روابط صور منتجاتك</span> إلى وصف احترافي باللغة العربية في دقائق.</p>
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

# ✅ ما هو وصفلي؟ (داخل Expander)
with st.expander("ما هي وصفلي؟"):
    st.markdown("""
    <p><strong>وصفلي</strong> هي أداة ذكية تساعدك على توليد وصف منتجات <span style='color:#0072b5;'>عربي تلقائي</span> بالاعتماد على الصور فقط، لتوفير وقتك وجهدك في كتابة المحتوى، ورفع جودة متجرك.</p>
    """, unsafe_allow_html=True)

# ✅ المميزات
st.markdown("""
<div class="section">
<h3>مميزات الأداة:</h3>
<ul>
<li>وصف احترافي باللغة العربية (فصحى ولهجات)</li>
<li>لا حاجة لكتابة أو تحرير يدوي</li>
<li>سريع ويدعم حتى 1000 منتج في النسخ المدفوعة</li>
<li>يدعم المتاجر الإلكترونية: Shopify, WooCommerce, Jumia, Noon</li>
<li>نتائج قابلة للتنزيل فورًا</li>
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
اجعل صلاحية الوصول "Anyone with the link can view".
</div>
<div class='step-box'>
<b>3. الصق الرابط</b><br>
في الحقل بالأعلى، ثم اضغط على "ابدأ التوليد".
</div>
<div class='step-box'>
<b>4. حمّل الملف الناتج</b><br>
CSV يحتوي على وصف تلقائي وجاهز للنشر.
</div>
</div>
""", unsafe_allow_html=True)

# ✅ CTA إضافي
st.markdown("""
<div class="section" style="text-align: center;">
<p>هل لديك أكثر من 1000 منتج أو ترغب في دمج الأداة داخل موقعك؟</p>
<a href="#" style="color: #0066cc; font-weight: bold;">تواصل معنا الآن</a>
</div>
""", unsafe_allow_html=True)

# ✅ أيقونات التواصل الاجتماعي
st.markdown("""
<div class="social-icons">
    <a href="https://wa.me/966500000000" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" alt="واتساب"></a>
    <a href="https://twitter.com" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="تويتر"></a>
    <a href="https://facebook.com" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="فيسبوك"></a>
</div>
""", unsafe_allow_html=True)

# ✅ Footer
st.markdown("""
<div class="footer">
<p>© 2025 وصفلي - جميع الحقوق محفوظة</p>
</div>
""", unsafe_allow_html=True) 

# ✅ صفحة الأسعار (جديدة)
st.markdown("""
<div class="section">
<h3>خطط الأسعار:</h3>
<ul>
<li><b>الخطة المجانية:</b> حتى 20 رابط صورة - تجربة مباشرة بدون تسجيل</li>
<li><b>خطة المحترفين:</b> 1000 رابط شهريًا - 39 دولار</li>
<li><b>خطة الشركات:</b> API مخصص وتكامل مباشر - حسب الطلب</li>
</ul>
</div>
""", unsafe_allow_html=True)
