/**
 *   \file Program.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

using System;

namespace SavingInterface
{
    class Program
    {
        static void Main(string[] args)
        {
            TodoList tdl = new TodoList();
            tdl.Add("Invite friends");
            tdl.Add("Buy decorations");
            tdl.Add("Party");

            PasswordManager pm = new PasswordManager("iluvpie", true);
        }
    }
}


/**
 *   \file TodoList.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */ 


namespace SavingInterface
{
    class TodoList : IDisplayable
    {
        public string[] Todos
        { get; private set; }

        private int nextOpenIndex;

        public void Display() {
            for (int i = 0; i < Todos.Length; i++) {
                Console.WriteLine(Todos[i]);
            }
        }

        public TodoList()
        {
            Todos = new string[5];
            nextOpenIndex = 0;
        }

        public void Add(string todo)
        {
            Todos[nextOpenIndex] = todo;
            nextOpenIndex++;
        }
    }
}

/**
 *   \file PasswordManager.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */
namespace SavingInterface
{
    class PasswordManager
    {
        private string Password
        { get; set; }

        public bool Hidden
        { get; private set; }

        public PasswordManager(string password, bool hidden)
        {
            Password = password;
            Hidden = hidden;
        }
    }
}

/**
 *   \file IDisplayable.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */

// Define IDisplayable in this file

namespace SavingInterface
{
    Interface IDisplayable {
        public void Display() {
            ;
        }
    }
}

/**
 *   \file IResetable.cs
 *   \brief A Documented file.
 *
 *  Detailed description
 *
 */
// Define IResetable in this file

namespace SavingInterface
{
    public void Reset {

    }
}
