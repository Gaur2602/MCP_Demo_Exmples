{
  "mcpServers": {
    "server-name": {
      "command": "python3",
      "args": ["/absolute/path/to/your/server.py"],
      "env": {
        "API_KEY": "your_key_here"
      }
    }
  }
}


{
  "mcpServers": {
    "file_system_reader": {
      "command": "python",
      "args": ["F:/MCP_Demo/file_system_reader.py"],
      "env": {
        "FILE_READER_DIRECTORY": "E:/desktop files/K8S_Interview"
      }
    },
    "playwright_mcp.py": {
      "command": "C:/Users/hp/AppData/Local/Programs/Python/Python313/python.exe",
      "args": ["F:/MCP_Demo/playwright_mcp.py"],
      }
    }
}




pip install -r requirements.txt
playwright install
python file_system_reader.py