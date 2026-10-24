   import streamlit as st

st.set_page_config(page_title="TIMÔTEË DÃL AI TIMES", layout="wide")

st.title("TIMÔTEË DÃL AI TIMES")
st.subheader("Your AI News Portal")

st.write("Welcome CEO! Your app is now LIVE! 🚀")

st.success("App deployed successfully!")

# Add your news content here
if st.button("Refresh News"):
    st.balloons()
    st.write("Latest news loading...")