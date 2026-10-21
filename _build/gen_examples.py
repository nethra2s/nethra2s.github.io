# -*- coding: utf-8 -*-
"""Generate illustrative example sections for the technical service pages."""
import os
D = os.path.dirname(os.path.abspath(__file__))

def bi(en, ta, tag="span"):
    return f'<{tag} class="en">{en}</{tag}><{tag} class="ta">{ta}</{tag}>'
def tb(en, ta):  # svg tspans
    return f'<tspan class="en">{en}</tspan><tspan class="ta">{ta}</tspan>'

def shell(h2en, h2ta, bus_en, bus_ta, ask_en, ask_ta, figs, res, note_en=None, note_ta=None):
    note_en = note_en or "Actual results depend on each business. Your own solution is designed from your processes and numbers."
    note_ta = note_ta or "உண்மையான பலன்கள் ஒவ்வொரு தொழிலையும் பொறுத்தது. உங்கள் தீர்வு உங்கள் நடைமுறைகள் மற்றும் எண்களைக் கொண்டு வடிவமைக்கப்படும்."
    lis = "".join(f"<li>{bi(e, t)}</li>" for e, t in res)
    return f'''<section class="example" id="example">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">{bi("See an example", "ஒரு எடுத்துக்காட்டு")}</p>
      <h2>{bi(h2en, h2ta)}</h2>
      <p class="ex-badge">{bi("Illustrative example, not a client project", "மாதிரி எடுத்துக்காட்டு, உண்மையான வாடிக்கையாளர் திட்டம் அல்ல")}</p>
    </div>
    <div class="scenario box">
      <h3>{bi("The business", "தொழில்")}</h3>
      <p>{bi(bus_en, bus_ta)}</p>
      <h3>{bi("What they asked", "அவர்கள் கேட்டது")}</h3>
      <p>{bi(ask_en, ask_ta)}</p>
    </div>
    <div class="ex-grid">
{figs}
    </div>
    <div class="box outcome">
      <h3>{bi("The kind of results to expect", "எதிர்பார்க்கக்கூடிய பலன்கள்")}</h3>
      <ul>{lis}</ul>
      <p class="fig-note">{bi(note_en, note_ta)}</p>
    </div>
  </div>
</section>
'''

def fig(cap_en, cap_ta, note_en, note_ta, body):
    return f'''      <figure class="box fig">
        <figcaption>{bi(cap_en, cap_ta)}</figcaption>
        <p class="fig-note">{bi(note_en, note_ta)}</p>
        {body}
      </figure>'''

# ---------------------------------------------------------------- sales & marketing
def funnel():
    stages = [("Enquiries received", "வந்த விசாரணைகள்", 120, "Instant reply, 24/7", "உடனடிப் பதில், 24/7"),
              ("Replied the same day", "அதே நாளில் பதில்", 66, "Auto follow-up on day 1 and 3", "1, 3-ஆம் நாளில் Automated Follow-up"),
              ("Visited the showroom", "ஷோரூம் வருகை", 30, "Visit reminder with location", "இருப்பிடத்துடன் வருகை நினைவூட்டல்"),
              ("Bought", "வாங்கினர்", 12, "Thank-you and review request", "நன்றி & மதிப்புரை கோரிக்கை")]
    W, X0, BW, rh = 460, 10, 300, 52
    o = [f'<div class="fig-scroll"><svg viewBox="0 0 {W} {len(stages)*rh+10}" role="img" aria-labelledby="fn-t" class="chart">',
         '<title id="fn-t">Sample enquiry funnel with demo numbers: 120 enquiries, 66 replied the same day, 30 visited, 12 bought</title>']
    for i, (en, ta, n, fen, fta) in enumerate(stages):
        w = BW * n / 120; y = 6 + i * rh
        o.append(f'<g class="bar{" win" if i == 0 else ""}"><title>{en}: {n} (demo number)</title><rect x="{X0}" y="{y}" width="{w:.0f}" height="26" rx="5"/></g>')
        o.append(f'<text x="{X0 + w + 8:.0f}" y="{y + 18}" class="val">{n}</text>')
        o.append(f'<text x="{X0}" y="{y + 42}" class="rl" text-anchor="start">{tb(en, ta)}</text>')
        o.append(f'<text x="{W - 4}" y="{y + 42}" class="fix" text-anchor="end">{tb("AI fix: " + fen, "AI தீர்வு: " + fta)}</text>')
    o.append('</svg></div>')
    return "\n".join(o)

