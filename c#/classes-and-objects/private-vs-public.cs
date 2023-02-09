using System;

/**
 *   \file program.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

namespace BasicClasses
{
    class Program
    {
        static void Main(string[] args)
        {
            Forest f = new Forest();
            f.Name = "Congo";
            f.Trees = 0;
            f.age = 0;
            f.Biome = "Desert";
      
            Console.WriteLine(f.Name);
            Console.WriteLine(f.Biome);
        }
    }
}

/**
 *   \file Forest.cs
 *   \brief A Documented file.
 *
 */

namespace BasicClasses
{
    class Forest
    {
        public int age;
        private string biome;
    
        public string Name
        { get; set; }
    
        public int Trees
        { get; set; }
    
        private string Biome
        {
            get { return biome; }
            set
            {
                if (value == "Tropical" || value == "Temperate" || value == "Boreal")
                {
                    biome = value;
                }
                else
                {
                    biome = "Unknown";
                }
            }
        }
    }

}
