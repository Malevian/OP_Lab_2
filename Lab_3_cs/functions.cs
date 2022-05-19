using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab_3_cs
{
    class text_abstraction
    {
        string text;
        public text_abstraction(string Text)
        {
            text = Text;
        }
        public void add_text()
        {
            Console.WriteLine("Add the text:");
            text += "\n" + Console.ReadLine();
        }
        public int CountAllVowels()
        {
            int vowels = 0;
            for(int i = 0; i < text.Length; i++)
            {
                if (text[i] == 'a' || text[i] == 'A' ||
                    text[i] == 'e' || text[i] == 'E' ||
                    text[i] == 'i' || text[i] == 'I' ||
                    text[i] == 'y' || text[i] == 'Y' ||
                    text[i] == 'o' || text[i] == 'O' ||
                    text[i] == 'u' || text[i] == 'U')
                {
                    vowels++;
                }
            }
            return vowels;
        }
        public void outText()
        {
            Console.WriteLine(text);
        }
    }
    class otherThings
    {
        public string setText()
        {
            string text;
            char stop_botton = (char)19; // Ctrl+S
            Console.WriteLine("Enter the text:");
            string line;
            List<string> list = new List<string>();
            while (true)
            {
                line = Console.ReadLine();
                if (line == "" || line[0] != stop_botton)
                {
                    list.Add(line);
                }
                else break;
            }
            text = "";
            for (int i = 0; i < list.Count; i++)
            {
                text += list[i];
                if (i != list.Count - 1)
                {
                    text += "\n";
                }
            }
            return text;
        }
        public text_abstraction[] MoreText(ref int amount)
        {
            string Text;
            Console.Write("Enter the amount of objects you want to create: ");
            amount = Convert.ToInt32(Console.ReadLine());
            text_abstraction[] Objects = new text_abstraction[amount];
            for (int i = 0; i < amount; i++)
            {
                Text = setText();
                text_abstraction temp = new text_abstraction(Text);
                Objects[i] = temp;
            }
            return Objects;
        }
        public void ExtendTheText(text_abstraction[] ArrayOfText)
        {
            int TextPosition;
            Console.WriteLine("Press Y to extend the text\nPress any key to stop writing text");
            char choice = Convert.ToChar(Console.ReadLine());
            while (choice == 'Y' || choice == 'y')
            {
                Console.Write("Choose the text to extend it(Less than {0}): ", ArrayOfText.Length);
                TextPosition = Convert.ToInt32(Console.ReadLine());
                ArrayOfText[TextPosition-1].add_text();
                Console.WriteLine("Continue?");
                try
                {
                    choice = Convert.ToChar(Console.ReadLine());
                }
                catch (FormatException)
                {
                    Console.WriteLine("You must enter one symbol");
                }
            }
        }
        public text_abstraction TextWithTheLargestAmountOfVowels(text_abstraction[] Objects)
        {
            int amountOfVowels = 0,
                ToCompare = 0,
                pos = 0;

            for(int i = 0; i < Objects.Length; i++)
            {
                ToCompare = Objects[i].CountAllVowels();
                if(ToCompare > amountOfVowels)
                {
                    amountOfVowels = ToCompare;
                    pos = i;
                }
            }
            Console.WriteLine("The largest amount of vowels in {0} position - {1} vowels", pos + 1, amountOfVowels);
            return Objects[pos];
        }
        public void output(text_abstraction[] Objects)
        {
            for(int i = 0; i < Objects.Length; i++)
            {
                Console.WriteLine("Text {0}", i+1);
                Objects[i].outText();
                Console.WriteLine("\n");
            }
        }
    }
}
