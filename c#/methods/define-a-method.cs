using System;

namespace DefineAMethod
{
    class Program
    {
        static void Main(string[] args)
        {
            VisitPlanets(12);
            VisitPlanets(1);
            VisitPlanets(3);
        }

        static void VisitPlanets(int numberOfPlanets)
        {
            Console.WriteLine($"You visited {numberOfPlanets} new planets...");
        }

    }
}
