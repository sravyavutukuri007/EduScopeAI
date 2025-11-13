import streamlit as st
import pandas as pd
from eduscope.data import load_dataset
from eduscope.parser import run_query

# -------------------------------
# Page setup
# -------------------------------
st.set_page_config(page_title="EduScope AI", layout="wide")
st.title("🎓 EduScope AI — Natural Language Query System")

st.markdown(
    """
    This demo lets **admins** query student performance and homework data using plain English.  
    Access is limited to their assigned **grade** and **class**.
    """
)

# -------------------------------
# Admin login simulation
# -------------------------------
st.sidebar.header("🔐 Admin Access")
admin_grade = st.sidebar.selectbox("Select your grade", [7, 8, 9], index=1)
admin_class = st.sidebar.selectbox("Select your class", ["A", "B", "C"], index=0)

st.sidebar.success(f"Access granted for Grade {admin_grade} - Class {admin_class}")

# -------------------------------
# Load dataset
# -------------------------------
df = load_dataset()
st.subheader("📋 Available Data (for reference)")
st.dataframe(df.head())

# -------------------------------
# Query input
# -------------------------------
st.markdown("### 💬 Ask your question below:")
query = st.text_input(
    "Example: 'Which students haven’t submitted their homework yet?'",
    placeholder="Type your question here..."
)

# -------------------------------
# Run query
# -------------------------------
if st.button("Run Query"):
    if query.strip():
        with st.spinner("Processing your query..."):
            result = run_query(df, query, admin_grade=admin_grade, admin_class=admin_class)
        st.success("Query processed successfully!")

        if isinstance(result, pd.DataFrame):
            st.dataframe(result)
        else:
            st.warning(result)
    else:
        st.warning("Please enter a valid query.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and LangChain | Dumroo.ai Assessment Project")
