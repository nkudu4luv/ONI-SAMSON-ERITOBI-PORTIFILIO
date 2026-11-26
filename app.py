"""Portfolio of Samson Eritobi Oni, built with Streamlit.

Run:  streamlit run app.py
"""
import base64
import re
from html import escape as e
from pathlib import Path

import streamlit as st

BASE = Path(__file__).resolve().parent

def find_asset(filename: str) -> Path:
    """Find an asset either beside app.py or inside an assets folder."""
    candidates = (BASE / filename, BASE / "assets" / filename)
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    # Return the root-level path so missing-file messages are easy to understand.
    return candidates[0]

PHOTO = find_asset("samson.jpg")
CV = find_asset("Samson_Oni_CV.pdf")

NAME = "Oni Samson Eritobi"
EMAIL = "Onisamson10@gmail.com"
GITHUB = "https://github.com/OniSamson"
PHONE = "(+234) 8162752066"

st.set_page_config(page_title=f"{NAME} | Portfolio", page_icon="∑", layout="wide")


# --------------------------------------------------------------------------- content
ABOUT = (
    "Mathematics Education graduate from the University of Lagos with strong interests in applied "
    "mathematics, numerical analysis and mathematical modelling. Experienced in mathematics teaching, "
    "tutoring undergraduate students and developing educational initiatives. Motivated to bring "
    "analytical skills and practical experience to a stimulating international academic environment "
    "such as Erasmus Mundus InterMaths."
)

FACTS = [
    ("4.04 / 5.00", "CGPA, Second Class Honours (Upper Division)"),
    ("200+", "underserved students tutored free of charge"),
    ("2,000+", "learners supported through his initiative"),
    ("200+", "participants supported at the 26th Nigerian University Games"),
]

MODULES = ["Numerical Analysis", "Real Analysis", "Calculus", "Linear Algebra", "Probability Theory",
           "Mathematical Modelling", "Differential Equations"]

EXPERIENCE = [
    dict(role="Seasonal WASSCE Further Mathematics Examiner", org="West African Examination Council (WAEC)",
         place="Lagos, Nigeria", when="Current",
         points=["Marked and reviewed Further Mathematics exam scripts adhering strictly to official marking guidelines."],
         link=("View evidence", "https://drive.google.com/file/d/11LKO7mRf3eJux0H8r0h9W7oChRgq9GO7/view?usp=drivesdk")),
    dict(role="Founder and Lead", org="F.O.C Embrace Success Educational Consult", place="Lagos, Nigeria",
         when="09/2021 to Present",
         points=["Founded an educational initiative providing free math tutorials to over 200 underserved students "
                 "and supporting 2,000+ learners.",
                 "Developed practice materials and coordinated volunteer tutors to improve students' mathematical "
                 "understanding."]),
    dict(role="Mathematics Teacher (NYSC)", org="The King's Anchor College", place="Lagos, Nigeria",
         when="07/2025 to 06/2026",
         points=["Delivered the mathematics curriculum at junior and senior secondary levels, preparing students for "
                 "exams with targeted revision and assessments."]),
    dict(role="University Teaching Assistant", org="University of Lagos, Department of Science Education",
         place="Lagos, Nigeria", when="12/2024 to 05/2025",
         points=["Provided supplemental teaching support, preparing materials and helping undergraduates strengthen "
                 "problem-solving skills."]),
]

TOOLBOX = [
    ("Data and programming", ["Python (basic)", "R syntax for data science", "SQL", "Power BI", "Data analytics",
                              "MATLAB (basic)"]),
    ("Mathematics", ["Numerical analysis", "Mathematical modelling", "Statistical analysis"]),
    ("People and teaching", ["Effective communication", "Leadership", "Mentoring", "Problem solving",
                             "Time management"]),
]

