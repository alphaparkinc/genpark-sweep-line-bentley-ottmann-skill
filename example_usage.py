from client import SweepLineIntersection

def main():
    print("=== Testing Bentley-Ottmann Sweep-Line Intersection ===")
    sli = SweepLineIntersection()

    s1 = ((0.0, 0.0), (4.0, 4.0))
    s2 = ((0.0, 4.0), (4.0, 0.0))

    crossings = sli.find_intersections([s1, s2])
    print("Detected intersection point:", crossings)
    assert crossings == [(2.0, 2.0)]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
