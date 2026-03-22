def score_match(selected, role_skills):
    return len(set(selected) & set(role_skills)) / len(role_skills) * 100


def advanced_suggest(skills, coding, dsa, english, communication):

    CAREER_MAP = {
        "Machine Learning Engineer": ["python", "sql", "machine learning", "deep learning"],
        "Data Scientist": ["python", "sql", "statistics", "pandas"],
        "Backend Developer": ["python", "java", "sql", "docker"],
        "Frontend Developer": ["javascript", "react", "html", "css"],
        "Full Stack Developer": ["python", "javascript", "react", "sql"],
        "DevOps Engineer": ["docker", "aws", "linux"],
        "Cybersecurity Analyst": ["linux", "networking", "security"]
    }

    results = {}
    best_role = None
    best_score = 0

    for role, req_skills in CAREER_MAP.items():

        skill_score = score_match(skills, req_skills)

        coding_fit = (coding / 10) * 100
        dsa_fit = (dsa / 10) * 100
        communication_fit = ((english + communication) / 2) * 10

        final_score = (
            skill_score * 0.5 +
            coding_fit * 0.2 +
            dsa_fit * 0.2 +
            communication_fit * 0.1
        )

        results[role] = {
            "skill_score": round(skill_score, 2),
            "coding_fit": round(coding_fit, 2),
            "dsa_fit": round(dsa_fit, 2),
            "communication_fit": round(communication_fit, 2),
            "final_score": round(final_score, 2)
        }

        if final_score > best_score:
            best_score = final_score
            best_role = role

    explanation = f"""
Based on your profile:

- Strongest match: {best_role}
- Decision is based on:
  • Skill alignment
  • Coding ability
  • DSA strength
  • Communication skills

To improve:
- Increase missing skills in weak categories
- Focus on DSA for backend roles
- Focus on JS + UI for frontend roles
"""

    return {
        "best_role": best_role,
        "all_roles": results,
        "explanation": explanation
    }