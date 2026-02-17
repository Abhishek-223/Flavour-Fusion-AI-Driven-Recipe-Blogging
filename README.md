# 🍽️ Flavour Fusion: AI-Driven Recipe Blogging

Flavour Fusion is an interactive Streamlit application that leverages the power of Google's Gemini AI to generate creative, detailed, and engaging recipe blogs. Whether you're a food enthusiast looking for inspiration or a developer exploring AI integration, this tool creates unique culinary content on demand.

## ✨ Features

- **AI-Powered Recipes**: Generates comprehensive recipe blogs including introductions, ingredients, step-by-step instructions, and cooking tips.
- **Customizable Output**: Users can specify the recipe topic and the desired word count (from 100 to 2000 words).
- **Interactive UI**: Clean and user-friendly interface built with Streamlit.
- **Entertaining Loading**: Displays random programmer jokes while the AI generates your content.
- Error Handling: Gracefully handles API errors and empty inputs.

## 🎥 Video Demo

Watch the application in action: [Click here to watch the demo video](https://drive.google.com/file/d/19gdzkg9R3FgiyhT_-ng3N-vgmlHuZgl5/view?usp=sharing)

## 🛠️ Tech Stack

- **Python**: Core programming language.
- **Streamlit**: For building the web application interface.
- **Google Generative AI (Gemini)**: The engine behind the recipe generation (`gemini-2.5-flash` model).
- **Python-dotenv**: For managing environment variables securely.

## 🚀 Installation & Setup

Follow these steps to get the project running locally.

### Prerequisites

- Python 3.9 or higher installed.
- A Google Cloud API Key for Gemini.

### Steps

1.  **Clone the Repository**
    ```bash
    git clone <your-repo-url>
    cd "Flavour Fusion AI-Driven Recipe Blogging"
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    Create a `.env` file in the root directory and add your Gemini API Key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

## 💡 Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

1.  The app will open in your default browser (usually at `http://localhost:8501`).
2.  Enter a **Recipe Topic** (e.g., "Authentic Italian Lasagna").
3.  Set the desired **Word Count**.
4.  Click **Generate Recipe Blog**.
5.  Enjoy your AI-generated recipe!

## 📂 Project Structure

```
Flavour Fusion AI-Driven Recipe Blogging/
├── app.py                # Main application logic and UI
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (not committed)
├── .gitignore            # Files to ignore in git
└── README.md             # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👥 Team Details

**Team ID:** LTVIP2026TMIDS76104  
**Team Size:** 5  

| Role | Name |
| :--- | :--- |
| **Team Leader** | Peetha Madhurima |
| **Team Member** | Nithin Tirukkovalluri |
| **Team Member** | Abhishek Kumar Sah |
| **Team Member** | Dommeti Pujitha |
| **Team Member** | Indra Narayan Yadav |

## 📄 License

This project is licensed under the MIT License.
