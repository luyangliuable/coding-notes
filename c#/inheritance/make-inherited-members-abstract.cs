/**
 *   \file Program.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

using System;

namespace LearnInheritance
{
    class Program
    {
        static void Main(string[] args)
        {
            Sedan s = new Sedan(60);
            Console.WriteLine(s.Describe());
      
            Truck t = new Truck(45, 500);
            Console.WriteLine(t.Describe());
      
            Bicycle b = new Bicycle(10);
            Console.WriteLine(b.Describe());
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
    abstract class Vehicle
    {
        public string LicensePlate
        { get; private set; }

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
            Console.WriteLine("HONK!");
        }

        public abstract string Describe();

    }
}
/**
 *   \file Bicycle.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

namespace LearnInheritance
{
    class Bicycle : Vehicle
    {

        public Bicycle(double speed) : base(speed)
        {
            Wheels = 2;
        }

        public override void SpeedUp()
        {
            Speed += 5;
      
            if (Speed > 15)
            {
                Speed = 15;
            }
        }

        public override void SlowDown()
        {
            Speed -= 5;

            if (Speed < 0)
            {
                Speed = 0;
            }
        }

        public override string Describe()
        {
            return $"This Bicycle is moving on {Wheels} wheels at {Speed} km/h, with license plate {LicensePlate}.";
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
    
        public override string Describe()
        {
            return $"This Sedan is moving on {Wheels} wheels at {Speed} km/h, with license plate {LicensePlate}.";
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

        public override string Describe()
        {
            return $"This Truck is moving on {Wheels} wheels at {Speed} km/h, with license plate {LicensePlate}.";
        }

    }
}
