import streamlit as st
import pandas as pd
import catboost as cb
import os

# Page config
st.set_page_config(page_title="GlucoGuide", layout="wide")

# Inject CSS for styling
st.markdown("""
    <style>
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    .orange-header {
        background-color: #f7931e;
        padding: 60px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 40px;
    }
    .orange-header h1 {
        font-size: 60px;
        font-weight: 900;
        color: white;
        margin: 0;
    }
    .info-panel {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        font-size: 18px;
        line-height: 1.7;
        color: #333;
    }
    .info-panel h2 {
        font-size: 28px;
        font-weight: 700;
        color: #222;
        margin-bottom: 15px;
    }
    .info-panel ul {
        margin-top: 10px;
        margin-bottom: 20px;
    }

    /* Input card styling */
    .input-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        height: 100%;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .input-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
    }
    .input-card h3 {
        font-size: 20px;
        color: #f7931e;
        margin-bottom: 15px;
        font-weight: 600;
    }
    .input-card label {
        font-size: 16px;
        color: #555;
        margin-bottom: 8px;
        display: block;
    }

    /* Sidebar wrapper only */
    [data-testid="stSidebar"] {
        padding: 2rem 1rem;
        background-color: #fafafa;
    }

    /* Sidebar title text */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2 {
        font-size: 24px !important;
        font-weight: 800 !important;
        color: #f7931e !important;
        margin-bottom: 20px;
    }

    /* Sidebar labels and radio/button text */
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stRadio div {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #333 !important;
    }
    
    /* Custom button styling */
    .stButton > button {
        background-color: #f7931e;
        color: white;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        width: 100%;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #e57f1d;
    }
    
    /* Results styling */
    .results-container {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 25px;
        margin-top: 30px;
        box-shadow: inset 0 0 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🔍 Explore GlucoGuide")
menu = st.sidebar.radio("Navigate", ["🏠 Home", "📊 Check Your Risk", "🧰 Tools & Resources"])

# Home Page content
if menu == "🏠 Home":
    # Header
    st.markdown('<div class="orange-header"><h1>GlucoGuide</h1></div>', unsafe_allow_html=True)

    # Layout
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="info-panel">
            <h2>Type 1 Diabetes</h2>
            <p>Type 1 diabetes is an autoimmune condition. Your immune system mistakenly attacks the insulin-producing beta cells in your pancreas. This results in very little or no insulin production.</p>
            <p>Insulin is vital for moving glucose from the bloodstream into cells for energy. Without insulin, glucose builds up in the blood, leading to high blood sugar (hyperglycemia), which can cause severe complications if untreated.</p>
            <p><strong>Symptoms of Type 1:</strong></p>
            <ul>
                <li>Urinating often</li>
                <li>Feeling very thirsty</li>
                <li>Extreme fatigue</li>
                <li>Blurry vision</li>
                <li>Slow healing cuts or bruises</li>
                <li>Weight loss even while eating more</li>
            </ul>
            <p>Type 1 diabetes usually appears in childhood or adolescence, but can occur at any age. It cannot currently be prevented.</p>
            <p>Treatment involves insulin therapy, an eating plan, physical activity, and close monitoring with your care team.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-panel">
            <h2>Type 2 Diabetes</h2>
            <p>Type 2 diabetes occurs when the body becomes resistant to insulin or does not produce enough of it. Initially, the pancreas compensates by producing more insulin, but over time it can not keep up.</p>
            <p>This type is more common in adults over 45, but it is increasingly affecting younger populations.</p>
            <p><strong>Symptoms of Type 2:</strong></p>
            <ul>
                <li>Urinating often</li>
                <li>Increased thirst and hunger</li>
                <li>Fatigue</li>
                <li>Blurry vision</li>
                <li>Slow healing cuts or bruises</li>
                <li>Tingling in hands/feet</li>
            </ul>
            <p>Treatment typically begins with healthy eating and exercise. Medications or insulin may be needed over time to control blood sugar.</p>
            <p>Some cases may be misdiagnosed. If you are not responding to typical treatment, consult an endocrinologist.</p>
        </div>
        """, unsafe_allow_html=True)

