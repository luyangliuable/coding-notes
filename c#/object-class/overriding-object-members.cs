namespace TheObjectClass
{
    class Book
    {
        public string Author
        { get; private set; }
    
        public string Title
        { get; private set; }

        public Book(string author = "Unknown", string title = "Untitled")
        {
            Author = author;
            Title = title;
        }

        public virtual string Stringify()
        {
            return "This is a Book object!";
        }

        public override string ToString() {
            return $"{Author}, {Title}.";
        }
    }
}

/**
 *   \file program.cs
 *   \brief A Documented file.
 *
 */
namespace TheObjectClass
{
    class Program
    {
        static void Main(string[] args)
        {
            Book bk = new Book("Ta-Nehisi Coates", "Between the World and Me");
      
            Console.WriteLine(bk.ToString());
        }
    }
}
