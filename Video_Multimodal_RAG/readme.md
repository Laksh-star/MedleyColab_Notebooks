# Video Multimodal Retrieval-Augmented Generation (RAG)

This project demonstrates how to process YouTube videos, extract keyframes and audio, transcribe the audio, and implement a multimodal Retrieval-Augmented Generation (RAG) pipeline using **LangChain** and **Anthropic's Claude** model. The notebook shows how to process videos from YouTube and answer questions related to them using both textual and visual context.

## Features

- **Download YouTube Videos**: Download videos directly from YouTube.
- **Frame Extraction**: Extract frames from videos at specified intervals.
- **Audio Transcription**: Use **Whisper** to transcribe audio into text.
- **Vector Embedding**: Create vector embeddings for frames and their corresponding transcriptions using **OpenAI Embeddings**.
- **Multimodal Retrieval**: Use vector similarity to retrieve the most relevant frames and their transcriptions based on a query.
- **Language Model Integration**: Use **Anthropic’s Claude** to answer questions using the retrieved visual and textual context.

## Prerequisites

Before running this notebook, ensure you have the following installed:

1. **Python 3.7+**
2. Install necessary libraries:
   ```bash
   pip install pytubefix
   pip install whisper
   pip install moviepy
   pip install lancedb
   pip install langchain-openai
   pip install anthropic
   pip install tqdm
   pip install opencv-python
   ```

3. API keys for the following:
   - **OpenAI API** for generating embeddings.
   - **Anthropic API** for the language model used in the multimodal pipeline.

## How It Works

1. **Video Processing**: The video is downloaded from YouTube, frames are extracted at the specified intervals, and the audio is transcribed using **OpenAI's Whisper**.
   
2. **Embedding Creation**: Each frame, along with its corresponding transcription, is embedded using **OpenAI’s Embedding API** and stored in a vector database using **LanceDB**.

3. **Multimodal Retrieval**: When a question is asked, the top relevant frames and their transcriptions are retrieved using vector similarity search.

4. **Question Answering**: Using **Anthropic’s Claude** model, the retrieved context (both visual and textual) is used to answer the question posed by the user.

## Project Structure

- `VideoProcessor`: Handles downloading, frame extraction, audio extraction, and transcription.
- `VectorStore`: Manages the vector embeddings for frames and their corresponding transcriptions.
- `MultimodalRAGPipeline`: A pipeline that combines retrieval and the language model to generate answers.
- `LVLMInference`: Handles interaction with **Anthropic’s Claude** language model.
- `MultimodalRAGSystem`: Combines all components into a cohesive system that processes videos and answers questions.

## How to Use

1. Clone this repository or download the Jupyter notebook.
   ```bash
   git clone https://github.com/Laksh-star/MedleyColab_Notebooks
   ```

2. Open the notebook in **Jupyter** or **Google Colab**.

3. Set your API keys in the notebook:
   ```python
   OPENAI_API_KEY = 'your-openai-api-key'
   ANTHROPIC_API_KEY = 'your-anthropic-api-key'
   ```

4. Run the notebook step by step:
   - Enter the YouTube URL for the video you want to process.
   - Ask questions related to the video, and the system will return both textual answers and keyframes relevant to your query.

## Example

### Step 1: Enter YouTube URL
```python
Enter YouTube URL (or type 'quit' to exit): https://www.youtube.com/watch?v=example_video_id
```

### Step 2: Ask Questions
```python
Ask a question about the video (or type 'quit' to exit): What is happening in the middle of the video?
```

### Output:
- **Textual Answer**: Based on the context and the frames, the system answers your query.
- **Relevant Frames**: Displays the relevant frames that correspond to the answer.

## Progress Tracking

- Progress bars are displayed during:
  - **Video downloading**
  - **Frame extraction**
  - **Audio transcription**

These progress bars keep you informed of the current processing step.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Laksh-star/MedleyColab_Notebooks/issues).

## Acknowledgments

Special thanks to **OpenAI** for providing powerful tools like **Whisper** and **Embeddings API**, and to **Anthropic** for their robust language models like **Claude**.

---

**Happy Coding!**

3. Push the updated repository to GitHub.

This README provides clear guidance on how to use the notebook and explains the functionality of your system. Let me know if you'd like any further changes!
