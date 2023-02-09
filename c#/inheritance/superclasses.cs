using System;

namespace LearnInheritance
{
    class Vehicle {

        // Properties
        public string LicensePlate{
            get;
        }

        public double Speed {
            get; private set;
        }

        public int Wheels {
            get;
        }

        // Methods
        public void Honk() {
        }

        public void SpeedUp() {
        }

        public void SlowDown() {
            
        }
        
    }

}


/**
 *   \file Sedan.cs
 */

namespace LearnInheritance
{
    class Sedan : Vehicle
    {
    
        public Sedan(double speed)
        {
            Speed = speed;
        }
    
    }
}
