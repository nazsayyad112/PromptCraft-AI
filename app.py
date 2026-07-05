import streamlit as st
import streamlit.components.v1 as components
from optimizer import optimize_prompt
from analyzer import analyze_prompt
from prompt_templates import PROMPT_TEMPLATE
from template_library import TEMPLATES

st.set_page_config(
    page_title="PromptCraft AI",
    page_icon="🤖",
    layout="wide"
)

with open("assets/styles.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.title("🤖 PromptCraft AI")
st.caption("Transform ordinary prompts into professional AI prompts.")

st.divider()
if "history" not in st.session_state:
    st.session_state.history = []
if "selected_template" not in st.session_state:
        st.session_state.selected_template = ""

# -----------------------------
# LEFT COLUMN
# -----------------------------
with st.sidebar:
    st.header("📜 Prompt History")

    if st.session_state.history:
        for i, prompt in enumerate(st.session_state.history, start=1):
            st.write(f"{i}. {prompt}")
    else:
        st.info("No prompts yet.")
col1, col2 = st.columns(2)

with col1:

    st.subheader("Input")

    category = st.selectbox(
        "Category",
        [
            "General",
            "Coding",
            "Research",
            "Study",
            "Resume",
            "Marketing",
            "Content Writing"
        ]
    )

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Creative",
            "Friendly",
            "Academic"
        ]
    )

    length = st.selectbox(
        "Output Length",
        [
            "Short",
            "Medium",
            "Detailed"
        ]
    )
    selected_template = st.selectbox(
        "📚 Choose a Prompt Template",
        ["None"] + list(TEMPLATES.keys())
    )

    if selected_template != "None":
        st.session_state.selected_template = TEMPLATES[selected_template]
        
    user_prompt = st.text_area(
    "Enter your prompt",
    value=st.session_state.selected_template,
    height=200,
    placeholder="Example: Explain Artificial Intelligence"
    )

    optimize = st.button(
        "✨ Optimize Prompt",
        use_container_width=True
    )

# -----------------------------
# RIGHT COLUMN
# -----------------------------
with col2:

    st.subheader("Optimized Prompt")

    if optimize:

        if user_prompt.strip() == "":
            st.warning("Please enter a prompt.")

        else:

            # Analyze prompt
            score, issues = analyze_prompt(user_prompt)

            st.metric("Prompt Score", f"{score}/100")

            st.progress(score / 100)

            if score >= 80:
                st.success("🟢 Excellent prompt!")

            elif score >= 60:
                st.info("🟡 Good prompt. A few improvements can make it even better.")

            else:
                st.error("🔴 Weak prompt. Consider the suggestions below.")

            if issues:
                st.warning("Suggestions for improvement:")

                for issue in issues:
                    st.write("•", issue)

            # Optimize prompt
            with st.spinner("Optimizing your prompt..."):

                optimized = optimize_prompt(
                    user_prompt,
                    category,
                    tone,
                    length
                )

            st.success("✅ Prompt optimized successfully!")
            st.session_state.history.insert(0, user_prompt)

            
            st.code(optimized, language="text")

            copy_html = f"""
            <button onclick="navigator.clipboard.writeText(`{optimized}`)"
            style="
            background-color:#4CAF50;
            color:white;
            padding:10px 20px;
            border:none;
            border-radius:8px;
            cursor:pointer;
            font-size:16px;">
            📋 Copy Prompt
            </button>
            """

            components.html(copy_html, height=60)

            st.download_button(
                label="📥 Download Prompt",
                data=optimized,
                file_name="optimized_prompt.txt",
                mime="text/plain",
                use_container_width=True
            )
                