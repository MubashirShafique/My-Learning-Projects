# +++++++++++++++++++++++++++++  Importing Libraries  ++++++++++++++++++++++++++++++++++++++++
import os
import re
import streamlit as st
from dotenv import load_dotenv
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Aapke purane files se imports
from search_agent import agent
from final_report_generator_agent import research_chain


load_dotenv()


st.set_page_config(page_title="AI Research Assistant", page_icon="📝", layout="centered")

st.title("📝 Autonomous AI Research Assistant")
st.write("Enter your research topic or question below. The agent will browse the web and generate a clean report.")

# this function is for make a report clean and professional
def clean_markdown_for_reportlab(text):
    """
    Safely converts Markdown to ReportLab-compatible XML tags.
    """
    if not text:
        return ""
    
   
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = text.replace("&lt;br/&gt;", "<br/>").replace("&lt;br&gt;", "<br/>")
    
  
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    
   
    text = re.sub(r'^#+\s*(.*)$', r'<font size="14"><b>\1</b></font>', text, flags=re.MULTILINE)
    
    # 4. Handle standard markdown bullets
    text = re.sub(r'^\s*[-*+]\s+', r'• ', text, flags=re.MULTILINE)
    
    # 5. Convert line breaks
    text = text.replace("\n", "<br/>")
    
    return text

# Helper function to generate PDF bytes
def generate_pdf(report_text, urls):
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, 
        pagesize=letter, 
        rightMargin=54, 
        leftMargin=54, 
        topMargin=54, 
        bottomMargin=54
    )
    story = []
    
    styles = getSampleStyleSheet()
    
    # Custom Styles for Beautiful PDF
    title_style = ParagraphStyle(
        'PDFTitle', parent=styles['Heading1'], fontSize=24, spaceAfter=20, textColor=colors.HexColor("#1E3A8A")
    )
    body_style = ParagraphStyle(
        'PDFBody', parent=styles['BodyText'], fontSize=10, leading=15, spaceAfter=10, textColor=colors.HexColor("#1F2937")
    )
    url_heading_style = ParagraphStyle(
        'PDFUrlHeading', parent=styles['Heading2'], fontSize=14, spaceBefore=20, spaceAfter=10, textColor=colors.HexColor("#0D9488")
    )
    url_style = ParagraphStyle(
        'PDFUrl', parent=styles['BodyText'], fontSize=9, leading=13, textColor=colors.HexColor("#2563EB")
    )

    # Add Content to PDF
    story.append(Paragraph("Research Report", title_style))
    story.append(Spacer(1, 10))
    
    # Process text using our new safe regex cleaner
    cleaned_text = clean_markdown_for_reportlab(report_text)
    
    # Wrap in explicit <para> tags to enforce parser validation rules safely
    final_xml = f"<para>{cleaned_text}</para>"
    
    story.append(Paragraph(final_xml, body_style))
    
    # Add URLs Section
    if urls:
        story.append(Spacer(1, 15))
        story.append(Paragraph("Sources & References", url_heading_style))
        for url in urls:
            link_tag = f"<a href='{url}' color='#2563EB'>{url}</a>"
            story.append(Paragraph(link_tag, url_style))
            story.append(Spacer(1, 4))
            
    doc.build(story)
    buffer.seek(0)
    return buffer


# User Input Form

user_query = st.text_input("What do you want to research today?", placeholder="e.g., Latest tech trends in Pakistan")

if st.button("Generate Report", type="primary"):
    if not user_query.strip():
        st.warning("Please enter a valid question or topic.")
    else:
        with st.spinner("🕵️‍♂️ Agent is searching the web and compiling data... Please wait."):
            try:
                # 1. Run Search Agent
                config = {"configurable": {"thread_id": "streamlit_session"}}
                response = agent.invoke(
                    {"messages": [("user", user_query)]},
                    config=config
                )
                
                # 2. Extract History
                raw_history = ""
                for msg in response['messages']:
                    raw_history += f"[{msg.type.upper()}]: {msg.content}\n\n"
                
                # 3. Run Structured Reporter Chain 
                final_response = research_chain.invoke({"agent_output": raw_history})
                
                # Session State saving
                st.session_state['report'] = final_response.research_report
                st.session_state['urls'] = final_response.urls
                st.session_state['generated'] = True
                
            except Exception as e:
                st.error(f"An error occurred: {e}")


if st.session_state.get('generated'):
    st.success("✨ Report Generated Successfully!")
    
    # Visual Container for UI Report
    st.subheader("📋 Generated Report Preview")
    with st.container(border=True):
        st.markdown(st.session_state['report'])
        
        if st.session_state['urls']:
            st.markdown("### 🔗 Sources & References")
            for url in st.session_state['urls']:
                st.markdown(f"- [{url}]({url})") 

    st.write("---")
    
   # for PDF 
    try:
        pdf_data = generate_pdf(st.session_state['report'], st.session_state['urls'])
        
        st.download_button(
            label="📥 Download PDF Report",
            data=pdf_data,
            file_name="AI_Research_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    except Exception as pdf_err:
        st.error(f"Could not construct PDF layout due to unparseable agent markdown: {pdf_err}")