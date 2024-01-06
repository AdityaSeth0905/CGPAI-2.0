import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import mysql.connector


#Global variables
top=None

#superclass
class func():
    #functions for the system
    def on_escape(self, event):
        global top
        top.destroy()

    def loginWindow():
        print("")
    #main window creation
    def mainwindow():
        global top
        root=ctk.CTk()
        top=ctk.CTkToplevel(root)
        top.title("CIIE")
        top.geometry("800x800")
        top.configure(bg='black')
        top.bind("<Escape>", func().on_escape)
        
        image_path1 = "SRMUH-logo.png"
        image_path2 = "./pics/IIC logo.png"

        # Open the image
        image1 = Image.open(image_path1)

        # Resize the image using Lanczos interpolation
        resized_image1 = image1.resize((400, 300), Image.BILINEAR)

        # Convert the resized image to a PhotoImage object
        photo_image1 = ImageTk.PhotoImage(resized_image1)
        # Create a label to display the image
        image_label1 = tk.Label(top, image=photo_image1, bg="black")
        image_label1.pack(side="left" , pady=1)
        # Open the image
        image2 = Image.open(image_path2)
        # Resize the image using Lanczos interpolation
        resized_image2 = image2.resize((400, 300), Image.BILINEAR)
        # Convert the resized image to a PhotoImage object
        photo_image2 = ImageTk.PhotoImage(resized_image2)
        # Create a label to display the image
        image_label2 = tk.Label(top, image=photo_image2, bg="black")
        image_label2.pack(side="right" ,pady=1)
        
        top.mainloop()
    #Login Window


#class containing widgets
class widgets():
    def bgChangerBtn():
        print('')

#class containing all the sql functions
class sqlfunctions():
    #sql connection
    def connect_to_database():
        try:
            # Connect to your MySQL database
            db_connection = mysql.connector.connect(
                host="localhost", 
                user="root",  
                passwd="8882187203",
                database="ciie"
            )
    
            # Create a cursor object to execute SQL queries
            cursor = db_connection.cursor()
    
            # Execute an SQL query to retrieve data
            cursor.execute("SELECT * FROM members")
    

            # Fetch all the data from the query result
            data = cursor.fetchall()
    
            # Close the cursor and the database connection
            cursor.close()
            db_connection.close()
    
            return data
    
        except mysql.connector.Error as e:
            print("Error:", e)
            return None

#Main function
def main():
    print("The code is working!")
    func.mainwindow()

if __name__=="__main__":
    main()
