# -*- coding: utf-8 -*-
"""'Our work' sections for the creative service pages, using the owner's real work."""
import os
D = os.path.dirname(os.path.abspath(__file__))
def bi(en, ta): return f'<span class="en">{en}</span><span class="ta">{ta}</span>'

YT_ID = "hCELszvT_no"
YT_TITLE_EN = "Naan: Mahakavi Bharathiyar song, Tamil AI music video"
YT_TITLE_TA = "நான்: மகாகவி பாரதியார் பாடல், தமிழ் AI இசை Video"
CHANNEL = "https://www.youtube.com/@TamilAIWonders"

def yt_card(cap_en, cap_ta, note_en, note_ta):
    return f'''      <figure class="box fig">
        <figcaption>{bi(cap_en, cap_ta)}</figcaption>
        <p class="fig-note">{bi(note_en, note_ta)}</p>
        <button class="yt" type="button" data-id="{YT_ID}" aria-label="Play video: {YT_TITLE_EN}">
          <img src="https://i.ytimg.com/vi/{YT_ID}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360" onerror="this.remove()">
          <span class="yt-play" aria-hidden="true"></span>
        </button>
        <p class="work-t">{bi(YT_TITLE_EN, YT_TITLE_TA)}</p>
        <a class="work-link" href="https://youtu.be/{YT_ID}" target="_blank" rel="noopener">{bi("Watch on YouTube ↗", "யூடியூபில் பார்க்க ↗")}</a>
      </figure>'''

def img_card(cap_en, cap_ta, note_en, note_ta, src, alt, w, h, cls=""):
    return f'''      <figure class="box fig">
        <figcaption>{bi(cap_en, cap_ta)}</figcaption>
        <p class="fig-note">{bi(note_en, note_ta)}</p>
        <img class="work-img {cls}" src="../img/work/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy">
      </figure>'''

def video_card(cap_en, cap_ta, note_en, note_ta):
    return f'''      <figure class="box fig">
        <figcaption>{bi(cap_en, cap_ta)}</figcaption>
        <p class="fig-note">{bi(note_en, note_ta)}</p>
        <video class="work-video" controls playsinline preload="none" poster="../img/work/intro-poster.jpg" width="1280" height="720">
          <source src="../media/intro.mp4" type="video/mp4">
        </video>
      </figure>'''

YT_JS = '''<script>
document.querySelectorAll('.yt').forEach(function(b){ b.addEventListener('click', function(){
  var f=document.createElement('iframe');
  f.src='https://www.youtube-nocookie.com/embed/'+b.dataset.id+'?autoplay=1&rel=0';
  f.title=b.getAttribute('aria-label')||'YouTube video'; f.allow='autoplay; encrypted-media; picture-in-picture'; f.allowFullscreen=true;
  f.className='yt-frame'; b.replaceWith(f);
}); });
</script>'''

def section(h_en, h_ta, intro_en, intro_ta, cards, extra=""):
    return f'''<section class="example work" id="work">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">{bi("Our work", "எங்கள் படைப்புகள்")}</p>
      <h2>{bi(h_en, h_ta)}</h2>
      <p class="ex-badge real">{bi("Real work by Nethra's founder", "நேத்ரா நிறுவனரின் உண்மையான படைப்பு")}</p>
      <p>{bi(intro_en, intro_ta)}</p>
    </div>
    <div class="ex-grid">
{cards}
    </div>
{extra}
  </div>
</section>
{YT_JS}
'''

channel_btn = f'<p class="work-cta"><a class="btn ghost" href="{CHANNEL}" target="_blank" rel="noopener">{bi("Visit Tamil AI Wonders Hub on YouTube ↗", "Tamil AI Wonders Hub YouTube சேனலைப் பார்க்க ↗")}</a></p>'

