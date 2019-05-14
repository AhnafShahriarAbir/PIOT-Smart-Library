import speech_recognition as sr
import MySQLdb, subprocess

HOST = "35.244.94.254"
USER = "root"
PASSWORD = "password"
DATABASE = "lms"

MIC_NAME = "Microsoft® LifeCam HD-3000: USB Audio (hw:1,0)"


def main():
    bookName = getBookNameToSearch()

    if(bookName is None):
        print("Failed to get book name.")
        return

    print()
    print("Looking for book with title '{}'...".format(bookName))
    print()

    rows = searchBookName(bookName)
    if(rows):
        print("Found:", rows)
    else:
        print("No results found.")


def getBookNameToSearch():
    # To test searching without the microphone uncomment this line of code
    # return input("Enter the Book name to search for: ")

    # Set the device ID of the mic that we specifically want
    # to use to avoid ambiguity
    for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
        if(microphone_name == MIC_NAME):
            device_id = i
            break

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone(device_index = device_id) as source:
        # clear console of errors
        subprocess.run("clear")

        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)

        print("Say the first name to search for.")
        try:
            audio = r.listen(source, timeout = 1.5)
        except sr.WaitTimeoutError:
            return None

    # recognize speech using Google Speech Recognition
    bookName = None
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google
        # (audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        bookName = r.recognize_google(
            audio, key="AIzaSyBUpWsKw8mv8IRC60VUyfsntXUXffHcNEA")
        print("Google Speech Recognition thinks you said '{}'".format(bookName))
    except(sr.UnknownValueError, sr.RequestError):
        pass
    finally:
        return bookName


def searchBookName(bookName):
    connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)
    title = bookName
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Book WHERE Title = %s", (bookName,))
        rows = cursor.fetchall()

    connection.close()

    return rows

# Execute program.
if __name__ == "__main__":
    main()