def followups():
    steps = [("Minute 0", "0 நிமிடம்", "Thank you for your enquiry! Here is our sofa catalogue and today's offers. Which style do you like?", "உங்கள் விசாரணைக்கு நன்றி! எங்கள் சோபா பட்டியலும் இன்றைய சலுகைகளும் இதோ. எந்த வகை பிடிக்கும்?"),
             ("Day 1", "நாள் 1", "Hi Ravi, did you get a chance to look at the catalogue? I can share prices for the 3-seater you liked.", "வணக்கம் ரவி, பட்டியலைப் பார்த்தீர்களா? நீங்கள் விரும்பிய 3-இருக்கை சோபாவின் விலையைப் பகிரலாமா?"),
             ("Day 3", "நாள் 3", "Our showroom is open till 9 pm. Would Saturday suit you for a visit? Location: (map link)", "எங்கள் ஷோரூம் இரவு 9 மணி வரை திறந்திருக்கும். சனிக்கிழமை வர வசதியா? இருப்பிடம்: (வரைபட இணைப்பு)"),
             ("Day 7", "நாள் 7", "Festival offer: free delivery this week. Shall I reserve the sofa for you?", "பண்டிகைச் சலுகை: இந்த வாரம் இலவச டெலிவரி. சோபாவை உங்களுக்காக ஒதுக்கி வைக்கலாமா?")]
    lis = "".join(f'<li><span class="when">{bi(a, b)}</span><span class="bubble">{bi(c, d)}</span></li>' for a, b, c, d in steps)
    return f'<ol class="seq">{lis}</ol>'

def sales():
    figs = fig("Where enquiries are lost", "விசாரணைகள் எங்கே இழக்கப்படுகின்றன",
               "One month of enquiries (demo numbers) and the AI fix for each drop.", "ஒரு மாத விசாரணைகள் (மாதிரி எண்கள்) மற்றும் ஒவ்வொரு இழப்புக்குமான AI தீர்வு.", funnel()) + "\n" + \
           fig("Automatic WhatsApp follow-ups", "Automated WhatsApp பின்தொடர்தல்",
               "Sent automatically; staff step in when the customer replies.", "தானாக அனுப்பப்படும்; வாடிக்கையாளர் பதிலளிக்கும்போது பணியாளர் தொடர்வார்.", followups())
    return shell("How AI turns more enquiries into sales", "AI எப்படி அதிக விசாரணைகளை விற்பனையாக மாற்றுகிறது",
                 "A furniture showroom in Madurai receives about 120 enquiries a month on Instagram and WhatsApp. Staff reply late on busy days and rarely follow up.",
                 "மதுரையில் ஒரு ஃபர்னிச்சர் ஷோரூம் மாதம் சுமார் 120 விசாரணைகளை Instagram, WhatsApp-ல் பெறுகிறது. பரபரப்பான நாட்களில் பணியாளர்கள் தாமதமாகப் பதிலளிக்கின்றனர்; பின்தொடர்வது அரிது.",
                 "\"We get enquiries but very few buy. Where are we losing them?\"", "\"விசாரணைகள் வருகின்றன, ஆனால் மிகச் சிலரே வாங்குகிறார்கள். எங்கே இழக்கிறோம்?\"",
                 figs,
                 [("Every enquiry gets an instant reply, even at night", "இரவிலும் ஒவ்வொரு விசாரணைக்கும் உடனடிப் பதில்"),
                  ("No customer is forgotten: follow-ups go out on schedule", "எந்த வாடிக்கையாளரும் மறக்கப்படுவதில்லை: பின்தொடர்தல் அட்டவணைப்படி செல்லும்"),
                  ("Staff spend their time on customers who are ready to buy", "வாங்கத் தயாரான வாடிக்கையாளர்களுக்கே பணியாளர்கள் நேரம் செலவிடுவர்"),
                  ("The owner sees which campaigns bring buyers", "எந்தப் Campaigns வாங்குபவர்களைக் கொண்டு வருகின்றன என்பதை உரிமையாளர் காண்பார்")])

