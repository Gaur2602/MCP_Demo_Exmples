import os
from pathlib import Path
from mcp.server.fastmcp import FastMCP

SCRIPT_DIR = Path(__file__).parent
BASE_DIR = Path(os.getenv("FILE_READER_DIRECTORY", SCRIPT_DIR / "documents"))

mcp = FastMCP("file-system-reader")

@mcp.tool()
def read_file(filename: str) -> str:
    "Read a file from the document or any given directory."
    
    try:
        file_path = BASE_DIR / filename
        if not str(file_path.resolve()).startswith(str(BASE_DIR.resolve())):
            return "Error: Access denied - invalid path"
        
        content = file_path.read_text(encoding="utf-8")
        return f"File :{filename}\n\n{content}"
    
    except Exception as e:
        return f"Error reading the given file: {e}"
    
@mcp.tool()
def list_files() -> str:
    """List files in directory."""
    try:
        files = [f.name for f in BASE_DIR.iterdir() if f.is_file()]
        files_text = "\n".join(sorted(files)) if files else "No files found"
        return f"Files:\n\n{files_text}"
        
    except Exception as e:
        return f"Error listing files: {e}"


if __name__ == "__main__":
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"BASE_DIR: {BASE_DIR.resolve()}")  # Shows absolute path
    print(f"Does it exist? {BASE_DIR.exists()}")
    BASE_DIR.mkdir(parents=True, exist_ok=True)
    mcp.run()