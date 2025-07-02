from openai import OpenAI
 
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)
def get_resume_feedback(resume_text, job_description):
    prompt = f"""
You are an expert resume reviewer. Your task is to provide feedback on a resume based on a job description.
    Resume:
{resume_text}
    Job Description:
{job_description}
    Provide a detailed analysis of how well the resume matches the job description, including strengths and areas for improvement."""    
    
    response = client.chat.completions.create(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content.strip()