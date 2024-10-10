import json
from pathlib import Path
from os import listdir, path

# Takes in a file path, and returns THE text 
# content without newline characters.
def loadFile(file_path):
    text_file_with_newline = Path(file_path).read_text()
    text_file = text_file_with_newline.replace("\n", "")
    return text_file

# Retrieves all HTML form components, their HTML code
# and returns them as a dictionary.
# Format: html_objects["header"] = "<h2>HEADER_TEXT_CONFIG</h2>" 
def objectifyHTMLComponents():
    html_objects = {}

    html_elements = listdir(form_elements_path)
    for element in html_elements:
        element_name = element.split(".")[0]
        element_html = loadFile(f"{form_elements_path}\\{element}")

        html_objects[element_name] = element_html

    return html_objects

def getKey(dictionary):
    keys = list(dictionary.keys())
    if (len(keys) == 1):
        return keys[0]
    else:
        print("Misuse of function getKeys()\n\t Dictionary:\n", dictionary)
    


# Current Python file location within the system.
current_location = path.dirname(path.realpath(__file__))
# config.json path.
json_config_path = f"{current_location}\\config.json"
# Base HTML template.
base_template_path = f"{current_location}\\template.html"
# HTML components.
form_elements_path = f"{current_location}\\form_elements\\"

# Gets all HTML form elements.
html_components_object = objectifyHTMLComponents()

# Loads JSON file.
config_json = json.loads(loadFile(json_config_path))

html_template = loadFile(base_template_path)

for template_attribute in config_json:
    if (type(config_json[template_attribute]) != list):
        # if the config content is not a list
        # replace TEMPLATE_ATTRIBUTE_CONFIG with the content
        # of the json config.
        html_template = html_template.replace(f"{template_attribute.upper()}_CONFIG", f"{config_json[template_attribute]}")

    elif (type(config_json[template_attribute]) == list and template_attribute == "form_elements"):
        # Builds the body of the form.
        form_elements = ""

        for form_element_object in config_json[template_attribute]:

            html_component_name = getKey(form_element_object) # Example: header, password
            if (html_component_name.split("_")[0] != "grouped"): 
                html_component_body = html_components_object[html_component_name] # Actual html code.

                for attribute_name, attribute_value in form_element_object[html_component_name].items():
                    html_component_body = html_component_body.replace(f"{attribute_name.upper()}_CONFIG", f"{attribute_value}")
                
                # After all the _CONFIG attributes are replaced,
                # we add the HTML code to the form.
                form_elements += html_component_body
            
            else:
                multi_element_attribs = {} # group of components that share attributes.
                for attribute_name, attribute_value in form_element_object[html_component_name].items():
                    multi_elements_html = ""
                    if (type(attribute_value) != list):
                        multi_element_attribs[attribute_name] = attribute_value
                    else: # item is a list, meaning this is where the 
                          # the component gets parsed and added
                          # for a multi element component.
                        for sub_element in attribute_value:
                            html_component_body = html_components_object[html_component_name.split("_")[1]]
                            # adds the multi-elements attributes 
                            for multi_element_attribute in multi_element_attribs:
                                html_component_body = html_component_body.replace(f"{multi_element_attribute.upper()}_CONFIG", f"{multi_element_attribs[multi_element_attribute]}")
                            # adds specific element attribute
                            for sub_element_attribute_name, sub_element_attribute_value in sub_element.items():
                                html_component_body = html_component_body.replace(f"{sub_element_attribute_name.upper()}_CONFIG", f"{sub_element_attribute_value}")
                            
                            multi_elements_html += html_component_body
                
                form_elements += multi_elements_html
    
        # Places the form elements in the HTML file.
        html_template = html_template.replace(f"{template_attribute.upper()}_CONFIG", f"{form_elements}")



# Actually makes the file.
with open("test.html", "w+") as file:
    file.write(html_template)
