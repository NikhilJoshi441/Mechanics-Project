import math
import numpy as np

def get_components(force, angle_deg):
    angle_rad = math.radians(angle_deg)
    x_component = math.cos(angle_rad) * force
    y_component = math.sin(angle_rad) * force
    return x_component, y_component

def calculate_resultant(forces):
    x_resul, y_resul = 0, 0
    for force, ang_deg, direc in forces:
        ang_rad = math.radians(ang_deg)
        if direc == 'ne':
            x_resul += math.cos(ang_rad) * force
            y_resul += math.sin(ang_rad) * force
        elif direc == 'nw':
            x_resul -= math.cos(ang_rad) * force
            y_resul += math.sin(ang_rad) * force
        elif direc == 'se':
            x_resul += math.cos(ang_rad) * force
            y_resul -= math.sin(ang_rad) * force
        elif direc == 'sw':
            x_resul -= math.cos(ang_rad) * force
            y_resul -= math.sin(ang_rad) * force

    resultant = math.sqrt(x_resul**2 + y_resul**2)
    return x_resul, y_resul, resultant

def calculate_moment(forces):
    moment = 0
    for force, ang_deg, direc, xcoord, ycoord in forces:
        ang_rad = math.radians(ang_deg)
        if direc in ["ne", "sw"]:
            moment += (force * math.sin(ang_rad) * xcoord) - (force * math.cos(ang_rad) * ycoord)
        elif direc in ["nw", "se"]:
            moment += (-1 * (force * math.sin(ang_rad) * xcoord)) + (force * math.cos(ang_rad) * ycoord)
    return moment

def zero_moment():
    n = int(input("Enter number of forces excluding unknown force: "))
    forces = []
    for _ in range(n):
        force = float(input("Enter value of force: "))
        deg = float(input("Enter angle force makes wrt 'x axis': "))
        direc = input("Enter direction of force: ").lower()
        xcoord = float(input("Enter x coordinate taking point of rotation as origin: "))
        ycoord = float(input("Enter y coordinate taking point of rotation as origin: "))
        forces.append((force, deg, direc, xcoord, ycoord))

    moment = calculate_moment(forces)
    deg1 = float(input("Enter angle force makes wrt 'x axis': "))
    direc1 = input("Enter direction of force: ").lower()
    xcoord1 = float(input("Enter x coordinate taking point of rotation as origin: "))
    ycoord1 = float(input("Enter y coordinate taking point of rotation as origin: "))
    ang_rad1 = math.radians(deg1)
    if direc1 in ["ne", "sw"]:
        unknown_force = moment / ((math.sin(ang_rad1) * xcoord1) - (math.cos(ang_rad1) * ycoord1))
    elif direc1 in ["nw", "se"]:
        unknown_force = moment / (-1 * (math.sin(ang_rad1) * xcoord1) + (math.cos(ang_rad1) * ycoord1))

    print(f"Unknown force is: {unknown_force}")

def main():
    while True:
        quest = input("Enter key words of the question: ").lower()

        if 'component' in quest or 'components' in quest:
            k = int(input("Enter number of forces: "))
            for _ in range(k):
                ang = float(input("Enter the angle in degrees for force (Float value): "))
                force = int(input("Enter the force value in newtons only: "))
                x_comp, y_comp = get_components(force, ang)
                print(f"Force x scalar component is: {x_comp}")
                print(f"Force y scalar component is: {y_comp}")

        elif 'resultant' in quest or 'resultants' in quest:
            k = int(input("Enter number of forces: "))
            forces = []
            for _ in range(k):
                ang = float(input("Enter the angle in degrees for force wrt 'x axis': "))
                force = int(input("Enter the force value in newtons only: "))
                direc = input("Enter direction of force: ").lower()
                forces.append((force, ang, direc))
            x_resul, y_resul, res = calculate_resultant(forces)
            print(f"{x_resul}i + {y_resul}j")
            print(f"Resultant is: {res}")

        elif 'moment' in quest and 'zero' not in quest:
            n = int(input("Enter number of forces: "))
            forces = []
            for _ in range(n):
                force = float(input("Enter value of force: "))
                deg = float(input("Enter angle force makes wrt 'x axis': "))
                direc = input("Enter direction of force: ").lower()
                xcoord = float(input("Enter x coordinate taking point of rotation as origin: "))
                ycoord = float(input("Enter y coordinate taking point of rotation as origin: "))
                forces.append((force, deg, direc, xcoord, ycoord))
            moment = calculate_moment(forces)
            print(f"Total moment is: {moment}")

        elif 'zero moment' in quest:
            zero_moment()

        elif "equilibrium" in quest:
            k = int(input("Enter number of forces to find: "))
            if k > 1:
                lx = []
                ly = []
                for i in range(k):
                    deg = math.radians(float(input("Enter angle force makes wrt 'x axis': ")))
                    direc = input("Enter direction of force: ").lower()
                    if direc == 'ne':
                        lx.append(math.cos(deg))
                        ly.append(math.sin(deg))
                    elif direc == 'nw':
                        lx.append(-math.cos(deg))
                        ly.append(math.sin(deg))
                    elif direc == 'sw':
                        lx.append(-math.cos(deg))
                        ly.append(-math.sin(deg))
                    elif direc == 'se':
                        lx.append(math.cos(deg))
                        ly.append(-math.sin(deg))

                # Solving the equilibrium equations
                a = np.array([lx[:2], ly[:2]])
                b = np.array([-lx[2], -ly[2]])
                solution = np.linalg.solve(a, b)
                print(f"The unknown forces are: {solution}")

        choice = int(input("Do you want to quit? (1=Quit, 0=Don't Quit): "))
        if choice == 1:
            break

if __name__ == "__main__":
    main()
