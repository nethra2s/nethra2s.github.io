# -*- coding: utf-8 -*-
"""Build a service detail page (e.g. ai-strategy/index.html) from a content module,
reusing the header, styles, footer and core script from the main index.html.

Usage: python3 make_service_page.py <content_module> <index.html> <out.html> <asset_prefix> <home_prefix>
  asset_prefix: prefix for img/ paths ("../" for the live repo, "" for the preview)
  home_prefix:  prefix for links back to the home page ("../" live, "" preview)
"""
import importlib.util, sys, re, html

mod_path, index_path, out_path, A, H = sys.argv[1:6]
spec = importlib.util.spec_from_file_location("c", mod_path); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
src = open(index_path, encoding="utf-8").read()

style = src[src.index("<style>"):src.index("</style>") + len("</style>")]
fonts = src[src.index('<link rel="preconnect"'):src.index("<style>")]
header = src[src.index("<header>"):src.index("</header>") + len("</header>")]
footer = src[src.index("<footer>"):src.index("</footer>") + len("</footer>")]
script_full = src[src.rindex("<script>"):]
core_js = script_full[:script_full.index("  var form=document.getElementById('enquiry')")] + "})();\n</script>\n"
ver = re.search(r'<meta name="version" content="([^"]+)"', src)
ver = ver.group(1) if ver else ""

# header links back to home page sections
header = header.replace('src="img/', f'src="{A}img/')
header = header.replace('class="brand" href="#home"', f'class="brand" href="{H}"')
for sec in ["home", "about", "services", "contact"]:
    header = header.replace(f'href="#{sec}"', f'href="{H}#{sec}"')

def bi(en, ta):
    return f'<span class="en">{en}</span><span class="ta">{ta}</span>'

book = f'{H}?service={html.escape(c.SERVICE.replace("&", "%26").replace(" ", "%20"))}#contact'

