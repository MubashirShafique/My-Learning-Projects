import streamlit as st
from quiz_generator import generate_quiz
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Quiz Generator")

# Sidebar for Inputs
with st.sidebar:
    st.header("Quiz Settings")
    topic = st.text_input("Enter Quiz Topic", placeholder="e.g., Python, History")
    
    # User can select diffuclty level
    difficulty = st.selectbox(
        "Select Difficulty Level",
        options=["Easy", "Medium", "Hard"]
    )
    
    num_questions = st.slider(
        "Number of Questions",
        min_value=5,
        max_value=50,
        value=10,
        step=5
    )
    
    generate_btn = st.button("Generate Quiz", use_container_width=True)

# Session State Initialization
if "quiz" not in st.session_state:
    st.session_state.quiz = None
if "score" not in st.session_state:
    st.session_state.score = None

# Generate Quiz Logic
if generate_btn:
    if not topic:
        st.warning("Please enter a topic.")
        st.stop()
        
    with st.spinner(f"Generating {difficulty} Quiz on '{topic}'..."):
       
        quiz = generate_quiz(topic, num_questions, difficulty=difficulty)
        st.session_state.quiz = quiz
        st.session_state.score = None
        st.rerun()

# Display Quiz
if st.session_state.quiz:
    st.divider()
    st.subheader(f"📝 Quiz: {topic} ({difficulty} Level)")
 
    with st.form(key="quiz_form"):
        user_answers = {}
        for idx, q in enumerate(st.session_state.quiz.quiz_questions):
            st.markdown(f"**Q{idx+1}. {q.question}**")
            user_answers[idx] = st.radio(
                label="Select your answer:",
                options=q.options,
                key=f"q_{idx}"
            )
            st.write("")
            
        submit_btn = st.form_submit_button("Submit Answers", use_container_width=True)
        
        if submit_btn:
            score = sum(1 for idx, q in enumerate(st.session_state.quiz.quiz_questions) if user_answers[idx] == q.correct_answer)
            st.session_state.score = score

    # Display Results & PDF Download
    if st.session_state.score is not None:
        score = st.session_state.score
        total = len(st.session_state.quiz.quiz_questions)
        percentage = round((score / total) * 100, 2)
        
        st.success(f"🎯 Your Score: {score}/{total} ({percentage}%)")
        
        # PDF Generation Logic
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer)
        styles = getSampleStyleSheet()
        elements = [
            Paragraph(f"Quiz Result Report: {topic}", styles["Title"]),
            Spacer(1, 12),
            Paragraph(f"Difficulty Level: {difficulty}", styles["Heading2"]),
            Paragraph(f"Score: {score}/{total} ({percentage}%)", styles["Heading2"]),
            Spacer(1, 20)
        ]
        
        for idx, q in enumerate(st.session_state.quiz.quiz_questions):
            elements.append(Paragraph(f"{idx+1}. {q.question}", styles["BodyText"]))
            elements.append(Paragraph(f"Correct Answer: {q.correct_answer}", styles["BodyText"]))
            elements.append(Spacer(1, 8))
            
        doc.build(elements)
        pdf = buffer.getvalue()
        
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf,
            file_name=f"{topic}_quiz_result.pdf",
            mime="application/pdf",
            use_container_width=True
        )