using System;

namespace MethodOverloading
{
    class Program
    {
        static void Main(string[] args)
        {
            NamePets("Laika", "Albert");
            NamePets("Mango", "Puddy", "Bucket");
            NamePets();
        }
    
        static void NamePets(string pet1, string pet2)
        {
            Console.WriteLine($"Your pets {pet1} and {pet2} will be joining your voyage across space!");
        }  
    
        static void NamePets(string pet1, string pet2, string pet3)
        {
            Console.WriteLine($"Your pets {pet1}, {pet2}, and {pet3} will be joining your voyage across space!");
        }  
    
        static void NamePets()
        {
            Console.WriteLine("Aw, you have no spacefaring pets :(");
        }
    }
}
