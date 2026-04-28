import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

import base64
st.set_page_config(page_title="Olympic Analysis", layout="wide")

# Some css styling for side-bar :

st.markdown("""
<style>

/* Sidebar background */
[data-testid="stSidebar"] {
    background: #111827;
    padding: 18px 12px;
}

/* Title */
.sidebar-title {
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    color: #f9fafb;
    margin-bottom: 25px;
}

/* Radio container */
.stRadio > div {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

/* Each option */
.stRadio label {
    position: relative;
    background: #1f2933;
    padding: 12px 16px;
    border-radius: 10px;
    border: 1px solid #2d3748;
    transition: background 0.2s ease;
}

/* Left indicator (hidden by default) */
.stRadio label::before {
    content: "";
    position: absolute;
    left: 0;
    top: 20%;
    height: 60%;
    width: 4px;
    background: transparent;
    border-radius: 4px;
}

/* Hover */
.stRadio label:hover {
    background: #2d3748;
    cursor: pointer;
}

/* Selected option */
.stRadio input:checked + div {
    background: #111827 !important;
    color: #ffffff !important;
    font-weight: 600;
}

/* Active left indicator */
.stRadio input:checked + div::before {
    background: #9ca3af;  /* subtle grey highlight */
}

/* Remove radio circle */
.stRadio input {
    display: none;
}

/* Selectbox */
.stSelectbox > div {
    background-color: #1f2933;
    border-radius: 8px;
    border: 1px solid #111827;
    color: white;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Selectbox main box */
.stSelectbox > div {
    background-color: #111827 !important;
    border-radius: 8px;
    border: 1px solid #333;
    color: white !important;
}

/* Dropdown menu */
div[data-baseweb="select"] > div {
    background-color: #111827 !important;
    color: white !important;
}

/* Dropdown options */
div[role="listbox"] {
    background-color: #111827 !important;
    color: white !important;
}

/* Each option */
div[role="option"] {
    background-color: #111827;
    color: white !important;
}

/* Hover on option */
div[role="option"]:hover {
    background-color: #1f2933 !important;
}

/* Selected option */
div[aria-selected="true"] {
    background-color: #374151 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)



def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()
    



df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

logo_base64 = get_base64_image("olympic_logo.png")

st.markdown(f"""
    <div style="
        display: flex;
        align-items: center;
        gap: 15px;
        padding: 10px 0;
    ">
        <img src="data:image/png;base64,{logo_base64}" width="70">
        <h1 style="margin:0; font-size:38px;">
            Olympic Analysis
        </h1>
    </div>
""", unsafe_allow_html=True)

st.sidebar.title('Olympic Dashboard')
st.markdown("<hr>", unsafe_allow_html=True)
user_menu = st.sidebar.radio(
    'Select an Option',
    ('🏅 Medal-Tally','📊 Overall-Analysis','🌍 Country Wise-Analysis','👤 Athelete wise-Analysis')
)


if user_menu == '🏅 Medal-Tally':

    st.sidebar.header('Medal tally')
    year, country =helper.country_year_list(df)


    selected_year= st.sidebar.selectbox('Select Year',year)
    selected_country= st.sidebar.selectbox('Select Country',country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title('Overall Medal Tally')
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title('Medal Tally in ' + str(selected_year) + ' Olympics')
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title('Medal Tally of ' + str(selected_country) + ' in Olympics')
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title('Medal Tally of ' + str(selected_country) + ' in ' + str(selected_year) + ' Olympics')
    st.table(medal_tally)       


if user_menu == '📊 Overall-Analysis':
        editions = df['Year'].unique().shape[0] -1
        sports = df['Sport'].unique().shape[0]
        events = df['Event'].unique().shape[0]
        atheletes = df['Name'].unique().shape[0]
        nations = df['region'].unique().shape[0]
        cities = df['City'].unique().shape[0]

        st.title("Top Statistics")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header('Editions')
            st.title(editions)
        with col2:
            st.header('Host Cities')
            st.title(cities)
        with col3:
            st.header('Sports')
            st.title(sports)
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header('Events')
            st.title(events)
        with col2:
            st.header('Nations')
            st.title(nations)
        with col3:
            st.header('Atheletes')
            st.title(atheletes)

        nations_over_time = helper.data_over_time(df,'region')
        fig = px.line(nations_over_time, x='Edition', y='No of region')
        st.title('Participating Nations over the years')
        st.plotly_chart(fig)

        events_over_time = helper.data_over_time(df,'Event')
        fig = px.line(events_over_time, x='Edition', y='No of Event')
        st.title('Events over the years')
        st.plotly_chart(fig)

        athelete_over_time = helper.data_over_time(df,'Name')
        fig = px.line(athelete_over_time, x='Edition', y='No of Name')
        st.title('Atheletes over the years')
        st.plotly_chart(fig)

        x = df.drop_duplicates(['Year','Sport','Event'])

        heatmap_data = x.pivot_table(
            index='Sport',
            columns='Year',
            values='Event',
            aggfunc='count'
        ).fillna(0)

        fig = px.imshow(heatmap_data, aspect='auto', text_auto=True)
        fig.update_layout(height=1200)

        st.title('No. of Events over time for every Sport:')
        st.plotly_chart(fig) 

        st.title('Most Successful Atheletes')
        sport_list = df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0,'Overall')
        selected_sport = st.selectbox('Select a Sport',sport_list)  
        
        x = helper.most_successful(df,selected_sport)
        st.table(x)

if user_menu == '🌍 Country Wise-Analysis':

    st.sidebar.title('Country Wise Analysis of Olympics')

    countries = df['region'].dropna().unique().tolist()
    countries.sort()

    selected_country = st.sidebar.selectbox('Select a Country',countries)


    country_df = helper.year_wise_medal_tally(df,selected_country)
    fig = px.line(country_df, x='Year', y='Medal')
    st.title(selected_country + ' Medal tally over the years')
    st.plotly_chart(fig)

    st.title(selected_country + ' Event Heatmap')
    heatmap_data = helper.country_event_heatmap(df,selected_country)
    fig = px.imshow(heatmap_data, aspect='auto', text_auto=True)
    fig.update_layout(height=1200)
    st.plotly_chart(fig)

    st.title('Most Successful Atheletes of ' + selected_country)
    player_df = helper.most_successful_countrywise(df,selected_country) 
    st.table(player_df)

if user_menu == '👤 Athelete wise-Analysis':

    st.sidebar.title('Athelete Wise Analysis of Olympics')

    atheletes_df = df.drop_duplicates(subset=['Name','region'])

    x1 = atheletes_df['Age'].dropna()
    x2 = atheletes_df[atheletes_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = atheletes_df[atheletes_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = atheletes_df[atheletes_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1,x2,x3,x4],['Overall Age','Gold Medalist','Silver Medalist','Bronze Medalist'],show_hist=False,show_rug=False)
    fig.update_layout(autosize=False, width=800, height=500)

    st.title('Distribution of Age')
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    
    for sport in famous_sports:
        temp_df = atheletes_df[atheletes_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)

    temp_df = helper.weight_v_height(df, selected_sport)

    fig = px.scatter(
        temp_df,
        x='Weight',
        y='Height',
        color='Medal',
        symbol='Sex',
        hover_name='Name',
        opacity=0.8
    )

    fig.update_layout(
        template='plotly_dark',
        title='Height vs Weight Analysis',
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)

    #footer
st.markdown("---")

st.markdown("""
<style>
.footer {
    width: 100%;
    text-align: center;
    padding: 15px 10px;
    font-size: 14px;
    color: #666;
}

.footer a {
    color: #1f77b4;
    text-decoration: none;
    margin: 0 8px;
    font-weight: 500;
}

.footer a:hover {
    text-decoration: underline;
}
</style>

<div class="footer">
    © Olympic Analysis | Designed by <b>Mihir Tomar</b> 🚀 <br>
    <a href="https://github.com/mihirchaudhary3747" target="_blank">GitHub</a> |
    <a href="https://www.linkedin.com/in/mihirtomar3747" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)