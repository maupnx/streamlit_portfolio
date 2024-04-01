import streamlit as st
import pandas as pd

def markdown_progress(x: float) -> str:
    return f"""![](https://geps.dev/progress/{x})"""

with st.expander("Tech Stack Skills"):
    st.write("My Tech Skills")

    df = pd.DataFrame({"Data Analysis Language":["Python", "SQL", "R", "Excel/Google Sheets"], "x": [80, 100, 70, 100]})
    df["Mastery"] = df["x"].map(markdown_progress)
    st.markdown(df.to_markdown())

    st.write("")
    st.write("")

    df = pd.DataFrame({"Web/App Analytics Tool":["Google Analytics", "Adobe Analytics", "Google Tag Manager"], "x": [100, 70, 90]})
    df["Mastery"] = df["x"].map(markdown_progress)
    st.markdown(df.to_markdown())

    st.write("")
    st.write("")

    df = pd.DataFrame({"Dashboard Tools":["Looker Studio", "Power BI"], "x": [100, 100]})
    df["Mastery"] = df["x"].map(markdown_progress)
    st.markdown(df.to_markdown())
    
    st.write("")
    st.write("")

    df = pd.DataFrame({"Cloud Platforms": ["Google Cloud Platform", "AWS", "Azure"], "x": [60, 60, 10]})
    df["Mastery"] = df["x"].map(markdown_progress)
    st.markdown(df.to_markdown())
        
    st.write("")
    st.write("")


    df = pd.DataFrame({"CRM Tools": ["Salesforce Marketing Cloud", "RD Station", "Hubspot"], "x": [90, 100, 100]})
    df["Mastery"] = df["x"].map(markdown_progress)
    st.markdown(df.to_markdown())

           
    st.write("")
    st.write("")


    df = pd.DataFrame({"AdTech Tools": ["Google Ads", "Google Display & Video 360", "Google Search 360", "Amazon Ads" ,"Meta Ads", "TikTok Ads"], "x": [100, 100, 100, 100, 100, 100]})
    df["Mastery"] = df["x"].map(markdown_progress)
    st.markdown(df.to_markdown())
    
           
    st.write("")
    st.write("")


    df = pd.DataFrame({"Others Martech": ["VWO (AB Test)", "Optimizely (A/B Test)", "Segment (CDP)", "Hotjar"], "x": [100, 100, 100, 100]})
    df["Mastery"] = df["x"].map(markdown_progress)
    st.markdown(df.to_markdown())