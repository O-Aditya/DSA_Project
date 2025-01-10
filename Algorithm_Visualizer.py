import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# Bubble Sort Algorithm
def bubble_sort(data, speed, plot_area):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            draw_plot(data, [j, j + 1], plot_area)
            time.sleep(speed)
    draw_plot(data, [], plot_area)  # Final sorted state

# Selection Sort Algorithm
def selection_sort(data, speed, plot_area):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
            draw_plot(data, [i, j, min_idx], plot_area)
            time.sleep(speed)
        data[i], data[min_idx] = data[min_idx], data[i]
    draw_plot(data, [], plot_area)  # Final sorted state

# Insertion Sort Algorithm
def insertion_sort(data, speed, plot_area):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            draw_plot(data, [j, j + 1], plot_area)
            time.sleep(speed)
            j -= 1
        data[j + 1] = key
        draw_plot(data, [], plot_area)
    draw_plot(data, [], plot_area)  # Final sorted state

# Function to draw the bar plot
def draw_plot(data, highlights, plot_area):
    plt.clf()  # Clear the current figure
    colors = ['blue' if x not in highlights else 'red' for x in range(len(data))]
    plt.bar(range(len(data)), data, color=colors)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Sorting Algorithm Visualization")

    # Display values on top of each bar
    for i, value in enumerate(data):
        plt.text(i, value + 1, str(value), ha='center', va='bottom', fontsize=8)

    plot_area.pyplot(plt)  # Update the Streamlit plot area

# Streamlit UI
st.title("Algorithm Visualizer")
st.write("Visualize various sorting algorithms interactively.")

# Sidebar
st.sidebar.header("Configuration")
array_size = st.sidebar.slider("Array Size", 10, 100, 20)
speed = st.sidebar.slider("Speed (Seconds per Step)", 0.01, 1.0, 0.1)
algorithm = st.sidebar.selectbox("Select Algorithm", ["Bubble Sort", "Selection Sort", "Insertion Sort"])

# Generate array
if st.sidebar.button("Generate New Array"):
    data = list(np.random.randint(10, 100, size=array_size))
    st.session_state["data"] = data

# Load array into session state if not already loaded
if "data" not in st.session_state:
    st.session_state["data"] = list(np.random.randint(10, 100, size=array_size))

data = st.session_state["data"]

# Show the array
st.write("Generated Array:", data)

# Create a placeholder for the plot
plot_area = st.empty()

# Start visualization
if st.button("Start Visualization"):
    if algorithm == "Bubble Sort":
        bubble_sort(data, speed, plot_area)
    elif algorithm == "Selection Sort":
        selection_sort(data, speed, plot_area)
    elif algorithm == "Insertion Sort":
        insertion_sort(data, speed, plot_area)

# Initial plot
draw_plot(data, [], plot_area)
