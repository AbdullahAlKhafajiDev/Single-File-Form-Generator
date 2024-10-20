import json
from pathlib import Path
from os import listdir, path

# Takes in a file path, and returns the text 
# content without newline characters.
def loadFile(file_path):
    text_file_with_newline = Path(file_path).read_text()
    text_file = text_file_with_newline.replace("\n", "")
    return text_file

# Takes in an HTML file path, and returns 
# the HTML code as <String>.
def loadHTML(html_file_path):
    html_file = Path(html_file_path).read_text()
    return html_file

# Retrieves all HTML form components, their HTML code
# and returns them as a dictionary.
# Format: html_objects["header"] = "<h2>HEADER_TEXT_CONFIG</h2>" 
def objectifyHTMLComponents(FORM_ELEMENTS_PATH):
    html_objects = {}

    html_elements = listdir(FORM_ELEMENTS_PATH)
    for element in html_elements:
        element_html = loadHTML(f"{FORM_ELEMENTS_PATH}\\{element}")

        element_name = element.split(".")[0]
        html_objects[element_name] = element_html

    return html_objects

# Takes in a dictionary that has ONE key:value pair.
# and returns the key as <String>.
def getKey(dictionary):
    keys = list(dictionary.keys())
    if (len(keys) == 1):
        return keys[0]
    else:
        ("Misuse of function getKeys()\n\t Dictionary:\n", dictionary)
    
def handleMultiAtribElement(form_element_object, html_components_object, html_component_name):
    multi_element_attribs = {} # Group of components that share attributes.

    master_element = html_components_object[html_component_name.replace("grouped_", "")] # the wrapper element, example: <div></div>.

    for attribute_name, attribute_value in form_element_object[html_component_name].items():
        multi_elements_html = ""
        
        # attribute_value is not a list, therefore is a 
        # common attribute between all sub-instances of
        # the component.
        if (type(attribute_value) != list):
            multi_element_attribs[attribute_name] = attribute_value
        
        else: # item is a list, meaning this is where the 
                # the sub-components get parsed and added
                # to the master multi-element component.
            sub_element_name = attribute_name.replace("_options", "")

            for sub_element in attribute_value:
                html_component_body = html_components_object[sub_element_name]
                
                # adds specific element attribute
                for sub_element_attribute_name, sub_element_attribute_value in sub_element.items():
                    html_component_body = html_component_body.replace(f"{sub_element_attribute_name.upper()}_CONFIG", f"{sub_element_attribute_value}")
                
                multi_elements_html += html_component_body

    # adds the sub-elements to the master_element.
    master_element = master_element.replace(f"{attribute_name.upper()}_CONFIG", multi_elements_html)

    # adds the multi-elements attributes 
    for multi_element_attribute in multi_element_attribs:
        master_element = master_element.replace(f"{multi_element_attribute.upper()}_CONFIG", f"{multi_element_attribs[multi_element_attribute]}")

    return master_element

def handleSingleAtribElement(form_element_object, html_components_object, html_component_name):
    html_component_body = html_components_object[html_component_name] # Actual html code.

    for attribute_name, attribute_value in form_element_object[html_component_name].items():
        html_component_body = html_component_body.replace(f"{attribute_name.upper()}_CONFIG", f"{attribute_value}")
    
    # After all the _CONFIG attributes are replaced,
    # we add the HTML code to the form.
    # form_elements += html_component_body
    return html_component_body

def handleFormElements(config_json, html_components_object, html_template):
    form_elements = ""

    for form_element_object in config_json["form_elements"]:
        # form_element_object: [{"header": {<HEADER_CONFIG}}, {"password": {<PASSWORD_CONFIG}}...]

        html_component_name = getKey(form_element_object) # Example: header, password
        if (html_component_name.split("_")[0] != "grouped"): 
            form_elements += handleSingleAtribElement(form_element_object, html_components_object, html_component_name)

        else:
            form_elements += handleMultiAtribElement(form_element_object, html_components_object, html_component_name)
            
    # Places the form elements in the HTML file.
    return html_template.replace(f"{"form_elements".upper()}_CONFIG", f"{form_elements}")

def main():
    # Current Python file location within the system.
    CURRENT_LOCATION = path.dirname(path.realpath(__file__))
    # config.json path.
    JSON_CONFIG_PATH = f"{CURRENT_LOCATION}\\config.json"
    # Base HTML template.
    BASE_TEMPLATE_PATH = f"{CURRENT_LOCATION}\\template.html"
    # HTML components directory.
    FORM_ELEMENTS_PATH = f"{CURRENT_LOCATION}\\form_elements\\"

    # Gets all HTML form elements.
    html_components_object = objectifyHTMLComponents(FORM_ELEMENTS_PATH)

    # Loads JSON file.
    config_json = json.loads(loadFile(JSON_CONFIG_PATH))

    # Loads the base HTML template.
    html_template = loadHTML(BASE_TEMPLATE_PATH)

    for template_attribute in config_json:
        if (type(config_json[template_attribute]) != list):
            # if the config content is not a list replace
            # TEMPLATE_ATTRIBUTE_CONFIG in the HTML file
            # with the value of the json_config[attribute].
            html_template = html_template.replace(f"{template_attribute.upper()}_CONFIG", f"{config_json[template_attribute]}")

        # Builds the body of the form.
        elif (type(config_json[template_attribute]) == list and template_attribute == "form_elements"):
            html_template = handleFormElements(config_json, html_components_object, html_template)

    # Actually makes the file.
    with open("test.html", "w+") as file:
        file.write(html_template)

main()