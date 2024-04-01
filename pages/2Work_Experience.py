import streamlit as st
import pandas as pd

st.set_page_config(page_title="Maurício's Portfolio", page_icon=":nerd_face:", layout="wide")

# Content under each tab
with st.expander("Companies i Worked For"):
    col1, col2 = st.columns([1, 4])  # Divide the expander into two columns

    with col1:
        st.image("pages/images/gama.jpeg", width=50)
        st.write("Gama Academy")
        st.write("(Set/2022 - Jan/2024)")
        st.write("")
        st.write("")
        st.write("")
        st.write("")               

        st.image("pages/images/dp6.jpeg", width=50)
        st.write("DP6 Consultancy")
        st.write("(May/2023 - Nov/2017) and (Jan/2021 - Apr/2023)")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        st.image("pages/images/estadao.png", width=50)
        st.write("Estadão")
        st.write(" (Nov/2017 - Jan/2021)")
        st.write("")
        st.write("")

    with col2:
        st.write("In 2023, I was recognized by Gama as one of the top 50 BI professionals to follow on LinkedIn. As a result, they invited me to join their Data Analytics training and MBA program. I was responsible for the Data-Driven Decision Making module and also provided corporate training in Data Storytelling, Data-Driven Mindset and Data Governance.")  # Text appears in the column to the right of the image
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("In my initial journey, I began as an intern in 2012, working within the Business Intelligence team supporting Philips e-commerce. It was during this time that I acquired much of my knowledge in web analytics, BI methodologies, data ETL, and performance metrics. Progressing steadily and earning recognition, I advanced to an analyst role, contributing to various projects. A significant milestone during this phase was my specialization in performance rooms/war rooms, which underscored my growing expertise.")
        st.write("")
        st.write("In my subsequent role as Business Analytics Manager, I returned to lead multiple projects involving collaboration with data scientists, data engineers, and business analysts. These projects encompassed a wide scope, including Multichannel Attribution, assessing the impact of offline media on digital channels, Media Mix Modeling, Data Quality & Governance initiatives, Google Analytics 4 implementation, and integration with Salesforce. Furthermore, I actively participated in strategic discussions pertaining to project management and overarching organizational goals.")
        st.write("")
        st.write("")
        st.write("At Estadão, I spearheaded the Business Intelligence department during the publisher's digital transformation initiative. In this capacity, I was tasked with structuring the BI framework, implementing analytical tools across digital products, and establishing processes for generating dashboards and conducting strategic analyses for various editorial units and departments. Additionally, I provided training to 220 journalists, BI professionals, and business teams on metrics and data analysis methodologies. Concurrently, I led a team of 12 individuals in Business Analytics, ensuring effective coordination and project execution.")
        st.write("")
        st.write("Building upon the foundation of analytical processes and enhancing visibility into the performance of digital products such as the App Estadão, estadao.com.br, Clube+ Estadão, Estadão Incentiva, and Assine.estadao, I was promoted to the role of Growth Marketing Analytics Manager. In this capacity, I spearheaded efforts to drive acquisition, retention, and customer lifetime value (CLV) growth through strategic marketing initiatives, media optimization, and seamless data integration. The outcomes were remarkable, with a notable increase of +18% in subscribers and a staggering +138% growth in revenue. As the leader of the growth team comprising 7 individuals, I took charge of coordinating analysts and coordinators, fostering collaboration with cross-functional teams, and orchestrating the optimization of digital channels, products, and community engagement (subscribers). Leveraging advanced data analysis techniques, A/B testing methodologies, predictive models, and Martech integration, we achieved significant enhancements in performance and effectiveness.")

from PIL import Image
import streamlit as st
import os

def display_image(url_or_path, width=100):
    try:
        if os.path.exists(url_or_path):  # Check if the path exists locally
            image = Image.open(url_or_path)
        else:
            response = requests.get(url_or_path)
            image = Image.open(BytesIO(response.content))
        st.image(image, width=width)
    except Exception as e:
        st.error(f"Error loading image from {url_or_path}: {e}")

