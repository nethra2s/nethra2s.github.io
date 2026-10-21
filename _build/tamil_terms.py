# -*- coding: utf-8 -*-
"""Option B: technical terms in English inside Tamil text; headings keep a Tamil hint.
apply(text) converts Tamil technical words (with their case endings) to English + Tamil suffix.
Text inside ⟦ ⟧ is left untouched (used for Tamil hints)."""
import re

PHRASES = [
 ("தரவு உள்ளீட்டுத் தானியக்கம்", "Data Entry Automation"),
 ("தரவு உள்ளீட்டில்", "Data Entry-ல்"),
 ("தரவு உள்ளீடு", "Data Entry"),
 ("சமூக ஊடகங்களிலிருந்து", "Social Media-விலிருந்து"),
 ("சமூக ஊடகங்களில்", "Social Media-வில்"),
 ("சமூக ஊடகங்களுக்கான", "Social Media-க்கான"),
 ("சமூக ஊடகங்களுக்கு", "Social Media-க்கு"),
 ("சமூக ஊடகங்களையும்", "Social Media-வையும்"),
 ("சமூக ஊடகப்", "Social Media"),
 ("சமூக ஊடகத்", "Social Media"),
 ("சமூக ஊடகம்", "Social Media"),
 ("சமூக ஊடக", "Social Media"),
 ("உள்ளடக்க அட்டவணை", "Content Calendar"),
]
WORDS = {
 "அனிமேஷன்": "Animation", "அனிமேஷன்கள்": "Animations",
 "அறிக்கை": "Report", "அறிக்கைகளில்": "Reports-ல்", "அறிக்கைகளுக்காக": "Reports-க்காக", "அறிக்கைகளுக்கு": "Reports-க்கு",
 "அறிக்கைகளைச்": "Reports-ஐ", "அறிக்கைகளையும்": "Reports-ஐயும்", "அறிக்கைகள்": "Reports", "அறிக்கையும்": "Report-ம்",
 "இணையதள": "Website", "இணையதளம்": "Website", "இணையதளங்கள்": "Websites",
 "இன்வாய்ஸ்": "Invoice", "இன்வாய்ஸ்கள்": "Invoices",
 "உத்தி": "Strategy", "உத்தியாளர்": "Strategist",
 "ஊடகம்": "Media",
 "எடிட்": "Edit", "எடிட்டிங்": "Editing",
 "ஏஜென்ட்": "Agent", "ஏஜென்ட்கள்": "Agents",
 "ஒப்புதல்": "Approval", "ஒப்புதல்கள்": "Approvals", "ஒப்புதல்களைத்": "Approvals-ஐ",
 "கருவி": "Tool", "கருவிகளில்": "Tools-ல்", "கருவிகளுடன்": "Tools-உடன்", "கருவிகளும்": "Tools-ம்", "கருவிகளை": "Tools-ஐ",
 "கருவிகளைத்": "Tools-ஐ", "கருவிகளைப்": "Tools-ஐ", "கருவிகள்": "Tools", "கருவியும்": "Tool-ம்", "கருவியையும்": "Tool-ஐயும்",
 "குரல்பதிவு": "Voice-over", "குரல்பதிவுகள்": "Voice-overs",
 "சந்தாதாரர்களுடன்": "Subscribers-உடன்", "சந்தாதாரர்களைக்": "Subscribers-ஐ", "சந்தாதாரர்களையும்": "Subscribers-ஐயும்",
 "சாட்பாட்": "Chatbot", "சாட்பாட்கள்": "Chatbots", "பாட்": "Bot", "பாட்கள்": "Bots",
 "சிறுபடம்": "Thumbnail", "சிறுபடங்கள்": "Thumbnails",
 "சேனல்": "Channel", "ஜிங்கிள்": "Jingle", "ஜிங்கிள்கள்": "Jingles", "டப்பிங்": "Dubbing",
 "டாஷ்போர்டு": "Dashboard", "டாஷ்போர்டுகளும்": "Dashboards-ம்", "டாஷ்போர்டை": "Dashboard-ஐ", "டாஷ்போர்டையும்": "Dashboard-ஐயும்",
 "டிஜிட்டல்": "Digital",
 "தரவால்": "Data-வால்", "தரவின்": "Data-வின்", "தரவிலிருந்து": "Data-விலிருந்து", "தரவு": "Data", "தரவுப்": "Data",
 "தரவும்": "Data-வும்", "தரவை": "Data-வை", "தரவைக்": "Data-வை", "தரவைச்": "Data-வை", "தரவைத்": "Data-வை", "தரவைப்": "Data-வை",
 "தானியக்கம்": "Automation", "தானியக்கங்கள்": "Automations", "தானியக்கங்களை": "Automations-ஐ", "தானியக்கங்களைக்": "Automations-ஐ",
 "தானியக்கத்": "Automation", "தானியக்கத்தைச்": "Automation-ஐ", "தானியக்கத்தையும்": "Automation-ஐயும்", "தானியக்கப்": "Automation",
 "நாட்காட்டி": "Calendar", "நாட்காட்டியில்": "Calendar-ல்",
 "பகுப்பாய்வு": "Analytics", "பகுப்பாய்வும்": "Analytics-ம்",
 "பட்டறை": "Workshop", "பட்டறைகள்": "Workshops",
 "பணிச்சுழற்சி": "Workflow", "பணிச்சுழற்சிகள்": "Workflows",
 "பாட்காஸ்ட்": "Podcast", "பாட்காஸ்ட்கள்": "Podcasts", "பாட்காஸ்டுக்குத்": "Podcast-க்கு",
 "பிரச்சாரங்கள்": "Campaigns", "பிரச்சாரங்களையும்": "Campaigns-ஐயும்",
 "பிராண்டிங்": "Branding", "பிராண்டின்": "Brand-இன்", "பிராண்டுகளுக்கு": "Brands-க்கு", "பிராண்டுகள்": "Brands",
 "பிராண்டுக்குக்": "Brand-க்கு", "பிராண்டுக்குத்": "Brand-க்கு", "பிராண்ட்": "Brand",
 "பிளேலிஸ்ட்கள்": "Playlists", "பேனர்": "Banner", "பேனர்களின்": "Banners-இன்", "பேனர்கள்": "Banners",
 "போஸ்டர்களைத்": "Posters-ஐ", "போஸ்டர்கள்": "Posters",
 "ப்ராம்ப்ட்": "Prompt", "ப்ராம்ப்ட்கள்": "Prompts",
 "மார்க்கெட்டிங்": "Marketing", "மார்க்கெட்டிங்கில்": "Marketing-ல்",
 "முன்கணிப்பு": "Forecast", "முன்கணிப்புகளும்": "Forecasts-ம்", "முன்கணிப்புகளையும்": "Forecasts-ஐயும்", "முன்கணிப்புகள்": "Forecasts",
 "முன்னோட்டம்": "Pilot",
 "மென்பொருள்": "Software", "மென்பொருள்களிலிருந்து": "Software-லிருந்து", "மென்பொருள்களில்": "Software-ல்",
 "மென்பொருள்களுக்கும்": "Software-க்கும்", "மென்பொருள்களை": "Software-ஐ",
 "யூடியூப்": "YouTube", "ரீல்ஸ்": "Reels", "ஷார்ட்ஸ்": "Shorts", "லீட்": "Lead", "லோகோ": "Logo", "லோகோவும்": "Logo-வும்",
 "வழிவரைபடம்": "Roadmap", "வழிவரைபடத்துக்குப்": "Roadmap-க்கு",
 "விற்பனையாளர்": "Vendor", "விற்பனையாளர்கள்": "Vendors",
 "வீடியோ": "Video", "வீடியோக்களை": "Videos-ஐ", "வீடியோக்களைக்": "Videos-ஐ", "வீடியோக்களைத்": "Videos-ஐ",
 "வீடியோக்களையும்": "Videos-ஐயும்", "வீடியோக்கள்": "Videos", "வீடியோவில்": "Video-வில்", "வீடியோவுக்கும்": "Video-க்கும்",
 "வீடியோவுடன்": "Video-உடன்", "வீடியோவும்": "Video-வும்", "வீடியோவை": "Video-வை", "வீடியோவைத்": "Video-வை",
 "ஸ்கிரிப்ட்": "Script", "கிட்": "Kit", "கிட்கள்": "Kits", "தானியங்கியாக்குதல்": "Automate செய்தல்", "தானியங்கியாக்குகிறோம்": "Automate செய்கிறோம்", "ஸ்டோரிகள்": "Stories", "ஸ்லைடுகள்": "Slides", "ஸ்லாட்": "Slot",
}
T = r"஀-௿"
_word_re = re.compile(rf"(?<![{T}])([{T}]+)(?![{T}])")

def _conv(seg):
    for a, b in PHRASES:
        seg = re.sub(rf"(?<![{T}]){re.escape(a)}(?![{T}])", b, seg)
    return _word_re.sub(lambda m: WORDS.get(m.group(1), m.group(1)), seg)

def apply(text):
    parts = re.split(r"(⟦.*?⟧)", text, flags=re.S)
    return "".join(p if p.startswith("⟦") else _conv(p) for p in parts)

def unmark(text):
    return text.replace("⟦", "").replace("⟧", "")

def hint(en_plain, ta_orig):
    """Heading in Tamil mode: English term + Tamil hint."""
    return f"{en_plain} ⟦({ta_orig})⟧"
