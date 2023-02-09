using System;

namespace LearnInheritance
{
    class Bicycle : Vehicle {
        public Bicycle(double speed) : base(speed) {
            Wheels = 2;
        }

        public override void SpeedUp() {
            if (Speed + 5 <= 16) {
                Speed += 5;
            }
        }


        public override void SlowDown() {
            if (Speed - 5 >= 0) {
                Speed -= 5;
            }
        }
    }
}


/**
 *   \file Vehicle.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

namespace LearnInheritance
{
    class Bicycle : Vehicle {
        public Bicycle(double speed) : base(speed) {
            Wheels = 2;
        }

        public override void SpeedUp() {
            if (Speed + 5 <= 16) {
                Speed += 5;
            }
        }


        public override void SlowDown() {
            if (Speed - 5 >= 0) {
                Speed -= 5;
            }
        }
    }
}


namespace LearnInheritance
{
    class Vehicle
    {
        public string LicensePlate
        { get; protected set; }

        public double Speed
        { get; protected set; }

        public int Wheels
        { get; protected set; }

        public Vehicle(double speed)
        {
            Speed = speed;
            LicensePlate = Tools.GenerateLicensePlate();
        }

        public virtual void SpeedUp()
        {
            Speed += 5;
        }
        
        public virtual void SlowDown()
        {
            Speed -= 5;
        }
    
        public void Honk()
        {
            // Console.WriteLine("HONK!");
        }

    }
}
