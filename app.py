import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained KMeans model and scaler
with open("kmeans_model.pkl", "rb") as f:
    kmeans_model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("pca.pkl", "rb") as f:
    pca = pickle.load(f)

# Features used during training
features = [
    'Income', 'Age', 'Family_Size',
    'Total_Spending', 'Spending_per_person',
    'MntWines_Share', 'MntFruits_Share', 'MntMeatProducts_Share',
    'MntFishProducts_Share', 'MntSweetProducts_Share', 'MntGoldProds_Share',
    'Total_Accepted_Campaigns', 'Recency',
    'NumWebPurchases_Share', 'NumCatalogPurchases_Share', 'NumStorePurchases_Share',
    'NumWebVisitsMonth'
]

# Mapping clusters to meaningful customer categories (example – adjust as per your analysis)
cluster_labels = {
    0: "Luxury Spenders ",                 
    1: "Budget-Conscious Shoppers ",      
    2: "Loyal Families ",             
    3: "Occasional Discount Hunters "      
}

# Streamlit App
st.set_page_config(page_title="Customer Segmentation", page_icon="📊", layout="wide")

# Banner / Header
st.markdown("""
    <div style="background-color: #f5f9ff; padding: 15px; border-radius: 12px; text-align: center;">
        <h1 style="color: #2E86C1;">📊 Customer Segmentation Model</h1>
        <p style="color: #34495E; font-size: 18px;">
            Upload your Customer dataset and discover segmentataion of customers.<br>
            Gain insights into Nature and behaviour of Customers.
        </p>
    </div>
""", unsafe_allow_html=True)

# File Upload
uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader(" Preview of Uploaded Data")
    st.dataframe(df.head())

    # Check for missing features
    missing = [col for col in features if col not in df.columns]
    if missing:
        st.error(f"❌ Missing required features in uploaded dataset: {missing}")
    else:
        # Keep only the features used during training
        df_model = df[features]

        # Preprocessing
        X_scaled = scaler.transform(df_model)
        X_pca = pca.transform(X_scaled)

        # Predict clusters
        clusters = kmeans_model.predict(X_pca)
        df["Customer Segment"] = [cluster_labels[c] for c in clusters]

        # Show results
        st.subheader("📑 Customer Segmentation Results")
        st.dataframe(df.head(20))

        # Visualization
        st.subheader("📊 Cluster Visualization (PCA 2D Projection)")
        fig, ax = plt.subplots(figsize=(8,6))
        sns.scatterplot(
            x=X_pca[:,0], y=X_pca[:,1], hue=df["Customer Segment"],
            palette="Set2", s=60, ax=ax
        )
        ax.set_title("Customer Segments", fontsize=14)
        st.pyplot(fig)

        # Download segmented data
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Segmented Data", data=csv, file_name="customer_segments.csv", mime="text/csv")
else:
    st.info("👆 Please upload a CSV file to start segmentation.")
