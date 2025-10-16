# database_setup.py
# This is the final, corrected version that contains all the data and saves it properly.

import sqlite3

# --- Connect to the database (or create it) ---
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# --- Create all three tables ---
# 1. The main jobs table for the homepage
cursor.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    post_name TEXT, exam_name TEXT, conducting_body TEXT, "group" TEXT, 
    gazetted_status TEXT, pay_level INTEGER, salary TEXT, eligibility TEXT, 
    age_limit TEXT, pet_status TEXT
);
''')
# 2. The details table for the info cards
cursor.execute('''
CREATE TABLE IF NOT EXISTS job_details (
    id INTEGER PRIMARY KEY,
    job_id INTEGER, category TEXT, title TEXT, description TEXT, 
    FOREIGN KEY (job_id) REFERENCES jobs (id)
);
''')
# 3. The cutoffs table for the details page
cursor.execute('''
CREATE TABLE IF NOT EXISTS job_cutoffs (
    id INTEGER PRIMARY KEY,
    job_id INTEGER, category TEXT, cutoff_score TEXT, year INTEGER, 
    FOREIGN KEY (job_id) REFERENCES jobs (id)
);
''')

# --- Clear any old data to prevent duplicates ---
cursor.execute('DELETE FROM jobs')
cursor.execute('DELETE FROM job_details')
cursor.execute('DELETE FROM job_cutoffs')

# --- Here is ALL the data for the main table ---
jobs_data = [
    ('IAS Officer', 'UPSC CSE', 'UPSC', 'A', 'Gazetted', 10, '₹56,100+', 'Any Graduation', '21-32', 'No PET'),
    ('IPS Officer', 'UPSC CSE', 'UPSC', 'A', 'Gazetted', 10, '₹56,100+', 'Any Graduation', '21-32', 'PET Required'),
    ('IFS Officer', 'UPSC CSE', 'UPSC', 'A', 'Gazetted', 10, '₹60,000+', 'Any Graduation', '21-32', 'No PET'),
    ('RBI Grade B', 'RBI Grade B Exam', 'RBI', 'A', 'Gazetted', 10, '₹70,000+', 'Graduation (50%+)', '21-30', 'No PET'),
    ('SBI PO', 'SBI PO Exam', 'SBI', 'A', 'Gazetted', 7, '₹40,000+', 'Any Graduation', '21-30', 'No PET'),
    ('IBPS PO', 'IBPS PO Exam', 'IBPS', 'A', 'Gazetted', 7, '₹35,000+', 'Any Graduation', '20-30', 'No PET'),
    ('SSC CGL (AAO)', 'SSC CGL', 'SSC', 'B', 'Non-Gazetted', 8, '₹45,000+', 'Any Graduation', '18-32', 'No PET'),
    ('NDA Officer', 'NDA Exam', 'UPSC', 'A', 'Gazetted', 10, '₹56,100+', '10+2 (PCM)', '16.5-19.5', 'PET Required'),
    ('ISRO Scientist', 'ISRO ICRB', 'ISRO', 'A', 'Gazetted', 10, '₹60,000+', 'B.Tech/B.E (60%+)', '21-35', 'No PET'),
    ('DRDO Scientist', 'DRDO Entry Test', 'DRDO', 'A', 'Gazetted', 10, '₹60,000+', 'B.Tech/B.E (First Class)', '21-28', 'No PET'),
    ('Railway Group A', 'UPSC ESE', 'UPSC', 'A', 'Gazetted', 10, '₹56,100+', 'B.Tech/B.E', '21-30', 'No PET'),
    ('LIC AAO', 'LIC AAO Exam', 'LIC', 'B', 'Non-Gazetted', 8, '₹40,000+', 'Any Graduation', '21-30', 'No PET')
]
cursor.executemany('INSERT INTO jobs VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', jobs_data)

# --- Here is the sample data for the details page ---
details_data = [
    (1, 'Eligibility', 'Core Eligibility Criteria', 'Must be a citizen of India, hold a degree, and be between 21-32 years of age.'),
    (1, 'Exam Pattern', 'Three-Stage Process', 'Consists of Preliminary (objective), Mains (descriptive), and an Interview.'),
    (12, 'Selection Process', 'Online Examination', 'Consists of Prelims, Mains, and an interview. Focuses on reasoning, quant, and insurance awareness.'),
    (12, 'Salary', 'Attractive Package', 'Includes basic pay plus allowances, resulting in a competitive in-hand salary.')
]
cursor.executemany('INSERT INTO job_details VALUES (NULL, ?, ?, ?, ?)', details_data)

cutoffs_data = [
    (1, 'UR (General)', '92.51', 2023), (1, 'OBC', '89.12', 2023),
    (12, 'UR (General)', '55.25', 2023), (12, 'OBC', '51.50', 2023), (12, 'SC', '48.75', 2023)
]
cursor.executemany('INSERT INTO job_cutoffs VALUES (NULL, ?, ?, ?, ?)', cutoffs_data)


# --- THIS IS THE MOST IMPORTANT LINE ---
# It's like hitting the "Save" button. Without this, no data gets saved.
conn.commit()

# --- Close the connection ---
conn.close()

print("Database 'jobs.db' has been created and populated correctly!")
