import streamlit as st

class StreamlitApp:
    def __init__(self):
        """
        Initialize the Streamlit app.
        """
        
        if "input_file" not in st.session_state:
            st.session_state.input_file = None
        if "file_content" not in st.session_state:
            st.session_state.file_content = ""
        if "words" not in st.session_state:
            st.session_state.words = 0
        if "lines" not in st.session_state:
            st.session_state.lines = 0
        if "chars" not in st.session_state:
            st.session_state.chars = 0

    def upload(self):
        """
        Upload a file to the Streamlit app.
        """
        
        uploaded = st.file_uploader("Choose a .txt file", type="txt")
        # Check if it's a new file
        if uploaded and uploaded != st.session_state.input_file:
            st.session_state.input_file = uploaded
            content = uploaded.read().decode("utf-8")
            st.session_state.file_content = content
            self.analyze(content)

    def analyze(self, content):
        """
        Analyze the content of the uploaded file.
        """

        st.session_state.words = 0
        st.session_state.lines = 0
        st.session_state.chars = 0

        lines = content.splitlines()
        st.session_state.lines = len(lines)
        for line in lines:
            words = line.strip().split()
            st.session_state.words += len(words)
            for w in words:
                st.session_state.chars += len(w)

    def results(self):
        """
        return the results of the analysis.
        """

        return (
            f"Total Lines: {st.session_state.lines}\n"
            f"Total Words: {st.session_state.words}\n"
            f"Total Characters: {st.session_state.chars}\n"
        )

    def display_result(self):
        """
        Display the result of the analysis in the Streamlit app.
        """

        st.text(self.results())

    def download_result(self):
        """
        Download the result of the analysis as a .txt file.
        """

        st.download_button(
            label="📥 Download Summary",
            data=self.results(),
            file_name="summary.txt",
        )

    def run(self):
        """
        Run the Streamlit app.
        """

        st.title("✨ Text File Analyzer")

        self.upload()

        if st.session_state.file_content:
            st.subheader("File Content")
            st.text_area("File Text", st.session_state.file_content,height=200)

            st.subheader("Results")
            self.display_result()

            self.download_result()



app = StreamlitApp()
app.run()
