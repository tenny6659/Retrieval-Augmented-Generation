prompt_template = (
    "You are a code converter.\n"
    "Convert the following SAS code to equivalent Python using pandas.\n"
    "DO NOT explain anything.\n"
    "DO NOT describe what the code does.\n"
    "DO NOT say 'Step 1', 'Let's go through', or use markdown.\n"
    "JUST return valid Python code ONLY.\n\n"
    "{sas_code}"
)