PAGES = {
 "ai-design-branding": section(
   "Brand identity for Tamil AI Wonders Hub", "Tamil AI Wonders Hub-க்கான Brand அடையாளம்",
   "The logo and YouTube channel banner for our own Tamil AI channel, created with AI tools and finished by hand.",
   "எங்கள் சொந்தத் தமிழ் AI சேனலுக்கான Logo மற்றும் YouTube Channel Banner; AI Tools-உடன் உருவாக்கி கையால் முடிக்கப்பட்டவை.",
   img_card("Channel logo", "Channel Logo", "Round badge for the profile picture, readable at small sizes.", "சுயவிவரப் படத்துக்கான வட்ட Logo; சிறிய அளவிலும் தெளிவாகத் தெரியும்.",
            "taw-logo.webp", "Tamil AI Wonders Hub logo: veena and music notes above the channel name", 600, 600, "logo") + "\n" +
   img_card("YouTube channel banner", "YouTube Channel Banner", "Tamil heritage meets AI: veena, palm-leaf manuscripts, film reels and the coastline.", "தமிழ் பாரம்பரியமும் AI-யும்: வீணை, ஓலைச்சுவடிகள், திரைச்சுருள்கள், கடற்கரை.",
            "taw-banner.jpg", "Tamil AI Wonders Hub YouTube banner with a poet, children, veena and film reels around the logo", 1600, 635)),
 "ai-video": section(
   "Videos we have made", "நாங்கள் உருவாக்கிய Videos",
   "An animated channel intro and a full AI music video, both made for our own channel.",
   "Animation Channel அறிமுகமும் முழு AI இசை Video-வும்; இரண்டும் எங்கள் சொந்தச் சேனலுக்காக உருவாக்கப்பட்டவை.",
   video_card("Channel intro animation (12 seconds)", "Channel அறிமுக Animation (12 வினாடிகள்)", "Logo reveal with particles, light and music; the kind of intro we make for brands.", "துகள்கள், ஒளி, இசையுடன் Logo வெளிப்பாடு; Brands-க்கு நாங்கள் உருவாக்கும் அறிமுக வகை.") + "\n" +
   yt_card("AI music video", "AI இசை Video", "A complete music video created with AI visuals and music.", "AI காட்சிகள் மற்றும் இசையுடன் உருவாக்கப்பட்ட முழு இசை Video.")),
 "ai-voice-music": section(
   "Music we have made", "நாங்கள் உருவாக்கிய இசை",
   "A Tamil song set to Mahakavi Bharathiyar's poem, composed and produced with AI tools for our channel.",
   "மகாகவி பாரதியாரின் கவிதைக்கு இசையமைக்கப்பட்ட தமிழ்ப் பாடல்; எங்கள் சேனலுக்காக AI Tools-உடன் உருவாக்கப்பட்டது.",
   yt_card("Naan: Bharathiyar song", "நான்: பாரதியார் பாடல்", "Tamil vocals and music produced with AI, with a matching music video.", "AI மூலம் தயாரிக்கப்பட்ட தமிழ்க் குரலும் இசையும், பொருத்தமான இசை Video-உடன்.") + "\n" +
   video_card("Sound for a brand intro", "Brand அறிமுகத்துக்கான ஒலி", "Music and sound effects timed to the logo animation.", "Logo அனிமேஷனுக்கு ஏற்ப நேரமிட்ட இசையும் ஒலி விளைவுகளும்.")),
 "youtube-content": section(
   "Our own channel: Tamil AI Wonders Hub", "எங்கள் சொந்தச் Channel: Tamil AI Wonders Hub",
   "We run our own Tamil AI channel with 17K+ subscribers, so the advice we give comes from doing it ourselves.",
   "17K+ Subscribers-உடன் எங்கள் சொந்தத் தமிழ் AI சேனலை நடத்துகிறோம்; எனவே நாங்கள் தரும் ஆலோசனை எங்கள் சொந்த அனுபவத்திலிருந்து வருகிறது.",
   img_card("Channel branding", "Channel Branding", "Banner and logo designed for the channel.", "சேனலுக்காக வடிவமைக்கப்பட்ட பேனரும் Logo-வும்.",
            "taw-banner.jpg", "Tamil AI Wonders Hub YouTube banner", 1600, 635) + "\n" +
   yt_card("A video from the channel", "சேனலிலிருந்து ஒரு Video", "Music video created, edited and published by our team.", "எங்கள் குழு உருவாக்கி, Edit செய்து, வெளியிட்ட இசை Video."),
   channel_btn),
}
if __name__ == "__main__":
    for slug, html in PAGES.items():
        name = f"work_{slug}.html"
        open(os.path.join(D, name), "w", encoding="utf-8").write(html)
        mod = os.path.join(D, f"content_{slug}.py")
        c = open(mod, encoding="utf-8").read()
        if "EXAMPLE_FILE" not in c:
            open(mod, "a", encoding="utf-8").write(f'EXAMPLE_FILE="{name}"\n')
        print("wrote", name)
