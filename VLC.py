import tkinter as tk
from tkinter import filedialog
import vlc

class DennisMediaPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Dennis Media Player")
        self.root.geometry("400x200")
        self.root.configure(bg="#1C1C1C")  # Dark background color
        
        self.instance = vlc.Instance("--no-xlib")
        self.player = self.instance.media_player_new()

        # Styling
        self.button_style = {"bg": "#333333", "fg": "#FFFFFF", "activebackground": "#666666", "activeforeground": "#FFFFFF"}

        self.play_button = tk.Button(self.root, text="▶ Play", command=self.play_media, **self.button_style)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="❚❚ Pause", command=self.pause_media, state=tk.DISABLED, **self.button_style)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="⏹ Stop", command=self.stop_media, state=tk.DISABLED, **self.button_style)
        self.stop_button.pack(pady=5)

        self.file_path = tk.StringVar()
        self.file_path_entry = tk.Entry(self.root, textvariable=self.file_path, width=50, bg="#333333", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.file_path_entry.pack(pady=5)

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file, **self.button_style)
        self.browse_button.pack(pady=5)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=(("Media files", "*.mp3;*.mp4"), ("All files", "*.*")))
        self.file_path.set(file_path)

    def play_media(self):
        media_path = self.file_path.get()
        if media_path:
            media = self.instance.media_new(media_path)
            self.player.set_media(media)
            self.player.play()
            self.play_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)

    def pause_media(self):
        self.player.pause()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    def stop_media(self):
        self.player.stop()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    player = DennisMediaPlayer(root)
    root.mainloop()
