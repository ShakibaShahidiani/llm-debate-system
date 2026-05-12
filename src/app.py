import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(__file__))

from main import debate
from database import get_all_debates
from datetime import timedelta

st.set_page_config(
    page_title="LLM Debate System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 LLM Debate System")
st.subheader("Ask a question and watch AI agents debate it from different perspectives")

st.divider()

# --- Sidebar ---
st.sidebar.header("⚙️ Configuration")

models = [
    "groq/llama-3.1-8b-instant",
    "groq/llama-3.3-70b-versatile",
    "groq/meta-llama/llama-4-scout-17b-16e-instruct"
]

persona1 = st.sidebar.text_area(
    "Agent 1 Persona",
    value="You are an optimistic agent. Always highlight the positive sides of any topic."
)
persona2 = st.sidebar.text_area(
    "Agent 2 Persona",
    value="You are a critical agent. Always challenge ideas and highlight risks."
)
persona3 = st.sidebar.text_area(
    "Agent 3 Persona",
    value="You are a neutral agent. Always provide balanced and objective perspectives."
)

personas = [persona1, persona2, persona3]

# --- Main Area ---
question = st.text_input(
    "💬 Enter your question:",
    placeholder="e.g. Should artificial intelligence replace human doctors?"
)

if st.button("🚀 Start Debate", type="primary"):
    if not question:
        st.warning("Please enter a question first!")
    else:
        with st.spinner("Debate in progress..."):
            try:
                conversation_history, final_answer = debate(
                    question=question,
                    models=models,
                    personas=personas
                )

                st.success("Debate completed!")
                st.divider()
                st.subheader("📋 Final Answer")
                st.markdown(final_answer)

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")

st.divider()

# --- Debate History ---
st.subheader("📚 Past Debates")

debates = get_all_debates()

if not debates:
    st.info("No debates yet. Ask your first question above!")
else:
    for d in reversed(debates):
        with st.expander(f"❓ {d.question} — {(d.created_at + timedelta(hours=2)).strftime('%Y-%m-%d %H:%M')}"):
            st.markdown(d.final_answer)
            st.caption(f"Rounds: {d.num_rounds} | Models: {d.models}")