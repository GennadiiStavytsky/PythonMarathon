import json
import cmath


def quad(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and a != 0:
        dis = b ** 2 - 4 * a * c

        sol1 = (-b - cmath.sqrt(dis)) / (2 * a)
        sol2 = (-b + cmath.sqrt(dis)) / (2 * a)

        sol1 = round(sol1.real, 3)
        sol2 = round(sol2.real, 3)

        print(sol1)
        print(sol2)

        print(round(sol1))

        if sol1 == sol2:
            if round(sol1) == -0:
                full_x = abs(sol1)
            full_x = sol1
        else:
            full_x = [sol1, sol2]

        if a > 1 and (b > 1 or b < -1) and c > 0:
            if b > 1:
                result = {'equation': f'{a}x^2+{b}x+{c}=0', 'solution': {'discriminant': float(dis), 'x': full_x}}
                print(json.dumps(result, indent=3))
            elif b < -1:
                result = {'equation': f'{a}x^2{b}x+{c}=0', 'solution': {'discriminant': float(dis), 'x': full_x}}
                print(json.dumps(result, indent=3))
        elif a == 1 and b == 0 and c == 0:
            result = {'equation': f'x^2=0', 'solution': {'discriminant': float(dis), 'x': full_x}}
            print(json.dumps(result, indent=3))
        elif (a < 0 or a > 1) and b == 0 and c == 0:
            result = {'equation': f'{a}x^2=0', 'solution': {'discriminant': float(dis), 'x': full_x}}
            print(json.dumps(result, indent=3))
        elif a > 1 and (b > 1 or b < 0) and c == 0:
            result = {'equation': f'{a}x^2-x=0', 'solution': {'discriminant': float(dis), 'x': full_x}}
            print(json.dumps(result, indent=3))
        elif a == 1 and b > 1 and c > 0:
            result = {'equation': f'x^2+{b}x+{c}=0', 'solution': {'discriminant': float(dis), 'x': full_x}}
            print(json.dumps(result, indent=3))
        elif a < -1 and b < -1 and c < -1:
            result = {'equation': f'{a}x^2{b}x{c}=0', 'solution': {'discriminant': float(dis), 'x': full_x}}
            print(json.dumps(result, indent=3))
    else:
        return 'Cannot generate a quadratic equation.'
