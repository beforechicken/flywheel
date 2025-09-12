import sys, re, pathlib

def redact(text:str)->str:
    pattern = re.compile(r"<!--\s*PRIVATE:start\s*-->.*?<!--\s*PRIVATE:end\s*-->", re.DOTALL|re.IGNORECASE)
    return pattern.sub("", text)

def main(paths):
    for p in paths:
        pth = pathlib.Path(p)
        if pth.is_file() and pth.suffix.lower() in {".md", ".txt"}:
            s = pth.read_text(encoding="utf-8")
            pth.write_text(redact(s), encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/redact.py <files...>")
        sys.exit(1)
    main(sys.argv[1:])
