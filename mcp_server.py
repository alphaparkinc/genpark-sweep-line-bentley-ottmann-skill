import sys
import json
from client import SweepLineIntersection

sli = SweepLineIntersection()

def handle_call(name, arguments):
    if name == "intersect":
        segs = [tuple(tuple(p) for p in s) for s in arguments["segments"]]
        return {"intersections": sli.find_intersections(segs)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
