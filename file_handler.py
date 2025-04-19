import json
import os

def save_resume(resume_data, encrypted_data):
    # Create or load existing resumes
    try:
        with open('resumes.json', 'r') as file:
            resumes = json.load(file)  # Try to load the existing data from the file
    except (FileNotFoundError, json.JSONDecodeError):
        resumes = []  # If file not found or invalid JSON, start with an empty list
    
    # Add the new encrypted data to the list
    resumes.append({"resume": encrypted_data})
    
    # Save the updated list back to the file
    with open('resumes.json', 'w') as file:
        json.dump(resumes, file, indent=4)  # Using indent for pretty printing

def load_resumes():
    # Load all the resumes from the file
    try:
        with open('resumes.json', 'r') as file:
            resumes = json.load(file)  # Try to load the existing data from the file
    except (FileNotFoundError, json.JSONDecodeError):
        resumes = []  # If file not found or invalid JSON, return an empty list
    return resumes

def find_resume(resume_data):
    """Find a resume by its identifier (can be partial)"""
    resumes = load_resumes()
    
    # Clean up the input by removing whitespace
    resume_data = resume_data.strip()
    
    # If exact match exists, return it
    for resume in resumes:
        if resume.get("resume") == resume_data:
            return resume.get("resume")
    
    # If no exact match, try to find a resume that contains the provided data
    # This is useful if the user only remembers part of their identifier
    if resume_data:
        for resume in resumes:
            stored_resume = resume.get("resume", "")
            if resume_data in stored_resume:
                return stored_resume
    
    return None
