using System;

namespace LearnInterfaces
{
    class Program
    {
        static void Main(string[] args)
        {
            Sedan s1 = new Sedan(60);
            Sedan s2 = new Sedan(70);
            Truck t1 = new Truck(45, 500);

            Console.WriteLine($"Sedan with license plate {s1.LicensePlate} with speed {s1.Speed}");
            Console.WriteLine($"Sedan with license plate {s2.LicensePlate} with speed {s2.Speed}");
            Console.WriteLine($"Truck with license plate {t1.LicensePlate} with speed {t1.Speed} and weight {t1.Weight}");

            s1.SpeedUp();
            s2.SpeedUp();
            t1.SpeedUp();

            Console.WriteLine($"Sedan new speed is {s1.Speed}.");
            Console.WriteLine($"Sedan new speed is {s2.Speed}.");
            Console.WriteLine($"Truck new speed is {t1.Speed}.");

        }
    }
}