# ---------------------------------------------------------------- data analytics
def dashboard():
    kpis = [("Today's sales", "இன்றைய விற்பனை", "₹2.4 L", "▲ 8% vs last week", "▲ கடந்த வாரத்தை விட 8%"),
            ("Payments due", "நிலுவைக் கட்டணங்கள்", "₹6.1 L", "23 customers", "23 வாடிக்கையாளர்கள்"),
            ("Low-stock items", "குறைந்த சரக்கு", "14", "Reorder today", "இன்றே மறு ஆர்டர்"),
            ("Gross margin", "மொத்த லாப விகிதம்", "18%", "This month", "இந்த மாதம்")]
    tiles = "".join(f'<div class="kpi"><span class="k">{bi(a, b)}</span><b>{v}</b><span class="d">{bi(c, d)}</span></div>' for a, b, v, c, d in kpis)
    days = [("Mon", "திங்", 2.1), ("Tue", "செவ்", 1.8), ("Wed", "புத", 2.6), ("Thu", "வியா", 2.2), ("Fri", "வெள்", 2.9), ("Sat", "சனி", 3.4), ("Sun", "ஞாயி", 2.4)]
    W, H, X0, Y0, BW, GAP = 420, 190, 36, 160, 40, 14
    mx = 4.0
    o = [f'<div class="fig-scroll"><svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="db-t" class="chart">',
         '<title id="db-t">Demo chart: daily sales for the last 7 days in lakh rupees, highest on Saturday at 3.4</title>']
    for t in (0, 1, 2, 3, 4):
        y = Y0 - t * (Y0 - 20) / mx
        o.append(f'<line x1="{X0}" y1="{y:.0f}" x2="{W - 6}" y2="{y:.0f}" class="gl"/><text x="{X0 - 6}" y="{y + 4:.0f}" class="tick" text-anchor="end">{t}</text>')
    for i, (en, ta, v) in enumerate(days):
        x = X0 + 10 + i * (BW + GAP); h = v * (Y0 - 20) / mx
        o.append(f'<g class="bar{" win" if en == "Sat" else ""}"><title>{en}: ₹{v} lakh (demo data)</title><rect x="{x}" y="{Y0 - h:.0f}" width="{BW}" height="{h:.0f}" rx="4"/></g>')
        o.append(f'<text x="{x + BW / 2:.0f}" y="{Y0 + 16}" class="tick" text-anchor="middle">{tb(en, ta)}</text>')
    o.append(f'<text x="{X0 + 10 + 5 * (BW + GAP) + BW / 2:.0f}" y="{Y0 - 3.4 * (Y0 - 20) / mx - 6:.0f}" class="val" text-anchor="middle">3.4</text>')
    o.append('</svg></div>')
    chart = "\n".join(o)
    head = f'<p class="dash-h">{bi("Daily sales, last 7 days (₹ lakh)", "கடந்த 7 நாள் தினசரி விற்பனை (₹ லட்சம்)")}</p>'
    return f'<div class="dash"><div class="kpis">{tiles}</div>{head}{chart}</div>'

def askdata():
    return f'''<div class="chat">
          <div class="msg me">{bi("Which customers did not order this month?", "இந்த மாதம் எந்த வாடிக்கையாளர்கள் ஆர்டர் செய்யவில்லை?")}</div>
          <div class="msg bot">{bi("7 regular customers have not ordered since September. The largest are Sri Murugan Hardware (avg ₹48,000/month) and KVR Traders (avg ₹31,000/month). Shall I prepare a follow-up list for the sales team?",
                                   "செப்டம்பர் முதல் 7 வழக்கமான வாடிக்கையாளர்கள் ஆர்டர் செய்யவில்லை. அவர்களில் பெரியவர்கள்: ஸ்ரீ முருகன் ஹார்டுவேர் (சராசரி ₹48,000/மாதம்), KVR டிரேடர்ஸ் (சராசரி ₹31,000/மாதம்). விற்பனைக் குழுவுக்குப் பின்தொடர் பட்டியல் தயாரிக்கட்டுமா?")}</div>
          <div class="msg me">{bi("Yes, and send it to Kumar on WhatsApp.", "ஆம், அதை குமாருக்கு WhatsApp-ல் அனுப்பவும்.")}</div>
          <div class="msg bot">{bi("Done. Kumar has the list with phone numbers and last order dates.", "முடிந்தது. தொலைபேசி எண்கள் மற்றும் கடைசி ஆர்டர் தேதிகளுடன் பட்டியல் குமாருக்கு அனுப்பப்பட்டது.")}</div>
        </div>
        <p class="fig-note">{bi("Customer names are invented for this example.", "இந்த எடுத்துக்காட்டுக்காக வாடிக்கையாளர் பெயர்கள் கற்பனையானவை.")}</p>'''

