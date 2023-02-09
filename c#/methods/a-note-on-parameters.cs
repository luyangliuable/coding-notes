using System;

namespace ANoteOnParameters
{
    class Program
    {
        static void Main(string[] args)
        {
            VisitPlanets(3);
            VisitPlanets(4);
            VisitPlanets(5);
            Console.WriteLine(numberOfPlanets);
        }
    
        static void VisitPlanets(int numberOfPlanets)
        {
            Console.WriteLine($"You visited {numberOfPlanets} new planets...");
        }
    }
}


