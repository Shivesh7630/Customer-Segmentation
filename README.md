# 📊 Customer Segmentation Project

This project demonstrates **Customer Segmentation** using **KMeans Clustering** and **Principal Component Analysis (PCA)**.  
It also includes an interactive **Streamlit web app** that allows users to upload customer datasets and visualize segmentation.

---

## 📖 Project Description  

This project focuses on **Customer Segmentation** using advanced **Machine Learning techniques** such as **KMeans Clustering** and **Principal Component Analysis (PCA)**. Businesses today collect vast amounts of customer data, but understanding customer behavior and preferences requires effective segmentation strategies. This project provides both the analytical workflow in a **Jupyter Notebook** and an interactive **Streamlit web application** for real-time exploration and insights.  

The **Jupyter Notebook** (`Cutomer_segmentation.ipynb`) demonstrates the complete process of cleaning raw marketing data, performing feature engineering, scaling, dimensionality reduction using PCA, and training a KMeans clustering model. The trained models (`kmeans_model.pkl`, `scaler.pkl`, `pca.pkl`) are saved for reuse in the deployed application. This ensures consistency between experimentation and production environments.  

The **Streamlit application** (`app.py`) allows users to upload their own customer datasets in CSV format. The app automatically preprocesses the data with the same scaler and PCA models used during training, applies clustering with the pre-trained KMeans model, and categorizes customers into meaningful groups such as:  

- **Luxury Spenders**  
- **Budget-Conscious Shoppers**  
- **Loyal Families**  
- **Occasional Discount Hunters**  

In addition to tabular results, the app also provides a **2D visualization** of customer clusters using PCA projections, making it easy to interpret the segments. Users can preview the processed dataset, download the segmented results, and quickly generate insights without writing any code.  

This project highlights practical applications of unsupervised learning in marketing and business strategy. By identifying different types of customers, businesses can optimize their **marketing campaigns, product recommendations, loyalty programs, and pricing strategies**.  

The repository includes:  
- **Datasets** (raw and cleaned versions)  
- **Notebook** for training and experimentation  
- **Pre-trained ML models** for clustering  
- **Streamlit app** for real-time segmentation  
- **requirements.txt** for easy setup  
- **.gitignore** for clean version control  

Overall, this project serves as a complete, end-to-end example of applying machine learning for customer analytics, combining research, reproducibility, and deployment into a single workflow.  

---

## 🚀 Features
- Upload customer data (CSV format).
- Automatic preprocessing with **Scaler** and **PCA**.
- Predict customer segments using a trained **KMeans model**.
- Interactive **2D cluster visualization**.
- Download segmented customer data.

---

## 🗂️ Project Structure
```
├── app.py                     # Streamlit app for interactive segmentation
├── Cutomer_segmentation.ipynb # Jupyter Notebook - data exploration & training
├── marketing_campaign.xlsx     # Raw dataset
├── marketing_campaign_cleaned.csv # Cleaned dataset
├── kmeans_model.pkl           # Trained KMeans model
├── pca.pkl                    # PCA transformation model
├── scaler.pkl                 # StandardScaler used for preprocessing
├── requirements.txt           # Project dependencies
├── .gitignore                 # Ignore unnecessary/large files
```

---

## ⚡ Installation & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Shivesh7630/Customer-Segmentation.git cd Customer-Segmentation

   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Upload your CSV file and explore the results! 🎉

---

## 🛠️ Development Notes
- **requirements.txt**: Lists all dependencies needed to run the project.  
- **.gitignore**: Ensures large or unnecessary files (datasets, pickle models, system files) are not pushed to GitHub.  

👉 If you want to share data or models, you can upload them separately (e.g., via Google Drive or Git LFS).

---

## 📌 Example Segments
The model categorizes customers into:
- **Luxury Spenders**  
- **Budget-Conscious Shoppers**  
- **Loyal Families**  
- **Occasional Discount Hunters**

---

## 📝 License
This project is open-source and available under the MIT License.

---
