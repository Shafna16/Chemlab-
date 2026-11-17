# MoleculeLab — Streamlit

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Create a GitHub repository and upload `app.py`, `requirements.txt`, and `README.md`.
2. Visit https://share.streamlit.io/ and sign in with GitHub.
3. Click **Create app**.
4. Select your repository, branch (usually `main`) and main file path `app.py`.
5. Click **Deploy**.

The 3D visualizer loads 3Dmol.js and structure data from PubChem, so it needs internet access.
