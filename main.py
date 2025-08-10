# run_server.py

import os
import uvicorn

def main():
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(
        "app:app",  # Refers to the 'app' object in app.py
        host="0.0.0.0",
        port=port,
        reload=False
    )

if __name__ == "__main__":
    main()
