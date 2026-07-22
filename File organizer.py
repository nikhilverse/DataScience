import shutil
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox


def get_category(file_path: Path) -> str:
    """Return a folder name based on the file extension."""
    ext = file_path.suffix.lower()

    image_exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"}
    document_exts = {".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"}
    audio_exts = {".mp3", ".wav", ".flac", ".aac", ".m4a"}
    video_exts = {".mp4", ".avi", ".mov", ".mkv", ".wmv", ".webm"}
    archive_exts = {".zip", ".rar", ".7z", ".tar", ".gz"}
    code_exts = {".js", ".ts", ".java", ".c", ".cpp", ".cs", ".html", ".css", ".json", ".xml"}

    if ext in image_exts:
        return "Images"
    if ext in document_exts:
        return "Documents"
    if ext in audio_exts:
        return "Audio"
    if ext in video_exts:
        return "Videos"
    if ext in archive_exts:
        return "Archives"
    if ext in code_exts:
        return "Code"
    return "Others"


def get_unique_destination(target_dir: Path, file_name: str) -> Path:
    """Avoid overwriting files by adding a number if needed."""
    destination = target_dir / file_name
    if not destination.exists():
        return destination

    stem = Path(file_name).stem
    suffix = Path(file_name).suffix
    counter = 1
    while True:
        new_name = f"{stem}_{counter}{suffix}"
        candidate = target_dir / new_name
        if not candidate.exists():
            return candidate
        counter += 1


def organize_folder(folder_path: str) -> int:
    folder = Path(folder_path).expanduser().resolve()

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")
    if not folder.is_dir():
        raise NotADirectoryError(f"Not a folder: {folder}")

    moved_count = 0
    for item in folder.iterdir():
        if item.is_dir():
            continue
        if item.name == Path(__file__).name:
            continue

        category = get_category(item)
        target_dir = folder / category
        target_dir.mkdir(exist_ok=True)

        destination = get_unique_destination(target_dir, item.name)
        shutil.move(str(item), str(destination))
        moved_count += 1

    return moved_count


class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("500x220")
        self.root.resizable(False, False)

        tk.Label(root, text="Select a folder to organize:", font=("Segoe UI", 11)).pack(pady=(20, 5))

        self.folder_var = tk.StringVar(value=str(Path.cwd()))
        entry = tk.Entry(root, textvariable=self.folder_var, width=50)
        entry.pack(pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Browse", width=12, command=self.browse_folder).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Organize", width=12, command=self.organize).pack(side=tk.LEFT, padx=5)

        tk.Label(root, text="Files will be sorted into Images, Documents, Audio, Videos, Archives, Code, and Others.", wraplength=450, justify="center").pack(pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select folder to organize")
        if folder:
            self.folder_var.set(folder)

    def organize(self):
        folder_path = self.folder_var.get().strip()
        if not folder_path:
            messagebox.showwarning("Warning", "Please select a folder first.")
            return

        try:
            moved_count = organize_folder(folder_path)
            messagebox.showinfo("Done", f"Organized {moved_count} file(s) successfully.")
        except Exception as exc:
            messagebox.showerror("Error", str(exc))


if __name__ == "__main__":
    root = tk.Tk()
    FileOrganizerApp(root)
    root.mainloop()
