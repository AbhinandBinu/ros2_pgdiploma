import customtkinter as ctk
import rclpy
from rclpy.node import Node
from threading import Thread
from smart_chatbot.chat_manager import ChatManager


class ChatUI:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("ROS Hybrid Smart Chatbot")
        self.root.geometry("600x700")

        self.chat_manager = ChatManager()

        # Header
        self.header = ctk.CTkLabel(
            self.root,
            text="🤖 ROS Hybrid Smart Chatbot",
            font=("Arial", 20, "bold")
        )
        self.header.pack(pady=10)

        # Chat Frame
        self.chat_frame = ctk.CTkScrollableFrame(
            self.root,
            width=560,
            height=550
        )
        self.chat_frame.pack(padx=20, pady=10)

        # Input Frame
        self.input_frame = ctk.CTkFrame(self.root)
        self.input_frame.pack(padx=20, pady=10, fill="x")

        self.entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="Type your message...",
            width=450
        )
        self.entry.pack(side="left", padx=10, pady=10)

        self.send_button = ctk.CTkButton(
            self.input_frame,
            text="Send",
            command=self.send_message
        )
        self.send_button.pack(side="right", padx=10)

        self.root.bind("<Return>", lambda event: self.send_message())

    # =====================================================
    # DISPLAY MESSAGE
    # =====================================================
    def display_message(self, sender, message):

        if sender == "You":
            bubble = ctk.CTkLabel(
                self.chat_frame,
                text=f"{message}",
                fg_color="#1f6aa5",
                corner_radius=10,
                anchor="e",
                justify="right",
                wraplength=350
            )
            bubble.pack(anchor="e", pady=5, padx=10)

        else:
            bubble = ctk.CTkLabel(
                self.chat_frame,
                text=f"{message}",
                fg_color="#2b2b2b",
                corner_radius=10,
                anchor="w",
                justify="left",
                wraplength=350
            )
            bubble.pack(anchor="w", pady=5, padx=10)

    # =====================================================
    # SEND MESSAGE
    # =====================================================
    def send_message(self):

        user_input = self.entry.get()

        if user_input == "":
            return

        self.display_message("You", user_input)
        self.entry.delete(0, "end")

        # Run ROS processing in separate thread
        Thread(target=self.process_response, args=(user_input,)).start()

    # =====================================================
    # PROCESS RESPONSE
    # =====================================================
    def process_response(self, text):

        self.chat_manager.process_message(text)

        # Wait until response is ready
        while self.chat_manager.latest_response == "":
            rclpy.spin_once(self.chat_manager)

        response = self.chat_manager.latest_response
        self.display_message("Bot", response)


def main():
    rclpy.init()
    ui = ChatUI()
    ui.root.mainloop()


if __name__ == '__main__':
    main()
