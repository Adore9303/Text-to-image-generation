# This code creates a tkinter application with a window that includes a prompt field (CTkEntry) for user input,
# a label (CTkLabel) for displaying the generated image, and a button (CTkButton) to trigger the image generation.
# The generate function retrieves the user input, generates an image based on the input using the StableDiffusion model, 
# and displays the generated image in the label.

# Importing all the neccesary modules and libraries to execute the application
import tkinter as tk
from tkinter import font
import customtkinter as ctk
from PIL import ImageTk
import torch
from diffusers import StableDiffusionPipeline

# Your authorization token for using the StableDiffusion model via huggingface
auth_token = "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"

# Create the main application window
app = tk.Tk()
app.geometry("532x632")  # Set the window dimensions
app.title("text to image generation")  # Set the window title
ctk.set_appearance_mode("dark")  # Use dark theme for customtkinter

# Create a frame to hold the CTkEntry and other widgets
frame = tk.Frame(app)
frame.pack()  # Pack the frame to place it in the window

# Create a CTkEntry widget for text input
prompt = ctk.CTkEntry(frame, height=40, width=512, text_color="black", fg_color="white")
prompt.pack()  # Pack the CTkEntry widget

# Set the font style for the CTkEntry
font_style = ("Arial", 20)
prompt.configure(font=font_style)

# Create a CTkLabel widget for displaying the generated image
label = ctk.CTkLabel(frame, height=512, width=512)
label.pack()  # Pack the CTkLabel widget

# Define the model ID, device, and load the StableDiffusion pipeline
modelid = "CompVis/stable-diffusion-v1-4"
device = "cpu"  # You can change this to "cuda" if you have a GPU
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float32, use_auth_token=auth_token)
pipe.to(device)

# Define the function to generate the image
def generate():
    # Get the text entered in the CTkEntry widget
    input_text = prompt.get()

    # Check if the input_text is not empty
    if input_text:
        # Generate the image using the input text
        output = pipe(input_text)

        # Check if the output contains images
        if output and output.images:
            image = output.images[0]

            # Save the generated image to a file
            image.save("generated_image.png")

            # Display the image in the CTkLabel widget
            img = ImageTk.PhotoImage(image)
            label.configure(image=img)
            label.image = img  # Keep a reference to avoid garbage collection issues

# Create a CTkButton for triggering the image generation
button = ctk.CTkButton(frame, height=40, width=120, text_color="white", fg_color="blue", command=generate)
button.configure(font=font_style)
button.configure(text="Generate") 
button.pack()  # Pack the CTkButton widget

# Start the tkinter main loop to run the application
app.mainloop()
