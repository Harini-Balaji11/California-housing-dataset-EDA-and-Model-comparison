import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="California Housing Demo", layout="centered")
st.title("California Housing — Interactive Demo")

@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
	try:
		data = fetch_california_housing(as_frame=True)
		return data.frame
	except Exception as e:
		st.error("Failed to load California Housing dataset. If this is on Streamlit Cloud, please retry in a minute or check app logs.")
		st.exception(e)
		return pd.DataFrame()

with st.spinner("Loading data..."):
	df = load_data()

if df.empty:
	st.stop()

st.write("Dataset shape:", df.shape)

feature = st.selectbox("Feature", [c for c in df.columns if c != "MedHouseVal"], index=0)
X = df[[feature]]
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

try:
	model = LinearRegression().fit(X_train_s, y_train)
	score = model.score(X_test_s, y_test)
except Exception as e:
	st.error("Model training failed. Try reloading the app or reducing data size.")
	st.exception(e)
	st.stop()

st.subheader("Baseline Linear Regression")
st.write(f"R² on holdout: {score:.3f}")

val = st.slider(f"Input {feature}", float(df[feature].min()), float(df[feature].max()), float(df[feature].median()))
val_df = pd.DataFrame({feature: [val]})
pred = model.predict(scaler.transform(val_df))[0]

st.metric("Predicted MedHouseVal ($100,000s)", f"{pred:.3f}")
