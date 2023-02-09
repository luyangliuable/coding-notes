using System;

namespace BasicClasses
{
    class Forest
    {


        public int age;
        private string biome;

        public int Grow() {
            age += 1;
            Trees += 30;

            return Trees;
        }


        public int Burn() {
            age += 1;
            Trees -= 20;

            return Trees;
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
    
    }

}
