import streamlit as st

# CONS
HERO_LEVEL_CAP_ATK = 500
HERO_LEVEL_CAP_HP = 5000
HERO_LEVEL_CAP_MARCH = 3

# HERO_LEVEL_CAP_TABLE = {
#     "1-30": {"hero_atk_base": 9, "hero_hp_base:": 90},
#     "31-50": {"hero_atk_base": 16.2, "hero_hp_base:": 162},
#     "51-70": {"hero_atk_base": 24.3, "hero_hp_base:": 243},
#     "71-90": {"hero_atk_base": 32.4, "hero_hp_base:": 324},
#     "91-100": {"hero_atk_base": 43.2, "hero_hp_base:": 432},
#     "101-110": {"hero_atk_base": 52.2, "hero_hp_base:": 522},
#     "111-120": {"hero_atk_base": 62.1, "hero_hp_base:": 621},
#     "121-130": {"hero_atk_base": 80.1, "hero_hp_base:": 801},
#     "131-140": {"hero_atk_base": 104.4, "hero_hp_base:": 1044},
#     "141-150": {"hero_atk_base": 130.5, "hero_hp_base:": 1277.7},
#     "151-160": {"hero_atk_base": 157.5, "hero_hp_base:": 1602.3},
#     "161-170": {"hero_atk_base": 189, "hero_hp_base:": 1890},
#     "171-180": {"hero_atk_base": 229.5, "hero_hp_base:": 2295},
#     "181-190": {"hero_atk_base": 270, "hero_hp_base:": 2700},
#     "191-200": {"hero_atk_base": 324, "hero_hp_base:": 3240},
#     "201-220": {"hero_atk_base": 378, "hero_hp_base:": 3780},
#     "221-240": {"hero_atk_base": 432, "hero_hp_base:": 4320},
#     "241-250": {"hero_atk_base": 437.4, "hero_hp_base:": 4374},
# }

STAT_TEMPLATE = {
    "hero_atk_base": 0,
    "hero_atk_pct": 0.0,
    "hero_hp_base": 0,
    "hero_hp_pct": 0.0,

    "soldier_atk_per": 0,
    "soldier_atk_pct": 0.0,
    "soldier_hp_per": 0,
    "soldier_hp_pct": 0.0,

    "march_size": 0,
    "hero_level_cap": 0,

    "gear_atk_base": 0,
    "gear_hp_base": 0,
    "gear_atk_pct": 0.0,
    "gear_hp_pct": 0.0,
}

