using System;

namespace ApplyingClasses
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length > 0)
            {
                string mainPhrase = String.Join(" and ", args);
                Console.WriteLine($"My favorite fruits are {mainPhrase}!");
            }

      
        }
    }
}


// Run with:
// dotnet run mango pineapple lychee
