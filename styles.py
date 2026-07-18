def load_css():
    return """
    <style>

    /* Hide Streamlit default menu & footer */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Main App */

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        padding-left:2rem;
        padding-right:2rem;
    }

    /* Card Style */

    div[data-testid="stVerticalBlock"]{
        border-radius:15px;
    }

    /* Buttons */

    .stButton>button{

        width:100%;
        border-radius:12px;
        height:50px;
        font-size:18px;
        font-weight:600;
    }

    /* Text Areas */

    textarea{

        border-radius:10px;
    }

    </style>
    """