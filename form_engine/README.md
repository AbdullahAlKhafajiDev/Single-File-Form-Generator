# Form-Engine Config.json -> HTML

## About:

Note the config.json file and the picture. The json config would yield the form in the picture. Feel free to adjust the config.json to get the HTML file looking however you need it. The chances of an error are minimal, but if you encounter any, please contact [me](https://www.linkedin.com/in/abdullah-al-khafaji-2718861bb/) or submit an issue to the repo [here](https://github.com/AbdullahAlKhafajiDev/remote-ESP32-communication/issues/new).

## Future:

To make this a bit easier for non-technical users, eventually I'd love to make an application that generates the json config in an interactive way.

## Configuration Parameters

### Application-wide changes:

**`background_image_url`**: Changes the background wallpaper of the application.  
**`title`**: Changes the title of the application window.  
**`target`**: Changes the server and port that the application hits with the `POST` request.

### Form changes:

**`form_elements`**: contains a list of inputs go in the form.

- **`header`**: Adds an `h2` HTML element header that seperates input sections of the form.

  - **`header_text`**: Changes the text of the header.

- **`password`**: Adds a required password field.

  - **`input_name`**: Changes the variable name that the backend can use to retrieve the password.
  - **`placeholder`**: Changes the placeholder text in the password field.

- **`grouped_radioMaster`**: Adds a wrapper with a group of radio inputs.

  - **`input_name`**: Changes the variable name that the backend can use to retrieve the selection.
  - **`radio_options`**: A list of options that a user can choose from.
    - **`option_label`**: The text of the radio input that the user sees.
    - **`option_value`**: The value of input that gets passed to the backend.

- **`grouped_selectMaster`**: Adds a select wrapper with a group of options.

  - **`input_name`**: Changes the variable name that the backend can use to retrieve the selection.
  - **`select_options`**: A list of options that a user can select from.
    - **`option_label`**: The text of the option input that the user sees.
    - **`option_value`**: The value of input that gets passed to the backend.

- **`submit`**: A button that's used to submit the form.
  - **`value`**: The text inside the submit button.
  - **`font_size`**: How big the text is. Can be in units of `px` `rem` `%` and more.
  - **`font_weight`**: A number dictating how bold or thin text is. Normal font weight is `500` less is thinner, more is bolder. Set in multiplications of 100s, meaning: `100`, `200`, `300`... `900`.

## Config -> HTML

The following json config will be rendered into the following picture.

```json
{
  "background_image_urls": [
    "https://giffiles.alphacoders.com/214/214384.gif",
    "https://i.pinimg.com/originals/4e/de/5a/4ede5a33c5490195b2b17466ad26d124.gif",
    "https://i.redd.it/bpxxqqvps4h91.gif",
    "https://i.redd.it/0k6meqvps4h91.gif",
    "https://i.redd.it/uwwte8wps4h91.gif"
  ],

  "title": "Abdullah's Power \nManagement Server",
  "target": "http://127.0.0.1:5000/",

  "form_elements": [
    {
      "header": {
        "header_text": "Password:"
      }
    },
    {
      "password": {
        "input_name": "password",
        "placeholder": "password"
      }
    },
    {
      "header": {
        "header_text": "Options:"
      }
    },
    {
      "grouped_radioMaster": {
        "input_name": "mode",
        "radio_options": [
          {
            "option_label": "Turn On",
            "option_value": "on"
          },
          {
            "option_label": "Turn Off",
            "option_value": "off"
          }
        ]
      }
    },
    {
      "submit": {
        "value": "☣",
        "font_size": "2rem",
        "font_weight": 600
      }
    }
  ]
}
```

<p align="center">
  <img src="https://github.com/AbdullahAlKhafajiDev/remote-ESP32-communication/blob/main/appImage.png?raw=true" />
</p>

## Under the hood

Under the hood, **Form-Engine** uses some fancy logic that will replace the code in the HTML template with the desired result in the config.json file.

Any value in the template or the form_elements that ends in **`_CONFIG`** is a target for substitution.

For non-form elements, the **Form-Engine** will look at the config name, for example: **`background_image_urls`**, will turn it into upper case and add **`_CONFIG`** at the end of it. The result will be `BACKGROUND_IMAGE_URLS_CONFIG`. After this, the **Form-Engine** will search the template for **`BACKGROUND_IMAGE_URLS_CONFIG`** and replace it with the value of it in the json config file.

For form elements, the **Form-Engine** check if it's an element that needs dynamically generated children (multi-dimensional element) or not (one-dimensional element).

- For single dimensional elements: The engine will replace the attributes of those elements with the values in the config.
- For multi-dimensional elements:
  - The engine will create a hash map of all the attributes that the parent or children will share.
  - The engine will dynamically create the children based on the number of items in the **`<element>_options`** array.
  - The engine will set the attributes of those children based on the values in the `config.json` file.
  - The engine will then check the hash map of all the values that should be shared amongst children or parent, and set them according to the config.

After the processing, the engine will insert the HTML code of the form_elements into the form.