CERTS = [
    dict(title="Basic Python", by="Barcode Analytics", when="15/06/2026",
         link="https://drive.google.com/file/d/1-JDZFhv10KL19l0_HbwDl_ptHAb33Slm/view?usp=drivesdk"),
    dict(title="Data Analytics", by="Barcode Analytics"),
    dict(title="SQL", by="Barcode Analytics"),
    dict(title="Power BI", by="Barcode Analytics"),
    dict(title="R Syntax for Data Science", by="Tim-R Programming Consult, Nigeria", when="14/08/2025",
         link="https://drive.google.com/file/d/19bnWcBWaSEIIpviUVeDKxFzNDzwsNvCh/view?usp=drivesdk"),
    dict(title="MATLAB Onramp Course Completion", by="MathWorks (online)", when="2026",
         note="Commands, vectors and matrices, array operations, functions, plotting, data import and programming.",
         link="https://matlabacademy.mathworks.com/progress/share/certificate.html?id=8104a63e-9be7-4154-9671-e5e7c17c4773"),
    dict(title="Licensed Professional Teacher", by="Teachers Registration Council of Nigeria (TRCN)",
         when="10/10/2024", note="Registration number LA/R/27298.",
         link="https://drive.google.com/file/d/1dz58szwAjk7SRS2Db95qYu26YGQdxw0G/view?usp=drivesdk"),
]

LEADERSHIP = [
    ("Departmental Stakeholder", "Department of Science Education, University of Lagos", "2021 to 2024",
     "Advocated for student welfare and contributed to academic program improvements. Awarded Best Departmental "
     "Stakeholder for outstanding contribution.", None),
    ("Course Representative", "University of Lagos", "2018 to 2024",
     "Represented student academic concerns and facilitated communication with faculty.", None),
    ("Treasurer, Hall of Residence", "University of Lagos", "2023 to 2024",
     "Managed financial resources and promoted transparency for student welfare activities.",
     "https://drive.google.com/file/d/1cTWEUFBjsBTJ6TfwsCERRDexGjUJR9Np/view?usp=drivesdk"),
]

VOLUNTEERING = [
    ("Medical CDS Volunteer, National Youth Service Corps", "Lagos", "06/2025 to 06/2026",
     "Supported community health outreach and malaria-prevention programs."),
    ("Tutor, Science Education Student Association Tutorials", "University of Lagos", "04/2021 to 06/2024",
     "Led tutorials in Real Analysis and Numerical Analysis, providing mentorship and academic support."),
    ("Logistics and Media Volunteer, NUGA Games", "Lagos, Nigeria", "16/03/2022 to 26/03/2022",
     "Supported the organization of the 26th Nigerian University Games at the University of Lagos by assisting with "
     "athlete accreditation and event scheduling for more than 200 participants."),
]

AWARDS = [
    ("Best Departmental Stakeholder Award", "University of Lagos Science & Technology Education Students Association",
     "Recognized for service as a departmental stakeholder and contribution to student representation.",
     ["https://drive.google.com/file/d/1eQ2wNUN9oil2moUU73qCq57bYHQueoBh/view?usp=drivesdk",
      "https://drive.google.com/file/d/1POmMSNBnmuBbfL1oZQMpbxwfK22sOulZ/view?usp=drivesdk"]),
    ("Academic Excellence Award", "SwitchCon", "Recognized for academic achievement.", []),
    ("NUESA Campus Champion Award", "Nigerian Universities Education Students' Association (NUESA), Unilag",
     "Recognized for peer tutoring and academic support to fellow students.", []),
]


# --------------------------------------------------------------------------- helpers
def H(s: str) -> str:
    """Collapse an HTML template to one line so Markdown never treats it as a code block."""
    return re.sub(r"\n\s*", "", s).strip()


def link(url: str, label: str, cls: str = "lnk") -> str:
    return f'<a class="{cls}" href="{e(url, quote=True)}" target="_blank" rel="noopener">{e(label)}</a>'


def photo_uri() -> str | None:
    """Return an embedded image URI, or None if the photo is missing."""
    if not PHOTO.is_file():
        return None
    data = base64.b64encode(PHOTO.read_bytes()).decode("utf-8")
    return f"data:image/jpeg;base64,{data}"


