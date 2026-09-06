import tkinter as tk
import re
from hasher import hash_text

# ─────────────────────────────────────────────
# Colors
# ─────────────────────────────────────────────

STATUS_READY = "#8B949E"
STATUS_SUCCESS = "#7EE787"
STATUS_WARNING = "#D29922"

BG_COLOR = "#0D1117"
PANEL_COLOR = "#161B22"

TEXT_COLOR = "#E6EDF3"
SECONDARY_COLOR = "#8B949E"

ACCENT_COLOR = "#58A6FF"
ACCENT_HOVER = "#79C0FF"

HASH_COLOR = "#7EE787"
HASH_COLOR2 = "#FF0000"

# ─────────────────────────────────────────────
# Window
# ─────────────────────────────────────────────

root = tk.Tk()

root.title("SHA-256 Encoder")
root.geometry("1100x650")
root.minsize(760, 480)

root.resizable(True, True)

root.configure(bg=BG_COLOR)


# ─────────────────────────────────────────────
# Functions
# ─────────────────────────────────────────────

def on_text_change(event):
    translate_text()

def on_hash_change(event):
    validate_hash()

def clear_input():
    input_text.delete("1.0", tk.END)
    input_text.focus_set()
    translate_text()

def translate_text():
    text = input_text.get("1.0", "end-1c")
    input_text.config(fg=TEXT_COLOR)

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)

    if not text:
        output_text.config(
            fg=SECONDARY_COLOR
        )

        output_text.config(
            state="normal"
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
        state="normal"
    )

    status_indicator.config(
    text="● LIVE HASHING",
    fg=STATUS_SUCCESS
    )

def validate_hash():
    hash_value = output_text.get("1.0", "end-1c").strip()

    input_text.delete("1.0", tk.END)

    if not hash_value:
        input_text.config(fg=SECONDARY_COLOR)

        status_indicator.config(
            text="● WAITING FOR INPUT",
            fg=STATUS_WARNING
        )

        return

    if not re.fullmatch(r"[0-9a-fA-F]{64}", hash_value):
        input_text.insert(
            "1.0",
            "Invalid SHA-256 hash."
        )

        input_text.config(fg=SECONDARY_COLOR)

        input_text.config(fg=HASH_COLOR2)

        status_indicator.config(
            text="● INVALID SHA-256 HASH",
            fg=STATUS_WARNING
        )

        return

    input_text.insert(
        "1.0",
        "Valid SHA-256 hash."
    )

    input_text.config(fg=HASH_COLOR)

    status_indicator.config(
        text="● VALID SHA-256 HASH",
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

def copy_button_enter(event):
    copy_button.config(
        fg=ACCENT_HOVER
    )

def copy_button_leave(event):
    copy_button.config(
        fg=TEXT_COLOR
    )

def draw_rounded_shape(canvas, tag, x1, y1, x2, y2, radius, fill):
    canvas.delete(tag)

    if x2 <= x1 or y2 <= y1:
        return

    radius = min(radius, (x2 - x1) / 2, (y2 - y1) / 2)

    canvas.create_rectangle(
        x1 + radius,
        y1,
        x2 - radius,
        y2,
        fill=fill,
        outline=fill,
        tags=tag
    )
    canvas.create_rectangle(
        x1,
        y1 + radius,
        x2,
        y2 - radius,
        fill=fill,
        outline=fill,
        tags=tag
    )

    for x, y, start in (
        (x1, y1, 90),
        (x2 - 2 * radius, y1, 0),
        (x2 - 2 * radius, y2 - 2 * radius, 270),
        (x1, y2 - 2 * radius, 180)
    ):
        canvas.create_arc(
            x,
            y,
            x + 2 * radius,
            y + 2 * radius,
            start=start,
            extent=90,
            fill=fill,
            outline=fill,
            tags=tag
        )

def create_rounded_panel(parent):
    canvas = tk.Canvas(
        parent,
        bg=BG_COLOR,
        highlightthickness=0,
        borderwidth=0
    )

    panel = tk.Frame(
        canvas,
        bg=PANEL_COLOR,
        highlightthickness=0,
        borderwidth=0
    )

    panel_margin = 8

    panel_window = canvas.create_window(
        panel_margin,
        panel_margin,
        anchor="nw",
        window=panel
    )

    def resize_panel(event):
        width = max(event.width - 2 * panel_margin, 1)
        height = max(event.height - 2 * panel_margin, 1)

        canvas.itemconfigure(
            panel_window,
            width=width,
            height=height
        )

        draw_rounded_shape(
            canvas,
            "rounded-background",
            0,
            0,
            event.width,
            event.height,
            18,
            PANEL_COLOR
        )
        canvas.tag_lower("rounded-background")

    canvas.bind("<Configure>", resize_panel)

    return canvas, panel

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
    padx=36,
    pady=26
)