def analytics():
    figs = fig("Owner's dashboard on the phone", "கைபேசியில் உரிமையாளர் Dashboard",
               "Demo data. Updates automatically from billing and Tally.", "மாதிரித் Data. பில்லிங் மற்றும் Tally-லிருந்து தானாகப் புதுப்பிக்கப்படும்.", dashboard()) + "\n" + \
           fig("Ask your data in plain language", "எளிய மொழியில் Data-வை கேளுங்கள்",
               "Type a question; get an answer from your own records.", "கேள்வியைத் தட்டச்சு செய்யுங்கள்; உங்கள் சொந்தப் பதிவுகளிலிருந்து பதில் பெறுங்கள்.", askdata())
    return shell("What a business dashboard looks like", "வணிக Dashboard எப்படி இருக்கும்",
                 "A hardware distributor in Coimbatore with 2 branches. Sales are in the billing software, accounts in Tally and stock in Excel. The owner gets a report once a month, prepared by hand.",
                 "கோயம்புத்தூரில் 2 கிளைகள் கொண்ட ஒரு ஹார்டுவேர் விநியோகஸ்தர். விற்பனை பில்லிங் மென்பொருளில், கணக்குகள் Tally-ல், சரக்கு Excel-ல். உரிமையாளருக்கு மாதம் ஒருமுறை கைமுறையாகத் தயாரித்த Report கிடைக்கிறது.",
                 "\"I want to see how the business is doing every day, without waiting for the accountant.\"", "\"கணக்காளருக்காகக் காத்திருக்காமல், தொழில் எப்படி நடக்கிறது என்று தினமும் பார்க்க விரும்புகிறேன்.\"",
                 figs,
                 [("Daily sales, dues and stock on one screen, on the phone", "தினசரி விற்பனை, நிலுவை, சரக்கு ஒரே திரையில், கைபேசியில்"),
                  ("Overdue payments and low stock flagged automatically", "தாமதக் கட்டணங்களும் குறைந்த சரக்கும் தானாகச் சுட்டிக்காட்டப்படும்"),
                  ("Monthly report ready on day 1 instead of day 10", "10-ஆம் நாளுக்குப் பதிலாக 1-ஆம் நாளே மாதாந்திர Report தயார்"),
                  ("Questions answered in seconds instead of asking staff", "பணியாளர்களைக் கேட்பதற்குப் பதிலாக நொடிகளில் பதில்")])

# ---------------------------------------------------------------- custom AI
def chatbot():
    return f'''<div class="chat phone-chat">
          <div class="chat-top">{bi("Service Centre Assistant", "சர்வீஸ் சென்டர் உதவியாளர்")} · <small>{bi("AI, replies instantly", "AI, உடனடிப் பதில்")}</small></div>
          <div class="msg me">{bi("How much is a general service for a Splendor bike?", "ஸ்பிளெண்டர் பைக்கிற்கு ஜெனரல் சர்வீஸ் எவ்வளவு?")}</div>
          <div class="msg bot">{bi("A general service for the Splendor is ₹650 including oil change. Parts, if needed, are extra. Would you like to book a slot?", "ஸ்பிளெண்டருக்கு ஜெனரல் சர்வீஸ் ஆயில் மாற்றம் உட்பட ₹650. தேவைப்பட்டால் உதிரிபாகங்கள் தனி. Slot முன்பதிவு செய்யலாமா?")}</div>
          <div class="msg me">{bi("Yes, tomorrow morning.", "ஆம், நாளை காலை.")}</div>
          <div class="msg bot">{bi("Booked for tomorrow at 10:00 am. Pick-up from home is available for ₹50. Shall I add it?", "நாளை காலை 10:00 மணிக்கு முன்பதிவு செய்யப்பட்டது. வீட்டிலிருந்து எடுத்துச் செல்ல ₹50. சேர்க்கட்டுமா?")}</div>
          <div class="msg me">{bi("My bike is making a strange noise from the engine.", "என் பைக் இன்ஜினில் விசித்திரமான சத்தம் வருகிறது.")}</div>
          <div class="msg bot hand">{bi("That needs a mechanic to check. I've passed your message to Senthil, our service advisor; he will call you within 15 minutes.", "அதை மெக்கானிக் பார்க்க வேண்டும். உங்கள் செய்தியை எங்கள் சர்வீஸ் ஆலோசகர் செந்திலுக்கு அனுப்பியுள்ளேன்; 15 நிமிடங்களில் அழைப்பார்.")}</div>
        </div>
        <p class="fig-note">{bi("Prices and names are invented for this example. The last reply shows the hand-over to a person.", "இந்த எடுத்துக்காட்டுக்காக விலைகளும் பெயர்களும் கற்பனையானவை. கடைசிப் பதில் மனிதரிடம் ஒப்படைப்பதைக் காட்டுகிறது.")}</p>'''

