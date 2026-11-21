"""
Embedded Media Player for Arch Linux / X11.

Python dependencies: none (uses tkinter + ctypes from the standard library).
System media engine: libmpv, supplied by Arch's "mpv" package.

Install once:
    sudo pacman -S mpv

Run:
    python embedded_media_player.py
"""

import ctypes
import ctypes.util
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path


def load_mpv_library():
    name = ctypes.util.find_library("mpv")
    if not name:
        raise RuntimeError(
            "libmpv was not found.\n\n"
            "On Arch Linux install it with:\n"
            "sudo pacman -S mpv"
        )
    return ctypes.CDLL(name)


class EmbeddedMPV:
    def __init__(self, video_window_id):
        self.lib = load_mpv_library()
        self._declare_functions()

        self.handle = self.lib.mpv_create()
        if not self.handle:
            raise RuntimeError("mpv_create() failed.")

        # Embed video output in the Tkinter video frame (X11 window ID).
        self._set_option("wid", str(video_window_id))
        self._set_option("vo", "x11")
        self._set_option("osc", "no")
        self._set_option("input-default-bindings", "no")

        result = self.lib.mpv_initialize(self.handle)
        if result < 0:
            self.lib.mpv_terminate_destroy(self.handle)
            self.handle = None
            raise RuntimeError(f"mpv initialization failed (error {result}).")

    def _declare_functions(self):
        self.lib.mpv_create.restype = ctypes.c_void_p

        self.lib.mpv_set_option_string.argtypes = [
            ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p
        ]
        self.lib.mpv_set_option_string.restype = ctypes.c_int

        self.lib.mpv_initialize.argtypes = [ctypes.c_void_p]
        self.lib.mpv_initialize.restype = ctypes.c_int

        self.lib.mpv_command.argtypes = [
            ctypes.c_void_p, ctypes.POINTER(ctypes.c_char_p)
        ]
        self.lib.mpv_command.restype = ctypes.c_int

        self.lib.mpv_set_property_string.argtypes = [
            ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p
        ]
        self.lib.mpv_set_property_string.restype = ctypes.c_int

        self.lib.mpv_terminate_destroy.argtypes = [ctypes.c_void_p]
        self.lib.mpv_terminate_destroy.restype = None

    def _set_option(self, name, value):
        result = self.lib.mpv_set_option_string(
            self.handle, name.encode(), value.encode()
        )
        if result < 0:
            raise RuntimeError(f"Could not set mpv option: {name} (error {result}).")

    def command(self, *args):
        encoded = [str(arg).encode("utf-8") for arg in args]
        array = (ctypes.c_char_p * (len(encoded) + 1))(*encoded, None)
        result = self.lib.mpv_command(self.handle, array)
        if result < 0:
            raise RuntimeError(f"mpv command failed (error {result}).")

    def load(self, path):
        self.command("loadfile", os.path.abspath(path), "replace")

    def play_pause(self):
        self.command("cycle", "pause")

    def stop(self):
        self.command("stop")

    def set_volume(self, value):
        self.lib.mpv_set_property_string(
            self.handle, b"volume", str(int(float(value))).encode()
        )

    def close(self):
        if self.handle:
            self.lib.mpv_terminate_destroy(self.handle)
            self.handle = None


class MediaPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Media Player")
        self.root.geometry("820x540")
        self.root.minsize(600, 400)
        self.root.configure(bg="#171717")
        self.mpv = None

        tk.Label(
            root, text="Simple Media Player",
            bg="#171717", fg="white", font=("Arial", 17, "bold")
        ).pack(pady=10)

        self.video_frame = tk.Frame(root, bg="black")
        self.video_frame.pack(fill="both", expand=True, padx=12, pady=8)

        self.status = tk.Label(
            root, text="Open an audio or video file",
            bg="#171717", fg="#cccccc"
        )
        self.status.pack(pady=5)

        controls = tk.Frame(root, bg="#171717")
        controls.pack(pady=10)

        self.button(controls, "Open file", self.open_file).pack(side="left", padx=5)
        self.button(controls, "Play / Pause", self.play_pause).pack(side="left", padx=5)
        self.button(controls, "Stop", self.stop).pack(side="left", padx=5)

        tk.Label(controls, text="Volume", bg="#171717", fg="white").pack(
            side="left", padx=(15, 4)
        )
        self.volume = tk.Scale(
            controls, from_=0, to=100, orient="horizontal",
            length=130, command=self.change_volume,
            bg="#171717", fg="white", troughcolor="#555555",
            highlightthickness=0
        )
        self.volume.set(80)
        self.volume.pack(side="left")

        self.root.update_idletasks()
        try:
            self.mpv = EmbeddedMPV(self.video_frame.winfo_id())
            self.mpv.set_volume(80)
        except Exception as error:
            messagebox.showerror("Media engine error", str(error))
            self.root.destroy()
            return

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    @staticmethod
    def button(parent, text, command):
        return tk.Button(
            parent, text=text, command=command,
            bg="#343434", fg="white", activebackground="#505050",
            activeforeground="white", relief="flat",
            padx=12, pady=7, cursor="hand2"
        )

    def open_file(self):
        path = filedialog.askopenfilename(
            title="Open media",
            filetypes=[
                ("Audio and video", "*.mp3 *.wav *.flac *.ogg *.m4a "
                                    "*.mp4 *.mkv *.avi *.mov *.webm"),
                ("All files", "*.*")
            ]
        )
        if path:
            try:
                self.mpv.load(path)
                self.status.config(text=Path(path).name)
            except Exception as error:
                messagebox.showerror("Playback error", str(error))

    def play_pause(self):
        try:
            self.mpv.play_pause()
        except Exception as error:
            messagebox.showerror("Playback error", str(error))

    def stop(self):
        try:
            self.mpv.stop()
            self.status.config(text="Stopped")
        except Exception as error:
            messagebox.showerror("Playback error", str(error))

    def change_volume(self, value):
        if self.mpv:
            self.mpv.set_volume(value)

    def close(self):
        if self.mpv:
            self.mpv.close()
        self.root.destroy()


if __name__ == "__main__":
    window = tk.Tk()
    app = MediaPlayerApp(window)
    window.mainloop()