# Check Your Risk page content 
elif menu == "📊 Check Your Risk":
    st.markdown('<div class="orange-header" style="padding: 40px;"><h1 style="font-size: 40px;">Check Your Diabetes Risk</h1></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align:center; margin-bottom: 30px;">
        <h2 style="font-size: 24px; color: #333;">Enter your health information to estimate your diabetes risk</h2>
        <p style="font-size: 16px; color: #666;">All information is processed locally and not stored</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load the model
    model_path = os.path.join(os.path.dirname(__file__), "model.cbm")
    model = cb.CatBoostClassifier()
    model.load_model(model_path)

    # First row of inputs
    col1, col2, col3, col4 = st.columns(4, gap="small")
    
    with col1:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<h3>Pregnancies</h3>', unsafe_allow_html=True)
        pregnancies = st.number_input("Number of pregnancies", min_value=0, max_value=20, value=1, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<h3>Glucose Level</h3>', unsafe_allow_html=True)
        glucose = st.number_input("Blood glucose (mg/dL)", min_value=0, max_value=250, value=100, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<h3>Blood Pressure</h3>', unsafe_allow_html=True)
        bp = st.number_input("Blood pressure (mm Hg)", min_value=0, max_value=200, value=70, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col4:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<h3>Skin Thickness</h3>', unsafe_allow_html=True)
        skin_thickness = st.number_input("Skin thickness (mm)", min_value=0, max_value=100, value=20, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Second row of inputs
    col5, col6, col7, col8 = st.columns(4, gap="small")
    
    with col5:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<h3>Insulin</h3>', unsafe_allow_html=True)
        insulin = st.number_input("Insulin level (mu U/ml)", min_value=0.0, max_value=900.0, value=80.0, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col6:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<h3>BMI</h3>', unsafe_allow_html=True)
        bmi = st.number_input("Body Mass Index", min_value=10.0, max_value=70.0, value=25.0, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col7:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<h3>Diabetes Pedigree</h3>', unsafe_allow_html=True)
        dpf = st.number_input("Family history function", min_value=0.0, max_value=2.5, value=0.5, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col8:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<h3>Age</h3>', unsafe_allow_html=True)
        age = st.number_input("Age in years", min_value=10, max_value=100, value=30, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # Center the predict button
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        predict_button = st.button("🔍 Predict My Risk", key="predict_button")

    # Prediction results
    if predict_button:
        feature_names = [
            'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
            'DiabetesPedigreeFunction', 'Age'
        ]
        
        user_input = pd.DataFrame([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]], columns=feature_names)
        prediction = model.predict(user_input)[0]
        probability = model.predict_proba(user_input)[0][1]
        
        st.markdown('<div class="results-container">', unsafe_allow_html=True)
        
        risk_color = "#e74c3c" if prediction == 1 else "#2ecc71"
        risk_text = "⚠️ Higher Risk" if prediction == 1 else "✅ Lower Risk"
        
        st.markdown(f"""
        <h2 style="text-align: center; font-size: 28px; margin-bottom: 20px;">Your Results</h2>
        <div style="display: flex; justify-content: center; margin-bottom: 30px;">
            <div style="background-color: {risk_color}; color: white; padding: 15px 30px; border-radius: 30px; font-size: 24px; font-weight: bold;">
                {risk_text} ({probability:.1%})
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Risk factors feedback
        st.subheader("💡 Personalized Insights")
        
        # Create two columns for feedback
        feedback_col1, feedback_col2 = st.columns(2)
        
        with feedback_col1:
            if bmi >= 30:
                st.warning("⚠️ Your BMI indicates obesity. This increases diabetes risk.")
            if glucose >= 126:
                st.warning("⚠️ Your glucose level is elevated. Consult a healthcare provider.")
            if pregnancies > 4:
                st.info("ℹ️ Multiple pregnancies can increase diabetes risk.")
                
        with feedback_col2:
            if bp >= 130:
                st.warning("⚠️ Your blood pressure is elevated. Monitor regularly.")
            if dpf > 0.8:
                st.info("ℹ️ Your family history shows increased risk.")
            if age > 45:
                st.info("ℹ️ Age is a risk factor for type 2 diabetes.")
        
        st.markdown("""
        <div style="background-color: #e8f4f8; padding: 15px; border-radius: 8px; margin-top: 20px;">
          <p style="font-size: 16px;"><strong>Note:</strong> This tool provides an estimate based on limited factors. 
          For accurate diagnosis, please consult a healthcare professional.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Tools & Resources page content
elif menu == "🧰 Tools & Resources":
    st.title("🧰 Tools & Resources")
    st.markdown("""
    <style>
    .resource-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        height: 100%;
    }
    .resource-card h3 {
        font-size: 22px;
        margin-bottom: 10px;
    }
    .resource-card p {
        font-size: 16px;
        color: #444;
    }
    .resource-card a {
        text-decoration: none;
        font-weight: 600;
        color: #f7931e;
    }
    </style>
    """, unsafe_allow_html=True)

    # Category filter
    filter = st.radio("Filter by category:", ["🧰 Show All", "🍽️ Food", "🛡️ Prevention", "🎓 Education", "💰 Financial", "📍 Community", "✅ Risk Test"], horizontal=True)

    # Define all cards
    resources = [
        {
            "category": "🍽️ Food",
            "title": "Diabetes Food Hub",
            "desc": "Browse diabetes-friendly recipes and meal plans to stay on track with delicious and healthy meals.",
            "link": "https://diabetesfoodhub.org/"
        },
        {
            "category": "🎓 Education",
            "title": "Education Programs",
            "desc": "Find certified diabetes self-management education programs for expert support and guidance.",
            "link": "https://diabetes.org/tools-resources/diabetes-education-programs"
        },
        {
            "category": "✅ Risk Test",
            "title": "Diabetes Risk Test",
            "desc": "Take a short, easy test to assess your risk of developing type 2 diabetes.",
            "link": "https://diabetes.org/diabetes-risk-test"
        },
        {
            "category": "🛡️ Prevention",
            "title": "Prevention Guide",
            "desc": "Learn science-backed strategies for reducing your risk of type 2 diabetes.",
            "link": "https://diabetes.org/about-diabetes/diabetes-prevention"
        },
        {
            "category": "📍 Community",
            "title": "Find Help Near You",
            "desc": "Search for local services—food, housing, transportation, financial aid—and more in your community.",
            "link": "https://diabetes.findhelp.com/"
        },
        {
            "category": "💰 Financial",
            "title": "Managing Diabetes Costs",
            "desc": "Discover programs, tips, and assistance to help lower the cost of managing diabetes.",
            "link": "https://diabetes.org/tools-resources/managing-diabetes-costs"
        },
    ]

    # Filter cards
    filtered = resources if filter == "🧰 Show All" else [r for r in resources if r["category"] == filter]

    # Display cards in 2 columns
    col1, col2 = st.columns(2, gap="large")
    for i, r in enumerate(filtered):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
            <div class="resource-card">
                <h3>{r['title']}</h3>  <!-- Removed category from the title -->
                <p>{r['desc']}</p>
                <a href="{r['link']}" target="_blank">Learn More →</a>
            </div>
            """, unsafe_allow_html=True)
