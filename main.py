import tkinter as tk
from hasher import hash_text

# ─────────────────────────────────────────────
# Colors
# ─────────────────────────────────────────────

STATUS_READY = "#8B949E"
STATUS_SUCCESS = "#7EE787"
STATUS_WARNING = "#D29922"

BG_COLOR = "#0D1117"
PANEL_COLOR = "#161B22"
BORDER_COLOR = "#30363D"

TEXT_COLOR = "#E6EDF3"
SECONDARY_COLOR = "#8B949E"

ACCENT_COLOR = "#58A6FF"
ACCENT_HOVER = "#79C0FF"

HASH_COLOR = "#7EE787"

# ─────────────────────────────────────────────
# Window
# ─────────────────────────────────────────────

root = tk.Tk()

root.title("SHA-256 Encoder")
root.geometry("1000x600")
root.minsize(900, 550)

root.resizable(True, True)

root.configure(bg=BG_COLOR)


# ─────────────────────────────────────────────
# Functions
# ─────────────────────────────────────────────

def on_text_change(event):
    translate_text()

def clear_input():
    input_text.delete("1.0", tk.END)
    input_text.focus_set()
    translate_text()

def translate_text():
    text = input_text.get("1.0", "end-1c")

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)

    if not text:
        output_text.insert(
            "1.0",
            "Enter some text to generate a hash."
        )

        output_text.config(
            fg=SECONDARY_COLOR
        )

        output_text.config(
            state="disabled"
        )

        status_indicator.config(
            text="● WAITING FOR INPUT",
            fg=STATUS_WARNING
        )

        return

    hashed_text = hash_text(text)

    output_text.config(
        fg=HASH_COLOR
    )

    output_text.insert(
        "1.0",
        hashed_text
    )

    output_text.config(
        state="disabled"
    )

    status_indicator.config(
    text="● LIVE HASHING",
    fg=STATUS_SUCCESS
    )

def copy_hash():
    hash_value = output_text.get("1.0", tk.END).strip()

    if not hash_value:
        status_indicator.config(
            text="● NOTHING TO COPY",
            fg=STATUS_WARNING
        )
        return

    root.clipboard_clear()
    root.clipboard_append(hash_value)
    root.update()

    status_indicator.config(
        text="● HASH COPIED",
        fg=STATUS_SUCCESS
    )

def on_button_enter(event):
    translate_button.config(
        bg=ACCENT_HOVER
    )

def on_button_leave(event):
    translate_button.config(
        bg=ACCENT_COLOR
    )

def copy_button_enter(event):
    copy_button.config(
        fg=ACCENT_HOVER
    )

def copy_button_leave(event):
    copy_button.config(
        fg=TEXT_COLOR
    )

# ─────────────────────────────────────────────
# Main Container
# ─────────────────────────────────────────────

main_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=50,
    pady=30
)

# Responsive vertical layout
main_frame.grid_rowconfigure(0, weight=0)  # Header
main_frame.grid_rowconfigure(1, weight=0)  # Status
main_frame.grid_rowconfigure(2, weight=1)  # Translation area
main_frame.grid_rowconfigure(3, weight=0)  # Button
main_frame.grid_rowconfigure(4, weight=0)  # Footer

main_frame.grid_columnconfigure(0, weight=1)


# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────

header_frame = tk.Frame(
    main_frame,
    bg=BG_COLOR
)

header_frame.grid(
    row=0,
    column=0,
    sticky="ew",
    pady=(0, 25)
)


title = tk.Label(
    header_frame,
    text="◈  SHA-256 ENCODER",
    font=("Consolas", 24, "bold"),
    fg=TEXT_COLOR,
    bg=BG_COLOR
)

title.pack(anchor="w")


subtitle = tk.Label(
    header_frame,
    text="Cryptographic hashing utility",
    font=("Consolas", 10),
    fg=SECONDARY_COLOR,
    bg=BG_COLOR
)

subtitle.pack(
    anchor="w",
    pady=(6, 0)
)

# ─────────────────────────────────────────────
# Status
# ─────────────────────────────────────────────

status_frame = tk.Frame(
    main_frame,
    bg=BG_COLOR
)

status_frame.grid(
    row=1,
    column=0,
    sticky="ew",
    pady=(0, 15)
)


status_indicator = tk.Label(
    status_frame,
    text="● READY",
    font=("Consolas", 9, "bold"),
    fg=STATUS_READY,
    bg=BG_COLOR
)

status_indicator.pack(anchor="w")

# ─────────────────────────────────────────────
# Translation Area
# ─────────────────────────────────────────────

translation_frame = tk.Frame(
    main_frame,
    bg=BG_COLOR
)

translation_frame.grid(
    row=2,
    column=0,
    sticky="nsew"
)

# Responsive columns
translation_frame.grid_columnconfigure(0, weight=1)
translation_frame.grid_columnconfigure(1, weight=0)
translation_frame.grid_columnconfigure(2, weight=1)

translation_frame.grid_rowconfigure(0, weight=1)


# ─────────────────────────────────────────────
# Input Panel
# ─────────────────────────────────────────────

input_container = tk.Frame(
    translation_frame,
    bg=BORDER_COLOR
)

input_container.grid(
    row=0,
    column=0,
    sticky="nsew"
)


input_panel = tk.Frame(
    input_container,
    bg=PANEL_COLOR
)

input_panel.pack(
    fill="both",
    expand=True,
    padx=1,
    pady=1
)