page_css = """
/* service page */
.crumbs{font-size:14px;color:var(--muted);margin-bottom:18px}
.crumbs a{color:var(--cyan);text-decoration:none}
.crumbs a:hover{text-decoration:underline}
.svc-hero{padding-block:56px 48px;background:radial-gradient(600px 300px at 85% 30%, rgba(34,169,236,.18), transparent 70%),var(--bg)}
.svc-hero .wrap{display:grid;grid-template-columns:auto 1fr;gap:32px;align-items:center}
.svc-hero .wrap > *{min-width:0}
.svc-hero img{width:150px;height:150px;border-radius:20px;object-fit:cover;box-shadow:0 20px 50px -18px rgba(34,169,236,.6)}
.svc-hero h1{font-size:clamp(30px,4vw,48px);font-weight:800;margin-top:10px}
body.lang-ta .svc-hero h1{font-size:clamp(24px,3vw,36px)}
.svc-hero .lead{font-size:18.5px;color:var(--muted);max-width:62ch;margin-block:14px 24px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.two > *{min-width:0}
.box{padding:24px 26px;border:1px solid var(--line);border-radius:var(--r);background:var(--surface)}
.box h2{font-size:20px;margin-bottom:12px}
.box ul{margin:0;padding-left:20px;display:grid;gap:8px;color:var(--muted)}
.box.q li{list-style:none;margin-left:-20px;padding-left:28px;position:relative;font-style:italic;color:var(--ink)}
.box.q li::before{content:"?";position:absolute;left:0;top:0;width:20px;height:20px;border-radius:50%;background:var(--red);color:#fff;font:700 12px/20px var(--f-display);text-align:center;font-style:normal}
.sols{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;list-style:none;margin:0;padding:0;counter-reset:sol}
.sol{counter-increment:sol;display:grid;grid-template-columns:44px 1fr;gap:4px 16px;padding:22px 24px;border:1px solid var(--line);border-radius:var(--r);background:linear-gradient(180deg,var(--surface-2),var(--surface))}
.sol::before{content:counter(sol);grid-row:span 2;width:40px;height:40px;border-radius:12px;background:var(--cyan-soft);color:var(--cyan);font:800 17px/40px var(--f-display);text-align:center;border:1px solid var(--line)}
.sol h3{font-size:18px}
.sol p{color:var(--muted);font-size:15.5px}
.get{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;list-style:none;margin:0;padding:0}
.get li{display:flex;gap:10px;align-items:flex-start;padding:16px 18px;border:1px solid var(--line);border-radius:12px;background:var(--surface);font-weight:600}
.get li::before{content:"";flex:none;width:18px;height:18px;margin-top:2px;border-radius:50%;background:var(--cyan) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M9 16.2l-3.5-3.5L4 14.2l5 5 11-11-1.5-1.5z' fill='%23011B47'/%3E%3C/svg%3E") center/14px no-repeat}
.meta{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:22px}
.meta > *{min-width:0}
.cta-band{text-align:center;padding-block:64px;background:var(--bg-deep);border-top:1px solid var(--line)}
.cta-band h2{font-size:clamp(24px,3vw,34px);font-weight:800;margin-bottom:12px}
.cta-band p{color:var(--muted);margin-bottom:24px}
.cta-band .btns{justify-content:center}
.related{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:28px}
.related a{padding:9px 16px;border:1px solid var(--line);border-radius:999px;color:var(--muted);text-decoration:none;font:600 14px/1 var(--f-display)}
.related a:hover{border-color:var(--cyan);color:var(--ink)}
body.lang-ta .related a{font-family:var(--f-tamil)}

/* illustrative example section */
.example .head{max-width:760px}
.ex-badge{display:inline-flex;align-self:start;justify-self:start;padding:6px 12px;border:1px dashed var(--cyan);border-radius:999px;color:var(--cyan);font:700 12.5px/1.2 var(--f-display);letter-spacing:.04em}
body.lang-ta .ex-badge{font-family:var(--f-tamil)}
.scenario{display:grid;gap:8px;margin-bottom:20px}
.scenario h3,.outcome h3{font-size:17px;color:var(--cyan)}
.scenario p{color:var(--ink)}
.ex-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px}
.ex-grid > *{min-width:0}
.fig{margin:0;display:grid;gap:10px;align-content:start}
.fig figcaption{font:800 18px/1.3 var(--f-display)}
body.lang-ta .fig figcaption{font-family:var(--f-tamil)}
.fig-note{color:var(--muted);font-size:14.5px}
.fig-scroll{overflow-x:auto}
.chart{width:100%;min-width:320px;height:auto;display:block}
.chart text{font-family:var(--f-body);fill:var(--ink)}
body.lang-ta .chart text{font-family:var(--f-tamil)}
.chart .q{fill:var(--bg-deep);stroke:var(--line)}
.chart .q-win{fill:rgba(34,169,236,.12);stroke:var(--cyan)}
.chart .ql{font-size:12.5px;font-weight:700;fill:var(--muted)}
.chart .ql.win{fill:var(--cyan)}
.chart .ax{stroke:var(--muted);stroke-width:1.5}
.chart .axl{font-size:12.5px;fill:var(--muted);font-weight:600}
.chart .dot circle{fill:var(--surface-2);stroke:var(--muted);stroke-width:2}
.chart .dot.win circle{fill:var(--cyan);stroke:var(--bg)}
.chart .dot text{font:800 13px var(--f-display);fill:var(--ink)}
.chart .dot.win text{fill:var(--bg-deep)}
.chart .dot:hover circle,.chart .bar:hover rect{stroke:#fff;stroke-width:2}
.chart .rl{font-size:12px;font-weight:600;fill:var(--muted)}
.chart .grid line{stroke:var(--line);stroke-width:1}
.chart .mlab text{font-size:12px;fill:var(--muted);font-weight:700}
.chart .bar rect{fill:var(--surface-2);stroke:var(--line)}
.chart .bar.win rect{fill:var(--cyan);stroke:none}
.chart .bar text{font-size:11.5px;font-weight:700;fill:var(--ink)}
.chart .bar.win text{fill:var(--bg-deep)}
.chart .gate line{stroke:var(--red);stroke-width:2;stroke-dasharray:4 4}
.chart .gate text{font-size:11px;fill:var(--red);font-weight:700}
.fig-legend{margin:0;padding-left:22px;display:grid;gap:4px;color:var(--muted);font-size:14.5px;columns:2}
.fig-key{display:flex;flex-wrap:wrap;align-items:center;gap:8px;color:var(--muted);font-size:14px}
.fig-key .sw{width:14px;height:14px;border-radius:4px;background:var(--surface-2);border:1px solid var(--line);margin-left:8px}
.fig-key .sw.win{background:var(--cyan);border:0;margin-left:0}
.outcome ul{margin:10px 0 12px;padding-left:20px;display:grid;gap:6px}
@media (max-width:860px){.ex-grid{grid-template-columns:1fr}.fig-legend{columns:1}}
@media (max-width:860px){.two,.meta,.sols{grid-template-columns:1fr}.get{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.svc-hero .wrap{grid-template-columns:1fr}.svc-hero img{width:110px;height:110px}.get{grid-template-columns:1fr}}
"""
style = style.replace("</style>", page_css + "</style>")

def li(items): return "".join(f"<li>{x}</li>" for x in items)
def li_bi(en, ta): return "".join(f"<li>{bi(e, t)}</li>" for e, t in zip(en, ta))

sols = "".join(f'<li class="sol"><h3>{bi(a, b)}</h3><p>{bi(d, e)}</p></li>' for a, b, d, e in c.SOL)
steps = "".join(f'<li><h3>{bi(a, b)}</h3><p>{bi(d, e)}</p></li>' for a, b, d, e in c.STEPS)
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__))); from pages import NAMES
related = "".join(f'<a href="{H}{slug}/">{bi(*NAMES[slug])}</a>' for slug in c.RELATED)
HOW_EN=getattr(c,'HOW_EN','From first conversation to a clear plan'); HOW_TA=getattr(c,'HOW_TA','முதல் உரையாடலிலிருந்து தெளிவான திட்டம் வரை')
NL_EN=getattr(c,'NEXT_LABEL_EN','After the plan'); NL_TA=getattr(c,'NEXT_LABEL_TA','திட்டத்துக்குப் பிறகு')
CTA_EN=getattr(c,'CTA_EN','Ready to find your AI starting point?'); CTA_TA=getattr(c,'CTA_TA','உங்கள் AI தொடக்கப் புள்ளியைக் கண்டறியத் தயாரா?')

