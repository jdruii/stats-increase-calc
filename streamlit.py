import streamlit as st

# DATA DICTIONARY
CASTLE_SKINS = {
    "None": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 0.0, "soldier_hp_per": 0, "soldier_hp_pct": 0.0,
        "march_size": 0
    },
    "Steam Ark": {
        "hero_atk_base": 4000, "hero_atk_pct": 0.0, "hero_hp_base": 40000, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 20.0, "soldier_hp_per": 0, "soldier_hp_pct": 0.0,
        "march_size": 30
    },
    "Cloud Castle": {
        "hero_atk_base": 4000, "hero_atk_pct": 0.0, "hero_hp_base": 40000, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 45.0,
        "march_size": 30
    },
    "Cherry Blossom": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 30.0,
        "march_size": 30
    },
    "Pumpkin Town": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 30.0,
        "march_size": 30
    },
    "Fantasy Ferris Wheel": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 20.0,
        "march_size": 20
    },
    "Concerto": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 30.0,
        "march_size": 20
    },
    "Dreamlike Dance": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 30.0,
        "march_size": 30
    },
    "Crab Fortress": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 0.0, "soldier_hp_per": 0, "soldier_hp_pct": 40.0,
        "march_size": 30
    },
    "Skybound (League)": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 10.0, "soldier_hp_per": 0, "soldier_hp_pct": 50.0,
        "march_size": 20
    },
    "Mountain Prime ⚡": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 50.0,
        "march_size": 0,
        "active_skill": {"soldier_hp_pct": 30.0}
    },
    "Steel Citadel ⚡": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 0.0, "soldier_hp_per": 0, "soldier_hp_pct": 35.0,
        "march_size": 20,
        "active_skill": {"march_size": 100}
    },
    "Cake Castle": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 0.0, "soldier_hp_per": 0, "soldier_hp_pct": 30.0,
        "march_size": 20
    },
    "Nightfall Castle (Nature)": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 20.0, "soldier_hp_per": 0, "soldier_hp_pct": 70.0,
        "march_size": 30
    },
    "Tower of Chaos (Horde)": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 30.0, "soldier_hp_per": 0, "soldier_hp_pct": 50.0,
        "march_size": 30
    },
    "Cute Egg Fun Castle": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 30.0,
        "march_size": 30
    },
    "Secluded Valley": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 30.0,
        "march_size": 30
    },
    "Shell Castle (Nature) ⚡": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 20.0, "soldier_hp_per": 0, "soldier_hp_pct": 20.0,
        "march_size": 0,
        "active_skill": {"soldier_hp_pct": 120.0}
    },
    "Temple of Soul": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 10.0, "soldier_hp_per": 0, "soldier_hp_pct": 25.0,
        "march_size": 20
    },
    "Blazing Fortress (Horde) ⚡": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 20.0, "soldier_hp_per": 0, "soldier_hp_pct": 20.0,
        "march_size": 0,
        "active_skill": {"soldier_atk_pct": 30.0, "soldier_hp_pct": 60.0}
    },
    "Spooky House": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 20.0, "soldier_hp_per": 0, "soldier_hp_pct": 5.0,
        "march_size": 30
    },
    "Fantasy Castle": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 30.0,
        "march_size": 30
    },
    "Christmas Castle": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 5.0, "soldier_hp_per": 0, "soldier_hp_pct": 30.0,
        "march_size": 30
    },
    "Unbeatable Glory": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 15.0, "soldier_hp_per": 0, "soldier_hp_pct": 35.0,
        "march_size": 30
    },
    "Season Castle": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 3.0, "soldier_hp_per": 0, "soldier_hp_pct": 25.0,
        "march_size": 15
    }
}

# SESSION STATE INIT
default_state = {
    "base_stats_done": False,
    "compare_mode": False,

    "hero_atk_base": 120798,
    "hero_atk_pct": 697.6,
    "hero_hp_base": 1563289,
    "hero_hp_pct": 1498.7,

    "march_size": 1815,
    "soldier_atk_per": 70,
    "soldier_atk_pct": 846.0,
    "soldier_hp_per": 1015,
    "soldier_hp_pct": 1785.26,
}

