import speech_recognition as sr
import MySQLdb, subprocess
MIC_NAME = "Microsoft® LifeCam HD-3000: USB Audio (hw:1,0)"

HOST = "35.244.94.254"
USER = "root"
PASSWORD = "password"
DATABASE = "lms"


class VoiceSearch():
    def main(self):
        bookName = self.getBookNameToSearch()

        if(bookName is None):
            print("Failed to get book name.")
            return

        print()
        print("Looking for book with title '{}'...".format(bookName))
        print()

        rows = self.searchBook(bookName)
        if(rows):
            print("Found:", rows)
            return rows
        else:
            print("No results found.")
            return None

    def getBookNameToSearch(self):
        # To test searching without the microphone uncomment this line of code
        # return input("Enter the Book name to search for: ")

        # Set the device ID of the mic that we specifically want
        # to use to avoid ambiguity
        for i, microphone_name in enumerate(
           sr.Microphone.list_microphone_names()):
            if(microphone_name == MIC_NAME):
                device_id = i
                break

        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone(device_index=device_id) as source:
            # clear console of errors
            subprocess.run("clear")

            # wait for a second to let the recognizer adjust the
            # energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source)

            print("Say the Book name to search for.")
            try:
                audio = r.listen(source, timeout=1.5)
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
                audio)
            return bookName
        except(sr.UnknownValueError, sr.RequestError):
            pass
        finally:
            return bookName

    def searchBook(self, bookName):
        connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)

        with connection.cursor() as cursor:
            cursor.execute(
                "select * from Book where title = %s", (bookName,))
            rows = cursor.fetchall()

        connection.close()
        return rows
       
