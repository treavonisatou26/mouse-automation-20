# Mouse Automation 2.0

Mouse Automation 2.0 is a powerful Python-based autoclicker designed to automate repetitive clicking tasks efficiently and effortlessly. This project aims to enhance productivity by allowing users to set customized click intervals and patterns to suit their needs.

## Features
- **Custom Click Intervals**: Set specific time delays between clicks, ranging from milliseconds to seconds.
- **Pattern Recording**: Record a sequence of clicks and automatically replay them with precision.
- **Hotkey Activation**: Easily start and stop the clicking process using customizable keyboard shortcuts.
- **User-Friendly Interface**: Intuitive command-line interface for straightforward navigation and control.

## Installation

To get started with Mouse Automation 2.0, ensure you have Python 3.6 or higher installed. You can install the necessary dependencies using pip. In your terminal, run the following commands:

```bash
git clone https://github.com/Developer/mouse-automation-20.git
cd mouse-automation-20
pip install -r requirements.txt
```

## Basic Usage Example

After installation, you can run the autoclicker directly from the command line. Here's a simple command to start clicking with a 500ms interval:

```bash
python autoclicker.py --interval 500
```

Press the defined hotkey (default is F8) to start and stop the clicking process. To record a custom clicking pattern, use the following command:

```bash
python autoclicker.py --record
```

Once recorded, you can replay it by simply running the script without any parameters:

```bash
python autoclicker.py
```

Feel free to explore the repository for more advanced configurations and options.

## License
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.