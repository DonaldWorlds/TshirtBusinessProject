Here's a sample `README.md` file for your Pinterest bot project. You can customize it further to suit your preferences or add any additional details you find necessary.

```markdown
# Pinterest Bot

A Python-based automation tool for interacting with Pinterest, allowing users to upload pins from a CSV file while employing proxy rotation and user-agent handling to simulate human-like behavior.

## Features

- **Automated Pin Upload**: Upload multiple pins from a CSV file to specified Pinterest boards.
- **Proxy Rotation**: Utilize ZenRows to rotate proxies for making requests, ensuring stability and preventing IP bans.
- **User-Agent Rotation**: Randomly select user-agent strings to simulate different browser environments.
- **Environment Variable Management**: Load sensitive information such as API keys, email, and passwords from a `.env` file.

## Requirements

- Python 3.6+
- `python-dotenv` for loading environment variables
- `py3pin` for interacting with the Pinterest API
- `zenrows` for proxy handling
- `requests` for making HTTP requests

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/pinterest-bot.git
   cd pinterest-bot
   ```

2. **Install required packages**:

   ```bash
   pip install python-dotenv py3pin zenrows requests
   ```

3. **Set up your environment variables**: Create a `.env` file in the root directory of the project with the following format:

   ```plaintext
   EMAIL=your_pinterest_email
   PASSWORD=your_pinterest_password
   USERNAME=your_pinterest_username
   CRED_ROOT=path_to_your_credentials_root
   ZENROWS_API_KEY=your_zenrows_api_key
   ```

4. **Prepare your CSV file**: Create a CSV file named `pins.csv` with the following columns:
   - `board_id`: The ID of the board to which the pin will be uploaded.
   - `image_path`: The filename of the image (stored in the `images` directory).
   - `description`: A description of the pin.
   - `title`: The title of the pin.
   - `link`: A link associated with the pin.

   Example `pins.csv` row:
   ```csv
   board_id,image_path,description,title,link
   939774715932751037,BrooklynUnitedStatesLiberty.png,HELLO EVERY ONE THIS IS MY FIRST PIN,Looking over the city,https://threadedretros.etsy.com
   ```

5. **Add your images**: Place your images in the `images` directory.

## Usage

1. Run the bot using the following command:

   ```bash
   python main.py
   ```

   This will log in to Pinterest and start uploading pins from the specified CSV file, using proxy rotation and random user-agent handling.

## Code Structure

- `main.py`: The main entry point of the application that initializes the PinterestBot and starts the upload process.
- `pinterest_bot.py`: Contains the `PinterestBot` class that handles Pinterest interactions.
- `proxy_handler.py`: Manages proxy requests using ZenRows.
- `user_agent_handler.py`: Provides a method for retrieving random user-agent strings.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Any contributions or suggestions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Notes

- Replace `https://github.com/yourusername/pinterest-bot.git` with the actual URL of your GitHub repository.
- Make sure the file structure, especially the location of the CSV and images, is clearly defined to help users understand how to set up the project correctly.
- Adjust any section to better reflect your project specifics or additional features that may be included.
