/**
 *   \file Sedan.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

using System;

namespace LearnInterfaces
{
    class Sedan : IAutomobile {
        public string LicensePlate { get; }
        public double Speed { get; }
        public int Wheels { get; }
        public void Honk() {
            Console.WriteLine("Honk!");
        }

    }
}

/**
 *   \file IAutomobile.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

namespace LearnInterfaces
{
    interface IAutomobile
    {
        string LicensePlate { get; }
        double Speed { get; }
        int Wheels { get; }
        void Honk();
        void speedUp();
    }
}
