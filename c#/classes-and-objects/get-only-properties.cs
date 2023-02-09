using System;

/**
 *   \file program.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

using System;

namespace basicClasses
{
    class program
    {
        static void main(string[] args)
        {
            forest f = new forest();
            f.name = "congo";
            f.trees = 0;
            f.biome = "desert";
      
            f.Age = 100;

            console.writeline(f.name);
            console.writeline(f.biome);
        }
    }
}



/**
 *   \file forest.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */


namespace BasicClasses
{
    class Forest
    {
        public int age;
        private string biome;

        public int Age {
            get {
                return age;
            };

            private set{
                age = value;
            };
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
    
    
    }

}
