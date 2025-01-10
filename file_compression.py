import heapq
import os
import streamlit as st
from collections import Counter, namedtuple

# Node structure for the Huffman tree
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree
def build_huffman_tree(frequencies):
    heap = [Node(char, freq, None, None) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0]

# Generate Huffman Codes
def generate_huffman_codes(tree, prefix="", code_map={}):
    if tree is None:
        return

    if tree.char is not None:
        code_map[tree.char] = prefix
    else:
        generate_huffman_codes(tree.left, prefix + "0", code_map)
        generate_huffman_codes(tree.right, prefix + "1", code_map)

    return code_map

# Compress File
def compress_file(file_content):
    frequencies = Counter(file_content)

    # Build Huffman tree
    huffman_tree = build_huffman_tree(frequencies)

    # Generate Huffman codes
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Encode content
    encoded_content = "".join(huffman_codes[char] for char in file_content)

    # Save metadata
    metadata = {
        "huffman_codes": huffman_codes,
        "original_size": len(file_content),
    }

    return encoded_content, metadata

# Decompress File
def decompress_file(encoded_content, metadata):
    huffman_codes = metadata["huffman_codes"]
    reverse_codes = {v: k for k, v in huffman_codes.items()}

    current_code = ""
    decoded_content = ""
    for bit in encoded_content:
        current_code += bit
        if current_code in reverse_codes:
            decoded_content += reverse_codes[current_code]
            current_code = ""

    return decoded_content

# Streamlit App
def main():
    st.title("File Compression Tool")
    st.write("A simple tool for compressing and decompressing files using Huffman Encoding.")

    option = st.selectbox("Choose an operation:", ["Compress File", "Decompress File"])

    if option == "Compress File":
        uploaded_file = st.file_uploader("Upload a file to compress", type=["txt"])
        if uploaded_file:
            file_content = uploaded_file.read().decode("utf-8")
            encoded_content, metadata = compress_file(file_content)

            st.subheader("Compression Successful!")
            st.write(f"Original Size: {metadata['original_size']} bytes")
            st.write(f"Compressed Size: {len(encoded_content) // 8} bytes (approx)")

            # Allow user to download the compressed file
            st.download_button(
                label="Download Compressed File",
                data=f"{metadata}\n{encoded_content}".encode("utf-8"),
                file_name="compressed.huff",
                mime="application/octet-stream",
            )

    elif option == "Decompress File":
        uploaded_file = st.file_uploader("Upload a compressed file to decompress", type=["huff"])
        if uploaded_file:
            file_content = uploaded_file.read().decode("utf-8")
            metadata_line, encoded_content = file_content.split("\n", 1)
            metadata = eval(metadata_line)

            decompressed_content = decompress_file(encoded_content, metadata)

            st.subheader("Decompression Successful!")
            st.text_area("Decompressed Content", decompressed_content, height=200)

            # Allow user to download the decompressed file
            st.download_button(
                label="Download Decompressed File",
                data=decompressed_content.encode("utf-8"),
                file_name="decompressed.txt",
                mime="text/plain",
            )

if __name__ == "__main__":
    main()