def photo_html() -> str:
    """Render the portrait when available; otherwise show a helpful placeholder."""
    uri = photo_uri()
    if uri:
        return (
            f'<div class="photo"><img src="{uri}" '
            f'alt="Portrait of {e(NAME)}"></div>'
        )
    return (
        '<div class="photo"><div style="background:#EEF2EE;padding:3rem 1rem;'
        'text-align:center;border:1px solid #D6DDD8;border-radius:4px;">'
        '<strong>Portrait not found</strong><br>'
        '<span style="font-size:.85rem;">Place samson.jpg beside app.py '
        'or inside an assets folder.</span></div></div>'
    )


def section(sid: str, title: str, body: str) -> str:
    return H(f'<section class="sec" id="{sid}"><h2>{e(title)}</h2>{body}</section>')


# --------------------------------------------------------------------------- styles
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Public+Sans:wght@400;500;600&display=swap');
:root{
  --board:#17352F; --board-dark:#112A25; --chalk:#F2F5EF; --gold:#E8C547; --ink:#12201C;
  --muted:#4D5C57; --line:#D6DDD8; --paper:#FBFCFA; --tint:#EEF2EE;
}
html, body, [class*="css"], .stApp{font-family:'Public Sans',system-ui,sans-serif;color:var(--ink);}
.stApp{background:var(--paper);}
#MainMenu, footer, header[data-testid="stHeader"]{visibility:hidden;height:0;}
.block-container{max-width:1100px;padding:4.6rem 1.5rem 3rem !important;}
h1,h2,h3{font-family:'Fraunces',Georgia,serif;letter-spacing:-0.01em;}
a{color:inherit;}
.nav{position:fixed;top:0;left:0;right:0;z-index:50;background:rgba(17,42,37,.96);backdrop-filter:blur(6px);}
.nav-in{max-width:1100px;margin:0 auto;padding:0 1.5rem;height:52px;display:flex;align-items:center;justify-content:space-between;gap:1rem;}
.nav-brand{font-family:'Fraunces',serif;font-weight:700;color:var(--chalk);text-decoration:none;font-size:1.05rem;white-space:nowrap;}
.nav-links{display:flex;gap:1.2rem;overflow-x:auto;scrollbar-width:none;}
.nav-links a{color:#C9D5CF;text-decoration:none;font-size:.86rem;font-weight:500;white-space:nowrap;padding:.3rem 0;border-bottom:2px solid transparent;}
.nav-links a:hover,.nav-links a:focus-visible{color:#fff;border-bottom-color:var(--gold);outline:none;}
.sec,.contact{scroll-margin-top:72px;}
.sec{margin-top:3.6rem;}
.sec h2{font-size:1.9rem;line-height:1.2;margin:0 0 1.4rem;padding-bottom:.7rem;border-bottom:1px solid var(--line);}
.hero{background:var(--board);color:var(--chalk);border-radius:6px;padding:3rem 3rem 2.6rem;display:grid;grid-template-columns:1.55fr 1fr;gap:3rem;align-items:center;
  background-image:linear-gradient(rgba(242,245,239,.045) 1px,transparent 1px);background-size:100% 34px;position:relative;overflow:hidden;}
.hero h1{font-size:3.5rem;line-height:1.04;margin:0 0 .9rem;color:#fff;font-weight:700;}
.hero .role{font-size:1.15rem;color:var(--gold);font-weight:500;margin:0 0 1.2rem;}
.hero p{font-size:1.02rem;line-height:1.7;color:#D8E1DC;max-width:56ch;margin:0 0 1.6rem;}
.btns{display:flex;flex-wrap:wrap;gap:.7rem;}
.btn{display:inline-block;padding:.7rem 1.15rem;border-radius:4px;font-weight:600;font-size:.93rem;text-decoration:none;border:1.5px solid var(--chalk);color:var(--chalk);}
.btn.solid{background:var(--gold);border-color:var(--gold);color:var(--board-dark);}
.btn:hover,.btn:focus-visible{background:#fff;color:var(--board-dark);border-color:#fff;outline:none;}
.btn.solid:hover,.btn.solid:focus-visible{background:#F3D86B;border-color:#F3D86B;}
.photo{justify-self:center;position:relative;width:min(100%,290px);}
.photo::before{content:"";position:absolute;inset:14px -14px -14px 14px;border:2px solid var(--gold);border-radius:4px;}
.photo img{position:relative;display:block;width:100%;height:auto;border-radius:4px;aspect-ratio:3/4;object-fit:cover;}
.facts{display:grid;grid-template-columns:repeat(4,1fr);background:var(--board-dark);border-radius:0 0 6px 6px;margin-top:-4px;}
.fact{padding:1.2rem 1.4rem;border-right:1px solid rgba(242,245,239,.14);}
.fact:last-child{border-right:none;}
.fact b{display:block;font-family:'Fraunces',serif;font-size:1.65rem;color:var(--gold);font-weight:700;}
.fact span{font-size:.83rem;line-height:1.4;color:#C9D5CF;display:block;margin-top:.2rem;}
.about{display:grid;grid-template-columns:1.6fr 1fr;gap:2.4rem;}
.about p{font-size:1.04rem;line-height:1.75;margin:0;max-width:62ch;}
.about h3{font-size:1.02rem;margin:0 0 .7rem;}
.chips{display:flex;flex-wrap:wrap;gap:.45rem;}
.chip{background:var(--tint);border:1px solid var(--line);border-radius:999px;padding:.32rem .8rem;font-size:.85rem;}
.tl{position:relative;margin-left:.5rem;padding-left:1.8rem;border-left:2px solid var(--line);}
.tl-item{position:relative;padding-bottom:1.9rem;}
.tl-item:last-child{padding-bottom:0;}
.tl-item::before{content:"";position:absolute;left:calc(-1.8rem - 7px);top:.4rem;width:12px;height:12px;border-radius:50%;background:var(--board);border:2px solid var(--paper);box-shadow:0 0 0 2px var(--board);}
.tl-when{font-size:.84rem;font-weight:600;color:var(--board);}
.tl h3{font-size:1.28rem;margin:.15rem 0 .1rem;}
.tl .org{color:var(--muted);font-size:.94rem;margin-bottom:.6rem;}
.tl ul{margin:0;padding-left:1.1rem;}
.tl li{line-height:1.65;margin-bottom:.3rem;max-width:70ch;}
.lnk{color:var(--board);font-weight:600;font-size:.88rem;text-decoration:underline;text-underline-offset:3px;}
.lnk:hover,.lnk:focus-visible{color:#000;}
.edu{border:1px solid var(--line);border-left:6px solid var(--board);border-radius:4px;padding:1.4rem 1.6rem;background:#fff;}
.edu h3{font-size:1.3rem;margin:0 0 .15rem;}
.edu .where{color:var(--muted);margin-bottom:.8rem;}
.edu dl{display:grid;grid-template-columns:max-content 1fr;gap:.35rem 1.2rem;margin:0;}
.edu dt{font-weight:600;}
.edu dd{margin:0;line-height:1.55;}
.cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem;}
.group h3{font-size:1.05rem;margin:0 0 .7rem;}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;}
.card{border:1px solid var(--line);border-radius:4px;padding:1.1rem 1.2rem;background:#fff;display:flex;flex-direction:column;gap:.25rem;}
.card h3{font-size:1.08rem;margin:0;line-height:1.25;}
.card .by{color:var(--muted);font-size:.88rem;}
.card .meta{font-size:.82rem;font-weight:600;color:var(--board);}
.card p{font-size:.88rem;line-height:1.55;margin:.2rem 0 0;color:var(--ink);}
.card .lnk{margin-top:auto;padding-top:.5rem;}
.sub{font-size:1.15rem;margin:0 0 .9rem;}
.entry{padding:0 0 1.05rem;margin-bottom:1.05rem;border-bottom:1px solid var(--line);}
.entry:last-child{border-bottom:none;margin-bottom:0;padding-bottom:0;}
.entry b{display:block;line-height:1.35;}
.entry .meta{font-size:.83rem;color:var(--muted);margin:.1rem 0 .3rem;}
.entry p{font-size:.9rem;line-height:1.6;margin:0 0 .3rem;}
.contact{background:var(--board);color:var(--chalk);border-radius:6px;padding:2.6rem 3rem;display:grid;grid-template-columns:1.2fr 1fr;gap:2rem;align-items:center;}
.contact h2{color:#fff;border:none;padding:0;margin:0 0 .7rem;}
.contact p{color:#D8E1DC;line-height:1.65;margin:0;max-width:46ch;}
.crow{display:grid;gap:.9rem;}
.crow div span{display:block;font-size:.8rem;color:#A9BAB2;}
.crow a{color:#fff;font-weight:600;text-decoration:none;word-break:break-all;border-bottom:1px solid var(--gold);}
.crow a:hover,.crow a:focus-visible{color:var(--gold);outline:none;}
.foot{text-align:center;color:var(--muted);font-size:.84rem;margin-top:2.4rem;}
div[data-testid="stDownloadButton"] button{background:var(--board);color:#fff;border:none;border-radius:4px;font-weight:600;padding:.6rem 1.2rem;}
div[data-testid="stDownloadButton"] button:hover{background:var(--board-dark);color:var(--gold);}
@media (max-width:860px){
  .hero{grid-template-columns:1fr;padding:2rem 1.5rem;gap:2rem;}
  .hero h1{font-size:2.5rem;}
  .photo{order:-1;width:min(70%,240px);}
  .facts{grid-template-columns:repeat(2,1fr);}
  .fact:nth-child(2){border-right:none;}
  .fact:nth-child(-n+2){border-bottom:1px solid rgba(242,245,239,.14);}
  .about,.cols3,.cards,.contact{grid-template-columns:1fr;}
  .contact{padding:2rem 1.5rem;}
  .nav-brand{display:none;}
}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth;}}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


# --------------------------------------------------------------------------- page
NAV = [("about", "About"), ("experience", "Experience"), ("education", "Education"), ("toolbox", "Toolbox"),
       ("certifications", "Certifications"), ("service", "Leadership and awards"), ("contact", "Contact")]
st.markdown(H(f"""
<nav class="nav" aria-label="Sections"><div class="nav-in">
<a class="nav-brand" href="#top">{e(NAME)}</a>
<div class="nav-links">{''.join(f'<a href="#{i}">{e(t)}</a>' for i, t in NAV)}</div>
</div></nav>
"""), unsafe_allow_html=True)

# Hero
hero = f"""
<div id="top"></div>
<header class="hero">
<div>
<h1>{e(NAME)}</h1>
<div class="role">Mathematics educator, growing in data analytics</div>
<p>{e(ABOUT)}</p>
<div class="btns">
<a class="btn solid" href="mailto:{e(EMAIL)}">Email me</a>
<a class="btn" href="{GITHUB}" target="_blank" rel="noopener">GitHub profile</a>
<a class="btn" href="#experience">See my experience</a>
</div>
</div>
{photo_html()}
</header>
<div class="facts">{''.join(f'<div class="fact"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in FACTS)}</div>
"""
st.markdown(H(hero), unsafe_allow_html=True)

# About
about = f"""
<div class="about">
<p>{e(ABOUT)}</p>
<div><h3>Relevant modules</h3><div class="chips">{''.join(f'<span class="chip">{e(m)}</span>' for m in MODULES)}</div></div>
</div>
"""
st.markdown(section("about", "About", about), unsafe_allow_html=True)

# Experience
items = []
for x in EXPERIENCE:
    pts = "".join(f"<li>{e(p)}</li>" for p in x["points"])
    lk = f'<div>{link(x["link"][1], x["link"][0])}</div>' if x.get("link") else ""
    items.append(f"""
<div class="tl-item"><div class="tl-when">{e(x['when'])}</div>
<h3>{e(x['role'])}</h3><div class="org">{e(x['org'])}, {e(x['place'])}</div>
<ul>{pts}</ul>{lk}</div>""")
st.markdown(section("experience", "Work experience", f'<div class="tl">{"".join(items)}</div>'), unsafe_allow_html=True)

# Education
edu = """
<div class="edu">
<h3>Bachelor of Science in Mathematics Education</h3>
<div class="where">University of Lagos, Nigeria &nbsp;|&nbsp; 09/2018 to 12/2024</div>
<dl>
<dt>Classification</dt><dd>Second Class Honours (Upper Division), CGPA 4.04 / 5.00</dd>
<dt>Thesis</dt><dd>Effect of Culture-Techno Contextual Approach on Student Motivation to Learn Mathematics at Senior Secondary School.</dd>
<dt>Modules</dt><dd>Numerical Analysis, Real Analysis, Calculus, Linear Algebra, Probability Theory, Mathematical Modelling, Differential Equations</dd>
</dl></div>
"""
st.markdown(section("education", "Education", edu), unsafe_allow_html=True)

# Toolbox
groups = "".join(
    f'<div class="group"><h3>{e(t)}</h3><div class="chips">{"".join(f"<span class=chip>{e(s)}</span>" for s in skills)}</div></div>'
    for t, skills in TOOLBOX)
st.markdown(section("toolbox", "Toolbox", f'<div class="cols3">{groups}</div>'), unsafe_allow_html=True)

# Certifications
cards = []
for c in CERTS:
    meta = f'<div class="meta">{e(c["when"])}</div>' if c.get("when") else ""
    note = f'<p>{e(c["note"])}</p>' if c.get("note") else ""
    lk = link(c["link"], "View certificate") if c.get("link") else ""
    cards.append(f'<div class="card"><h3>{e(c["title"])}</h3><div class="by">{e(c["by"])}</div>{meta}{note}{lk}</div>')
st.markdown(section("certifications", "Certifications and training", f'<div class="cards">{"".join(cards)}</div>'),
            unsafe_allow_html=True)

# Leadership, volunteering, awards
def entries(rows):
    out = []
    for r in rows:
        title, org, when, text = r[0], r[1], r[2], r[3]
        lk = ""
        if len(r) > 4 and r[4]:
            lk = f'<div>{link(r[4], "View evidence")}</div>'
        out.append(f'<div class="entry"><b>{e(title)}</b><div class="meta">{e(org)} &nbsp;|&nbsp; {e(when)}</div><p>{e(text)}</p>{lk}</div>')
    return "".join(out)

award_html = []
for t, org, text, links in AWARDS:
    lks = " ".join(link(u, f"View evidence {n}" if len(links) > 1 else "View evidence") for n, u in enumerate(links, 1))
    award_html.append(f'<div class="entry"><b>{e(t)}</b><div class="meta">{e(org)}</div><p>{e(text)}</p><div>{lks}</div></div>')

service = f"""
<div class="cols3">
<div><h3 class="sub">Leadership</h3>{entries(LEADERSHIP)}</div>
<div><h3 class="sub">Volunteering</h3>{entries(VOLUNTEERING)}</div>
<div><h3 class="sub">Honours and awards</h3>{''.join(award_html)}</div>
</div>
"""
st.markdown(section("service", "Leadership, volunteering and awards", service), unsafe_allow_html=True)

# Contact
contact = f"""
<div class="contact" id="contact">
<div><h2>Let's talk</h2>
<p>Open to academic opportunities, teaching and data analytics work. Email is the quickest way to reach me.</p></div>
<div class="crow">
<div><span>Email</span><a href="mailto:{e(EMAIL)}">{e(EMAIL)}</a></div>
<div><span>GitHub</span><a href="{GITHUB}" target="_blank" rel="noopener">github.com/OniSamson</a></div>
<div><span>Phone</span><a href="tel:+2348162752066">{e(PHONE)}</a></div>
</div></div>
"""
st.markdown(H('<div class="sec" id="contact-anchor" style="margin-top:3.6rem"></div>') + H(contact), unsafe_allow_html=True)

if CV.exists():
    st.write("")
    st.download_button("Download my CV (PDF)", data=CV.read_bytes(), file_name="Samson_Oni_CV.pdf",
                       mime="application/pdf")

st.markdown(H(f'<div class="foot">&copy; {NAME}. Built with Streamlit.</div>'), unsafe_allow_html=True)
