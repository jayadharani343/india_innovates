import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
from waste_classifier import WasteClassifier
import os
from datetime import datetime, timedelta
import random
import config

# Page config
st.set_page_config(
    page_title=config.PAGE_TITLE,
    page_icon=config.PAGE_ICON,
    layout=config.LAYOUT,
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    div[data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: bold;
        color: #60a5fa !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 16px;
        color: #e2e8f0 !important;
        font-weight: 600;
    }
    h1 {
        color: #ffffff !important;
        font-weight: 800;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    h2, h3 {
        color: #f1f5f9 !important;
        font-weight: 700;
    }
    p, label, span, div {
        color: #cbd5e1 !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.5);
    }
    .stMarkdown {
        color: #e2e8f0 !important;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    }
    [data-testid="stSidebar"] * {
        color: #f1f5f9 !important;
    }
    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: #1e293b;
        border: 2px dashed #475569;
        border-radius: 10px;
        padding: 1rem;
    }
    [data-testid="stFileUploader"] label {
        color: #e2e8f0 !important;
    }
    /* Dataframe */
    [data-testid="stDataFrame"] {
        background-color: #1e293b;
    }
    /* Info boxes */
    .stAlert {
        background-color: #1e293b !important;
        color: #e2e8f0 !important;
        border: 1px solid #475569;
    }
    /* Radio buttons */
    [data-testid="stRadio"] label {
        color: #f1f5f9 !important;
    }
    /* Divider */
    hr {
        border-color: #475569 !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize classifier with error handling
@st.cache_resource
def load_classifier():
    try:
        return WasteClassifier()
    except Exception as e:
        return None

classifier = load_classifier()

if classifier is None:
    st.warning("⚠️ Model not loaded. The system will work in demo mode. To enable classification, run: `python download_dataset.py`")

# Generate mock metrics data
@st.cache_data
def generate_metrics():
    return {
        "total_classified": random.randint(1200, 1500),
        "biodegradable": random.randint(400, 500),
        "recyclable": random.randint(450, 550),
        "waste": random.randint(250, 350),
        "accuracy": random.uniform(92, 97)
    }

metrics = generate_metrics()

# Header
st.title("♻️ AI Waste Recognition System")
st.markdown("### Intelligent Waste Classification Dashboard")

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/recycle-sign.png", width=80)
    st.title("Navigation")
    page = st.radio("", ["📊 Dashboard", "🔍 Classify Waste", "📈 Analytics"])
    
    st.divider()
    st.markdown("### About")
    st.info("AI-powered system using YOLOv8 to classify waste into:\n\n🌱 Biodegradable\n\n♻️ Recyclable\n\n🗑️ Waste")

# ==================== DASHBOARD PAGE ====================
if page == "📊 Dashboard":
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Classified",
            value=f"{metrics['total_classified']:,}",
            delta="+12%"
        )
    
    with col2:
        st.metric(
            label="🌱 Biodegradable",
            value=f"{metrics['biodegradable']:,}",
            delta="+8%"
        )
    
    with col3:
        st.metric(
            label="♻️ Recyclable",
            value=f"{metrics['recyclable']:,}",
            delta="+15%"
        )
    
    with col4:
        st.metric(
            label="Model Accuracy",
            value=f"{metrics['accuracy']:.1f}%",
            delta="+2.3%"
        )
    
    st.divider()
    
    # Charts Row 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Waste Distribution")
        
        # Pie chart
        fig = go.Figure(data=[go.Pie(
            labels=['Biodegradable', 'Recyclable', 'Waste'],
            values=[metrics['biodegradable'], metrics['recyclable'], metrics['waste']],
            hole=.4,
            marker=dict(colors=['#10b981', '#3b82f6', '#ef4444'])
        )])
        fig.update_layout(
            showlegend=True,
            height=350,
            margin=dict(t=0, b=0, l=0, r=0)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Weekly Classification Trend")
        
        # Line chart
        dates = [(datetime.now() - timedelta(days=i)).strftime("%b %d") for i in range(6, -1, -1)]
        data = {
            'Date': dates,
            'Biodegradable': [random.randint(50, 80) for _ in range(7)],
            'Recyclable': [random.randint(60, 90) for _ in range(7)],
            'Waste': [random.randint(30, 50) for _ in range(7)]
        }
        df = pd.DataFrame(data)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Biodegradable'], name='Biodegradable', line=dict(color='#10b981', width=3)))
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Recyclable'], name='Recyclable', line=dict(color='#3b82f6', width=3)))
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Waste'], name='Waste', line=dict(color='#ef4444', width=3)))
        
        fig.update_layout(
            height=350,
            margin=dict(t=20, b=0, l=0, r=0),
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Charts Row 2
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Hourly Classification Rate")
        
        hours = [f"{i:02d}:00" for i in range(8, 20)]
        classifications = [random.randint(20, 80) for _ in range(12)]
        
        fig = go.Figure(data=[
            go.Bar(x=hours, y=classifications, marker_color='#667eea')
        ])
        fig.update_layout(
            height=300,
            margin=dict(t=20, b=0, l=0, r=0),
            xaxis_title="Time",
            yaxis_title="Classifications"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Category Performance")
        
        categories = ['Biodegradable', 'Recyclable', 'Waste']
        accuracy = [95.2, 93.8, 91.5]
        
        fig = go.Figure(data=[
            go.Bar(
                x=categories,
                y=accuracy,
                marker_color=['#10b981', '#3b82f6', '#ef4444'],
                text=[f"{a}%" for a in accuracy],
                textposition='auto'
            )
        ])
        fig.update_layout(
            height=300,
            margin=dict(t=20, b=0, l=0, r=0),
            yaxis_title="Accuracy (%)",
            yaxis_range=[0, 100]
        )
        st.plotly_chart(fig, use_container_width=True)

# ==================== CLASSIFY WASTE PAGE ====================
elif page == "🔍 Classify Waste":
    st.header("Upload Image for Classification")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("Choose an image...", type=config.SUPPORTED_FORMATS)
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            if st.button("🔍 Classify Waste", use_container_width=True):
                if classifier is None:
                    with col2:
                        st.error("⚠️ Classifier not loaded. Please ensure YOLOv8 model is available.")
                        st.info("Run: `python download_dataset.py` first to download the base model.")
                else:
                    # Save temporarily
                    temp_path = config.TEMP_IMAGE_PATH
                    try:
                        image.save(temp_path)
                        
                        with st.spinner("Analyzing..."):
                            category, _, confidence, annotated_img = classifier.classify(temp_path)
                        
                        with col2:
                            if category == "Unknown" or confidence == 0.0:
                                st.warning("⚠️ Unable to classify image. Please try another image.")
                            else:
                                # Show annotated image if available
                                if annotated_img is not None:
                                    st.image(annotated_img, caption="Detection Result", use_column_width=True)
                                
                                st.success("✅ Classification Complete!")
                                
                                # Display result with color coding
                                color_map = config.CATEGORY_COLORS
                                
                                st.markdown(f"""
                                <div style='padding: 2rem; background: {color_map.get(category, '#6b7280')}; 
                                border-radius: 15px; text-align: center; color: white;'>
                                    <h1 style='margin: 0; color: white;'>{category}</h1>
                                    <h3 style='margin: 0; color: white;'>Confidence: {confidence:.1%}</h3>
                                </div>
                                """, unsafe_allow_html=True)
                                
                                st.divider()
                                
                                # Recommendations
                                st.subheader("♻️ Disposal Recommendations")
                                
                                if category == "Biodegradable":
                                    st.info("🌱 **Biodegradable Waste**\n\nCompost this waste or dispose in green bins. It will decompose naturally and enrich the soil.")
                                elif category == "Recyclable":
                                    st.info("♻️ **Recyclable Waste**\n\nPlace in recycling bins. Clean and dry items recycle better. Help reduce landfill waste!")
                                else:
                                    st.warning("🗑️ **General Waste**\n\nDispose in general waste bins. Cannot be recycled or composted. Consider reducing such waste.")
                    
                    finally:
                        # Cleanup
                        if os.path.exists(temp_path):
                            try:
                                os.remove(temp_path)
                            except:
                                pass

# ==================== ANALYTICS PAGE ====================
elif page == "📈 Analytics":
    st.header("Detailed Analytics & Insights")
    
    # Monthly statistics
    st.subheader("Monthly Statistics")
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    monthly_data = pd.DataFrame({
        'Month': months,
        'Biodegradable': [random.randint(300, 500) for _ in range(6)],
        'Recyclable': [random.randint(350, 550) for _ in range(6)],
        'Waste': [random.randint(200, 350) for _ in range(6)]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Biodegradable', x=monthly_data['Month'], y=monthly_data['Biodegradable'], marker_color='#10b981'))
    fig.add_trace(go.Bar(name='Recyclable', x=monthly_data['Month'], y=monthly_data['Recyclable'], marker_color='#3b82f6'))
    fig.add_trace(go.Bar(name='Waste', x=monthly_data['Month'], y=monthly_data['Waste'], marker_color='#ef4444'))
    
    fig.update_layout(barmode='group', height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Data table
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Recent Classifications")
        recent_data = pd.DataFrame({
            'Timestamp': [(datetime.now() - timedelta(minutes=i*5)).strftime("%H:%M") for i in range(10)],
            'Category': [random.choice(['Biodegradable', 'Recyclable', 'Waste']) for _ in range(10)],
            'Confidence': [f"{random.uniform(85, 99):.1f}%" for _ in range(10)]
        })
        st.dataframe(recent_data, use_container_width=True, hide_index=True)
    
    with col2:
        st.subheader("Environmental Impact")
        impact_data = pd.DataFrame({
            'Metric': ['CO₂ Saved', 'Trees Saved', 'Water Saved', 'Energy Saved'],
            'Value': ['245 kg', '12 trees', '1,500 L', '850 kWh'],
            'Icon': ['🌍', '🌳', '💧', '⚡']
        })
        st.dataframe(impact_data, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # Summary stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Items Processed", "8,542", "+234 this week")
    
    with col2:
        st.metric("Recycling Rate", "67.3%", "+5.2%")
    
    with col3:
        st.metric("Waste Diverted", "2.4 tons", "+0.3 tons")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 1rem;'>
    <p>🌍 AI Waste Recognition System | Powered by YOLOv8 | Making Earth Greener 🌱</p>
</div>
""", unsafe_allow_html=True)