# Define the data
brands_data = {
    "Brand": ["Raia Drogasil", "Danone", "Globoplay", "Bradesco", "Nubank", "Carrefour", "Fiat", "Itaú", "Renault", "Vivo", "Philips", "Meio & Mensagem"],
    "Logo": [
        "pages/images/raiadrogasil.png",
        "pages/images/danone.png",
        "pages/images/globoplay.png",
        "pages/images/telecine.jpeg",
        "pages/images/bradesco.png",
        "pages/images/stellantis.png",
        "pages/images/kroton.png",
        "pages/images/itau.png",
        "pages/images/renault.png",
        "pages/images/vivo.png",
        "pages/images/philips.png",
        "pages/images/meioemensagem.jpg"
    ],
    "Description": [
        "One notable project involved Omnichannel Attribution, analyzing digital media's true impact on both online channels and offline store purchases within the RaiaDrogasil group (including Drogaia and Drogasil). Additionally, I spearheaded the development of a native Customer Data Platform (AdSync), enabling audience segmentation and integration with CRM and AdTech platforms (Salesforce, Google Ads, Meta Ads). Furthermore, I led the implementation of Google Analytics 4 across the group's app and website, enhancing user insights and informing data-driven decisions. These initiatives fortified RaiaDrogasil's data infrastructure, enabling more informed marketing strategies and driving tangible business outcomes.",
        "Leveraging Amazon Ads' Data-Clean Room, I managed multifunctional teams to model data and extract performance insights from ad campaigns, pioneering this approach in Brazil. Through strategic product promotion on Amazon Ads and utilizing Amazon's Retail Media solution, our project significantly impacted sales and reach, resulting in a 30% increase in ROAS, a 47% boost in new-to-brand acquisitions. Our innovative approach propelled Danone Brasil's Amazon operations ahead of three European countries with more established Amazon operations, earning recognition in the company's global rankings.",
        "In response to the imperative to enhance the deliverability and user experience of the Globoplay streaming platform, the project centered around Data Quality. It involved displaying error data related to deliverability across various devices and operating systems (including Smart TVs, computers, and mobile devices), aiding in product optimization efforts.",
        "Led the restructure of Telecine's Salesforce Marketing Cloud, integrating audience and consumption databases with streamlined data engineering processes to create automated relationship workflows, adhering to industry best practices. Provided support for the implementation of Google Analytics on Telecineplay's app and website.",
        "Coordinated the Performance Room, optimizing media budget allocation for digital product conversions (insurance, cards, payroll loans, etc.). Oversaw monitoring and analysis of key performance indicators across paid channels, campaigns, and assets. Established a collaborative framework between agencies, the company, and consultants, facilitating scalable optimization adjustments and daily testing.",
        "Coordination of the Performance Room, with an approach to the best use of media budget in the digital conversion of automotive launches of the Fiat, Jeep and Chrysler brands and performance of the After-Sales areas through monitoring and analysis of key performance indicators of paid channels.",
        "Implemented a project to measure audience lift and enrollment conversion on Kroton universities' websites (Anhanguera and Unopar) resulting from offline advertising insertions in prime time slots on major TV networks (Globo, Record, Band, etc.). Identified optimal channels and time slots for performance, providing valuable insights for media buying planning.",
        "As an Analyst within Itaú's Performance Room, my primary responsibilities entail meticulously monitoring the performance metrics and indicators across various paid digital channels, specifically focusing on card and insurance acquisitions. Additionally, I oversee the seamless migration, implementation, and validation of data collection processes within Adobe Analytics. My role involves orchestrating a cohesive operation that integrates efforts between agencies, the company, and external consultancies to ensure optimal performance and alignment with organizational objectives.",
        "In my role as an analyst, I actively contributed to implementing Google Analytics on Renault's digital platforms. I focused on developing reports and attribution dashboards for brand launches such as Duster, Sandero, KWID, Logan, etc. This initiative enables precise tracking and analysis of sales performance, providing valuable insights into consumer behavior. By leveraging Google Analytics, we empower data-driven decisions to optimize the success of our product launches.",
        "I structured and monitored data quality from Vivo.com.br service sales channels, ensuring accuracy and optimizing performance.",
        "Implemented Adobe Analytics on Philips Web (www.philips.com.br) to enchance consumers purchase journey. Surveyed KPIs for site metric mapping. Validated data triggers for Adobe Analytics quality assurance. Updated reports using Adobe Analytics and Excel integration, with automatic updates in Power Point. Analyzed reports for insights to optimize Philips' paid digital media marketing budget, refining processes based on validation.",
        "Implemented Google Analytics on meioemensagem.com.br for content consumption analysis."
    ]
}

with st.expander("Brands I Worked With"):
    # Display the data in a table
    for i in range(len(brands_data["Description"])):
        display_image(brands_data["Logo"][i], width=100)
        st.write(brands_data["Description"][i])


def markdown_progress(x: float) -> str:
    return f"""![](https://geps.dev/progress/{x})"""

with st.expander("Volunteer Experience"):
    col1, col2 = st.columns([1, 4])  # Divide the expander into two columns

    with col1:
        st.image("https://media.licdn.com/dms/image/C4D0BAQHi7zurIfCpzA/company-logo_200_200/0/1631328599586?e=2147483647&v=beta&t=NE6oeoQu_Aj9D_6APe9QTY7zSEJ2CWSVcmb452XaI1Q", width=50)
        st.write("CTC Digital")
    
    with col2:
        st.write("One of the most transformative experiences of my personal and professional life was creating the Google Analytics and Data Analysis for Digital Cultural Program for Digital Culture - Casas Taiguara in partnership with three colleagues, Leandro Nascimento, Fernando Patini and Lucas Antônio, with full support from dp6. Through this program, I was able to share my years of experience with youth living in downtown Sao Paulo. We taught them how to use Google Analytics, Excel, introduced the basics of data analysis, and helped them create strategic presentations to share their learnings in meetings with company stakeholders. Over the almost three years that I hosted the program, we invited experienced people from the digital marketing business to provide students with exposure to real-life experience.")
