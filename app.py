import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Full-Stack Developer Resume",
    page_icon="💻",
    layout="wide"
)

# Sidebar for navigation
st.sidebar.title("Navigation")
sections = ["About Me", "Skills", "Work Experience", "Projects", "Testimonials", "Contact"]
selected_section = st.sidebar.radio("Go to", sections)

# Main Header
st.title("💻 Full-Stack Developer Resume")
st.markdown("### 10 Years of Expertise in App Development, Website Development, and Funnel Design")

# About Me Section
if selected_section == "About Me":
    st.header("About Me")
    st.markdown("""
    Hi! I'm a passionate **Full-Stack Developer** with 10 years of experience delivering 
    cutting-edge solutions for businesses of all sizes.  
    My expertise spans:
    - Building **user-friendly apps** with optimal performance.
    - Developing **responsive websites** tailored to client goals.
    - Designing and implementing **sales funnels** to maximize ROI.

    I bring a unique combination of creativity and technical acumen to every project, 
    ensuring seamless functionality and exceptional user experience.
    """)
    st.image("https://via.placeholder.com/800x400.png", caption="A glimpse of my professional journey", use_column_width=True)

    st.subheader("Career Highlights")
    st.markdown("""
    - Developed over **100 applications and websites**, serving diverse industries.
    - Increased client lead conversion rates by an average of **35%** with custom funnels.
    - Trained and mentored **20+ junior developers**, fostering growth and innovation.
    - Managed large-scale projects for clients with budgets exceeding **$500,000**.
    """)

# Skills Section
if selected_section == "Skills":
    st.header("Skills")
    st.markdown("### Technical Expertise")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Frontend Development")
        st.markdown("""
        - HTML5, CSS3, JavaScript  
        - React.js, Angular, Vue.js  
        - Bootstrap, TailwindCSS  
        - Next.js, Gatsby  
        """)

        st.subheader("DevOps & Tools")
        st.markdown("""
        - Docker, Kubernetes  
        - AWS, Azure, Google Cloud  
        - CI/CD Pipelines, Jenkins  
        """)

    with col2:
        st.subheader("Backend Development")
        st.markdown("""
        - Node.js, Python (Django, Flask)  
        - PHP (Laravel, CodeIgniter)  
        - Ruby on Rails, Java (Spring Boot)  
        """)

        st.subheader("Databases")
        st.markdown("""
        - SQL: MySQL, PostgreSQL, SQLite  
        - NoSQL: MongoDB, Firebase, Redis  
        """)

    # Skills Proficiency Chart
    st.markdown("### Skills Proficiency")
    skills_data = pd.DataFrame({
        'Skill': ['Frontend', 'Backend', 'DevOps', 'Databases'],
        'Proficiency': [90, 85, 80, 85]
    })
    st.bar_chart(skills_data.set_index('Skill'))

# Work Experience Section
if selected_section == "Work Experience":
    st.header("Work Experience")
    work_experiences = [
        {
            "role": "Senior Full-Stack Developer",
            "company": "Tech Solutions Inc.",
            "period": "2018 - Present",
            "description": """
            - Led the development of over **50 web and mobile applications**.  
            - Designed scalable, secure software architectures.  
            - Trained junior developers and enhanced team productivity.  
            """
        },
        {
            "role": "Web Developer",
            "company": "Innovate Web Studio",
            "period": "2014 - 2018",
            "description": """
            - Designed and launched **30+ websites** with modern UX/UI principles.  
            - Implemented effective funnels, increasing client conversions by **25%**.  
            - Optimized website performance for better SEO rankings.  
            """
        },
        {
            "role": "Freelance Developer",
            "company": "Self-Employed",
            "period": "2012 - 2014",
            "description": """
            - Delivered **custom websites and apps** for small businesses.  
            - Managed full-stack solutions from concept to completion.  
            """
        }
    ]

    for experience in work_experiences:
        st.subheader(f"**{experience['role']}** - {experience['company']}")
        st.markdown(f"📅 {experience['period']}")
        st.markdown(experience["description"])

# Projects Section
if selected_section == "Projects":
    st.header("Selected Projects")
    projects = [
        {
            "title": "E-Commerce App",
            "description": "Built a full-stack e-commerce solution with a secure payment gateway.",
            "technologies": "React, Node.js, Stripe API",
            "impact": "Increased online sales by 50% for the client."
        },
        {
            "title": "Social Media Platform",
            "description": "Developed a platform connecting 10,000+ users with real-time chat features.",
            "technologies": "Vue.js, Firebase, WebRTC",
            "impact": "Enhanced user engagement by 70%."
        },
        {
            "title": "Sales Funnel System",
            "description": "Designed a funnel that increased lead generation by 40%.",
            "technologies": "PHP, Laravel, Google Analytics",
            "impact": "Generated an additional $200,000 in revenue."
        }
    ]

    for project in projects:
        st.subheader(project["title"])
        st.markdown(f"**Description:** {project['description']}")
        st.markdown(f"**Technologies Used:** {project['technologies']}")
        st.markdown(f"**Impact:** {project['impact']}")
        st.markdown("---")

# Testimonials Section
if selected_section == "Testimonials":
    st.header("What Clients Say")
    testimonials = [
        "“A brilliant developer who understands client needs and delivers on time!” – Client A",
        "“Their expertise in funnels significantly boosted our revenue. Highly recommend!” – Client B",
        "“An exceptional professional with an eye for detail and design!” – Client C"
    ]
    for testimonial in testimonials:
        st.markdown(f"- {testimonial}")

# Contact Section
if selected_section == "Contact":
    st.header("Contact Me")
    st.markdown("""
    📧 **Email**: [youremail@example.com](mailto:youremail@example.com)  
    🔗 **LinkedIn**: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)  
    🖥 **Portfolio**: [yourportfolio.com](https://yourportfolio.com)  
    📂 **Download Resume**: [Click here to download](#)
    """)
    st.image("https://via.placeholder.com/600x200.png", caption="Let's Connect!", use_column_width=True)