page_title_txt = html.unescape(c.TITLE_EN)
import os
EXAMPLE = open(os.path.join(os.path.dirname(os.path.abspath(mod_path)), c.EXAMPLE_FILE), encoding="utf-8").read() if getattr(c, "EXAMPLE_FILE", None) else ""
out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="version" content="{ver}">
<title>{c.TITLE_EN} | Nethra Strategic Solutions</title>
<meta name="description" content="{html.escape(c.LEAD_EN)}">
<link rel="icon" href="{A}img/logo.jpg">
{fonts}{style}
</head>
<body>
{header}

<main>
<section class="svc-hero" id="home">
  <div class="wrap">
    <img src="{A}img/{c.ICON}" alt="" width="240" height="240">
    <div>
      <p class="crumbs"><a href="{H}">{bi("Home", "முகப்பு")}</a> › <a href="{H}#services">{bi("Services", "சேவைகள்")}</a> › {bi(c.TITLE_EN, c.TITLE_TA)}</p>
      <p class="eyebrow">{bi(c.TAG_EN, c.TAG_TA)}</p>
      <h1>{bi(c.TITLE_EN, c.TITLE_TA)}</h1>
      <p class="lead">{bi(c.LEAD_EN, c.LEAD_TA)}</p>
      <div class="btns">
        <a class="btn primary" href="{book}">{bi("Book a free AI consultation", "இலவச AI ஆலோசனை பெறுங்கள்")}</a>
        <a class="btn ghost" href="#solutions">{bi("See what we provide", "நாங்கள் வழங்குவது")}</a>
      </div>
    </div>
  </div>
</section>

<section class="deep">
  <div class="wrap two">
    <div class="box"><h2>{bi("Who it's for", "யாருக்கு ஏற்றது")}</h2><ul>{li_bi(c.FOR_EN, c.FOR_TA)}</ul></div>
    <div class="box q"><h2>{bi("Questions we answer", "நாங்கள் பதிலளிக்கும் கேள்விகள்")}</h2><ul>{li_bi(c.PROB_EN, c.PROB_TA)}</ul></div>
  </div>
</section>

<section id="solutions">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">{bi("Solutions", "தீர்வுகள்")}</p>
      <h2>{bi("What we provide", "நாங்கள் வழங்குவது")}</h2>
      <p>{bi("Choose the parts you need, or take the complete package.", "உங்களுக்குத் தேவையானவற்றைத் தேர்ந்தெடுக்கலாம், அல்லது முழுத் தொகுப்பையும் எடுத்துக்கொள்ளலாம்.")}</p>
    </div>
    <ol class="sols">{sols}</ol>
  </div>
</section>

{EXAMPLE}
<section class="deep">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">{bi("How it works", "செயல்முறை")}</p>
      <h2>{bi(HOW_EN, HOW_TA)}</h2>
    </div>
    <ol class="steps">{steps}</ol>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">{bi("Deliverables", "வழங்கப்படுபவை")}</p>
      <h2>{bi("What you receive", "நீங்கள் பெறுவது")}</h2>
    </div>
    <ul class="get">{li_bi(c.GET_EN, c.GET_TA)}</ul>
    <div class="meta">
      <div class="box"><h2>{bi("Typical duration", "வழக்கமான காலம்")}</h2><p>{bi(c.DUR_EN, c.DUR_TA)}</p></div>
      <div class="box"><h2>{bi(NL_EN, NL_TA)}</h2><p>{bi(c.NEXT_EN, c.NEXT_TA)}</p></div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <h2>{bi(CTA_EN, CTA_TA)}</h2>
    <p>{bi("The first consultation is free. Tell us about your business and we will reply within two working days.", "முதல் ஆலோசனை இலவசம். உங்கள் தொழில் பற்றி சொல்லுங்கள்; இரண்டு வேலை நாட்களுக்குள் பதிலளிப்போம்.")}</p>
    <div class="btns">
      <a class="btn primary" href="{book}">{bi("Book a free AI consultation", "இலவச AI ஆலோசனை பெறுங்கள்")}</a>
      <a class="btn ghost" href="{H}#services">{bi("All services", "அனைத்து சேவைகள்")}</a>
    </div>
    <p style="margin:28px 0 0;font-size:14px">{bi("Related services", "தொடர்புடைய சேவைகள்")}</p>
    <div class="related">{related}</div>
  </div>
</section>
</main>

{footer}

{core_js}</body>
</html>
"""
open(out_path, "w", encoding="utf-8").write(out)
print("written", out_path, len(out))