def clear_base_stats():
    st.session_state.hero_atk_base = 0
    st.session_state.hero_atk_pct = 0.0
    st.session_state.hero_hp_base = 0
    st.session_state.hero_hp_pct = 0.0
    st.session_state.soldier_atk_per = 0
    st.session_state.soldier_atk_pct = 0.0
    st.session_state.soldier_hp_per = 0
    st.session_state.soldier_hp_pct = 0.0
    st.session_state.march_size = 0
    st.rerun()

for key, value in default_state.items():
    if key not in st.session_state:
        st.session_state[key] = value

if "upgrade1" not in st.session_state:
    st.session_state.upgrade1 = {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 0.0, "soldier_hp_per": 0, "soldier_hp_pct": 0.0,
        "march_size": 0,
    }

if "upgrade2" not in st.session_state:
    st.session_state.upgrade2 = {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 0.0, "soldier_hp_per": 0, "soldier_hp_pct": 0.0,
        "march_size": 0,
    }

# CONFIG
st.set_page_config(page_title="Stat Increase Calculator", layout="centered")

st.title("Stat Increase Calculator")

# INPUT
if not st.session_state.base_stats_done:
    st.markdown("""
    Ever wondered if getting the Cloud Castle skin is really better than getting the Tower of Chaos skin for your Horde queue? 
    Well, this is the tool for you. See the actual raw stat gain from different sources and how it affects your heroes!
    """)

    st.caption("""
    Note that for now, only Attack and HP stats are considered, as well as stats that can be directly turned into Attack or HP like Hero Level Cap and Soldier 
    Count. Other stats like Crit, Block, etc are ignored.
    """)

    st.caption("Re: Hero Level Cap - +1 is turned into +3 March Size, +400 Hero ATK, and +4000 Hero HP.")

    st.header("Base Stats Input")

    st.markdown("""
    Input the current stats of your hero. 
    To see these stats, go to your hero screen -> click your desired hero -> click the (i) beside its stats.
    """)

    st.caption("The default values here are the actual stats of my Wukong as of the time that I made this. Your values should more or less look the same.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hero Stats")
        st.session_state.hero_atk_base = st.number_input("Hero Attack Base", min_value=0, step=1, value=st.session_state.hero_atk_base)
        st.session_state.hero_atk_pct = st.number_input("Hero Attack Percentage (%)", min_value=0.0, step=0.1, value=st.session_state.hero_atk_pct)
        st.session_state.hero_hp_base = st.number_input("Hero HP Base", min_value=0, step=1, value=st.session_state.hero_hp_base)
        st.session_state.hero_hp_pct = st.number_input("Hero HP Percentage (%)", min_value=0.0, step=0.1, value=st.session_state.hero_hp_pct)

        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        if st.button("Clear Fields", use_container_width=True):
            clear_base_stats()

    with col2:
        st.subheader("Soldier Stats")
        st.session_state.soldier_atk_per = st.number_input("Soldier Attack per Soldier", min_value=0, step=1, value=st.session_state.soldier_atk_per)
        st.session_state.soldier_atk_pct = st.number_input("Soldier Attack Percentage (%)", min_value=0.0, step=0.1, value=st.session_state.soldier_atk_pct)
        st.session_state.soldier_hp_per = st.number_input("Soldier HP per Soldier", min_value=0, step=1, value=st.session_state.soldier_hp_per)
        st.session_state.soldier_hp_pct = st.number_input("Soldier HP Percentage (%)", min_value=0.0, step=0.1, value=st.session_state.soldier_hp_pct)
        st.session_state.march_size = st.number_input("March Size", min_value=0, step=1, value=st.session_state.march_size)

    soldier_atk_base = (st.session_state.soldier_atk_per * st.session_state.march_size)
    soldier_hp_base = (st.session_state.soldier_hp_per * st.session_state.march_size)
    hero_atk_total = (st.session_state.hero_atk_base * (1 + st.session_state.hero_atk_pct / 100))
    hero_hp_total = (st.session_state.hero_hp_base * (1 + st.session_state.hero_hp_pct / 100))
    soldier_atk_total = (soldier_atk_base * (1 + st.session_state.soldier_atk_pct / 100))
    soldier_hp_total = (soldier_hp_base * (1 + st.session_state.soldier_hp_pct / 100))

    st.header("Total Stats")
    st.markdown("""
    Make sure that the calculated value below matches the total values in your hero screen before proceeding.
    """)

    rev_col1, rev_col2 = st.columns(2)
    with rev_col1:
        st.metric("Total Hero ATK", f"{hero_atk_total:,.0f}")
        st.metric("Total Hero HP", f"{hero_hp_total:,.0f}")
    with rev_col2:
        st.metric("Total Soldier ATK", f"{soldier_atk_total:,.0f}")
        st.metric("Total Soldier HP", f"{soldier_hp_total:,.0f}")

    if st.button("✔ Confirm", use_container_width=True, type="primary"):
        st.session_state.base_stats_done = True
        st.rerun()

