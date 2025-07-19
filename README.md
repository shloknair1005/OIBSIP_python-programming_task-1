# OIBSIP_python-programming_task-1

🗣️ Max Jr. - Python Voice Assistant
Max Jr. is a simple voice-activated assistant built using Python. It listens to voice commands, responds with speech, and can perform basic tasks like telling the time, date, opening websites, and greeting the user.

🧠 Features
Listens to voice commands using your microphone

Responds back with speech using text-to-speech

Tells the current date and time

Opens Google or YouTube in your web browser

Introduces itself when asked

Can exit the program when you say exit, quit, or bye

🛠️ Requirements
To run this project, you’ll need:

Python installed on your system

A working microphone

Python libraries like SpeechRecognition, pyttsx3, and vosk

A pre-trained Vosk speech recognition model

Note: Vosk needs a separate offline model to transcribe audio. The model must be downloaded from the Vosk website and integrated into the project.

🚀 How to Use
Connect your microphone

Start the program from your terminal or editor

Speak commands like:

"Hello"

"What’s the time?"

"What’s today’s date?"

"Open Google"

"Open YouTube"

"What’s your name?"

"Exit" or "Quit" or "Bye" to stop the assistant

🧠 Future Improvements
Add weather updates

Integrate with ChatGPT or other AI for smart conversations

Add a simple GUI to display logs

Enable voice-based user authentication

⚠️ Notes
The recognize_vosk method used in the code is not part of the default SpeechRecognition library. To use Vosk, it needs to be set up and handled separately. If you'd rather use an internet-based option, switching to Google’s recognizer is an alternative.

👨‍💻 Author
Shlok Nair
Aspiring Machine Learning Engineer | Python Enthusiast | Tech Explorer