def how_bot():
    rows = [("Learns from", "கற்றுக்கொள்வது", "Price list, service menu, timings, FAQs", "விலைப் பட்டியல், சர்வீஸ் மெனு, நேரம், அடிக்கடி கேட்கப்படும் கேள்விகள்"),
            ("Connected to", "இணைக்கப்பட்டது", "Booking calendar and job-card system", "முன்பதிவு Calendar மற்றும் ஜாப்-கார்டு அமைப்பு"),
            ("Answers in", "பதில் மொழி", "Tamil and English, 24/7", "தமிழ் மற்றும் ஆங்கிலம், 24/7"),
            ("Hands over when", "ஒப்படைப்பது எப்போது", "Repairs, complaints or anything unsure", "பழுதுகள், புகார்கள் அல்லது உறுதியில்லாத எதுவும்"),
            ("Never does", "ஒருபோதும் செய்யாதது", "Guess prices or share other customers' data", "விலையை ஊகிப்பது அல்லது பிற வாடிக்கையாளர் Data-வை பகிர்வது")]
    trs = "".join(f"<tr><th>{bi(a, b)}</th><td>{bi(c, d)}</td></tr>" for a, b, c, d in rows)
    return f'<table class="spec">{trs}</table>'

def custom_ai():
    figs = fig("A WhatsApp chatbot conversation", "ஒரு WhatsApp Chatbot உரையாடல்",
               "Shown in the page language; the bot replies in whichever language the customer uses.", "பக்க மொழியில் காட்டப்படுகிறது; வாடிக்கையாளர் பயன்படுத்தும் மொழியிலேயே Bot பதிலளிக்கும்.", chatbot()) + "\n" + \
           fig("How the assistant is set up", "உதவியாளர் எப்படி அமைக்கப்படுகிறது",
               "Clear rules decide what the bot may answer and when a person takes over.", "Bot எதற்குப் பதிலளிக்கலாம், எப்போது மனிதர் பொறுப்பேற்க வேண்டும் என்பதைத் தெளிவான விதிகள் தீர்மானிக்கின்றன.", how_bot())
    return shell("What a custom AI assistant looks like", "தனிப்பயன் AI உதவியாளர் எப்படி இருக்கும்",
                 "A two-wheeler service centre in Tirunelveli. Customers call and message all day about prices, bookings and bike status, and staff struggle to answer while working on bikes.",
                 "திருநெல்வேலியில் ஒரு இருசக்கர வாகன சர்வீஸ் சென்டர். விலை, முன்பதிவு, வாகன நிலை பற்றி வாடிக்கையாளர்கள் நாள் முழுவதும் அழைக்கின்றனர், செய்தி அனுப்புகின்றனர்; வேலை செய்துகொண்டே பதிலளிக்கப் பணியாளர்கள் சிரமப்படுகின்றனர்.",
                 "\"Can something answer the common questions so my mechanics can keep working?\"", "\"என் மெக்கானிக்குகள் தொடர்ந்து வேலை செய்ய, பொதுவான கேள்விகளுக்கு ஏதாவது பதிலளிக்க முடியுமா?\"",
                 figs,
                 [("Common questions answered instantly, day and night", "பொதுவான கேள்விகளுக்கு இரவும் பகலும் உடனடிப் பதில்"),
                  ("Bookings made directly into the calendar", "முன்பதிவுகள் நேரடியாக Calendar-ல் பதிவாகும்"),
                  ("Fewer phone interruptions for the mechanics", "மெக்கானிக்குகளுக்குக் குறைவான தொலைபேசி இடையூறுகள்"),
                  ("Complex issues reach the right person quickly", "சிக்கலான பிரச்சினைகள் விரைவாகச் சரியான நபரைச் சென்றடையும்")])

