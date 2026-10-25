import os
import random
import streamlit as st

st.set_page_config(
    page_title="Antoine's Level 24 Birthday Quest 💙",
    page_icon="💙",
    layout="centered",
)

# -------------------- Theme --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&display=swap');
.stApp {
  background: radial-gradient(ellipse at top, #183d70 0%, #07152f 58%);
  color: #f5f8ff;
}
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1, h2, h3 { font-family: 'Playfair Display', Georgia, serif !important; }
.hero {
  padding: 2.3rem 1.2rem; text-align: center; border: 1px solid #36537c;
  border-radius: 24px; background: linear-gradient(145deg,#153662,#0a1a37 75%);
  margin-bottom: 1rem;
}
.eyebrow { letter-spacing: 2px; text-transform: uppercase; color: #9cc8ff; font-size: .72rem; font-weight: 700; }
.hero-title { font-family: 'Playfair Display', Georgia, serif; font-size: clamp(2.7rem, 8vw, 4.8rem); line-height: 1.06; margin: .8rem 0; }
.hero-title em { color: #9cc8ff; }
.muted { color: #b4c4df; }
.card {
  border: 1px solid #36537c; border-radius: 18px; padding: 1.1rem;
  background: linear-gradient(155deg,#11294c,#0b1a34); margin: .7rem 0;
}
.frame { background: #dce8ff; color: #11294c; border: 3px solid #b6cfff; outline: 3px solid #203e67; border-radius: 8px; padding: 10px; }
.frame-caption { text-align:center; font-size:.75rem; font-weight:700; letter-spacing:1px; padding:.45rem; }
.letter { border: 1px solid #739bd2; border-radius: 15px; padding: 1.25rem; background: linear-gradient(145deg,#1c3c68,#102443); line-height: 1.9; }
div.stButton > button {
  border-radius: 12px; border: 1px solid #739bd2; background: #172f54;
  color: #e4edff; min-height: 2.6rem;
}
div.stButton > button:hover { border-color: #b7d4ff; color: white; }
div[data-testid="stFormSubmitButton"] button, div.stButton button[kind="primary"] {
  background: linear-gradient(120deg,#dceaff,#8cbcff); color: #07152f; font-weight: 700; border: 0;
}
div[data-testid="stMetric"] { background:#1a365d; border:1px solid #36537c; padding:12px; border-radius:14px; }
.stTabs [data-baseweb="tab-list"] { gap: 5px; flex-wrap: wrap; }
.stTabs [data-baseweb="tab"] { background:#0c2040; border-radius:9px; padding:8px 12px; }
footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# -------------------- Session state --------------------
defaults = {
    "quiz_answers": {},
    "matched_pairs": [],
    "flipped_tiles": [],
    "fortune": "",
    "generated_note": "",
    "music_bytes": None,
    "music_name": "",
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

fortunes = [
    "A new adventure is waiting for you. Take the first step. ⭐",
    "Your next chapter will be worth the wait. 💙",
    "A little courage can unlock a whole new world. ⚔️",
    "Someone in Toronto is incredibly proud of you. 💌",
    "Your lucky number is 5. Your mission is to enjoy today! 🐆",
    "May your next year bring great stories, big wins, and peace. 🌙",
    "Legendary birthday reward: unlimited hugs when we reunite. 🎁",
    "Even an ocean apart, you are someone's favourite person. 🌊",
    "May your Level 24 be full of plot twists that turn out beautifully. ✨",
]
questions = [
    ("⚽ Liverpool", "What is Antoine's favourite football team?", ["Manchester City", "Liverpool", "Arsenal", "Chelsea"], 1, "You'll Never Walk Alone. ❤️"),
    ("📚 The Stormlight Archive", "Who wrote The Stormlight Archive?", ["J.R.R. Tolkien", "Brandon Sanderson", "George R.R. Martin", "Patrick Rothfuss"], 1, "A whole universe of adventures to explore!"),
    ("🎮 Brawl Stars", "What kind of challenge is this birthday quest?", ["A daily chore", "A ranked match", "A legendary birthday mission", "An exam"], 2, "Correct! Your reward is unlimited kisses. 💋"),
    ("🐆 Antoine trivia", "Which is Antoine's favourite animal?", ["Tiger", "Cheetah", "Wolf", "Panda"], 1, "Fast, beautiful, and one of a kind."),
    ("💙 A little detail", "What is Antoine's favourite number?", ["7", "10", "24", "5"], 3, "Number 5 unlocked! ⭐"),
    ("🎵 Our soundtrack", "Which song belongs on our birthday soundtrack?", ["Always — Daniel Caesar", "A random alarm", "Elevator music", "A football chant"], 0, "Always choosing you. 💙"),
    ("🌙 Anime corner", "Which pair are among Antoine's favourite anime?", ["Hunter x Hunter & Frieren", "Naruto & One Piece", "Bleach & Death Note", "Haikyuu!! & Blue Lock"], 0, "Anime night date idea unlocked!"),
    ("🧸 Tiny treasures", "Which little collectible does Antoine love?", ["Smiskis", "Snow globes", "Thimbles", "Marbles"], 0, "A tiny green friend for the collection. ✨"),
]

st.markdown("""
<div class="hero">
  <div style="font-size:1.5rem">✦ · ✧ · ✦ · ✧ · ✦</div>
  <div class="eyebrow">A VERY SPECIAL QUEST BEGINS</div>
  <div class="hero-title">Happy Birthday,<br><em>Antoine!</em></div>
  <p class="muted">One boy. Twenty-four years. A million reasons to be loved.<br>A little adventure made just for you.</p>
  <div style="display:inline-block;border:1px solid #719bd1;border-radius:30px;padding:7px 13px;letter-spacing:1px;font-size:.75rem">✦ BIRTHDAY QUEST #24 ✦</div>
  <p class="muted" style="font-size:.8rem;margin-top:1rem">Toronto ♡ Singapore · Together in our own little way</p>
</div>
""", unsafe_allow_html=True)

st.progress(1.0, text="💙 Your birthday universe is ready to explore")

tabs = st.tabs(["🏰 Welcome", "⭐ Trivia", "🀄 Mahjong", "📸 Album", "💌 Love note", "🎁 Finale"])

# -------------------- Welcome --------------------
with tabs[0]:
    st.markdown('<div class="eyebrow">YOUR MISSION, SHOULD YOU ACCEPT IT</div>', unsafe_allow_html=True)
    st.header("Welcome to Level 24 💙")
    st.write("Hey, birthday boy. Today, the universe is celebrating you. I made this little adventure to remind you of the things you love, the memories we share, and how very loved you are.")
    a, b, c = st.columns(3)
    a.metric("Years of you", "24")
    b.metric("Your lucky number", "5")
    c.metric("Reasons I love you", "∞")
    st.markdown('<div class="card"><h3>📜 Today’s quest log</h3><p>⚽ Test your football knowledge</p><p>🀄 Find the matching tiles</p><p>📸 Visit our memory gallery</p><p>💌 Create a personalized birthday letter</p><p>🎁 Unlock the final surprise</p></div>', unsafe_allow_html=True)
    st.subheader("🔮 Your birthday fortune")
    st.write("Tap for a tiny message from the universe, just for you.")
    if st.button("Reveal my fortune ✨", key="fortune_button"):
        st.session_state.fortune = random.choice(fortunes)
    if st.session_state.fortune:
        st.info(st.session_state.fortune)
    st.subheader("🎵 Our soundtrack")
    st.write("You can add an audio file you have permission to use, such as a personal instrumental version of “Always”.")
    audio = st.file_uploader("Choose an audio file", type=["mp3", "wav", "ogg", "m4a"], key="music_upload")
    if audio:
        st.audio(audio)
        st.caption(f"Now playing: {audio.name}")
    st.caption("For browser playback, press play. This app does not include the copyrighted song itself.")

# -------------------- Trivia --------------------
with tabs[1]:
    st.markdown('<div class="eyebrow">CHALLENGE 01 · KNOW YOURSELF</div>', unsafe_allow_html=True)
    st.header("The Antoine Quiz ⭐")
    st.write("How well does this birthday quest know its favourite human?")
    for i, (category, question, options, correct, fact) in enumerate(questions):
        with st.container(border=True):
            st.markdown(f"**{category} · {i+1}/{len(questions)}**")
            st.write(question)
            choice = st.radio("Choose your answer", options, key=f"quiz_{i}", index=None, label_visibility="collapsed")
            if st.button("Lock it in", key=f"lock_{i}"):
                st.session_state.quiz_answers[i] = options.index(choice) if choice is not None else -1
            if i in st.session_state.quiz_answers:
                selected = st.session_state.quiz_answers[i]
                if selected == correct:
                    st.success("✓ Correct! " + fact)
                elif selected == -1:
                    st.warning("Pick an answer first, then lock it in.")
                else:
                    st.info(f"The answer is **{options[correct]}**. {fact}")
    score = sum(1 for i, answer in st.session_state.quiz_answers.items() if answer == questions[i][3])
    st.metric("Your current score", f"{score}/{len(questions)}")
    if st.button("Reset quiz"):
        st.session_state.quiz_answers = {}
        st.rerun()

# -------------------- Mahjong memory game --------------------
with tabs[2]:
    st.markdown('<div class="eyebrow">CHALLENGE 02 · TILE MASTER</div>', unsafe_allow_html=True)
    st.header("Mahjong Memory 🀄")
    st.write("Find all five matching pairs. Tap two tiles at a time. This is a simple matching game inspired by tile games.")
    symbols = ["🌙", "⭐", "🐆", "💙", "5"]
    tiles = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    # Stable layout per session; shuffle once and keep the same order.
    if "tile_order" not in st.session_state:
        random.shuffle(tiles)
        st.session_state.tile_order = tiles
    grid = st.columns(5)
    for idx, tile in enumerate(st.session_state.tile_order):
        with grid[idx % 5]:
            if idx in st.session_state.matched_pairs:
                st.button(symbols[tile-1], key=f"tile_{idx}", disabled=True, use_container_width=True)
            elif idx in st.session_state.flipped_tiles:
                st.button(symbols[tile-1], key=f"tile_{idx}", disabled=True, use_container_width=True)
            else:
                if st.button("✦", key=f"tile_{idx}", use_container_width=True):
                    flipped = st.session_state.flipped_tiles
                    if len(flipped) < 2:
                        flipped.append(idx)
                    if len(flipped) == 2:
                        first, second = flipped
                        if st.session_state.tile_order[first] == st.session_state.tile_order[second]:
                            st.session_state.matched_pairs.extend([first, second])
                            st.session_state.flipped_tiles = []
                        else:
                            st.session_state.last_mismatch = True
                    st.rerun()
    if getattr(st.session_state, "last_mismatch", False):
        st.warning("Not a match yet! Press “Hide unmatched tiles” to keep playing.")
        if st.button("Hide unmatched tiles"):
            st.session_state.flipped_tiles = []
            st.session_state.last_mismatch = False
            st.rerun()
    st.write(f"Pairs found: {len(st.session_state.matched_pairs)//2}/5")
    if len(st.session_state.matched_pairs) == 10:
        st.success("🏆 Mahjong Master unlocked! You matched every pair.")
    if st.button("Restart tile game"):
        for key in ["matched_pairs", "flipped_tiles", "tile_order", "last_mismatch"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# -------------------- Photo album --------------------
with tabs[3]:
    st.markdown('<div class="eyebrow">CHAPTER 03 · OUR LITTLE UNIVERSE</div>', unsafe_allow_html=True)
    st.header("Memories across oceans 📸")
    st.write("Add your pictures and videos, silly screenshots, dates, and little moments you never want to forget.")
    st.markdown('<div class="frame"><div class="frame-caption">♡ OUR STORY ♡ · TORONTO × SINGAPORE · ♡</div><div style="text-align:center;padding:12px;color:#25466f">MY FAVOURITE PLACE IS WITH YOU 💙</div></div>', unsafe_allow_html=True)
    uploads = st.file_uploader("Choose photos and videos", type=["jpg", "jpeg", "png", "webp", "gif", "mp4", "mov", "webm"], accept_multiple_files=True, key="memories")
    if uploads:
        cols = st.columns(2)
        for i, file in enumerate(uploads):
            with cols[i % 2]:
                if file.type.startswith("image/"):
                    st.image(file, caption=f"♡ memory #{i+1} ♡", use_container_width=True)
                elif file.type.startswith("video/"):
                    st.video(file)
                    st.caption(f"♡ memory #{i+1} ♡")
    st.caption("Privacy note: these uploads are used for display in this app session. They are not automatically saved to a permanent shared album. On a hosted app, avoid uploading sensitive media unless you understand the host's storage and privacy settings.")
    with st.expander("💭 A few memory prompts"):
        st.write("• What's a moment with him that made you laugh uncontrollably?")
        st.write("• What tiny thing does he do that makes you feel loved?")
        st.write("• What's one future memory you're excited to make together?")
        st.write("• What's an inside joke that would make him smile instantly?")

# -------------------- AI birthday note --------------------
with tabs[4]:
    st.markdown('<div class="eyebrow">CHALLENGE 04 · A GIFT MADE OF WORDS</div>', unsafe_allow_html=True)
    st.header("One memory, one love note 💌")
    st.write("Enter a memory or inside joke and let AI turn it into a personalized birthday note for Antoine.")
    memory = st.text_area("Your memory or inside joke", placeholder="Remember when we... One thing I always laugh about is... Something I want you to know is...", max_chars=2500, height=170, key="memory_input")
    st.caption("This optional AI feature needs a Google Gemini API key. The app works without it; you can still write and copy a note manually.")
    api_key = st.text_input("Gemini API key (optional; not saved by this app)", type="password", help="Get a key from Google AI Studio. For a public deployment, use the host's secrets manager instead of entering a key into a shared app.")
    if st.button("✧ Write my birthday note", type="primary"):
        if not memory.strip():
            st.warning("Add a memory or inside joke first. 💙")
        elif not api_key.strip():
            st.warning("Add your Gemini API key to generate with AI, or use the manual note box below.")
        else:
            try:
                from google import genai
                client = genai.Client(api_key=api_key.strip())
                prompt = f"""
Write a sincere, warm, personal birthday note addressed to Antoine, who is turning 24.
He lives in Singapore and his girlfriend lives in Toronto; they are long-distance.
His favourite colour is blue, favourite number is 5, and he loves Liverpool football,
mahjong, Brawl Stars, Hunter x Hunter, Frieren, The Stormlight Archive by Brandon Sanderson,
Smiskis, Daniel Caesar's song Always, and cheetahs.
Use the memory below as the heart of the note. Aim for 150-220 words, natural and intimate.
You may use one or two relevant personal references, but don't force every detail in.
Do not invent events or facts. Return only the finished letter.

Memory or inside joke:
{memory.strip()}
"""
                response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                st.session_state.generated_note = response.text or "The model didn't return text. Please try again."
            except Exception as exc:
                st.error(f"Couldn't generate the note. Check your API key and try again. Details: {exc}")
    if st.session_state.generated_note:
        st.markdown('<div class="letter"><div class="eyebrow">A LITTLE LETTER FOR ANTOINE</div></div>', unsafe_allow_html=True)
        st.text_area("Your generated letter (you can edit it)", value=st.session_state.generated_note, height=260, key="editable_letter")
        st.caption("Tip: select and copy the letter above, then paste it into a card or message.")
    st.subheader("Or write one yourself")
    manual_note = st.text_area("Your own birthday message", placeholder="Happy 24th birthday, my love...", height=180, key="manual_note")
    if manual_note:
        st.download_button("Download my note as a text file", data=manual_note, file_name="antoine-birthday-note.txt", mime="text/plain")

# -------------------- Finale --------------------
with tabs[5]:
    st.markdown('<div class="eyebrow">QUEST COMPLETE · LEVEL 24</div>', unsafe_allow_html=True)
    st.header("To my favourite person, Antoine 💙")
    st.markdown("""
<div class="letter">
<p>Happy 24th birthday, my love. I wish I could be beside you today, giving you the biggest hug and celebrating every little thing that makes you who you are.</p>
<p>Even with an ocean between Toronto and Singapore, you are part of my everyday life. Thank you for being you, for the laughter, the love, the little moments, and the future we're building together.</p>
<p>At 24, I hope you discover more of the world, chase the things that make you happy, grow in the ways you dream of, and always remember that you have someone cheering you on from afar.</p>
<p>You're my favourite story, my favourite teammate, and one of the best things that has ever happened to me. Here's to more birthdays, more adventures, more memories, and one day, celebrating side by side.</p>
<p style="text-align:center;color:#9cc8ff"><b>♡ ALWAYS YOURS · 5 · ♡</b></p>
</div>
""", unsafe_allow_html=True)
    if "secret_open" not in st.session_state:
        st.session_state.secret_open = False
    if st.button("🎁 Open your secret gift"):
        st.session_state.secret_open = not st.session_state.secret_open
    if st.session_state.secret_open:
        st.markdown("""
<div class="letter">
<h3>One last thing, birthday boy...</h3>
<p>If I could give you one thing for your 24th birthday, it would be the ability to see yourself through my eyes. You would understand how special you are, how proud I am of you, and how deeply you are loved.</p>
<p>Now come claim your real-life birthday hugs. 💙🐆</p>
</div>
""", unsafe_allow_html=True)
    st.subheader("🏆 Your birthday achievements")
    quiz_score = sum(1 for i, ans in st.session_state.quiz_answers.items() if ans == questions[i][3])
    x, y, z = st.columns(3)
    x.metric("Quiz score", f"{quiz_score}/{len(questions)}")
    y.metric("Matching pairs", f"{len(st.session_state.matched_pairs)//2}/5")
    z.metric("Memories added", str(len(st.session_state.get("memories") or [])))
    st.markdown('<p style="text-align:center;color:#9cc8ff;letter-spacing:2px;font-size:.75rem">MADE WITH LOVE FROM TORONTO TO SINGAPORE<br>✦ BLUE SKIES · ALWAYS · 24 ✦</p>', unsafe_allow_html=True)

st.divider()
st.caption("Made with 💙 for Antoine · Level 24 · Toronto × Singapore")