input_header = tk.Frame(
    input_panel,
    bg=PANEL_COLOR
)

input_header.pack(
    fill="x",
    padx=18,
    pady=(15, 8)
)


input_label = tk.Label(
    input_header,
    text="PLAIN TEXT",
    font=("Consolas", 10, "bold"),
    fg=SECONDARY_COLOR,
    bg=PANEL_COLOR
)

input_label.pack(
    anchor="w",
    side="left"
)


clear_button = tk.Button(
    input_header,
    text="×",
    command=clear_input,
    font=("Consolas", 16, "bold"),
    bg=PANEL_COLOR,
    fg=TEXT_COLOR,
    activebackground=PANEL_COLOR,
    activeforeground=ACCENT_HOVER,
    relief="flat",
    borderwidth=0,
    cursor="hand2",
    padx=4,
    pady=0
)

clear_button.pack(
    anchor="e",
    side="right"
)


input_text = tk.Text(
    input_panel,
    bg=PANEL_COLOR,
    fg=TEXT_COLOR,
    insertbackground=ACCENT_COLOR,
    selectbackground=ACCENT_COLOR,
    selectforeground=BG_COLOR,
    font=("Consolas", 12),
    relief="flat",
    borderwidth=0,
    wrap="word",
    padx=18,
    pady=12
)

input_text.pack(
    fill="both",
    expand=True,
    padx=2,
    pady=(0, 5)
)


# Reset status when typing
input_text.bind(
    "<KeyRelease>",
    on_text_change
)


# ─────────────────────────────────────────────
# Arrow
# ─────────────────────────────────────────────

arrow = tk.Label(
    translation_frame,
    text="→",
    font=("Consolas", 24),
    fg=ACCENT_COLOR,
    bg=BG_COLOR
)

arrow.grid(
    row=0,
    column=1,
    padx=25
)


# ─────────────────────────────────────────────
# Output Panel
# ─────────────────────────────────────────────

output_container = tk.Frame(
    translation_frame,
    bg=BORDER_COLOR
)

output_container.grid(
    row=0,
    column=2,
    sticky="nsew"
)


output_panel = tk.Frame(
    output_container,
    bg=PANEL_COLOR
)

output_panel.pack(
    fill="both",
    expand=True,
    padx=1,
    pady=1
)

output_panel.grid_rowconfigure(0, weight=0)
output_panel.grid_rowconfigure(1, weight=1)
output_panel.grid_rowconfigure(2, weight=0)

output_panel.grid_columnconfigure(0, weight=1)

output_label = tk.Label(
    output_panel,
    text="SHA-256 HASH",
    font=("Consolas", 10, "bold"),
    fg=SECONDARY_COLOR,
    bg=PANEL_COLOR
)

output_label.grid(
    row=0,
    column=0,
    sticky="w",
    padx=18,
    pady=(15, 8)
)


output_text = tk.Text(
    output_panel,
    bg=PANEL_COLOR,
    fg=HASH_COLOR,
    font=("Consolas", 12),
    relief="flat",
    borderwidth=0,
    wrap="char",
    padx=18,
    pady=12,
    state="disabled"
)

output_text.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=2,
    pady=(0, 5)
)

copy_button = tk.Button(
    output_panel,
    text="⧉",
    command=copy_hash,
    font=("Consolas", 18),
    bg=PANEL_COLOR,
    fg=TEXT_COLOR,
    activebackground=PANEL_COLOR,
    activeforeground=TEXT_COLOR,
    relief="flat",
    borderwidth=0,
    cursor="hand2",
    padx=8,
    pady=4
)

copy_button.grid(
    row=2,
    column=0,
    sticky="e",
    padx=18,
    pady=(5, 15)
)

# ─────────────────────────────────────────────
# Button
# ─────────────────────────────────────────────

translate_button = tk.Button(
    main_frame,
    text="HASH TEXT",
    command=translate_text,
    font=("Consolas", 10, "bold"),
    fg=BG_COLOR,
    bg=ACCENT_COLOR,
    activeforeground=BG_COLOR,
    activebackground=ACCENT_HOVER,
    relief="flat",
    borderwidth=0,
    padx=35,
    pady=12,
    cursor="hand2"
)

translate_button.grid(
    row=3,
    column=0,
    pady=(20, 15)
)

translate_button.bind(
    "<Enter>",
    on_button_enter
)

translate_button.bind(
    "<Leave>",
    on_button_leave
)


copy_button.bind(
    "<Enter>",
    copy_button_enter
)

copy_button.bind(
    "<Leave>",
    copy_button_leave
)


def clear_button_enter(event):
    clear_button.config(
        fg=ACCENT_HOVER
    )

def clear_button_leave(event):
    clear_button.config(
        fg=TEXT_COLOR
    )


clear_button.bind(
    "<Enter>",
    clear_button_enter
)

clear_button.bind(
    "<Leave>",
    clear_button_leave
)

# ─────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────

footer = tk.Label(
    main_frame,
    text="SHA-256  •  LOCAL PROCESSING  •  NO DATA TRANSMITTED",
    font=("Consolas", 8),
    fg=SECONDARY_COLOR,
    bg=BG_COLOR
)

footer.grid(
    row=4,
    column=0,
    pady=(0, 5)
)


# ─────────────────────────────────────────────
# Start
# ─────────────────────────────────────────────

root.mainloop()
