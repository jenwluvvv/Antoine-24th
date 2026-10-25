# Antoine's Level 24 Birthday Quest 💙

A Python + Streamlit birthday website for Antoine. No Vercel required.

## Run it on your computer

1. Install Python 3.10 or newer from https://www.python.org/downloads/
2. Open Terminal (Mac) or Command Prompt / PowerShell (Windows).
3. Move into this folder:
   `cd path/to/antoine_level_24`
4. Install the dependencies:
   `python -m pip install -r requirements.txt`
5. Start the website:
   `python -m streamlit run app.py`
6. It should open in your browser. If it doesn't, visit http://localhost:8501

## AI birthday note (optional)

The app runs without AI. To generate a personalized note:

1. Get an API key from Google AI Studio: https://aistudio.google.com/apikey
2. Open the **Love note** tab in the app.
3. Enter your memory or inside joke and paste the API key into the optional password field.
4. Press **Write my birthday note**.

The key is not saved by this app. API availability, free-tier limits, and model names can change. Don't publish a real API key in your code or share it with anyone.

## Share with Antoine for free

For a shareable website, you can deploy this project using Streamlit Community Cloud:
1. Create a GitHub account and a new repository.
2. Upload `app.py` and `requirements.txt`.
3. Visit https://share.streamlit.io/ and connect the repository.
4. Deploy `app.py`.
5. Share the resulting `streamlit.app` link with Antoine.

For a public deployment, avoid asking visitors to paste their own API keys into a shared app. A safer production setup uses Streamlit secrets and server-side rate limiting. The current starter app is intended as a personal project, not a hardened public service.

## Photos, videos, and music

- Uploaded photos/videos are shown in the app session; they are not saved as a permanent shared album.
- Add your own audio file in the Welcome tab. The app does not include copyrighted music.
- If you want photos to persist across devices, add a storage service later.

## Contents

- `app.py`: the whole interactive birthday app
- `requirements.txt`: Python packages
