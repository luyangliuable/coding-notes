/**
 *   \file Vehicle.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

using System;

namespace LearnInheritance
{
    class Vehicle
    {
        public Vehicle(double speed) {
            Speed = speed;
            LicensePlate = Tools.GenerateLicensePlate();
        }


        public string LicensePlate
        { get; private set; }

        public double Speed
        { get; private set; }

        public int Wheels
        { get; private set; }

        public void SpeedUp()
        {
            Speed += 5;
        }

        public void SlowDown()
        {
            Speed -= 5;
        }
    
        public void Honk()
        {
            Console.WriteLine("HONK!");
        }

    }
}

/**
 *   \file Sedan.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

namespace LearnInheritance
{
    class Sedan : Vehicle, IAutomobile
    {
        public Sedan(double speed) : base(speed)
        {
            Wheels = 4;
        }
    
    }
}


/**
 *   \file Truck.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

namespace LearnInheritance
{
    class Truck : Vehicle, IAutomobile
    { 
        public double Weight
        { get; }

        public Truck(double speed, double weight) : base(speed)
        {
            Weight = weight;

            if (weight < 400)
            {
                Wheels = 8;
            }
            else
            {
                Wheels = 12;
            }
        }

    }
}