# ---------------------------------------------------------------- workflow automation
def flow():
    before = [("Bill arrives by email or WhatsApp", "பில் மின்னஞ்சல் அல்லது WhatsApp-ல் வருகிறது"),
              ("Staff downloads and prints it", "பணியாளர் பதிவிறக்கி அச்சிடுகிறார்"),
              ("Checks it against the purchase order", "கொள்முதல் ஆர்டருடன் சரிபார்க்கிறார்"),
              ("Manager signs the paper copy", "மேலாளர் காகித நகலில் கையொப்பமிடுகிறார்"),
              ("Typed into Tally by hand", "Tally-ல் கைமுறையாகத் தட்டச்சு")]
    after = [("Bill arrives by email or WhatsApp", "பில் மின்னஞ்சல் அல்லது WhatsApp-ல் வருகிறது"),
             ("AI reads the supplier, items and amounts", "சப்ளையர், பொருட்கள், தொகைகளை AI படிக்கிறது"),
             ("Matched to the purchase order automatically", "கொள்முதல் ஆர்டருடன் தானாகப் பொருத்தப்படுகிறது"),
             ("Manager approves on the phone with one tap", "மேலாளர் கைபேசியில் ஒரே தட்டில் Approval"),
             ("Entry posted to Tally, copy filed", "Tally-ல் பதிவு, நகல் சேமிப்பு")]
    def col(items, cls, h_en, h_ta, t_en, t_ta):
        lis = "".join(f'<li>{bi(e, t)}</li>' for e, t in items)
        return f'<div class="flow-col {cls}"><h4>{bi(h_en, h_ta)}</h4><ol>{lis}</ol><p class="flow-t">{bi(t_en, t_ta)}</p></div>'
    return '<div class="flow">' + col(before, "before", "Before: manual", "முன்பு: கைமுறை", "About 10 minutes per bill", "ஒரு பில்லுக்குச் சுமார் 10 நிமிடங்கள்") + \
           col(after, "after", "After: automated", "பின்பு: தானியங்கி", "About 1 minute of human time per bill", "ஒரு பில்லுக்குச் சுமார் 1 நிமிட மனித நேரம்") + '</div>'

def hours():
    W, X0, BW = 420, 130, 215
    rows = [("Manual", "கைமுறை", 50, False), ("Automated", "தானியங்கி", 5, True)]
    o = [f'<div class="fig-scroll"><svg viewBox="0 0 {W} 110" role="img" aria-labelledby="hr-t" class="chart">',
         '<title id="hr-t">Illustrative estimate: about 50 staff hours a month on 300 bills manually, about 5 hours when automated</title>']
    for i, (en, ta, v, win) in enumerate(rows):
        y = 14 + i * 44; w = BW * v / 50
        o.append(f'<text x="{X0 - 10}" y="{y + 18}" class="rl" text-anchor="end">{tb(en, ta)}</text>')
        o.append(f'<g class="bar{" win" if win else ""}"><title>{en}: about {v} hours a month (estimate)</title><rect x="{X0}" y="{y}" width="{max(w, 6):.0f}" height="26" rx="5"/></g>')
        o.append(f'<text x="{X0 + max(w, 6) + 8:.0f}" y="{y + 18}" class="val">{tb(f"~{v} h", f"~{v} மணி")}</text>')
    o.append('</svg></div>')
    return "\n".join(o)