CASTLE_SKINS = {
    "None": {
        "hero_atk_base": 0, "hero_atk_pct": 0.0, "hero_hp_base": 0, "hero_hp_pct": 0.0,
        "soldier_atk_per": 0, "soldier_atk_pct": 0.0, "soldier_hp_per": 0, "soldier_hp_pct": 0.0,
        "march_size": 0, "hero_level_cap": 0
    },
    "Steam Ark": {
        "soldier_atk_pct": 20.0, "hero_level_cap": 10
    },
    "Cloud Castle": {
        "soldier_atk_pct": 5.0, "soldier_hp_pct": 45.0, "hero_level_cap": 10
    },
    "Cherry Blossom": {
        "soldier_atk_pct": 5.0, "soldier_hp_pct": 30.0,"march_size": 30
    },
    "Pumpkin Town": {
        "soldier_atk_pct": 5.0, "soldier_hp_pct": 30.0, "march_size": 30
    },
    "Fantasy Ferris Wheel": {
        "soldier_atk_pct": 5.0, "soldier_hp_pct": 20.0, "march_size": 20
    },
    "Concerto": {
        "soldier_atk_pct": 5.0, "soldier_hp_pct": 30.0, "march_size": 20
    },
    "Dreamlike Dance": {
        "soldier_atk_pct": 5.0, "soldier_hp_pct": 30.0, "march_size": 30
    },
    "Crab Fortress": {
        "soldier_hp_pct": 40.0, "march_size": 30
    },
    "Skybound (League)": {
        "soldier_atk_pct": 10.0, "soldier_hp_pct": 50.0, "march_size": 20
    },
    "Mountain Prime ⚡": {
        "soldier_hp_pct": 50.0, "active_skill": {"soldier_hp_pct": 30.0}
    },
    "Steel Citadel ⚡": {
        "soldier_hp_pct": 35.0, "march_size": 20, "active_skill": {"march_size": 100}
    },
    "Cake Castle": {
        "soldier_hp_pct": 30.0, "march_size": 20
    },
    "Nightfall Castle (Nature)": {
        "soldier_atk_pct": 20.0, "soldier_hp_pct": 70.0, "march_size": 30
    },
    "Tower of Chaos (Horde)": {
        "soldier_atk_pct": 30.0, "soldier_hp_pct": 50.0, "march_size": 30
    },
    "Cute Egg Fun Castle": {
        "soldier_atk_pct": 5.0, "soldier_hp_pct": 30.0, "march_size": 30
    },
    "Secluded Valley": {
        "soldier_atk_pct": 5.0, "soldier_hp_pct": 30.0, "march_size": 30
    },
    "Shell Castle (Nature) ⚡": {
        "soldier_atk_pct": 20.0, "soldier_hp_pct": 20.0, "active_skill": {"soldier_hp_pct": 120.0}
    },
    "Temple of Soul": {
        "soldier_atk_pct": 10.0, "soldier_hp_pct": 25.0, "march_size": 20
    },
    "Blazing Fortress (Horde) ⚡": {
        "soldier_atk_pct": 20.0, "soldier_hp_pct": 20.0, "active_skill": {"soldier_atk_pct": 30.0, "soldier_hp_pct": 60.0}
    },
    "Spooky House": {
        "soldier_atk_pct": 20.0, "soldier_hp_pct": 5.0, "march_size": 30
    },
    "Fantasy Castle": {
        "soldier_atk_pct": 5.0, "soldier_hp_pct": 30.0, "march_size": 30
    },
    "Christmas Castle": {
        "soldier_atk_pct": 5.0, "soldier_hp_pct": 30.0, "march_size": 30
    },
    "Unbeatable Glory": {
        "soldier_atk_pct": 15.0, "soldier_hp_pct": 35.0, "march_size": 30
    },
    "Season Castle": {
        "soldier_atk_pct": 3.0, "soldier_hp_pct": 25.0, "march_size": 15
    }
}

# INIT
default_state = {
    "base_stats_done": False,
    "compare_mode": False,
    "show_gears": True,
    "faction_aura": True,

    "hero_atk_base": 121272,
    "hero_atk_pct": 693.2,
    "hero_hp_base": 1565392,
    "hero_hp_pct": 1493.1,

    "march_size": 1835,
    "soldier_atk_per": 71,
    "soldier_atk_pct": 853.61,
    "soldier_hp_per": 1015,
    "soldier_hp_pct": 1812.36,

    "gear_atk_base": 136860,
    "gear_atk_pct": 340.26,
    "gear_hp_base": 1260548,
    "gear_hp_pct": 213.46,
    "faction_aura_pct": 35,

}

# UTILS
def normalize_stats(partial: dict) -> dict:
    full = STAT_TEMPLATE.copy()
    full.update(partial)
    return full

