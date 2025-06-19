import streamlit as st
import pandas as pd

st.set_page_config(page_title="وصفلي - توليد وصف المنتجات", layout="centered")

st.title("🧠 وصفلي")
st.subheader("أدخل رابط Google Sheet، واحصل على وصف عربي احترافي للمنتجات من الصور")

# 📥 إدخال رابط Google Sheet
sheet_url = st.text_input("📎 أدخل رابط Google Sheet فيه روابط الصور (عمود Image_URL)")

# زر توليد
if st.button("✅ توليد الأوصاف"):
    if sheet_url:
        # تحويل الرابط لـ CSV
        csv_url = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=")
        
        try:
            df = pd.read_csv(csv_url)
            st.success("✅ تم قراءة الشيت بنجاح!")
            
            # 👇 هنا بنعرض مثال مؤقت (ممكن تربطه بعدين بـ GPT)
            df["الوصف"] = "مثال: هذا منتج رائع مصنوع بجودة عالية."
            st.dataframe(df)

            # زر تنزيل وهمي للآن
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 تحميل النتائج (CSV)",
                data=csv,
                file_name='منتجات_بوصف.csv',
                mime='text/csv',
            )

        except Exception as e:
            st.error(f"❌ حدث خطأ أثناء قراءة الملف: {e}")
    else:
        st.warning("يرجى إدخال رابط Google Sheet أولاً.")
