import tkinter as tk
from tkinter import filedialog, messagebox
import random
from core.score_calculator import TennisScorer
from utils.file_parser import parse_file


class TennisScoreboard:
    def __init__(self, root):
        self.score_display = None
        self.input_display_p1 = None
        self.input_display_p2 = None
        self.input_frame = None
        self.player1_entry = None
        self.player2_entry = None
        self.button_frame = None
        self.submit_button = None
        self.generate_button = None
        self.upload_button = None

        self.root = root
        self.root.title("Tennis Scoreboard")

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.scorer = TennisScorer()
        self.uploaded_scores = []
        self.current_index = 0

        self.default_score1 = 0
        self.default_score2 = 0

        self.font_family = "Helvetica"
        self.score_font_size = 14
        self.input_label_font_size = 18

        self.create_ui()

    def create_ui(self):
        initial_result = self.scorer.calculate_score(self.default_score1, self.default_score2)

        self.score_display = tk.Label(
            self.root, text=initial_result, font=("Courier", 48), bg="black", fg="red"
        )
        self.score_display.grid(row=0, column=0, pady=20, sticky="n")

        self.input_display_p1 = tk.Label(
            self.root, text=f"Player 1: {self.default_score1}", font=(self.font_family, self.input_label_font_size), fg="red"
        )
        self.input_display_p1.grid(row=1, column=0, pady=5, sticky="n")

        self.input_display_p2 = tk.Label(
            self.root, text=f"Player 2: {self.default_score2}", font=(self.font_family, self.input_label_font_size), fg="red"
        )
        self.input_display_p2.grid(row=2, column=0, pady=5, sticky="n")

        self.input_frame = tk.Frame(self.root)
        self.input_frame.grid(row=3, column=0, pady=20)

        tk.Label(self.input_frame, text="Player 1 Score:", font=(self.font_family, self.score_font_size)).grid(row=0, column=0, padx=10, pady=5)
        self.player1_entry = tk.Entry(self.input_frame, font=("Courier", 16), width=5)
        self.player1_entry.insert(0, str(self.default_score1))
        self.player1_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.input_frame, text="Player 2 Score:", font=(self.font_family, self.score_font_size)).grid(row=1, column=0, padx=10, pady=5)
        self.player2_entry = tk.Entry(self.input_frame, font=("Courier", 16), width=5)
        self.player2_entry.insert(0, str(self.default_score2))
        self.player2_entry.grid(row=1, column=1, padx=10, pady=5)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=4, column=0, pady=20)

        self.submit_button = tk.Button(self.button_frame, text="Submit Scores", command=self.submit_scores, width=20)
        self.submit_button.grid(row=0, column=0, padx=10)

        self.generate_button = tk.Button(
            self.button_frame, text="Generate Random Scores", command=self.generate_scores, width=20
        )
        self.generate_button.grid(row=0, column=1, padx=10)

        self.upload_button = tk.Button(self.button_frame, text="Upload Scores File", command=self.upload_scores, width=20)
        self.upload_button.grid(row=0, column=2, padx=10)

    def submit_scores(self):
        try:
            score1 = int(self.player1_entry.get())
            score2 = int(self.player2_entry.get())
            result = self.scorer.calculate_score(score1, score2)

            if result == "Invalid Score":
                messagebox.showerror("Validation Error", "The entered scores are invalid according to tennis rules.")
                return

            self.score_display.config(text=result)
            self.input_display_p1.config(text=f"Player 1: {score1}")
            self.input_display_p2.config(text=f"Player 2: {score2}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for scores.")

    def generate_scores(self):
        while True:
            score1 = random.randint(0, 6)
            score2 = random.randint(0, 6)

            if self.scorer.validate_tennis_scores(score1, score2):
                break

        self.player1_entry.delete(0, tk.END)
        self.player2_entry.delete(0, tk.END)
        self.player1_entry.insert(0, str(score1))
        self.player2_entry.insert(0, str(score2))

        result = self.scorer.calculate_score(score1, score2)
        self.score_display.config(text=result)
        self.input_display_p1.config(text=f"Player 1: {score1}")
        self.input_display_p2.config(text=f"Player 2: {score2}")

    def upload_scores(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        try:
            data = parse_file(file_path)
            self.uploaded_scores = [(row.get(0), row.get(0)) for _, row in data.iterrows()]
            if not self.uploaded_scores:
                messagebox.showerror("Upload Error", "No valid scores found in the file.")
                self.return_to_home()
                return

            self.current_index = 0
            self.show_score_navigation()
        except ValueError as e:
            messagebox.showerror("File Error",
                                 "An error occurred while processing the file. Please check your input data.")
            self.return_to_home()

    def show_score_navigation(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        score = self.uploaded_scores[self.current_index]
        score1, score2 = score
        result = self.scorer.calculate_score(score1, score2)

        score_display = tk.Label(self.root, text=result, font=("Courier", 48), bg="black", fg="red")
        score_display.grid(row=0, column=0, pady=20, sticky="n")

        input_display_p1 = tk.Label(self.root, text=f"Player 1: {score1}", font=(self.font_family, self.input_label_font_size), fg="red")
        input_display_p1.grid(row=1, column=0, pady=5, sticky="n")

        input_display_p2 = tk.Label(self.root, text=f"Player 2: {score2}", font=(self.font_family, self.input_label_font_size), fg="red")
        input_display_p2.grid(row=2, column=0, pady=5, sticky="n")

        page_indicator = tk.Label(
            self.root,
            text=f"{self.current_index + 1}/{len(self.uploaded_scores)}",
            font=(self.font_family, self.score_font_size),
            fg="red",
        )
        page_indicator.grid(row=5, column=0, pady=10, sticky="n")

        nav_frame = tk.Frame(self.root)
        nav_frame.grid(row=4, column=0, pady=20)

        prev_button = tk.Button(nav_frame, text="Previous", command=self.previous_score, width=15)
        prev_button.grid(row=0, column=0, padx=10)

        next_button = tk.Button(nav_frame, text="Next", command=self.next_score, width=15)
        next_button.grid(row=0, column=1, padx=10)

        home_button = tk.Button(nav_frame, text="Home", command=self.return_to_home, width=15)
        home_button.grid(row=0, column=2, padx=10)

    def previous_score(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_score_navigation()
        else:
            messagebox.showinfo("Navigation", "This is the first score.")

    def next_score(self):
        if self.current_index < len(self.uploaded_scores) - 1:
            self.current_index += 1
            self.show_score_navigation()
        else:
            messagebox.showinfo("Navigation", "This is the last score.")

    def return_to_home(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_ui()
