import streamlit as st
from encryptor import encrypt_resume, decrypt_resume
from file_handler import save_resume, load_resumes, find_resume
from ui import get_user_input

# Function to display the UI and handle user input
def main():
    st.title("ResumeVault")
    
    # Navigation options
    menu = ["Home", "Store Resume", "Retrieve Resume"]
    choice = st.sidebar.selectbox("Select an option", menu)
    
    if choice == "Home":
        st.subheader("Welcome to ResumeVault")
        st.write("Store and retrieve your encrypted resumes securely using passkeys.")
        st.write("How to use:")
        st.write("1. Store Resume: Enter your resume text and a secure passkey to encrypt and store it")
        st.write("2. Retrieve Resume: Enter your resume identifier and passkey to decrypt and view it")
        
    elif choice == "Store Resume":
        st.subheader("Store Resume Securely")
        resume_data, passkey = get_user_input()
        
        if st.button("Store Resume"):
            if resume_data and passkey:
                encrypted_data = encrypt_resume(resume_data, passkey)
                if encrypted_data:
                    save_resume(resume_data, encrypted_data)
                    st.success("Resume stored successfully!")
                    st.info(f"Your resume identifier: {encrypted_data[:20]}... (Save this for retrieval)")
                else:
                    st.error("Failed to encrypt resume. Please try again.")
            else:
                st.error("Please enter both resume and passkey.")
    
    elif choice == "Retrieve Resume":
        st.subheader("Retrieve Your Resume")
        resume_identifier = st.text_area("Enter your Resume Identifier:")
        passkey = st.text_input("Enter passkey:", type="password")
        
        if st.button("Retrieve Resume"):
            if resume_identifier and passkey:
                # Show the available resumes in debug mode
                if st.checkbox("Debug Mode"):
                    resumes = load_resumes()
                    st.write("Available resume identifiers:")
                    for i, resume in enumerate(resumes):
                        st.write(f"{i+1}. {resume.get('resume')[:20]}...")
            
            # Find the full resume data using the identifier
            full_resume_data = find_resume(resume_identifier)
            
            if full_resume_data:
                decrypted_data = decrypt_resume(full_resume_data, passkey)
                if decrypted_data:
                    st.success("Resume retrieved successfully!")
                    st.text_area("Your Resume:", value=decrypted_data, height=300)
                else:
                    st.error("Incorrect passkey. Unable to decrypt resume.")
            else:
                st.error("Resume not found. Please check your identifier.")
                st.info("Make sure you're using the correct identifier. Try using just the first part of the identifier.")
        else:
            st.error("Please enter both resume identifier and passkey.")

if __name__ == "__main__":
    main()
