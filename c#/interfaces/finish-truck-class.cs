namespace LearnInterfaces
{
    class Truck : IAutomobile
    {
        public Truck(double speed, double weight) {
            Speed = speed;
            Weight = weight;
            LicensePlate  = Tools.GenerateLicensePlate();
            if (weight <= 399) {
                Wheels = 8;
            } else {
                Wheels = 12;
            }

        }

        // Properties
        public string LicensePlate
        { get; }


        public double Speed
        { get; set; }



        public int Wheels
        { get; }
     
        public double Weight {
            get;
        }

        // Methods
        public void slowDown() {
            Speed -= 5;
        }


        public void SpeedUp() {
            Speed += 5;
        }

        public void Honk()
        {
            Console.WriteLine("HONK!");
        }

    }
}
