import streamlit as st
from prompt_improver import ConstructionPromptImprover

def main():
    st.set_page_config(
        page_title="Construction Claims Prompt Improver",
        page_icon="🏗️",
        layout="wide"
    )

    st.title("Construction Claims Prompt Improver")
    st.write("""
    This tool helps improve raw construction claim prompts into well-structured, 
    legally-sound queries suitable for LLMs.
    """)

    # Initialize the prompt improver
    improver = ConstructionPromptImprover()

    # Input text area
    raw_prompt = st.text_area(
        "Enter your construction claim prompt:",
        height=100,
        placeholder="e.g., eot due to material delay. how to justify?"
    )

    if st.button("Improve Prompt"):
        if raw_prompt:
            with st.spinner("Improving your prompt..."):
                improved_prompt = improver.improve_prompt(raw_prompt)
                st.success("Prompt improved successfully!")
                st.text_area("Improved Prompt:", value=improved_prompt, height=200)
        else:
            st.warning("Please enter a prompt to improve.")

    # Example section
    with st.expander("See example prompts"):
        st.markdown("""
        **Example 1:**
        - Raw: eot due to material delay. how to justify?
        - Improved: Please generate a formal justification for an Extension of Time (EOT) claim caused by delays in material delivery. Include contractual references, time impact analysis, and explanation of entitlement.

        **Example 2:**
        - Raw: client not paying for variation works
        - Improved: Please provide guidance on preparing a payment claim for variation works, including: 1) Relevant contract clauses for variations, 2) Required documentation for work verification, 3) Proper valuation methodology, and 4) Notice requirements under the contract.
        """)

if __name__ == "__main__":
    main()