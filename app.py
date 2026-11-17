import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(page_title="MoleculeLab", page_icon="⚛️", layout="wide")
MOLECULES = [
 {"name":"Water","formula":"H₂O","mass":18.02,"type":"Inorganic","description":"Essential compound found in living organisms.","atoms":{"H":2,"O":1},"cid":962},
 {"name":"Carbon dioxide","formula":"CO₂","mass":44.01,"type":"Inorganic","description":"Gas used by plants during photosynthesis.","atoms":{"C":1,"O":2},"cid":280},
 {"name":"Methane","formula":"CH₄","mass":16.04,"type":"Organic","description":"The simplest alkane and a component of natural gas.","atoms":{"C":1,"H":4},"cid":297},
 {"name":"Ammonia","formula":"NH₃","mass":17.03,"type":"Inorganic","description":"A compound made from nitrogen and hydrogen.","atoms":{"N":1,"H":3},"cid":222},
 {"name":"Glucose","formula":"C₆H₁₂O₆","mass":180.16,"type":"Organic","description":"A simple sugar and important energy source.","atoms":{"C":6,"H":12,"O":6},"cid":5793},
 {"name":"Ethanol","formula":"C₂H₆O","mass":46.07,"type":"Organic","description":"A small organic molecule also called ethyl alcohol.","atoms":{"C":2,"H":6,"O":1},"cid":702},
 {"name":"Oxygen","formula":"O₂","mass":32.00,"type":"Inorganic","description":"A diatomic gas important for respiration.","atoms":{"O":2},"cid":977},
 {"name":"Benzene","formula":"C₆H₆","mass":78.11,"type":"Organic","description":"An aromatic hydrocarbon with a six-carbon ring.","atoms":{"C":6,"H":6},"cid":241},
]
lookup={m["name"]:m for m in MOLECULES}
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono&family=Manrope:wght@400;600;700;800&display=swap');
html,body,[class*="css"]{font-family:Manrope,sans-serif}
.stApp{background:#090e18;color:#edf4ff}
section[data-testid="stSidebar"]{background:#0b121e}
.hero{padding:35px;border:1px solid #294052;border-radius:14px;background:radial-gradient(ellipse at 80% 50%,#1b4550,#101927 70%);margin-bottom:25px}
.hero h1{font-size:52px;line-height:1.05}.hero span{color:#76e4c2}
.eyebrow{font:10px 'DM Mono';letter-spacing:2px;color:#76e4c2}
.tile{background:#101927;border:1px solid #26364b;border-radius:10px;padding:17px;min-height:125px;margin-bottom:12px}
.tile small{color:#76e4c2;font:10px 'DM Mono'}.tile p{color:#8494aa;font-size:12px}
div[data-testid="stMetric"]{background:#101927;border:1px solid #26364b;padding:14px;border-radius:9px}
</style>""",unsafe_allow_html=True)

with st.sidebar:
 st.markdown("## ✳ MoleculeLab")
 st.caption("MOLECULAR UNIVERSE")
 page=st.radio("WORKSPACE",["Overview","Explore molecules","3D visualizer","Compare","Analytics","Learning studio","About"])
 st.divider()
 st.caption("● MOLECULAR ENGINE ONLINE")
 st.caption("Educational use only")

if page=="Overview":
 st.markdown('<div class="hero"><div class="eyebrow">✦ THE MOLECULAR UNIVERSE</div><h1>Visualize the<br><span>invisible.</span></h1><p>Explore chemical space. Discover molecular structures, compare properties and make chemistry easier to understand.</p></div>',unsafe_allow_html=True)
 st.subheader("Explore the elements")
 cards=[("01 / DISCOVERY","Explore molecules","Search a starter library of familiar compounds."),("02 / STRUCTURE","3D visualizer","View molecular structures in interactive 3D."),("03 / ANALYSIS","Compare","Compare formulas and molecular properties."),("04 / INSIGHTS","Analytics","Explore a snapshot of the sample library."),("05 / LEARNING","Learning studio","Review chemistry concepts and vocabulary."),("06 / PROJECT","About","Learn about this educational project.")]
 cols=st.columns(3)
 for i,(tag,title,desc) in enumerate(cards):
  with cols[i%3]: st.markdown(f'<div class="tile"><small>{tag}</small><h3>{title}</h3><p>{desc}</p></div>',unsafe_allow_html=True)
 st.info("Choose a section from the left sidebar.")
elif page=="Explore molecules":
 st.markdown('<p class="eyebrow">DISCOVERY / 01</p>',unsafe_allow_html=True);st.title("Explore molecules")
 q=st.text_input("Search by name, formula or type",placeholder="Example: water, H₂O")
 found=[m for m in MOLECULES if q.lower() in (m["name"]+m["formula"]+m["type"]).lower()]
 st.caption(f"{len(found)} MOLECULE(S) FOUND")
 for start in range(0,len(found),2):
  cols=st.columns(2)
  for col,m in zip(cols,found[start:start+2]):
   with col:
    with st.container(border=True):
     st.subheader("✧ "+m["name"]);st.markdown(f"**{m['formula']}** · {m['mass']:.2f} g/mol")
     st.caption(m["type"]);st.write(m["description"])
 if not found: st.warning("No matching molecule found.")
elif page=="3D visualizer":
 st.markdown('<p class="eyebrow">STRUCTURE / 02</p>',unsafe_allow_html=True);st.title("3D visualizer")
 name=st.selectbox("Choose compound",list(lookup));m=lookup[name]
 a,b,c=st.columns(3);a.metric("Formula",m["formula"]);b.metric("Molecular mass",f"{m['mass']:.2f} g/mol");c.metric("Type",m["type"])
 st.write(m["description"])
 if st.button("Load 3D structure",type="primary"):
  html=f"""<div id="v" style="height:460px;background:#0b1420;border-radius:10px"></div>
  <script src="https://3Dmol.org/build/3Dmol-min.js"></script><script>
  const el=document.getElementById('v');const v=$3Dmol.createViewer(el,{{backgroundColor:'#0b1420'}});
  fetch('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{m["cid"]}/SDF?record_type=3d')
  .then(r=>{{if(!r.ok)throw Error();return r.text()}}).then(s=>{{v.addModel(s,'sdf');v.setStyle({{}},{{stick:{{radius:.16}},sphere:{{scale:.25}}}});v.zoomTo();v.render();}})
  .catch(()=>el.innerHTML='<p style="color:white;padding:20px">Structure could not be loaded. Try again later.</p>');</script>"""
  components.html(html,height=480)
 else: st.info("Select a molecule and press Load 3D structure. Internet access is required.")
elif page=="Compare":
 st.markdown('<p class="eyebrow">ANALYSIS / 03</p>',unsafe_allow_html=True);st.title("Compare molecules")
 c1,c2=st.columns(2)
 with c1:n1=st.selectbox("MOLECULE A",list(lookup),0)
 with c2:n2=st.selectbox("MOLECULE B",list(lookup),1)
 a,b=lookup[n1],lookup[n2]
 st.dataframe(pd.DataFrame({"Property":["Formula","Molecular mass","Type","Description"],n1:[a["formula"],f'{a["mass"]:.2f} g/mol',a["type"],a["description"]],n2:[b["formula"],f'{b["mass"]:.2f} g/mol',b["type"],b["description"]]}),hide_index=True,use_container_width=True)
elif page=="Analytics":
 st.markdown('<p class="eyebrow">INSIGHTS / 04</p>',unsafe_allow_html=True);st.title("Library analytics")
 counts={}
 for m in MOLECULES:
  for atom,n in m["atoms"].items():counts[atom]=counts.get(atom,0)+n
 organic=sum(m["type"]=="Organic" for m in MOLECULES)
 cols=st.columns(4)
 for col,label,value in zip(cols,["MOLECULES","ELEMENT TYPES","ORGANIC","INORGANIC"],[len(MOLECULES),len(counts),organic,len(MOLECULES)-organic]):col.metric(label,value)
 st.subheader("Atoms across the sample library")
 st.bar_chart(pd.DataFrame({"Atom count":counts}).sort_values("Atom count",ascending=False))
elif page=="Learning studio":
 st.markdown('<p class="eyebrow">KNOWLEDGE / 05</p>',unsafe_allow_html=True);st.title("Learning studio")
 lessons=[("What is a molecule?","A molecule is a group of two or more atoms held together by chemical bonds. Water (H₂O) and oxygen (O₂) are examples."),("Chemical formula","A chemical formula uses element symbols and numbers to show which atoms, and how many, are present."),("Covalent bond","A covalent bond forms when atoms share one or more pairs of electrons."),("Molecular geometry","Molecular geometry describes the three-dimensional arrangement of atoms.")]
 for i,(title,body) in enumerate(lessons,1):
  with st.expander(f"{i:02d} / {title}",expanded=i==1):st.write(body)
elif page=="About":
 st.markdown('<p class="eyebrow">ABOUT / 06</p>',unsafe_allow_html=True);st.title("About MoleculeLab")
 st.subheader("✳ Molecular Universe")
 st.write("MoleculeLab is an educational chemistry project with a searchable sample library, molecule comparison, learning notes and an optional 3D structure viewer.")
 st.info("The sample data is for learning and demonstration. Check trusted chemistry references for academic or laboratory work.")
st.divider();st.caption("MOLECULELAB · VISUALIZE THE INVISIBLE · EDUCATIONAL USE ONLY")
