# EduScopeAI

**EduScopeAI** is an interactive educational analytics tool that allows teachers and administrators to query student performance and homework submissions in natural language. It leverages **Python, Pandas, and Regex-based parsing** to filter and display data efficiently.

---

## **Features**

- ✅ View which students have submitted or not submitted their homework  
- ✅ Filter student performance based on quiz scores  
- ✅ Query by specific quiz date or subject  
- ✅ Restrict data access by grade and class  
- ✅ Supports interactive queries via **Streamlit** UI  

---

## **Tech Stack**

- **Python 3.10+** – Core programming language  
- **Pandas** – Data manipulation and filtering  
- **Regex** – Natural language query parsing  
- **Streamlit** – Interactive UI for querying  
- **Optional:** LangChain & OpenAI API (for AI-based parsing, can be integrated later)  

---

## **Dataset**

- File: `dumroo_dataset.csv`  
- Contains columns:  
  - `student_name` – Name of the student  
  - `grade` – Grade (e.g., 8)  
  - `class` – Section (e.g., A, B)  
  - `homework_submitted` – `"Submitted"` or `"Not Submitted"`  
  - `quiz_score` – Numeric score  
  - `quiz_date` – Date in `DD-MM-YYYY` format  
  - `subject` – Subject of the quiz (e.g., Math, Science)  

---

## **Setup & Installation**

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd eduscopeai
   ```

2. Create and activate the virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate    # Windows
   source .venv/bin/activate # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit UI:
   ```bash
   streamlit run eduscope/ui_app.py
   ```

5. Open the URL displayed in the terminal to interact with the app.

---

## **Usage**

Type natural language queries in the input box, for example:

- `"Which students haven’t submitted their homework yet?"`  
- `"Which students got quiz score greater than 85?"`  
- `"Show students who took the quiz on 03-11-2025"`  

The app will filter the dataset and display results accordingly.

---

## **Project Structure**

```
eduscopeai/
├── eduscope/
│   ├── __init__.py
│   ├── data.py              # Dataset loading
│   ├── parser.py            # Query parsing & filtering
│   ├── ui_app.py            # Streamlit UI
├── sample_dataset.csv       # Sample dataset
├── requirements.txt
└── README.md
```

---

## **Future Improvements**

- Integrate **LangChain + OpenAI API** for AI-driven queries  
- Add **Gradio UI** for an alternative web interface  
- Expand dataset and analytics features  
- Deploy online for real-time access  

---

## **License**

This project is **free to use** and open-source.

