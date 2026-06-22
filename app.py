import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(page_title="TikTok Motivation Booster", page_icon="📈", layout="centered")

st.title("📈 TikTok Growth & Analytics Dashboard")
st.subheader("Break the 300-500 View Tier (Mindset & Motivation)")
st.write("Enter your video metrics below to diagnose your content faults and hit 1k-3k views.")

# --- SECTION 1: CONFIGURATION ---
st.sidebar.header("🔑 Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# --- SECTION 2: METRICS INPUT ---
st.header("📊 Video Performance Metrics")

views = st.number_input("Total Views", min_value=0, value=350, step=10)
duration = st.number_input("Video Duration (seconds)", min_value=1, value=15)
retention_3s = st.slider("3-Second Retention Rate (%)", min_value=0, max_value=100, value=35)
top_country = st.text_input("Top Audience Country", value="Sri Lanka")

# --- SECTION 3: SCRIPT INPUT ---
st.header("📝 Video Script & Audio Hook")
video_script = st.text_area(
    "Paste your exact video transcript or text-on-screen:",
    placeholder="Example: Read this if you feel like giving up today. If you want to change your life..."
)

# --- SECTION 4: AI DIAGNOSTIC ENGINE ---
if st.button("🚀 Analyze & Generate Strategy"):
    if not api_key:
        st.error("Please add your Gemini API Key in the sidebar to run the analysis.")
    elif not video_script:
        st.error("Please paste your video script so the AI can analyze your hook.")
    else:
        with st.spinner("Analyzing watch-time drop-offs and regional hooks..."):
            try:
                # Configure the AI engine
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.5-flash')
                
                diagnostic_prompt = f"Analyze this TikTok video stuck in view jail. Views: {views}, Length: {duration}s, 3s Retention: {retention_3s}%, Audience: {top_country}. Script: '{video_script}'. Provide a critical fault analysis, geographical hook adjustments to target global US/UK audiences, and rewrite a highly engaging 3-second hook."
                
                response = model.generate_content(diagnostic_prompt)
                
                st.success("🎯 Optimization Blueprint Ready!")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
