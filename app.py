import streamlit as st
from optimizer import optimize_prompt
from analyzer import analyze_prompt

st.set_page_config(
    page_title="PromptCraft AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 PromptCraft AI")
st.caption("Transform ordinary prompts into professional AI prompts.")

st.divider()

# -----------------------------
# LEFT COLUMN
# -----------------------------
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

    user_prompt = st.text_area(
        "Enter your prompt",
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

            st.metric("📊 Prompt Score", f"{score}/100")

            if issues:
                st.warning("Suggestions for improvement:")

                for issue in issues:
                    st.write(f"• {issue}")

            # Optimize prompt
            with st.spinner("Optimizing your prompt..."):

                optimized = optimize_prompt(
                    user_prompt,
                    category,
                    tone,
                    length
                )

            st.success("✅ Prompt optimized successfully!")

            st.code(
                optimized,
                language="text"
            )