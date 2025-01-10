# Algorithm Visualizer and File Compression Tool

This project contains two main components: an Algorithm Visualizer and a File Compression Tool. Both components are implemented using Streamlit for the user interface.

## Algorithm Visualizer

The Algorithm Visualizer allows users to visualize various sorting algorithms interactively. The supported algorithms are:
- Bubble Sort
- Selection Sort
- Insertion Sort

### Features
- Visualize sorting algorithms step-by-step.
- Adjust the array size and speed of visualization.
- Generate new random arrays for sorting.

### Usage
1. Run the `Algorithm_Visualizer.py` script:
 
    ```sh
    streamlit run Algorithm_Visualizer.py
    ```
3. Use the sidebar to configure the array size, speed, and sorting algorithm.
4. Click "Generate New Array" to create a new random array.
5. Click "Start Visualization" to begin the sorting visualization.

## File Compression Tool

The File Compression Tool allows users to compress and decompress files using Huffman Encoding.

### Features
- Compress text files using Huffman Encoding.
- Decompress files that were compressed using the tool.
- Download the compressed and decompressed files.

### Usage
1. Run the `file_compression.py` script:
 
    ```sh
    streamlit run file_compression.py
    ```
3. Choose an operation: "Compress File" or "Decompress File".
4. Upload the file to compress or decompress.
5. Download the resulting file.

## Requirements

- Python 3.11
- Streamlit
- Matplotlib
- NumPy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/O-Aditya/DSA_Project
    ```
2. Navigate to the project directory:
 
    ```sh
    cd <project-directory>
    ```
4. Create a virtual environment:
 
    ```sh
    python -m venv venv
    ```
6. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
7. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## License

This project is licensed under the MIT License.