def workflow():
    figs = fig("Supplier bill processing: before and after", "சப்ளையர் பில் செயலாக்கம்: முன்பும் பின்பும்",
               "The same five steps; people only check and approve.", "அதே ஐந்து படிகள்; மனிதர்கள் சரிபார்த்து Approval மட்டும் அளிக்கின்றனர்.", flow()) + "\n" + \
           fig("Staff hours per month for 300 bills", "300 பில்களுக்கு மாதாந்திரப் பணியாளர் நேரம்",
               "Illustrative estimate based on the times shown alongside.", "அருகில் காட்டப்பட்ட நேரங்களின் அடிப்படையிலான மாதிரி மதிப்பீடு.", hours() +
               f'<p class="fig-note">{bi("The time saved goes to supplier follow-up and month-end closing.", "மிச்சமான நேரம் சப்ளையர் பின்தொடர்தலுக்கும் மாத இறுதிக் கணக்கு முடிப்புக்கும் செல்கிறது.")}</p>')
    return shell("What workflow automation looks like", "Workflow Automation எப்படி இருக்கும்",
                 "An automobile spare-parts distributor that receives about 300 supplier bills a month. Two accounts staff download, check and type each bill into Tally.",
                 "மாதம் சுமார் 300 சப்ளையர் பில்களைப் பெறும் ஒரு ஆட்டோமொபைல் உதிரிபாக விநியோகஸ்தர். இரண்டு கணக்குப் பணியாளர்கள் ஒவ்வொரு பில்லையும் பதிவிறக்கி, சரிபார்த்து, Tally-ல் தட்டச்சு செய்கின்றனர்.",
                 "\"My accounts team is always behind. Can bills be entered without so much typing?\"", "\"என் கணக்குக் குழு எப்போதும் பின்தங்கியுள்ளது. இவ்வளவு தட்டச்சு இல்லாமல் பில்களைப் பதிய முடியுமா?\"",
                 figs,
                 [("Bills entered the same day instead of piling up", "பில்கள் குவியாமல் அதே நாளில் பதிவாகும்"),
                  ("Fewer typing errors and duplicate entries", "குறைவான தட்டச்சுப் பிழைகள் மற்றும் இரட்டைப் பதிவுகள்"),
                  ("Approvals on the phone, with a full record", "முழுப் பதிவுடன் கைபேசியில் Approvals"),
                  ("Accounts staff freed for checking and follow-up work", "சரிபார்ப்பு மற்றும் பின்தொடர் வேலைக்குக் கணக்குப் பணியாளர்கள் விடுவிக்கப்படுவர்")])

# ---------------------------------------------------------------- training
def agenda():
    rows = [("9:30", "Why AI matters for your work", "உங்கள் வேலைக்கு AI ஏன் முக்கியம்"),
            ("10:15", "Hands-on: ChatGPT, Claude and Gemini basics", "நேரடிப் பயிற்சி: ChatGPT, Claude, Gemini அடிப்படைகள்"),
            ("11:30", "Writing good prompts (with templates)", "நல்ல Prompts எழுதுதல் (மாதிரிகளுடன்)"),
            ("12:30", "Lunch", "மதிய உணவு"),
            ("1:30", "Practice: emails, letters, reports in English and Tamil", "பயிற்சி: ஆங்கிலம், தமிழில் மின்னஞ்சல், கடிதங்கள், Reports"),
            ("2:45", "Safe use: what never to share with AI", "பாதுகாப்பான பயன்பாடு: AI-யுடன் ஒருபோதும் பகிரக்கூடாதவை"),
            ("3:30", "Your own task: bring real work and solve it with AI", "உங்கள் சொந்தப் பணி: உண்மையான வேலையைக் கொண்டு வந்து AI-ல் தீர்க்கவும்"),
            ("4:30", "Q&A and certificates", "கேள்வி-பதில் & சான்றிதழ்கள்")]
    lis = "".join(f'<li><time>{t}</time><span>{bi(e, ta)}</span></li>' for t, e, ta in rows)
    return f'<ol class="agenda">{lis}</ol>'

