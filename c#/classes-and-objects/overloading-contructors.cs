using System;

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
    
        public Forest(string name, string biome)
        {
            this.Name = name;
            this.Biome = biome;
            Age = 0;
        }

        // TODO wtf is this?
        public Forest(string name) : this(name, "Unknown")
        {
            Console.WriteLine("Warning: defaulted value biome.")
        }

    
        public string Name
        { get; set; }
    
        public int Trees
        { get; set; }
    
        public string Biome
        {
            get { return biome; }
            set
            {
                if (value == "Tropical" ||
                    value == "Temperate" ||
                    value == "Boreal")
                {
                    biome = value;
                }
                else
                {
                    biome = "Unknown";
                }
            }
        }
    
        public int Age
        { 
            get { return age; }
            private set { age = value; }
        }
     
        public int Grow()
        {
            Trees += 30;
            Age += 1;
            return Trees;
        }
    
        public int Burn()
        {
            Trees -= 20;
            Age += 1;
            return Trees;
        }
    
    }

}

/**
 *   \file program.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

using System;

namespace BasicClasses
{
    class Program
    {
        static void Main(string[] args)
        {
            Forest f = new Forest("Rendlesham");
            Console.WriteLine(f.Biome);
            // f.Trees = 0;

      
            // Console.WriteLine(f.Name);
        }

    }
}
