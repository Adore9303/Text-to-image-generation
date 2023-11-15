# Text-to-image-generation
This application was deisgned using the graphic user interface in python called tkinter which intakes the prompt text and generates the image using the stable diffusion model



Python Project: Text to Image Generation using Stable Diffusion Model

About the Project
This Python project is a simple GUI application that uses the Stable Diffusion model to generate images based on user input. The application is built using the Tkinter library and uses the Hugging Face’s implementation of the Stable Diffusion model.


Prerequisites
To run this project, you need:
•	Python 3.6 or above
•	Tkinter library for creating the GUI
•	CustomTkinter library for customizing the Tkinter widgets
•	PIL (Python Imaging Library) for handling images
•	PyTorch for running the Stable Diffusion model
•	Hugging Face’s Transformers library for loading the Stable Diffusion model
Framework Used
The project uses the Tkinter library, which is Python’s standard GUI package. It also uses CustomTkinter for customizing the appearance of the Tkinter widgets.




Code snippet explanation:

1.	Importing Libraries: The code begins by importing the necessary libraries. Tkinter is used for creating the GUI, customtkinter for customizing the Tkinter widgets, PIL (Python Imaging Library) for handling images, and torch for running the Stable Diffusion model.
 ![image](https://github.com/Adore9303/Text-to-image-generation/assets/107853973/51ed93bf-82c9-40c8-b022-2bfc0cb46698)



2.	Setting up the GUI: A Tkinter window is created and configured with a specific geometry and title. A dark theme is set for customtkinter widgets.
![image](https://github.com/Adore9303/Text-to-image-generation/assets/107853973/4b403366-1b8e-439e-b247-d96d11701dcc)


3.	Creating Widgets: A frame is created to hold other widgets. Inside this frame, a text entry field (CTkEntry) for user input, a label (CTkLabel) for displaying images, and a button (CTkButton) to trigger image generation are created.
![image](https://github.com/Adore9303/Text-to-image-generation/assets/107853973/be31ae37-053e-483c-a103-fe595a872e8f)
![image](https://github.com/Adore9303/Text-to-image-generation/assets/107853973/0cf4cb95-9e1b-4b22-a51e-3ab5658371d2)



4.	Loading the Model: The Stable Diffusion model is loaded using Hugging Face’s Transformers library.
 ![image](https://github.com/Adore9303/Text-to-image-generation/assets/107853973/ecdee12b-c525-45ed-aa30-f6cc695debd8)



5.	Defining the Generate Function: This function retrieves the user’s input text from the CTkEntry widget, generates an image using the Stable  Diffusion model, and displays it in the CTkLabel widget.
![image](https://github.com/Adore9303/Text-to-image-generation/assets/107853973/b9a99ff4-637d-45f3-85ec-42135a00f27b)



6.	Running the Application: Finally, the Tkinter main loop is started to run the application.
 ![image](https://github.com/Adore9303/Text-to-image-generation/assets/107853973/01008ede-ed0a-4d53-9e01-37ef2475f37b)



This code demonstrates how to create a simple GUI application in Python that uses a machine-learning model to generate images based on user input.



Output 
![WhatsApp Image 2023-10-04 at 23 13 43_9ffb499d](https://github.com/Adore9303/Text-to-image-generation/assets/107853973/e9675b06-eb85-4772-9ea6-6aaa81b06756)
![WhatsApp Image 2023-10-04 at 22 29 02_9b236895](https://github.com/Adore9303/Text-to-image-generation/assets/107853973/f13c6c5f-97cb-42ed-9914-6956795bd185)




Conclusion

This project demonstrates how to create a simple GUI application in Python that can generate images from text using a machine-learning model. It shows how to use Tkinter to create an interactive interface and Hugging Face’s Transformers library to load and use a pre-trained machine-learning model. The project can be further extended by adding more features or using different models.