def prompt_card():
    return f'''<div class="prompt-card">
          <p class="pc-h">{bi("Prompt card: reply to a customer complaint", "Prompt அட்டை: வாடிக்கையாளர் புகாருக்குப் பதில்")}</p>
          <pre>{bi("You are a polite customer-service officer at [company].\nA customer wrote: \"[paste message]\".\nWrite a short reply that:\n• apologises once\n• explains the next step and the date\n• gives our phone number [number]\nTone: warm, professional. Language: Tamil.",
                   "நீங்கள் [நிறுவனம்]-ல் பணிவான வாடிக்கையாளர் சேவை அலுவலர்.\nஒரு வாடிக்கையாளர் எழுதியது: \"[செய்தியை ஒட்டவும்]\".\nஒரு சிறிய பதில் எழுதவும்:\n• ஒருமுறை மன்னிப்பு கேட்கவும்\n• அடுத்த நடவடிக்கையையும் தேதியையும் விளக்கவும்\n• எங்கள் தொலைபேசி எண் [எண்] Data-வும்\nதொனி: அன்பான, தொழில்முறை. மொழி: தமிழ்.")}</pre>
          <p class="fig-note">{bi("Participants take home 25+ cards like this for daily tasks.", "தினசரிப் பணிகளுக்கு இதுபோன்ற 25+ அட்டைகளைப் பங்கேற்பாளர்கள் எடுத்துச் செல்வர்.")}</p>
        </div>'''

def training():
    figs = fig("Sample one-day workshop agenda", "மாதிரி ஒரு நாள் Workshop நிகழ்ச்சிநிரல்",
               "Adjusted to each group's work and level.", "ஒவ்வொரு குழுவின் வேலை மற்றும் நிலைக்கு ஏற்ப மாற்றப்படும்.", agenda()) + "\n" + \
           fig("Sample take-home prompt card", "மாதிரி Prompt அட்டை",
               "Fill in the brackets and paste into any AI assistant.", "அடைப்புக்குறிகளை நிரப்பி எந்த AI உதவியாளரிலும் ஒட்டவும்.", prompt_card())
    return shell("What an AI workshop looks like", "AI Workshop எப்படி இருக்கும்",
                 "An engineering college in Tirunelveli wants its 60 faculty members to use AI for teaching material, letters and reports, safely and confidently.",
                 "திருநெல்வேலியில் ஒரு பொறியியல் கல்லூரி, தன் 60 ஆசிரியர்களும் பாடப் பொருள், கடிதங்கள், Reports-க்கு AI-ஐப் பாதுகாப்பாகவும் நம்பிக்கையுடனும் பயன்படுத்த விரும்புகிறது.",
                 "\"Our staff have heard of ChatGPT but don't know how to use it properly. Can you train them in one day?\"", "\"எங்கள் ஆசிரியர்கள் ChatGPT பற்றிக் கேள்விப்பட்டுள்ளனர், ஆனால் சரியாகப் பயன்படுத்தத் தெரியவில்லை. ஒரே நாளில் பயிற்சி அளிக்க முடியுமா?\"",
                 figs,
                 [("Every participant completes real tasks with AI during the day", "ஒவ்வொரு பங்கேற்பாளரும் அன்றே AI மூலம் உண்மையான பணிகளை முடிப்பர்"),
                  ("Clear rules on what not to share with AI tools", "AI Tools-உடன் எதைப் பகிரக்கூடாது என்பதற்கான தெளிவான விதிகள்"),
                  ("Prompt cards and notes to keep using AI after the session", "அமர்வுக்குப் பிறகும் AI-ஐத் தொடர்ந்து பயன்படுத்த Prompt அட்டைகளும் குறிப்புகளும்"),
                  ("A follow-up session to answer questions from real use", "உண்மையான பயன்பாட்டிலிருந்து எழும் கேள்விகளுக்குப் பின்தொடர் அமர்வு")],
                 "Agenda and duration are adjusted for each organisation.", "நிகழ்ச்சிநிரலும் காலமும் ஒவ்வொரு நிறுவனத்துக்கும் ஏற்ப மாற்றப்படும்.")

OUT = {"ai-sales-marketing": sales, "data-analytics": analytics, "custom-ai": custom_ai,
       "workflow-automation": workflow, "ai-training": training}
if __name__ == "__main__":
    for slug, fn in OUT.items():
        name = f"example_{slug}.html"
        open(os.path.join(D, name), "w", encoding="utf-8").write(fn())
        mod = os.path.join(D, f"content_{slug}.py")
        c = open(mod, encoding="utf-8").read()
        if "EXAMPLE_FILE" not in c:
            open(mod, "a", encoding="utf-8").write(f'EXAMPLE_FILE="{name}"\n')
        print("wrote", name)
