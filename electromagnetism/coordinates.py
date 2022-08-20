from __future__ import annotations
from dataclasses import dataclass
import math

class OutOfRange(Exception):
    def __init__(self, message):
        super().__init__(message)

@dataclass
class CartesianPoint:
    x: float
    y: float
    z: float

    def Cylindrical(self) -> CylindricalPoint:
        rho = math.sqrt(self.x**2 + self.y**2)
        phi = self.__phiCalc()
        z = self.z
        return CylindricalPoint(rho, phi, z)

    def Spherical(self) -> SphericalPoint:
        r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        theta = math.acos(self.z / r)
        phi = self.__phiCalc()
        return SphericalPoint(r, theta, phi)

    def __phiCalc(self) -> float:
        if self.x > 0 and self.y >= 0:
            phi = math.atan(self.y/self.x)
        elif self.x < 0 and self.y >= 0:
            phi = math.pi - math.atan(self.y/abs(self.x))
        elif self.x < 0 and self.y < 0:
            phi = math.pi + math.atan(abs(self.y)/abs(self.x))
        elif self.x > 0 and self.y < 0:
            phi = (math.pi * 2) - math.atan(abs(self.y)/self.x)
        elif self.x == 0 and self.y > 0:
            phi = math.pi / 2
        elif self.x == 0 and self.y < 0:
            phi = math.pi * 3 / 2
        else:
            phi = 0
        return phi

@dataclass
class CylindricalPoint:
    rho: float
    phi: float
    z: float

    def __init__(self, rho: float, phi: float, z: float):
        self.rho = rho
        self.phi = phi
        self.z = z
        if (phi < 0) or (phi > math.pi*2):
            raise OutOfRange(f"Phi ({phi}) out of valid range [0, 2 pi)")
    
    def Cartesian(self) -> CartesianPoint:
        x = self.rho*math.cos(self.phi)
        y = self.rho*math.sin(self.phi)
        z = self.z
        return CartesianPoint(x, y, z)

@dataclass
class SphericalPoint:
    r: float
    theta: float
    phi: float

    def __init__(self, r: float, theta: float, phi: float):
        if (r < 0):
            raise OutOfRange(f"r ({r}) out of valid range [0, infinity)")
        if (theta < 0) or (theta > math.pi):
            raise OutOfRange(f"theta ({theta}) out of valid range [0, pi]")
        if (phi < 0) or (phi >= math.pi*2):
            raise OutOfRange(f"phi ({phi}) out of valid range [0, 2pi)")
        self.r = r
        self.theta = theta
        self.phi = phi

    def Cartesian(self) -> CylindricalPoint:
        x = self.r*math.sin(self.theta)*math.cos(self.phi)
        y = self.r*math.sin(self.theta)*math.sin(self.phi)
        z = self.r*math.cos(self.theta)
        return CartesianPoint(x, y, z)