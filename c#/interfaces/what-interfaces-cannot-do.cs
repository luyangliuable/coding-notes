using System;

namespace LearnInterfaces
{
    class Sedan : IAutomobile
    {
        public Sedan(double speed) {
            Speed = speed;
            LicensePlate = "Randomasd";
            Wheels = 4;
        }

        public double Speed
        { get; private set; }

        public string LicensePlate
        { get; }

        public int Wheels
        { get; }

    
        public void Honk()
        {
            Console.WriteLine("HONK!");
        }

        public void SpeedUp() {
            Speed += 5;
        }

        public void SlowDown() {
            Speed -= 5;
        }
    
    }
}
