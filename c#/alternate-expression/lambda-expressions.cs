using System;

namespace AlternateExpressions
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] spaceRocks = {"meteoroid", "meteor", "meteorite"};
      
            bool makesContact = Array.Exists(spaceRocks, (string desc) => desc == "meteorite" );
      
            if (makesContact)
            {
                Console.WriteLine("At least one space rock has reached the Earth's surface!");
            } 
        } 
    
        static bool HitGround(string s)
        {
            return s == "meteorite";
        }
    }
}
