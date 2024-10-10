# html-generator Config.json -> HTML

## About:

Note the config.json file and the picture. The json config would yield the form in the picture. Feel free to adjust  
the config.json to get the HTML file looking however you need it. The chances of an error are minimal, but if you encounter any, please contact [me](https://www.linkedin.com/in/abdullah-al-khafaji-2718861bb/) or submit an issue to the repo [here](https://github.com/AbdullahAlKhafajiDev/remote-ESP32-communication/issues/new).

## Future:

To make this a bit easier for non-technical users, eventually I'd love to make an application that generates the json config in an interactive way.

## Config -> HTML

The following json config will be rendered into the picture.

```json
{
  "background_image_url": "https://i.pinimg.com/originals/4e/de/5a/4ede5a33c5490195b2b17466ad26d124.gif",
  "title": "Abdullah's Remote Power\n Management Server",
  "target": "http://127.0.0.1:5000/",
  "input_fields": [
    {
      "password": {
        "input_label": "Password:",
        "input_name": "password",
        "placeholder": "password"
      }
    },
    {
      "radio": {
        "input_label": "Options:",
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
