# app.py
import streamlit as st
from src.umai_framework import UMAI

st.title("UMAI - Universal AI Agent")

if st.button("Run UMAI"):
    umai = UMAI()
    st.write("Running UMAI...")

    st.write("### Text Output")
    text_output = umai.multimodal_agent.process_text("Explain AI.")
    st.write(text_output)

    st.write("### Optimization Result")
    optimization_result = umai.optimizer.optimize()
    st.write(optimization_result)

    st.write("### Generated Code")
    generated_code = umai.task_automator.generate_code("Write a Python function to calculate factorial.")
    st.code(generated_code, language="python")