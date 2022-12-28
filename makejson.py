import json
import re
import glob
### Find all the markdown files in the current directory

all_markdown_files = glob.glob('*.md')

### Remove the README.md file from the list
all_markdown_files.remove('README.md')

print(all_markdown_files)

for i in all_markdown_files:
    # Open the markdown file
    with open(i, 'r') as f:
        syllabus = f.read()

    # Split the file into lines
    lines = syllabus.split('\n')

    # Initialize the JSON object
    json_syllabus = {}

    # Initialize variables to keep track of the current section and topic
    current_section = ''
    current_topic = ''

    # Iterate through each line
    for line in lines:
        # If the line starts with '##', it's a section header
        if line.startswith('###'):
            # Extract the section name and add it to the JSON object
            section_name = line[2:].strip().replace('#', '')
            # Trim the section name to remove any leading or trailing whitespace
            section_name = section_name.strip()
            json_syllabus[section_name] = []
            current_section = section_name
        # If the line starts with '-', it's a topic
        elif line.startswith('-'):
            # Extract the topic name and add it to the current section
            topic_name = re.sub(r'^-\s*', '', line).strip().replace('#', '')
            json_syllabus[current_section].append(topic_name)

    ### Save the JSON object to a file
    filename = i.replace('.md', '.json')
      # Write files to json folder
    file = open("json/"+filename, 'w')
    file.write(json.dumps(json_syllabus))
    file.close()