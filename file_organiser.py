import os
import shutil as s

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
    ".c", ".h", ".cpp", ".hpp", ".cc", ".cxx", ".ino", ".cs",".cs", ".csx",
    ".html", ".htm", ".xhtml", ".css", ".scss", ".sass", ".less",
    ".php", ".php3", ".php4", ".php5", ".phtml",".rb", ".rbw", ".rhtml",
    ".pl", ".pm", ".t", ".pod", ".psgi", ".sh", ".bash", ".bsh", ".csh", ".ksh", ".zsh", ".bat", ".cmd",".ps1", ".psm1", ".psd1",
    ".swift",  ".kt", ".kts", ".ts", ".tsx", ".go", ".rs", ".rlib", ".lua", ".r", ".rdata", ".rds",
    ".scala", ".sc",".groovy", ".gvy", ".gy", ".gsh",".hs", ".lhs",".m",".jl",
    ".m", ".mm", ".h",".sql", ".pls", ".plsql", ".db2",".asm", ".s", ".a51", ".inc",".vb", ".vbs", ".bas", ".frm", ".cls", ".ctl", ".vbhtml",
    ".pas", ".pp", ".inc", ".dart",".yml", ".yaml", ".json", ".toml")
}

folder_path = os.getcwd()
def file_finder(path, file_extensions):
    return [file for file in os.listdir(path) for extension in file_extensions if file.endswith(extension)]
def organize_files():
    for extension_type, extension_tuple in dict_files.items():
        files = file_finder(folder_path, extension_tuple)
        
        if files:
            folder_name = extension_type.split("_")[0] + " files"
            folder_path_full = os.path.join(folder_path, folder_name)
            os.makedirs(folder_path_full, exist_ok=True)
            for item in files:
                item_path = os.path.join(folder_path, item)
                item_new_path = os.path.join(folder_path_full, item)
                s.move(item_path, item_new_path)

organize_files()