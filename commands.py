import datetime
import platform
import subprocess
import webbrowser
import wikipedia


def get_current_time() -> str:
    now = datetime.datetime.now().strftime('%I:%M %p')
    return f'The current time is {now}.'


def get_current_date() -> str:
    today = datetime.datetime.now().strftime('%A, %B %d, %Y')
    return f'Today is {today}.'


def open_application(command: str) -> str:
    system = platform.system()
    app_map = {
        'notepad': {'Windows': ['notepad.exe']},
        'calculator': {'Windows': ['calc.exe']},
    }
    for app_name, os_cmds in app_map.items():
        if app_name in command:
            cmd = os_cmds.get(system)
            if not cmd:
                return f'Opening {app_name} is not configured for {system}.'
            try:
                subprocess.Popen(cmd)
                return f'Opening {app_name}.'
            except Exception as e:
                return f'Failed to open {app_name}: {e}'
    return 'Try saying open notepad or open calculator.'


def search_web(command: str) -> str:
    query = (
        command.replace('search for', '')
        .replace('search', '')
        .replace('google', '')
        .strip()
    )
    if not query:
        return 'What would you like me to search for?'
    url = f'https://www.google.com/search?q={query.replace(" ", "+")}'
    webbrowser.open(url)
    return f'Searching Google for {query}.'


def search_wikipedia(command: str) -> str:
    topic = (
        command.replace('who is', '')
        .replace('what is', '')
        .replace('wikipedia', '')
        .strip()
    )
    if not topic:
        return 'Please tell me what topic to look up.'
    try:
        return wikipedia.summary(topic, sentences=2, auto_suggest=False)
    except Exception:
        return f'Could not find a clear Wikipedia summary for {topic}.'


def open_website(command: str):
    sites = {
        'youtube': 'https://www.youtube.com',
        'github': 'https://github.com',
        'linkedin': 'https://www.linkedin.com',
        'google': 'https://www.google.com',
    }
    for name, url in sites.items():
        if name in command:
            webbrowser.open(url)
            return f'Opening {name.capitalize()}.'
    return None


def route_command(command: str):
    cmd = command.lower().strip()
    if any(w in cmd for w in ['exit', 'quit', 'stop', 'goodbye', 'bye']):
        return 'Goodbye! Shutting down.', False
    if any(w in cmd for w in ['hello', 'hi', 'hey']):
        return 'Hello! How can I help you?', True
    if 'time' in cmd:
        return get_current_time(), True
    if 'date' in cmd or 'day' in cmd:
        return get_current_date(), True
    if cmd.startswith('open '):
        site = open_website(cmd)
        return (site, True) if site else (open_application(cmd), True)
    if any(w in cmd for w in ['search', 'google']):
        return search_web(cmd), True
    if any(w in cmd for w in ['who is', 'what is', 'wikipedia']):
        return search_wikipedia(cmd), True
    return 'Sorry, I did not understand that command.', True
