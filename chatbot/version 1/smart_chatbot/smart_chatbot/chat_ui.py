import tkinter as tk
import threading
import rclpy
from smart_chatbot.chat_manager import ChatManager


class ChatUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("ROS 2 Smart Chatbot")
        self.root.geometry("500x600")
        self.root.configure(bg="#1e1e2f")

        # Chat Display Box
        self.chat_box = tk.Text(
            self.root,
            bg="#2a2a40",
            fg="white",
            font=("Arial", 12),
            wrap=tk.WORD
        )
        self.chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input Entry
        self.entry = tk.Entry(
            self.root,
            font=("Arial", 12)
        )
        self.entry.pack(padx=10, pady=10, fill=tk.X)

        # Send Button
        self.send_button = tk.Button(
            self.root,
            text="Send",
            bg="#4CAF50",
            fg="white",
            command=self.send_message
        )
        self.send_button.pack(pady=5)

        # Initialize ROS
        rclpy.init()
        self.node = ChatManager()

        # Spin ROS in background thread
        threading.Thread(
            target=rclpy.spin,
            args=(self.node,),
            daemon=True
        ).start()

        # Continuously check for new responses
        self.root.after(500, self.check_for_response)

    # ---------------------------------
    # Send Message
    # ---------------------------------
    def send_message(self):

        text = self.entry.get().strip()

        if text == "":
            return

        self.chat_box.insert(tk.END, f"You: {text}\n")
        self.node.process_message(text)
        self.entry.delete(0, tk.END)

    # ---------------------------------
    # Check ROS Responses
    # ---------------------------------
    def check_for_response(self):

        if self.node.latest_response:
            self.chat_box.insert(
                tk.END,
                f"Bot: {self.node.latest_response}\n"
            )
            self.node.latest_response = ""

        self.root.after(500, self.check_for_response)

    # ---------------------------------
    # Run UI
    # ---------------------------------
    def run(self):
        self.root.mainloop()


def main():
    app = ChatUI()
    app.run()


if __name__ == "__main__":
    main()