# Responsive vertical layout
main_frame.grid_rowconfigure(0, weight=0)  # Header
main_frame.grid_rowconfigure(1, weight=0)  # Status
main_frame.grid_rowconfigure(2, weight=1)  # Translation area
main_frame.grid_rowconfigure(3, weight=0)  # Footer

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
translation_frame.grid_columnconfigure(0, weight=1, minsize=280)
translation_frame.grid_columnconfigure(1, weight=0)
translation_frame.grid_columnconfigure(2, weight=1, minsize=280)

translation_frame.grid_rowconfigure(0, weight=1, minsize=220)


# ─────────────────────────────────────────────
# Input Panel
# ─────────────────────────────────────────────

input_column = tk.Frame(
    translation_frame,
    bg=BG_COLOR
)

input_column.grid(
    row=0,
    column=0,
    sticky="nsew"
)

input_column.grid_rowconfigure(1, weight=1)
input_column.grid_columnconfigure(0, weight=1)


input_header = tk.Frame(
    input_column,
    bg=BG_COLOR
)

input_header.grid(
    row=0,
    column=0,
    sticky="ew",
    pady=(0, 8)
)


input_label = tk.Label(
    input_header,
    text="PLAIN TEXT",
    font=("Consolas", 10, "bold"),
    fg=SECONDARY_COLOR,
    bg=BG_COLOR
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
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    activebackground=BG_COLOR,
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


input_container, input_panel = create_rounded_panel(
    input_column
)

input_container.grid(
    row=1,
    column=0,
    sticky="nsew"
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
    text="⇆",
    font=("Consolas", 24),
    fg=ACCENT_COLOR,
    bg=BG_COLOR
)

arrow.grid(
    row=0,
    column=1,
    padx=18
)


# ─────────────────────────────────────────────
# Output Panel
# ─────────────────────────────────────────────

output_column = tk.Frame(
    translation_frame,
    bg=BG_COLOR
)

output_column.grid(
    row=0,
    column=2,
    sticky="nsew"
)

output_column.grid_rowconfigure(1, weight=1)
output_column.grid_columnconfigure(0, weight=1)


output_header = tk.Frame(
    output_column,
    bg=BG_COLOR
)

output_header.grid(
    row=0,
    column=0,
    sticky="ew",
    pady=(0, 8)
)


output_label = tk.Label(
    output_header,
    text="SHA-256 HASH",
    font=("Consolas", 10, "bold"),
    fg=SECONDARY_COLOR,
    bg=BG_COLOR
)

output_label.pack(anchor="w")


output_container, output_panel = create_rounded_panel(
    output_column
)

output_container.grid(
    row=1,
    column=0,
    sticky="nsew"
)

output_panel.grid_rowconfigure(0, weight=1)
output_panel.grid_rowconfigure(1, weight=0)

output_panel.grid_columnconfigure(0, weight=1)


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
    state="normal"
)

output_text.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=2,
    pady=5
)


output_text.bind(
    "<KeyRelease>",
    on_hash_change
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
    row=1,
    column=0,
    sticky="e",
    padx=18,
    pady=(5, 12)
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
    row=3,
    column=0,
    pady=(16, 5)
)


# ─────────────────────────────────────────────
# Start
# ─────────────────────────────────────────────

root.mainloop()
