
SKILLS = {
    "run_tests": {
        "local": "pytest tests/",
        "breeze": "./breeze testing pytest tests/"
    },
    "static_checks": {
        "local": "pre-commit run --all-files",
        "breeze": "./breeze static-checks"
    }
}


def run_skill(skill_name, context):
    if skill_name not in SKILLS:
        return "Skill not found"
    
    if context not in SKILLS[skill_name]:  # error
        return "Invalid context"

    return SKILLS[skill_name][context]