# CALC
else:
    if st.button("↩ Return"):
        st.session_state.base_stats_done = False
        st.rerun()

    def apply_castle1():
        selection = st.session_state.castle_search_1
        if selection != "None":
            skin = CASTLE_SKINS[selection]
            st.session_state.upgrade1.update(skin)
            # FORCE update the widget states so the input boxes change
            st.session_state.u1_hab = skin["hero_atk_base"]
            st.session_state.u1_hap = skin["hero_atk_pct"]
            st.session_state.u1_hhb = skin["hero_hp_base"]
            st.session_state.u1_hhp = skin["hero_hp_pct"]
            st.session_state.u1_sap = skin["soldier_atk_per"]
            st.session_state.u1_s_atk_pct = skin["soldier_atk_pct"]
            st.session_state.u1_shp = skin["soldier_hp_per"]
            st.session_state.u1_s_hp_pct = skin["soldier_hp_pct"]
            st.session_state.u1_sc = skin["march_size"]


    def apply_castle2():
        selection = st.session_state.castle_search_2
        if selection != "None":
            skin = CASTLE_SKINS[selection]
            st.session_state.upgrade2.update(skin)
            # FORCE update the widget states
            st.session_state.u2_ha = skin["hero_atk_base"]
            st.session_state.u2_hap = skin["hero_atk_pct"]
            st.session_state.u2_hh = skin["hero_hp_base"]
            st.session_state.u2_hhp = skin["hero_hp_pct"]
            st.session_state.u2_sa = skin["soldier_atk_per"]
            st.session_state.u2_sap = skin["soldier_atk_pct"]
            st.session_state.u2_sh = skin["soldier_hp_per"]
            st.session_state.u2_shp = skin["soldier_hp_pct"]
            st.session_state.u2_sc = skin["march_size"]


    def clear_upgrade1():
        st.session_state.upgrade1.update(CASTLE_SKINS["None"])
        for k in ["u1_hab", "u1_hap", "u1_hhb", "u1_hhp", "u1_sap", "u1_s_atk_pct", "u1_shp", "u1_s_hp_pct", "u1_sc"]:
            if k in st.session_state:
                st.session_state[k] = 0
        st.session_state.castle_search_1 = "None"


    def clear_upgrade2():
        st.session_state.upgrade2.update(CASTLE_SKINS["None"])
        for k in ["u2_ha", "u2_hap", "u2_hh", "u2_hhp", "u2_sa", "u2_sap", "u2_sh", "u2_shp", "u2_sc"]:
            if k in st.session_state:
                st.session_state[k] = 0
        st.session_state.castle_search_2 = "None"


    def calculate_total(upgrade):
        soldier_atk_base = (st.session_state.soldier_atk_per + upgrade["soldier_atk_per"]) * \
                           (st.session_state.march_size + upgrade["march_size"])
        soldier_hp_base = (st.session_state.soldier_hp_per + upgrade["soldier_hp_per"]) * \
                          (st.session_state.march_size + upgrade["march_size"])

        hero_atk = (st.session_state.hero_atk_base + upgrade["hero_atk_base"]) * \
                   (1 + (st.session_state.hero_atk_pct + upgrade["hero_atk_pct"]) / 100)
        hero_hp = (st.session_state.hero_hp_base + upgrade["hero_hp_base"]) * \
                  (1 + (st.session_state.hero_hp_pct + upgrade["hero_hp_pct"]) / 100)

        soldier_atk = soldier_atk_base * (1 + (st.session_state.soldier_atk_pct + upgrade["soldier_atk_pct"]) / 100)
        soldier_hp = soldier_hp_base * (1 + (st.session_state.soldier_hp_pct + upgrade["soldier_hp_pct"]) / 100)

        return hero_atk + soldier_atk, hero_hp + soldier_hp


    def format_active_stats(upgrade):
        parts = []
        display_map = [
            ("hero_atk_base", "Hero ATK"),
            ("hero_atk_pct", "Hero ATK %"),
            ("hero_hp_base", "Hero HP"),
            ("hero_hp_pct", "Hero HP %"),
            ("soldier_atk_per", "Soldier ATK"),
            ("soldier_atk_pct", "Soldier ATK %"),
            ("soldier_hp_per", "Soldier HP"),
            ("soldier_hp_pct", "Soldier HP %"),
            ("march_size", "March Size")
        ]
        for key, label in display_map:
            val = upgrade.get(key, 0)
            if val > 0:
                if "%" in label:
                    parts.append(f"{label}: +{int(val)}%")
                else:
                    parts.append(f"{label}: +{val:,}")
        return ", ".join(parts) if parts else "No bonus stats"

    base_hero_atk = st.session_state.hero_atk_base * (1 + st.session_state.hero_atk_pct / 100)
    base_hero_hp = st.session_state.hero_hp_base * (1 + st.session_state.hero_hp_pct / 100)
    base_soldier_atk = st.session_state.soldier_atk_per * st.session_state.march_size * (1 + st.session_state.soldier_atk_pct / 100)
    base_soldier_hp = st.session_state.soldier_hp_per * st.session_state.march_size * (1 + st.session_state.soldier_hp_pct / 100)
    total_base_atk = base_hero_atk + base_soldier_atk
    total_base_hp = base_hero_hp + base_soldier_hp

    st.subheader("Calculate Increase")

    st.markdown("""
    Input the stats that you're gaining from a source. Alternatively, you can use the search bar to find in-game items that gives stat bonuses like Castle Skins.
    """)

    st.caption("Note: For now, only the legendary (gold) castle skins have templates. More categories will be added in the future (maybe). Attack, HP, "
               "and March Size from active skills of castle skins are also TBA.")

    # CASTLE SEARCH 1
    show_template1 = st.checkbox("Search Castle Skin", key="show_t1")
    if show_template1:
        st.selectbox(
            "⚡ denotes that the castle skin has an active skill that can be translated into ATK or HP.",
            options=["None"] + sorted([k for k in CASTLE_SKINS.keys() if k != "None"]),
            key="castle_search_1",
            on_change=apply_castle1
        )
    else:
        if st.session_state.get("castle_search_1", "None") != "None":
            clear_upgrade1()

    eff_up1 = st.session_state.upgrade1.copy()
    active_text1 = ""
    skin1_data = CASTLE_SKINS.get(st.session_state.get("castle_search_1", "None"), {})

    if "active_skill" in skin1_data:
        active_bonuses = skin1_data["active_skill"]
        label1 = format_active_stats(active_bonuses)
        if st.checkbox(f"⚡ Include Active Skill: {label1}", key="act1"):
            for k, v in active_bonuses.items():
                eff_up1[k] += v
            active_text1 = f" **Active Skill:** `{label1}`"

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Hero Upgrade**")
        st.session_state.upgrade1["hero_atk_base"] = st.number_input("+Hero ATK Base", min_value=0, step=1, key="u1_hab")
        st.session_state.upgrade1["hero_atk_pct"] = st.number_input("+Hero ATK %", min_value=0.0, step=0.1, key="u1_hap")
        st.session_state.upgrade1["hero_hp_base"] = st.number_input("+Hero HP Base", min_value=0, step=1, key="u1_hhb")
        st.session_state.upgrade1["hero_hp_pct"] = st.number_input("+Hero HP %", min_value=0.0, step=0.1, key="u1_hhp")

        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        st.button("Clear Calc Fields", on_click=clear_upgrade1, use_container_width=True)

    with col2:
        st.markdown("**Soldier Upgrade**")
        st.session_state.upgrade1["soldier_atk_per"] = st.number_input("+Soldier ATK per Soldier", min_value=0, step=1, key="u1_sap")
        st.session_state.upgrade1["soldier_atk_pct"] = st.number_input("+Soldier ATK %", min_value=0.0, step=0.1, key="u1_s_atk_pct")
        st.session_state.upgrade1["soldier_hp_per"] = st.number_input("+Soldier HP per Soldier", min_value=0, step=1, key="u1_shp")
        st.session_state.upgrade1["soldier_hp_pct"] = st.number_input("+Soldier HP %", min_value=0.0, step=0.1, key="u1_s_hp_pct")
        st.session_state.upgrade1["march_size"] = st.number_input("+March Size", min_value=0, step=1, key="u1_sc")

    # CALCULATE UPGRADE 1 VALUES
    t1_atk, t1_hp = calculate_total(eff_up1)
    atk_g1 = t1_atk - total_base_atk
    hp_g1 = t1_hp - total_base_hp
    atk_p1 = (atk_g1 / total_base_atk * 100) if total_base_atk else 0
    hp_p1 = (hp_g1 / total_base_hp * 100) if total_base_hp else 0

    if not st.session_state.compare_mode:
        st.divider()
        st.subheader("Actual Stat Increase")
        res1, res2 = st.columns(2)
        with res1:
            st.metric("Attack Gain", f"{atk_g1:,.0f}", f"{atk_p1:.2f}%")
        with res2:
            st.metric("HP Gain", f"{hp_g1:,.0f}", f"{hp_p1:.2f}%")

        if st.button("Compare", use_container_width=True):
            st.session_state.compare_mode = True
            st.rerun()

    # COMPARE
    if st.session_state.compare_mode:
        st.divider()

        st.subheader("Compare Options")
        st.markdown("""
        Input another set of stat increase or select another castle skin to compare.
        """)

        # CASTLE SEARCH 2
        show_template2 = st.checkbox("Search Castle Skin", key="show_t2")
        if show_template2:
            st.selectbox(
                "⚡ denotes that the castle skin has an active skill that can be translated into ATK or HP.",
                options=["None"] + sorted([k for k in CASTLE_SKINS.keys() if k != "None"]),
                key="castle_search_2",
                on_change=apply_castle2
            )
        else:
            if st.session_state.get("castle_search_2", "None") != "None":
                clear_upgrade2()

        eff_up2 = st.session_state.upgrade2.copy()
        skin2_data = CASTLE_SKINS.get(st.session_state.get("castle_search_2", "None"), {})

        eff_up2 = st.session_state.upgrade2.copy()
        active_text2 = ""
        skin2_data = CASTLE_SKINS.get(st.session_state.get("castle_search_2", "None"), {})

        if "active_skill" in skin2_data:
            active_bonuses = skin2_data["active_skill"]
            label2 = format_active_stats(active_bonuses)
            if st.checkbox(f"⚡ Include Active Skill: {label2}", key="act2"):
                for k, v in active_bonuses.items():
                    eff_up2[k] += v
                active_text2 = f"**Active Skill:** `{label2}`"

        t2_atk, t2_hp = calculate_total(eff_up2)

        col3, col4 = st.columns(2)
        with col3:
            st.markdown("**Hero Upgrade**")
            st.session_state.upgrade2["hero_atk_base"] = st.number_input("+Hero ATK Base", min_value=0, step=1, key="u2_ha")
            st.session_state.upgrade2["hero_atk_pct"] = st.number_input("+Hero ATK %", min_value=0.0, step=0.1, key="u2_hap")
            st.session_state.upgrade2["hero_hp_base"] = st.number_input("+Hero HP Base", min_value=0, step=1, key="u2_hh")
            st.session_state.upgrade2["hero_hp_pct"] = st.number_input("+Hero HP %", min_value=0.0, step=0.1, key="u2_hhp")

            st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
            st.button("Clear Compare Fields", on_click=clear_upgrade2, use_container_width=True, key="btn_clear_comp")

        with col4:
            st.markdown("**Soldier Upgrade**")
            st.session_state.upgrade2["soldier_atk_per"] = st.number_input("+Soldier ATK per Soldier", min_value=0, step=1, key="u2_sa")
            st.session_state.upgrade2["soldier_atk_pct"] = st.number_input("+Soldier ATK %", min_value=0.0, step=0.1, key="u2_sap")
            st.session_state.upgrade2["soldier_hp_per"] = st.number_input("+Soldier HP per Soldier", min_value=0, step=1, key="u2_sh")
            st.session_state.upgrade2["soldier_hp_pct"] = st.number_input("+Soldier HP %", min_value=0.0, step=0.1, key="u2_shp")
            st.session_state.upgrade2["march_size"] = st.number_input("+March Size", min_value=0, step=1, key="u2_sc")

        t2_atk, t2_hp = calculate_total(eff_up2)
        atk_g2 = t2_atk - total_base_atk
        hp_g2 = t2_hp - total_base_hp
        atk_p2 = (atk_g2 / total_base_atk * 100) if total_base_atk else 0
        hp_p2 = (hp_g2 / total_base_hp * 100) if total_base_hp else 0

        # SUMMARIES
        name1 = st.session_state.get("castle_search_1", "None")
        up1 = st.session_state.upgrade1
        title1 = f"{name1}" if name1 != "None" else "No Castle Selected"
        stats_text1 = format_active_stats(up1)

        name2 = st.session_state.get("castle_search_2", "None")
        up2 = st.session_state.upgrade2
        title2 = f"{name2}" if name2 != "None" else "No Castle Selected"
        stats_text2 = format_active_stats(up2)

        st.divider()

        # DISPLAY RESULT
        st.subheader("Comparison Result")

        combined_text1 = f"**{title1}** — `{stats_text1}`"
        if active_text1:
            combined_text1 += f"  \n{active_text1}"
        st.markdown(combined_text1)

        c1, c2 = st.columns(2)
        with c1:
            st.metric("Attack Gain", f"{atk_g1:,.0f}", f"{atk_p1:.2f}%")
        with c2:
            st.metric("HP Gain", f"{hp_g1:,.0f}", f"{hp_p1:.2f}%")

        st.write("")

        combined_text2 = f"**{title2}** — `{stats_text2}`"
        if active_text2:
            combined_text2 += f"  \n{active_text2}"
        st.markdown(combined_text2)

        c3, c4 = st.columns(2)
        with c3:
            st.metric("Attack Gain", f"{atk_g2:,.0f}", f"{atk_p2:.2f}%")
        with c4:
            st.metric("HP Gain", f"{hp_g2:,.0f}", f"{hp_p2:.2f}%")

        st.divider()

        _, close_col, _ = st.columns([1, 2, 1])
        with close_col:
            if st.button("Close Comparison", use_container_width=True):
                st.session_state.compare_mode = False
                st.rerun()
