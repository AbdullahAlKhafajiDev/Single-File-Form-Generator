# html-form-generator Config.json -> HTML

## About:

Note the config.json file and the picture. The json config would yield the form in the picture. Feel free to adjust the config.json to get the HTML file looking however you need it. The chances of an error are minimal, but if you encounter any, please contact [me](https://www.linkedin.com/in/abdullah-al-khafaji-2718861bb/) or submit an issue to the repo [here](https://github.com/AbdullahAlKhafajiDev/remote-ESP32-communication/issues/new).

## Future:

To make this a bit easier for non-technical users, eventually I'd love to make an application that generates the json config in an interactive way.

## Configuration Parameters

### Application-wide changes:

- `background_image_url`: Changes the background wallpaper of the application
- `title`: Changes the title of the application window.
- `target`: Changes the server and port that the application hits with the `POST` request.

### Form changes:

`form_elements` contains a list of inputs go in the form.

- `header`: Adds an `h2` HTML element header that seperates input sections of the form.

  - `header_text`: Changes the text of the header.

- `password`: Adds a required password field.

  - `input_name`: Changes the variable name that the backend can use to retrieve the password.
  - `placeholder`: Changes the placeholder text in the password field.

- `grouped_radio`: Adds a group of radio inputs.

  - `input_name`: Changes the variable name that the backend can use to retrieve the selection.
  - `radio_options`: A list of options that a user can choose from.
    - `option_label`: The text of the radio input that the user sees.
    - `option_value`: The value of input that gets passed to the backend.

- `submit`: A button that's used to submit the form.
  - `value`: The text inside the submit button.
  - `font_size`: How big the text is. Can be in units of `px` `rem` `%` and more.
  - `font_weight`: A number dictating how bold or thin text is. Normal font weight is `500` less is thinner, more is bolder. Set in multiplications of 100s, meaning: 100, 200, 300... 900.

## Config -> HTML

The following json config will be rendered into the picture.

```json
{
  "background_image_url": "https://i.pinimg.com/originals/4e/de/5a/4ede5a33c5490195b2b17466ad26d124.gif",
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
      "grouped_radio": {
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
