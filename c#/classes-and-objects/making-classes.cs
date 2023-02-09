using System;

namespace BasicClasses
{
    class Program
    {
        static void Main(string[] args)
        {
            Forest f = new Forest();
            f.name = "Am";
            f.biome = "rain";
            f.trees = 1221;
            f.age = 120;
            Console.WriteLine(f.name);
        }
    }

}
