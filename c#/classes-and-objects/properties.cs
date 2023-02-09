using System;

namespace BasicClasses
{
    class Forest
    {
        public string name;
        public int trees;
        public int age;
        public string biome;
    
    }

    public string Name
    {
        get { return name; }
        set { name = value; }
    }


    public int Trees
    {
        get { return trees; }
        set { trees = value; }
    }

    public string Biome
    {
        set {
            if ( value == "Tropical" ||
                 value == "Temperate" ||
                 value == "Boreal")
            {
                biome = value;
            } else {
                biome = "Unknown";
            }
        }

        get { return biome; }
    }

}

using System;

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
            f.biome = "Tropical";
      
            Console.WriteLine(f.name);
        }
    }
}
