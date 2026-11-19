import pyttsx3
import speech_recognition as sr
from commands import route_command


class PersonalVoiceAssistant:
    def __init__(self):
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 175)
        self.tts_engine.setProperty('volume', 1.0)
        self.recognizer = sr.Recognizer()

    def speak(self, text: str) -> None:
        print(f'Assistant: {text}')
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def listen(self):
        try:
            with sr.Microphone() as source:
                print('\nListening... Speak now.')
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print('Recognizing...')
            text = self.recognizer.recognize_google(audio)
            print(f'You said: {text}')
            return text
        except sr.WaitTimeoutError:
            print('Timed out waiting for speech.')
            return None
        except sr.UnknownValueError:
            self.speak('Sorry, I could not understand what you said.')
            return None
        except sr.RequestError:
            self.speak('Speech service unavailable. Using text fallback.')
            return input('Type your command: ').strip()
        except Exception:
            print('Microphone not available. Switching to text input.')
            return input('Type your command: ').strip()

    def run(self) -> None:
        self.speak('Voice assistant ready. Say a command or say exit.')
        running = True
        while running:
            cmd = self.listen()
            if not cmd:
                continue
            reply, running = route_command(cmd)
            self.speak(reply)


if __name__ == '__main__':
    PersonalVoiceAssistant().run()
