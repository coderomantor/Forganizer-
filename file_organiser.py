import os
import shutil
from pathlib import Path

dict_files = {
    'audio_files': (
    ".mp3", ".wav", ".aac", ".wma", ".ogg", ".flac", 
    ".m4a", ".aiff", ".alac", ".opus", ".amr", ".mid", 
    ".midi", ".ape", ".ac3", ".dts", ".pcm", ".ra", 
    ".weba", ".au", ".mp2", ".mp1", ".mka", ".spx", 
    ".voc", ".vox", ".snd", ".caf", ".kar", ".cda", 
    ".gsm", ".tta", ".swa", ".wv", ".dsf", ".dff", 
    ".m3u", ".pls", ".xspf", ".zab", ".itl", ".pkf"),
    'video_files': (
    ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", 
    ".webm", ".mpeg", ".mpg", ".m4v", ".3gp", ".ts", 
    ".rmvb", ".vob", ".ogv", ".divx", ".asf", ".m2ts",
    ".mts", ".f4v", ".mxf", ".m2v", ".dat", ".dv",
    ".rm", ".amv", ".svi", ".3g2", ".m1v", ".mpe",
    ".roq", ".nsv", ".nut", ".drc", ".ivf", ".bik",
    ".smk", ".ratdvd", ".gxf", ".tod", ".trp"),
    'document_files': (
    '.doc', '.pdf', '.txt', ".rtf", ".docx", ".odt",
    ".tex", ".pages", ".wpd", ".log", ".csv", ".xml",
    ".json", ".yaml", ".yml", ".html", ".htm", ".md",
    ".asc", ".cfg", ".ini", ".nfo", ".xls", ".xlsx", 
    ".ppt", ".pptx", ".ods", ".odp", ".dot", ".dotx", 
    ".xlsm", ".xltx", ".xltm", ".pptm", ".potx", 
    ".potm", ".key", ".numbers", ".epub", ".sxi", 
    ".stw", ".sxc", ".sxw", ".xps"),
    'image_files': (
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".ico",".svg", ".ai", ".eps", ".cdr", ".emf", ".wmf",
    ".raw", ".nef", ".cr2", ".orf", ".arw", ".dng", ".rw2", ".pef", ".sr2", ".srw",
    ".raf", ".3fr", ".erf", ".mrw", ".nrw", ".ptx", ".pxn", ".r3d", ".mef", ".kdc",
    ".obj", ".stl", ".ply", ".fbx", ".3ds", ".dae", ".gltf", ".glb",".heic", ".heif", ".avif",".psd", ".psb", ".xcf", ".cpt",
    ".cur", ".icns",".dicom", ".dcm", ".nii", ".hdr", ".img", ".tga", ".pcx", ".jp2", ".jpx", ".jpf", ".j2k", ".j2c", ".jpc", ".pgf", ".pam", 
    ".pbm", ".pgm", ".ppm", ".pnm", ".xbm", ".xpm", ".sgi", ".ras", ".sun"),
    'programming_files': (
    ".py", ".pyw", ".pyc", ".pyo", ".pyd",
    ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx", ".java", ".class", ".jar", ".jad", ".jsp",
    ".c", ".h", ".cpp", ".hpp", ".cc", ".cxx", ".ino", ".cs", ".csx",
    ".html", ".htm", ".xhtml", ".css", ".scss", ".sass", ".less",
    ".php", ".php3", ".php4", ".php5", ".phtml",".rb", ".rbw", ".rhtml",
    ".pl", ".pm", ".t", ".pod", ".psgi", ".sh", ".bash", ".bsh", ".csh", ".ksh", ".zsh", ".bat", ".cmd",".ps1", ".psm1", ".psd1",
    ".swift",  ".kt", ".kts", ".go", ".rs", ".rlib", ".lua", ".r", ".rdata", ".rds",
    ".scala", ".sc",".groovy", ".gvy", ".gy", ".gsh",".hs", ".lhs",".m",".jl",
    ".mm", ".sql", ".pls", ".plsql", ".db2",".asm", ".s", ".a51", ".inc",".vb", ".vbs", ".bas", ".frm", ".cls", ".ctl", ".vbhtml",
    ".pas", ".pp", ".dart",".yml", ".yaml", ".json", ".toml")
}

def get_unique_path(destination_path):
    """Returns a unique file path by appending a counter if the file already exists."""
    if not destination_path.exists():
        return destination_path
    
    counter = 1
    while True:
        new_name = f"{destination_path.stem}_{counter}{destination_path.suffix}"
        new_path = destination_path.with_name(new_name)
        if not new_path.exists():
            return new_path
        counter += 1

def file_finder(path, file_extensions):
    """Finds files (not directories) with matching case-insensitive extensions."""
    path_obj = Path(path)
    matching_files = []
    
    # Pre-calculate lowercase extensions for faster matching
    extensions_lower = {ext.lower() for ext in file_extensions}
    
    for item in path_obj.iterdir():
        if item.is_file() and item.suffix.lower() in extensions_lower:
            matching_files.append(item)
            
    return matching_files

def organize_files():
    folder_path = Path.cwd()
    
    for extension_type, extension_tuple in dict_files.items():
        files = file_finder(folder_path, extension_tuple)
        
        if files:
            # Create a nice folder name, e.g., "audio_files" -> "Audio Files"
            folder_name = extension_type.replace("_", " ").title()
            folder_path_full = folder_path / folder_name
            folder_path_full.mkdir(exist_ok=True)
            
            for item in files:
                item_new_path = get_unique_path(folder_path_full / item.name)
                shutil.move(str(item), str(item_new_path))

if __name__ == "__main__":
    organize_files()