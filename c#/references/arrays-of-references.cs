using System;

namespace LearnReferences
{
    class Program
    {
        static void Main(string[] args)
        {
            Dissertation diss1 = new Dissertation(32, "Anna Knowles-Smith", "Refugees and Theatre");
            Dissertation diss2 = new Dissertation(19, "Lajos Kossuth", "Shiny Happy People");
            Diary dy1 = new Diary(48, "Anne Frank", "The Diary of a Young Girl");
            Diary dy2 = new Diary(23, "Lili Elbe", "Man into Woman");
            Book[] book = new Book[] {diss1, diss2, dy1, dy2};

            foreach (Book eachBook in book) {
                Console.WriteLine($"{ eachBook.Title }");
            }
        }
    }
}
