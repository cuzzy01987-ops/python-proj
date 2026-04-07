from  sci_calc import velocity, force, kinetic_energy, moles, molarity, dilution, quadratic, circle_area, pythagoras
from pytest import approx
import pytest

def test_velocity():
  
    assert velocity(10,2) == approx(5.0)
    assert velocity(15,3) == approx(5.0)
    assert velocity(20,4) == approx(5.0)

def test_force():
   
    assert force(10,2) == approx(20.0)
    assert force(15,3) == approx(45.0)
    assert force(20,4) == approx(80.0)

def test_kinetic_energy():
    
    assert kinetic_energy(10,5) == approx(125.0)
    assert kinetic_energy(15,3) == approx(67.5)
    assert kinetic_energy(20,4) == approx(160.0)

def test_moles():
   
    assert moles(10,2) == approx(5.0)
    assert moles(15,3) == approx(5.0)
    assert moles(20,4) == approx(5.0)

def test_molarity():
    
    assert molarity(10,2) == approx(5.0)
    assert molarity(15,3) == approx(5.0)
    assert molarity(20,4) == approx(5.0)

def test_dilution():

    assert dilution(10,2,4) == approx(5.0)
    assert dilution(15,3,6) == approx(7.5)
    assert dilution(20,4,8) == approx(10.0)
    
def test_quadratic():
    assert quadratic(1, -3, 2) == approx((2.0,1.0))
    assert quadratic(1, 0, -4) == approx((-2.0,2.0))
    assert quadratic(1, -2, 1) == approx((1.0, 1.0))
    
def test_circle_area():
    assert circle_area(5) == approx(78.54)
    assert(circle_area(10) == approx(314.16))
    assert(circle_area(0)) == approx(0.0)
    
def test_pythagoras():
    assert pythagoras(3,4) == approx(5.0)
    assert pythagoras(5,12) == approx(13.0)
    assert pythagoras(8,15) == approx(17.0)
    




pytest.main(["-v", "--tb=line", "-rN", __file__])     

