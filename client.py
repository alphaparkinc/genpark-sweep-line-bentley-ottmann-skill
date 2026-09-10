class SweepLineIntersection:
    """
    Sweep-Line Segment Intersection (Bentley-Ottmann model).
    Events sorted by X coordinate.
    """
    def find_intersections(self, segments):
        intersections = []
        for i in range(len(segments)):
            for j in range(i + 1, len(segments)):
                s1, s2 = segments[i], segments[j]
                (x1, y1), (x2, y2) = s1
                (x3, y3), (x4, y4) = s2
                denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
                if abs(denom) > 1e-9:
                    t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) / denom
                    u = -((x1 - x2)*(y1 - y3) - (y1 - y2)*(x1 - x3)) / denom
                    if 0.0 <= t <= 1.0 and 0.0 <= u <= 1.0:
                        ix = x1 + t*(x2 - x1)
                        iy = y1 + t*(y2 - y1)
                        intersections.append((round(ix, 4), round(iy, 4)))
        return intersections
