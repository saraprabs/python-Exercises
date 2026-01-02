'''
Docstring for LAB8.pipeline6
'''
def pipeline(initial_value, *funcs):
    
    result = initial_value
    for func in funcs:
        result = func(result)
    return result
def remove_whitespace(text):
    return text.strip()
# Named function
def capitalize_text(text):
    return text.upper()
# The raw data
raw_input = "   hello functional world   "
# Running the pipeline
final_output = pipeline(
    raw_input,
    remove_whitespace,                # Named function
    capitalize_text,                  # Named function
    lambda s: s.replace(" ", "_"),    # Lambda expression
    lambda s: f"PROCESSED: {s}"       # Lambda expression
)
print(final_output)