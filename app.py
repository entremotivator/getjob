import streamlit as st

# Set page configuration
st.set_page_config(page_title="Full-Stack Developer Resume", page_icon="💻", layout="wide")

# App title and header
st.title("💻 Full-Stack Developer Resume")
st.subheader("10 Years of Expertise in App Development, Website Development, and Funnel Design")

# About Section
st.header("About Me")
st.markdown("""
Hi, I'm a seasoned **Full-Stack Developer** with a decade of experience crafting efficient, scalable, and user-centric solutions. 
I specialize in:
- **App Development**: Building robust applications tailored to meet diverse user needs.
- **Website Development**: Creating responsive, SEO-friendly websites with seamless user experiences.
- **Funnel Development**: Designing high-converting funnels to drive business success.
""")

# Skills Section
st.header("Skills")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Frontend")
    st.markdown("""
    - HTML5, CSS3, JavaScript
    - React.js, Angular, Vue.js
    - Bootstrap, TailwindCSS
    """)

with col2:
    st.subheader("Backend")
    st.markdown("""
    - Node.js, Python (Django, Flask)
    - PHP (Laravel, CodeIgniter)
    - Ruby on Rails
    """)

st.subheader("DevOps & Tools")
st.markdown("""
- Docker, Kubernetes
- Git, GitHub, GitLab, Bitbucket
- AWS, Azure, Google Cloud
""")

st.subheader("Databases")
st.markdown("""
- SQL: MySQL, PostgreSQL, SQLite
- NoSQL: MongoDB, Firebase, Redis
""")

# Work Experience Section
st.header("Work Experience")
st.markdown("""
### Senior Full-Stack Developer
**Tech Solutions Inc.** *(2018 - Present)*  
- Led the development of over 50 web and mobile applications for clients across industries.  
- Spearheaded the design of scalable and secure software architectures.  
- Trained junior developers and enhanced team productivity.

### Web Developer
**Innovate Web Studio** *(2014 - 2018)*  
- Designed and launched over 30 websites with modern UX/UI principles.  
- Implemented effective funnels that increased client conversions by 25%.  
- Optimized website performance for better SEO rankings.

### Freelance Developer
**Self-Employed** *(2012 - 2014)*  
- Worked with small businesses to create custom websites and apps.  
- Delivered full-stack solutions on time and within budget.
""")

# Projects Section
st.header("Selected Projects")
st.markdown("""
- **E-Commerce App**: Built a full-stack solution for a retail company, including a secure payment gateway.
- **Social Media Platform**: Developed a platform connecting 10,000+ users with real-time chat features.
- **Sales Funnel System**: Designed a funnel that increased lead generation by 40% for a marketing client.
""")

# Contact Section
st.header("Contact Me")
st.markdown("""
- **Email**: [youremail@example.com](mailto:youremail@example.com)  
- **LinkedIn**: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)  
- **GitHub**: [github.com/yourusername](https://github.com/yourusername)  
- **Portfolio**: [yourportfolio.com](https://yourportfolio.com)
""")
