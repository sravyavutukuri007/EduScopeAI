import pandas as pd
import re
from datetime import datetime

# Function to parse simple natural language queries
def parse_query(query, admin_grade=None, admin_class=None):
    query = query.lower()
    filters = {}

    # Restrict to admin's allowed scope
    if admin_grade:
        filters["grade"] = admin_grade
    if admin_class:
        filters["class"] = admin_class

    # Homework submission check
    if "haven’t" in query or "not submitted" in query or "missing homework" in query:
        filters["homework_submitted"] = "Not Submitted"
    elif "submitted" in query and "not" not in query:
        filters["homework_submitted"] = "Submitted"

    # Performance/score query
    if "performance" in query or "score" in query:
        filters["type"] = "quiz_performance"

    # Quiz score numeric filters
    score_pattern = re.search(r"(?:greater|above|more)\s+than\s+(\d+)", query)
    if score_pattern:
        filters["score_min"] = int(score_pattern.group(1))
    score_pattern = re.search(r"(?:less|below|under)\s+than\s+(\d+)", query)
    if score_pattern:
        filters["score_max"] = int(score_pattern.group(1))

    # Subject filter
    subjects = ["math", "science", "computer science"]
    for subj in subjects:
        if subj in query:
            filters["subject"] = subj.title()

    # Quiz date filters
    date_match = re.search(r"(\d{1,2}[-/]\d{1,2}[-/]\d{4})", query)
    if date_match:
        quiz_date = datetime.strptime(date_match.group(1).replace("-", "/"), "%d/%m/%Y").date()
        if "before" in query:
            filters["quiz_date_before"] = quiz_date
        elif "after" in query:
            filters["quiz_date_after"] = quiz_date
        else:
            filters["quiz_date_exact"] = quiz_date

    return filters


# Function to filter dataset based on parsed filters
def apply_filters(df, filters):
    df_filtered = df.copy()

    # Grade and class restriction
    if "grade" in filters:
        df_filtered = df_filtered[df_filtered["grade"] == filters["grade"]]
    if "class" in filters:
        df_filtered = df_filtered[df_filtered["class"] == filters["class"]]

    # Homework status
    if "homework_submitted" in filters:
        df_filtered = df_filtered[df_filtered["homework_submitted"] == filters["homework_submitted"]]

    # Subject filter
    if "subject" in filters:
        df_filtered = df_filtered[df_filtered["subject"].str.lower() == filters["subject"].lower()]

    # Convert quiz_date to datetime.date
    df_filtered["quiz_date"] = pd.to_datetime(df_filtered["quiz_date"], format="%d-%m-%Y", dayfirst=True, errors="coerce").dt.date

    # Date filters
    if "quiz_date_exact" in filters:
        df_filtered = df_filtered[df_filtered["quiz_date"] == filters["quiz_date_exact"]]
    if "quiz_date_before" in filters:
        df_filtered = df_filtered[df_filtered["quiz_date"] < filters["quiz_date_before"]]
    if "quiz_date_after" in filters:
        df_filtered = df_filtered[df_filtered["quiz_date"] > filters["quiz_date_after"]]

    # Quiz score filters
    if "score_min" in filters:
        df_filtered = df_filtered[df_filtered["quiz_score"] > filters["score_min"]]
    if "score_max" in filters:
        df_filtered = df_filtered[df_filtered["quiz_score"] < filters["score_max"]]

    # Format quiz_date back to string for display
    if "quiz_date" in df_filtered.columns:
        df_filtered["quiz_date"] = df_filtered["quiz_date"].apply(lambda x: x.strftime("%d/%m/%Y") if pd.notnull(x) else "N/A")

    return df_filtered


# Main function to run the system
def run_query(df, query, admin_grade=None, admin_class=None):
    filters = parse_query(query, admin_grade, admin_class)
    filtered_df = apply_filters(df, filters)

    if filtered_df.empty:
        return "No matching records found for this query."
    else:
        return filtered_df


if __name__ == "__main__":
    from eduscope.data import load_dataset

    df = load_dataset()
    query = "Which students submitted their homework?"
    print(run_query(df, query, admin_grade=8, admin_class="A"))
