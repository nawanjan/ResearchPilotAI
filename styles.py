def load_css():
    return """
    <style>

    .main {
        padding-top: 1rem;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1 {
        color: #4F8BF9;
        text-align: center;
    }

    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }

    .stTextInput input {
        border-radius: 10px;
    }

    div[data-testid="stExpander"] {
        border-radius: 10px;
        border: 1px solid #cccccc;
    }

    </style>
    """