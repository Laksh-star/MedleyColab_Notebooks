import streamlit as st
import pandas as pd
from datetime import datetime
from db import init_db, save_chat, get_chat_history, get_chat_history_df

# Page config
st.set_page_config(
    page_title="Leadership Wisdom | Panchatantra",
    page_icon="🦁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stButton > button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        border: none;
    }
    .stButton > button:hover {
        background-color: #FF6B6B;
        border: none;
    }
    div[data-testid="stSidebarNav"] {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
    }
    .css-1d391kg {
        padding: 1rem;
    }
    div.stMarkdown p {
        font-size: 1.1rem;
        line-height: 1.6;
    }
    div[data-testid="stSidebarUserContent"] {
        padding: 1rem;
    }
    .concept-tag {
        display: inline-block;
        background-color: #e9ecef;
        padding: 0.2rem 0.8rem;
        border-radius: 15px;
        margin: 0.2rem;
        font-size: 0.9rem;
    }
    .story-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #FF4B4B;
        margin: 1rem 0;
    }
    .advice-box {
        background-color: #e9ecef;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize database
init_db()

# Initialize session state
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "chat"

def switch_to_chat():
    st.session_state.active_tab = "chat"
    st.rerun()

def switch_to_history():
    st.session_state.active_tab = "history"

# Panchatantra stories and leadership lessons database
LEADERSHIP_STORIES = {
    "decision_making": {
        "lesson": "Consider all perspectives before making important decisions.",
        "story": "The Tale of the Blue Jackal: A jackal who fell into blue dye became king of the forest by being different, but his true nature was eventually revealed when he couldn't resist howling with other jackals.",
        "keywords": ["decision", "choose", "option", "pick", "select", "judgment", "choice"]
    },
    "teamwork": {
        "lesson": "Unity is strength; working together can solve seemingly impossible problems.",
        "story": "The Story of the Pigeons: A group of pigeons caught in a hunter's net flew together with the net, helping each other escape by working as one.",
        "keywords": ["team", "together", "group", "collaborate", "cooperation", "unity", "collective"]
    },
    "trust": {
        "lesson": "Trust should be earned and maintained through consistent actions.",
        "story": "The Tiger and the Traveler: A tiger gained a traveler's trust by showing his golden bracelet as proof of friendship, only to betray him later.",
        "keywords": ["trust", "faith", "belief", "confidence", "rely", "depend"]
    },
    "strategy": {
        "lesson": "Intelligence and strategy often triumph over brute force.",
        "story": "The Crow and the Serpent: A clever crow managed to defeat a dangerous snake by dropping pebbles on it, showing that strategic thinking beats raw power.",
        "keywords": ["strategy", "plan", "approach", "method", "solution", "solve", "tackle"]
    },
    "communication": {
        "lesson": "Clear and honest communication is key to successful leadership.",
        "story": "The Tale of Two Birds: Two birds living in the same tree had different approaches to communication. The one who spoke truthfully and clearly survived a woodcutter's attack, while the one who deceived met with misfortune.",
        "keywords": ["communicate", "speak", "talk", "message", "express", "discuss"]
    },
    "conflict_resolution": {
        "lesson": "Wisdom and patience are more effective than force in resolving conflicts.",
        "story": "The Story of Two Cats and the Monkey: Two cats fighting over a piece of bread asked a monkey to divide it fairly. The cunning monkey kept taking bites to 'even out' the pieces until nothing was left, teaching that hasty conflict resolution can lead to losing everything.",
        "keywords": ["conflict", "dispute", "fight", "resolve", "problem", "issue", "disagreement"]
    }
}

def get_leadership_advice(query):
    query = query.lower()
    best_match = None
    max_matches = 0
    matched_concepts = []
    
    # Check each category for keyword matches
    for category, content in LEADERSHIP_STORIES.items():
        matches = sum(1 for keyword in content["keywords"] if keyword in query)
        if matches > 0:
            matched_concepts.append(category.replace('_', ' ').title())
            if matches > max_matches:
                max_matches = matches
                best_match = category
    
    # If no direct matches, return the most general advice
    if not best_match:
        matched_concepts = ["General Leadership"]
        return {
            "advice": "Every situation is an opportunity for leadership. Consider the core principles of clear communication, teamwork, and strategic thinking.",
            "story": "The Tale of the Wise King: A king once gathered all his advisors and asked them the most important quality of leadership. Each gave different answers - strength, wisdom, decisiveness. The king concluded that true leadership requires a balance of all these qualities, adapting to each unique situation.",
            "concepts": matched_concepts
        }
    
    return {
        "advice": LEADERSHIP_STORIES[best_match]["lesson"],
        "story": LEADERSHIP_STORIES[best_match]["story"],
        "concepts": matched_concepts
    }

# UI Components
st.title("🦁 Leadership Wisdom from Panchatantra")
st.markdown("""
<p style='font-size: 1.2rem; color: #666;'>
    Discover ancient leadership wisdom through timeless stories. Ask questions about leadership 
    and management to receive insights backed by Panchatantra tales.
</p>
""", unsafe_allow_html=True)

# Create tabs in sidebar with custom styling
tab = st.sidebar.radio("Navigation", ["💭 Chat", "📜 History"], key="nav_tabs", 
                       index=0 if st.session_state.active_tab == "chat" else 1)

# Example queries in sidebar (only show in chat tab)
if tab == "💭 Chat":
    with st.sidebar.container():
        st.markdown("### 💡 Example Questions")
        example_questions = [
            "How do I make better decisions as a leader?",
            "What's the importance of teamwork?",
            "How should I build trust in my team?",
            "What's the best strategy to solve problems?",
            "How can I improve my communication skills?",
            "How do I resolve conflicts effectively?"
        ]
        for q in example_questions:
            st.markdown(f"• _{q}_")

# Display Chat History in sidebar history tab
if tab == "📜 History":
    st.sidebar.markdown("### 📜 Chat History")
    chat_history = get_chat_history()
    
    if chat_history:
        # Add export button
        df = get_chat_history_df()
        if df is not None:
            csv = df.to_csv(index=False)
            st.sidebar.download_button(
                label="📥 Export History as CSV",
                data=csv,
                file_name=f"leadership_chat_history_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                help="Download your chat history as a CSV file"
            )
        
        st.sidebar.markdown("#### Your Leadership Journey")
        for entry in chat_history:
            with st.sidebar.container():
                col1, col2 = st.sidebar.columns([1, 4])
                with col1:
                    st.markdown(f"**{entry['timestamp']}**")
                with col2:
                    st.markdown(f"_{entry['question']}_")
                if 'concepts' in entry:
                    st.sidebar.markdown("".join([f'<span class="concept-tag">{concept}</span> ' for concept in entry['concepts']]), unsafe_allow_html=True)
                st.sidebar.divider()
        
        if st.sidebar.button("💭 Return to Chat", type="primary"):
            switch_to_chat()
    else:
        st.sidebar.info("No chat history yet. Start asking questions!")

# Main chat interface
if tab == "💭 Chat":
    user_input = st.text_input("Your leadership question:", 
                              placeholder="Type your question here...",
                              help="Ask about leadership, management, or decision-making")

    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if st.button("🎯 Ask", type="primary"):
            if user_input:
                response = get_leadership_advice(user_input)
                
                # Save to database
                timestamp = datetime.now().strftime("%H:%M")
                save_chat(timestamp, user_input, response["concepts"])
                
                # Display response
                st.markdown("### 💡 Leadership Advice")
                st.markdown(f'<div class="advice-box">{response["advice"]}</div>', unsafe_allow_html=True)
                
                st.markdown("### 📚 Related Panchatantra Story")
                st.markdown(f'<div class="story-box">{response["story"]}</div>', unsafe_allow_html=True)
                
                # Show concepts for current query
                st.markdown("### 🏷️ Related Leadership Concepts")
                st.markdown("".join([f'<span class="concept-tag">{concept}</span> ' for concept in response["concepts"]]), unsafe_allow_html=True)
            else:
                st.warning("Please enter a question!")
