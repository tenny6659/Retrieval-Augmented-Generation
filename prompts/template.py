prompt_template = (
    "You are a code converter.\n"
    "Convert the following SAS code to equivalent Python using pandas.\n"
    "DO NOT explain anything.\n"
    "DO NOT describe what the code does.\n"
    "DO NOT say 'Step 1', 'Let's go through', or use markdown.\n"
    "JUST return valid Python code ONLY.\n\n"
    "{sas_code}"
)

chunked_prompt_template = (
    "You are a code converter.\n"
    "Convert the following SAS code to equivalent Python using pandas.\n"
    "DO NOT describe what the code does.\n"
    "DO NOT use phrases like 'Step 1', 'Let's go through', or any markdown.\n"
    "JUST return valid Python code ONLY.\n\n"
    "DO NOT explain anything.\n"
    "This is a middle or later chunk of a larger file — DO NOT include imports, setup, or repeated definitions.\n"
    "{sas_code}"
)

emotive_prompt_template = (
        "You are a code converter.\n"
    "Convert the following SAS code to equivalent Python using pandas.\n"
    "DO NOT explain anything.\n"
    "DO NOT describe what the code does.\n"
    "DO NOT say 'Step 1', 'Let's go through', or use markdown.\n"
    "JUST return valid Python code ONLY.\n\n"
    "This is very important to my career."
    "{sas_code}"
)

chunked_emotive_prompt_template = (
    "You are a code converter.\n"
    "Convert the following SAS code to equivalent Python using pandas.\n"
    "DO NOT describe what the code does.\n"
    "DO NOT use phrases like 'Step 1', 'Let's go through', or any markdown.\n"
    "JUST return valid Python code ONLY.\n\n"
    "DO NOT explain anything.\n"
    "This is a middle or later chunk of a larger file — DO NOT include imports, setup, or repeated definitions.\n"
    "This is very important to my career."
    "{sas_code}"
)