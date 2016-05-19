using Utility;
using System.IO;
namespace Monkey_Test {
    class Program {
        static void Main(string[] args) {
            RandomWELL rnd = new RandomWELL();
            FileStream rndWELL = new FileStream("random_WELL.txt", System.IO.FileMode.OpenOrCreate);
            StreamWriter bw = new StreamWriter(rndWELL);
            rnd.srand(7654321);
            for (int i = 0; i < 256*256; i++) {
                bw.WriteLine(rnd.frand2());
            }
            bw.Flush();
            bw.Close();
        }
    }
}
