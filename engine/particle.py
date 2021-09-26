from vector import Vector
import math


class Particle:

    position: Vector
    velocity: Vector
    acceleration: Vector
    damping: float
    inverseMass: float

    def __init__(self, *args):
        if len(args) == 5:
            self.position = args[0]
            self.velocity = args[1]
            self.acceleration = args[2]
            self.damping = args[3]
            self.inverseMass = args[4]
        elif len(args) == 4:
            self.position = args[0]
            self.velocity = args[1]
            self.acceleration = args[2]
            self.damping = args[3]
        elif len(args) == 3:
            self.position = args[0]
            self.velocity = args[1]
            self.acceleration = args[2]
        elif len(args) == 2:
            self.position = args[0]
            self.velocity = args[1]
        elif len(args) == 1:
            self.position = args[0]
        else:
            raise Exception('Invalid vector')

    def integrate(self, duration: float):

        assert self.inverseMass
        if self.inverseMass <= 0.0:
            return

        assert duration > 0.0

        self.position.addScaledVector(self.velocity, duration)

        resultAcc: Vector = self.acceleration

        # Update linear velocity from the acceleration
        self.velocity.addScaledVector(resultAcc, duration)

        # Impose drag
        self.velocity *= math.pow(self.damping, duration)

        del resultAcc


if __name__ == '__main__':
    v1 = Vector(2, 1)
    v2 = Vector(2, 4)
    print(v1)
    print(v2)
    v1.addScaledVector(v2, 3)
    print(v1)
    v1 *= 1/2
    print(v1)
    p = Particle(v1)
    p.inverseMass = 0.001
    p.velocity = v2
    p.acceleration = Vector(0, -2)
    p.damping = 0.79
    p.integrate(100)
    print(p.velocity)