CASTLE_SKINS = {
    name: normalize_stats(data)
    for name, data in CASTLE_SKINS.items()
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
    st.session_state.gear_atk_base = 0
    st.session_state.gear_hp_base = 0
    st.session_state.gear_atk_pct = 0.0
    st.session_state.gear_hp_pct = 0.0
    st.session_state.faction_aura_pct = 0
    st.rerun()

def apply_castle1():
    selection = st.session_state.castle_search_1
    if selection != "None":
        skin = CASTLE_SKINS[selection]
        st.session_state.upgrade1.update(skin)
        st.session_state.u1_hab = skin["hero_atk_base"]
        st.session_state.u1_hap = skin["hero_atk_pct"]
        st.session_state.u1_hhb = skin["hero_hp_base"]
        st.session_state.u1_hhp = skin["hero_hp_pct"]
        st.session_state.u1_sap = skin["soldier_atk_per"]
        st.session_state.u1_s_atk_pct = skin["soldier_atk_pct"]
        st.session_state.u1_shp = skin["soldier_hp_per"]
        st.session_state.u1_s_hp_pct = skin["soldier_hp_pct"]
        st.session_state.u1_sc = skin["march_size"]
        st.session_state.u1_hlc = skin["hero_level_cap"]


def apply_castle2():
    selection = st.session_state.castle_search_2
    if selection != "None":
        skin = CASTLE_SKINS[selection]
        st.session_state.upgrade2.update(skin)
        st.session_state.u2_ha = skin["hero_atk_base"]
        st.session_state.u2_hap = skin["hero_atk_pct"]
        st.session_state.u2_hh = skin["hero_hp_base"]
        st.session_state.u2_hhp = skin["hero_hp_pct"]
        st.session_state.u2_sa = skin["soldier_atk_per"]
        st.session_state.u2_sap = skin["soldier_atk_pct"]
        st.session_state.u2_sh = skin["soldier_hp_per"]
        st.session_state.u2_shp = skin["soldier_hp_pct"]
        st.session_state.u2_sc = skin["march_size"]
        st.session_state.u2_hlc = skin["hero_level_cap"]


def clear_upgrade1():
    st.session_state.upgrade1.update(CASTLE_SKINS["None"])
    for k in ["u1_hab", "u1_hap", "u1_hhb", "u1_hhp", "u1_sap", "u1_s_atk_pct", "u1_shp", "u1_s_hp_pct", "u1_sc", "u1_hlc"]:
        if k in st.session_state:
            st.session_state[k] = 0
    st.session_state.castle_search_1 = "None"


def clear_upgrade2():
    st.session_state.upgrade2.update(CASTLE_SKINS["None"])
    for k in ["u2_ha", "u2_hap", "u2_hh", "u2_hhp", "u2_sa", "u2_sap", "u2_sh", "u2_shp", "u2_sc", "u2_hlc"]:
        if k in st.session_state:
            st.session_state[k] = 0
    st.session_state.castle_search_2 = "None"


def calculate_total(upgrade):
    hlc = upgrade.get("hero_level_cap", 0)
    hero_atk_from_cap = hlc * HERO_LEVEL_CAP_ATK
    hero_hp_from_cap = hlc * HERO_LEVEL_CAP_HP
    march_from_cap = hlc * HERO_LEVEL_CAP_MARCH

    hero_atk_base = (st.session_state.hero_atk_base + upgrade["hero_atk_base"] + hero_atk_from_cap)
    hero_hp_base = (st.session_state.hero_hp_base + upgrade["hero_hp_base"] + + hero_hp_from_cap)

    hero_atk = hero_atk_base * (1 + (st.session_state.hero_atk_pct + upgrade["hero_atk_pct"]) / 100)
    hero_hp = hero_hp_base * (1 + (st.session_state.hero_hp_pct + upgrade["hero_hp_pct"]) / 100)

    soldier_atk_base = (st.session_state.soldier_atk_per + upgrade["soldier_atk_per"]) * (st.session_state.march_size + upgrade["march_size"] + march_from_cap)
    soldier_hp_base = (st.session_state.soldier_hp_per + upgrade["soldier_hp_per"]) * (st.session_state.march_size + upgrade["march_size"] + march_from_cap)

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
        ("hero_level_cap", "Hero Level Cap"),
        ("soldier_atk_per", "Soldier ATK"),
        ("soldier_atk_pct", "Soldier ATK %"),
        ("soldier_hp_per", "Soldier HP"),
        ("soldier_hp_pct", "Soldier HP %"),
        ("march_size", "March Size"),
    ]
    for key, label in display_map:
        val = upgrade.get(key, 0)
        if val > 0:
            if key == "hero_level_cap":
                parts.append(f"{label}: +{int(val)}")
            elif "%" in label:
                parts.append(f"{label}: +{val:,}%")
            else:
                parts.append(f"{label}: +{int(val):,}")
    return ", ".join(parts) if parts else "No bonus stats"

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
    Or if the path to Level 11 soldiers is more efficient than Brilliance 3 soldiers?
    Well, this is the tool for you. See the actual raw stat gain from different sources and how it affects your heroes!
    """)

    with st.expander("Advanced Settings"):
        st.toggle("Enable Gear Stats", key="show_gears", value=st.session_state.show_gears)
        st.toggle("Include Faction Aura", key="faction_aura", value=st.session_state.faction_aura)

    st.header("Base Stats Input")

    st.markdown("""
    Input the current stats of your hero. 
    To see these stats, go to your hero screen -> click your desired hero -> click the (i) beside its stats.
    """)

    st.subheader("Hero Stats")
    h_cols = st.columns(5)
    st.session_state.hero_atk_base = h_cols[0].number_input("Hero ATK Base", min_value=0, value=st.session_state.hero_atk_base, width=120)
    st.session_state.hero_atk_pct = h_cols[1].number_input("Hero ATK %", min_value=0.0, value=st.session_state.hero_atk_pct, width=120)
    st.session_state.hero_hp_base = h_cols[2].number_input("Hero HP Base", min_value=0, value=st.session_state.hero_hp_base, width=120)
    st.session_state.hero_hp_pct = h_cols[3].number_input("Hero HP %", min_value=0.0, value=st.session_state.hero_hp_pct, width=120)

    st.subheader("Soldier Stats")
    s_cols = st.columns(5)
    st.session_state.soldier_atk_per = s_cols[0].number_input("ATK per soldier", min_value=0, value=st.session_state.soldier_atk_per, width=120)
    st.session_state.soldier_atk_pct = s_cols[1].number_input("Soldier ATK %", min_value=0.0, value=st.session_state.soldier_atk_pct, width=120)
    st.session_state.soldier_hp_per = s_cols[2].number_input("HP per soldier", min_value=0, value=st.session_state.soldier_hp_per, width=120)
    st.session_state.soldier_hp_pct = s_cols[3].number_input("Soldier HP %", min_value=0.0, value=st.session_state.soldier_hp_pct, width=120)
    st.session_state.march_size = s_cols[4].number_input("March Size", min_value=0, value=st.session_state.march_size, width=120)

    if st.session_state.show_gears:
        st.subheader("Gear Stats")
        g_cols = st.columns(5)
        st.session_state.gear_atk_base = g_cols[0].number_input("Gear ATK", min_value=0, value=st.session_state.gear_atk_base, width=120)
        st.session_state.gear_hp_base = g_cols[1].number_input("Gear HP", min_value=0, value=st.session_state.gear_hp_base, width=120)
        st.session_state.gear_atk_pct = g_cols[2].number_input("Gear ATK %", min_value=0.0, value=st.session_state.gear_atk_pct, width=120)
        st.session_state.gear_hp_pct = g_cols[3].number_input("Gear HP %", min_value=0.0, value=st.session_state.gear_hp_pct, width=120)

    if st.session_state.faction_aura:
        st.subheader("Faction Aura")
        f_cols = st.columns(5)
        st.session_state.faction_aura_pct = f_cols[0].selectbox("Faction Aura", [0, 15, 25, 35], index=3, label_visibility="collapsed", width = 120)

    st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
    if st.button("Clear Fields", use_container_width=True):
        clear_base_stats()

    # TOTAL
    soldier_atk_base = st.session_state.soldier_atk_per * st.session_state.march_size
    soldier_hp_base = st.session_state.soldier_hp_per * st.session_state.march_size
    hero_atk_total = st.session_state.hero_atk_base * (1 + st.session_state.hero_atk_pct / 100)
    hero_hp_total = st.session_state.hero_hp_base * (1 + st.session_state.hero_hp_pct / 100)
    soldier_atk_total = soldier_atk_base * (1 + st.session_state.soldier_atk_pct / 100)
    soldier_hp_total = soldier_hp_base * (1 + st.session_state.soldier_hp_pct / 100)

    if st.session_state.faction_aura:
        faction_aura_pct = 1 + (st.session_state.faction_aura_pct/100)
    else:
        faction_aura_pct = 1

    if st.session_state.show_gears:
        gear_atk_total = (st.session_state.gear_atk_base * (1 + st.session_state.gear_atk_pct / 100))
        gear_hp_total = (st.session_state.gear_hp_base * (1 + st.session_state.gear_hp_pct / 100))
    else:
        gear_atk_total = 0
        gear_hp_total = 0

    st.header("Total Stats")
    st.markdown("""
    Make sure that the calculated value below matches the total values in your hero screen before proceeding.
    """)

    t_cols = st.columns(2)
    t_cols[0].metric("Total Hero ATK", f"{hero_atk_total:,.0f}")
    t_cols[0].metric("Total Soldier ATK", f"{soldier_atk_total:,.0f}")
    t_cols[1].metric("Total Hero HP", f"{hero_hp_total:,.0f}")
    t_cols[1].metric("Total Soldier HP", f"{soldier_hp_total:,.0f}")

    t_cols = st.columns(2)
    t_cols[0].metric("Total Gear ATK", f"{gear_atk_total:,.0f}")
    t_cols[1].metric("Total Gear HP", f"{gear_hp_total:,.0f}")
    t_cols[0].metric("**TOTAL ATK**", f"{(hero_atk_total + soldier_atk_total + gear_atk_total) * faction_aura_pct:,.0f}")
    t_cols[1].metric("**TOTAL HP**", f"{(hero_hp_total + soldier_hp_total + gear_hp_total) * faction_aura_pct:,.0f}")

    if st.button("✔ Confirm", use_container_width=True, type="primary"):
        st.session_state.base_stats_done = True
        st.rerun()

# CALC
else:
    if st.button("↩ Return"):
        st.session_state.base_stats_done = False
        st.rerun()

    base_hero_atk = st.session_state.hero_atk_base * (1 + st.session_state.hero_atk_pct / 100)
    base_hero_hp = st.session_state.hero_hp_base * (1 + st.session_state.hero_hp_pct / 100)
    base_soldier_atk = st.session_state.soldier_atk_per * st.session_state.march_size * (1 + st.session_state.soldier_atk_pct / 100)
    base_soldier_hp = st.session_state.soldier_hp_per * st.session_state.march_size * (1 + st.session_state.soldier_hp_pct / 100)

    if st.session_state.show_gears:
        base_gear_atk = st.session_state.gear_atk_base * (1 + st.session_state.gear_atk_pct / 100)
        base_gear_hp = st.session_state.gear_hp_base * (1 + st.session_state.gear_hp_pct / 100)
    else:
        base_gear_atk = 0
        base_gear_hp = 0

    total_base_atk = base_hero_atk + base_soldier_atk
    total_base_hp = base_hero_hp + base_soldier_hp

    st.subheader("Calculate Increase")

    st.markdown("""
    Input the stats that you're gaining from a source. Alternatively, you can toggle the search bar on to find in-game items that gives stat bonuses like Castle 
    Skins.
    """)

    # CASTLE SEARCH 1
    show_template1 = st.toggle("Search Castle Skin", key="show_t1")
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
        if st.toggle(f"⚡ Include Active Skill: {label1}", key="act1"):
            for k, v in active_bonuses.items():
                eff_up1[k] += v
            active_text1 = f" **Active Skill:** `{label1}`"

    st.markdown("Hero")
    h_cols = st.columns(5)
    st.session_state.upgrade1["hero_atk_base"] = h_cols[0].number_input("+Hero ATK Base", min_value=0, key="u1_hab", width=120)
    st.session_state.upgrade1["hero_atk_pct"] = h_cols[1].number_input("+Hero ATK %", min_value=0.0,  key="u1_hap", width=120)
    st.session_state.upgrade1["hero_hp_base"] = h_cols[2].number_input("+Hero HP Base", min_value=0, key="u1_hhb", width=120)
    st.session_state.upgrade1["hero_hp_pct"] = h_cols[3].number_input("+Hero HP %", min_value=0.0, key="u1_hhp", width=120)
    st.session_state.upgrade1["hero_level_cap"] = h_cols[4].number_input("+Hero Lvl Cap", min_value=0.0, key="u1_hlc", width=120)

    st.markdown("Soldier")
    s_cols = st.columns(5)
    st.session_state.upgrade1["soldier_atk_per"] = s_cols[0].number_input("+ATK per Soldier", min_value=0, key="u1_sap", width=120)
    st.session_state.upgrade1["soldier_atk_pct"] = s_cols[1].number_input("+Soldier ATK %", min_value=0.0, key="u1_s_atk_pct", width=120)
    st.session_state.upgrade1["soldier_hp_per"] = s_cols[2].number_input("+HP per Soldier", min_value=0, key="u1_shp", width=120)
    st.session_state.upgrade1["soldier_hp_pct"] = s_cols[3].number_input("+Soldier HP %", min_value=0.0, key="u1_s_hp_pct", width=120)
    st.session_state.upgrade1["march_size"] = s_cols[4].number_input("+March Size", min_value=0, key="u1_sc", width=120)

    if st.session_state.show_gears:
        st.markdown("Gear")
        g_cols = st.columns(5)
        st.session_state.upgrade1["gear_atk_base"] = g_cols[0].number_input("+Gear ATK Base", min_value=0, key="u1_gab", width=120)
        st.session_state.upgrade1["gear_hp_base"] = g_cols[1].number_input("+Gear HP Base", min_value=0, key="u1_ghb", width=120)
        st.session_state.upgrade1["gear_atk_pct"] = g_cols[2].number_input("+Gear ATK %", min_value=0.0, key="u1_gap", width=120)
        st.session_state.upgrade1["gear_hp_pct"] = g_cols[3].number_input("+Gear HP %", min_value=0.0, key="u1_ghp", width=120)

    st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
    st.button("Clear Calc Fields", on_click=clear_upgrade1, use_container_width=True)

    # CALCULATE UPGRADE 1 VALUES
    t1_atk, t1_hp = calculate_total(eff_up1)
    atk_g1 = t1_atk - total_base_atk
    hp_g1 = t1_hp - total_base_hp
    atk_p1 = (atk_g1 / total_base_atk * 100) if total_base_atk else 0
    hp_p1 = (hp_g1 / total_base_hp * 100) if total_base_hp else 0

    if not st.session_state.compare_mode:
        st.subheader("Actual Stat Increase")
        res1, res2 = st.columns(2)
        with res1:
            st.metric("ATK Gain", f"{atk_g1:,.0f}", f"{atk_p1:.2f}%")
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
        show_template2 = st.toggle("Search Castle Skin", key="show_t2")
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

        active_text2 = ""
        skin2_data = CASTLE_SKINS.get(st.session_state.get("castle_search_2", "None"), {})

        if "active_skill" in skin2_data:
            active_bonuses = skin2_data["active_skill"]
            label2 = format_active_stats(active_bonuses)
            if st.toggle(f"⚡ Include Active Skill: {label2}", key="act2"):
                for k, v in active_bonuses.items():
                    eff_up2[k] += v
                active_text2 = f"**Active Skill:** `{label2}`"

        t2_atk, t2_hp = calculate_total(eff_up2)

        st.markdown("Hero")
        h_cols = st.columns(5)
        st.session_state.upgrade2["hero_atk_base"] = h_cols[0].number_input("+Hero ATK Base", min_value=0, step=1, key="u2_ha")
        st.session_state.upgrade2["hero_atk_pct"] = h_cols[1].number_input("+Hero ATK %", min_value=0.0, step=0.1, key="u2_hap")
        st.session_state.upgrade2["hero_hp_base"] = h_cols[2].number_input("+Hero HP Base", min_value=0, step=1, key="u2_hh")
        st.session_state.upgrade2["hero_hp_pct"] = h_cols[3].number_input("+Hero HP %", min_value=0.0, step=0.1, key="u2_hhp")
        st.session_state.upgrade2["hero_level_cap"] = h_cols[4].number_input("+Hero Lvl Cap", min_value=0.0, key="u2_hlc", width=120)

        st.markdown("Soldier")
        s_cols = st.columns(5)
        st.session_state.upgrade2["soldier_atk_per"] = s_cols[0].number_input("+ATK per Soldier", min_value=0, step=1, key="u2_sa")
        st.session_state.upgrade2["soldier_atk_pct"] = s_cols[1].number_input("+Soldier ATK %", min_value=0.0, step=0.1, key="u2_sap")
        st.session_state.upgrade2["soldier_hp_per"] = s_cols[2].number_input("+HP per Soldier", min_value=0, step=1, key="u2_sh")
        st.session_state.upgrade2["soldier_hp_pct"] = s_cols[3].number_input("+Soldier HP %", min_value=0.0, step=0.1, key="u2_shp")
        st.session_state.upgrade2["march_size"] = s_cols[4].number_input("+March Size", min_value=0, step=1, key="u2_sc")

        if st.session_state.show_gears:
            st.markdown("Gear")
            g_cols = st.columns(5)
            st.session_state.upgrade2["gear_atk_base"] = g_cols[0].number_input("+Gear ATK Base", min_value=0, step=1, key="u2_gab")
            st.session_state.upgrade2["gear_hp_base"] = g_cols[1].number_input("+Gear HP Base", min_value=0, step=1, key="u2_ghb")
            st.session_state.upgrade2["gear_atk_pct"] = g_cols[2].number_input("+Gear ATK %", min_value=0.0, step=0.1, key="u2_gap")
            st.session_state.upgrade2["gear_hp_pct"] = g_cols[3].number_input("+Gear HP %", min_value=0.0, step=0.1, key="u2_ghp")


        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        st.button("Clear Compare Fields", on_click=clear_upgrade2, use_container_width=True, key="btn_clear_comp")

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
            st.metric("ATK Gain", f"{atk_g1:,.0f}", f"{atk_p1:.2f}%")
        with c2:
            st.metric("HP Gain", f"{hp_g1:,.0f}", f"{hp_p1:.2f}%")

        st.write("")

        combined_text2 = f"**{title2}** — `{stats_text2}`"
        if active_text2:
            combined_text2 += f"  \n{active_text2}"
        st.markdown(combined_text2)

        c3, c4 = st.columns(2)
        with c3:
            st.metric("ATK Gain", f"{atk_g2:,.0f}", f"{atk_p2:.2f}%")
        with c4:
            st.metric("HP Gain", f"{hp_g2:,.0f}", f"{hp_p2:.2f}%")

        st.divider()

        _, close_col, _ = st.columns([1, 2, 1])
        with close_col:
            if st.button("Close Comparison", use_container_width=True):
                st.session_state.compare_mode = False
                st.rerun()
