import streamlit as st
import google.generativeai as genai

# Page configuration for a clean mobile & desktop layout
st.set_page_config(page_title="TikTok Motivation Booster", page_icon="📈", layout="centered")

st.title("📈 TikTok Growth & Analytics Dashboard")
st.subheader("Break the 300-500 View Tier (Mindset & Motivation)")
st.write("Enter your video metrics below to diagnose your content faults and hit 1k-3k views.")

# --- SECTION 1: CONFIGURATION ---
st.sidebar.header("🔑 Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# --- SECTION 2: METRICS INPUT ---
st.header("📊 Video Performance Metrics")

col1, col2 = st.columns(2)
with col1:
views = st.number_input("Total Views", min_value=0, value=350, step=10)
duration = st.number_input("Video Duration (seconds)", min_value=1, value=15)
with col2:
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

# Expert prompt engineering tailored to short-form content scaling
diagnostic_prompt = f"""
You are an elite TikTok Growth Strategist specializing in the Mindset, Motivation, and Inspiration niche.
Analyze this video which is currently stuck in the 300-500 'view jail' tier.

METRICS TO EVALUATE:
- Total Views: {views}
- Video Length: {duration} seconds
- Retention at 3 Seconds: {retention_3s}%
- Primary Audience Location: {top_country}

VIDEO SCRIPT:
"{video_script}"

Provide a highly actionable, brutal, and precise report containing:
1. CRITICAL FAULT: Why did the video stall? (Look closely if the 3s retention is less than 60%, or if the hook in the script is slow).
2. GEOGRAPHIC TUNING: The creator's main traffic is from {top_country}. How can they tweak their text/sounds to make this appeal globally (US/UK/Global) to instantly clear 1k-3k views?
3. THE REWRITE: Provide an exact, high-retention alternative hook (first 3 seconds) for this exact script.
"""

response = model.generate_content(diagnostic_prompt)

# Output results elegantly onto the dashboard
st.success("🎯 Optimization Blueprint Ready!")
st.markdown("---")
st.markdown(response.text)

except Exception as e:
st.error(f"An error occurred: {e}")
