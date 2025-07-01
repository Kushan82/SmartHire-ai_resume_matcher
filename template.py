import os

folders = [
    "data/resumes",
    "data/job_descriptions",
    "notebooks",
    "src",
    "app",
    "config"
]

files = {
    "notebooks/01_eda_and_model.ipynb": "",
    "src/data_loader.py": "",
    "src/preprocessing.py": "",
    "src/feature_engineering.py": "",
    "src/matcher.py": "",
    "src/utils.py": "",
    "app/streamlit_app.py": "",
    "config/config.yaml": "",
    "requirements.txt": ""
}

def create_folders():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"✅ Created folder: {folder}")

def create_files():
    for file_path, content in files.items():
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(content)
            print(f"✅ Created file: {file_path}")
        else:
            print(f"⚠️ Skipped existing file: {file_path}")

if __name__ == "__main__":
    print("📁 Creating folders and files inside current directory...")
    create_folders()
    create_files()
    print("\n🎉 Project structure ready!")
