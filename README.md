<h1>Personal Desktop Assistant</h1>
This is a Personal Desktop Assistant project built using Python. The assistant can perform various tasks, including voice recognition, text-to-speech responses, opening applications, searching online, performing calculations, answering queries, and more.

<h2>Features</h2>
<h3>Voice Recognition:</h3> Listens for and processes user voice commands using the speech_recognition library.
<h3>Text-to-Speech:</h3> Converts text responses to speech using pyttsx3.
<h3>Online Searches:</h3> Conducts searches online using webbrowser and fetches information from Wikipedia.
<h3>Application Control:</h3> Opens and interacts with various applications installed on your system.
<h3>Web Automation:</h3> Performs automated web tasks, including fetching content using requests and parsing HTML using BeautifulSoup.
<h3>Geolocation Services:</h3> Finds locations and calculates distances using the geopy library.
<h3>System Monitoring:</h3> Provides information on CPU and memory usage with psutil.
<h3>Jokes and Entertainment:</h3> Tells jokes using pyjokes.
<h3>Automation and Controls:</h3> Automates tasks like keystrokes with pyautogui.
<h3>Math and Computation:</h3> Solves mathematical queries using WolframAlpha's API.
<h3>Screen Capturing:</h3> Utilizes OpenCV for screen capturing and other tasks.

<h2>Prerequisites</h2>
Ensure you have Python installed on your system. The recommended version is Python 3.x.

<h2>Libraries Used</h2>
The project uses the following Python libraries. They can be installed using pip:

Copy code
`pip install SpeechRecognition pyttsx3 geopy psutil requests beautifulsoup4 wolframalpha pyautogui opencv-python pyjokes`

<h2>Installation</h2>
Clone the repository:
Copy code
`git clone https://github.com/username/personal-desktop-assistant.git`
`cd personal-desktop-assistant`
`Install the required packages:`

Copy code
`pip install -r requirements.txt`
Run the assistant:

Copy code
`python tony.py`
<h2>Usage</h2>
Listening for Commands:

The assistant starts listening for your voice commands once you run the script.
Ensure your microphone is properly connected and working.

<h2>Example Commands:</h2>

"Open Chrome" - Opens the Google Chrome browser.
"Search Wikipedia for Python" - Searches for Python on Wikipedia and reads out the summary.
"What's the weather?" - Provides weather information if the API key is correctly set.
"Tell me a joke" - Tells a random joke.
"Calculate 5 plus 3" - Provides the result of the mathematical operation.

<h2>Additional Functionalities:</h2>

Geolocation Services: Fetches location details and calculates distances.
System Information: Retrieves and displays CPU and memory usage data.
Web Automation: Automates browser tasks and web scraping.

<h2>Customization</h2>
Feel free to extend the assistant's capabilities by adding more commands and integrating new libraries or APIs. The listen() and speak() functions provide a foundation for adding new functionalities.

<h2>License</h2>
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

<h2>Contribution</h2>
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements or report bugs.
