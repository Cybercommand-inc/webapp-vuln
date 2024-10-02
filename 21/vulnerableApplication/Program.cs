using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;

namespace VulnerableApp
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    // Specify the startup class
                    webBuilder.UseStartup<Startup>();

                    // Bind to all network interfaces (0.0.0.0) and expose port 5000
                    webBuilder.UseUrls("http://0.0.0.0:5000"); // Correctly chained method
                });
    }
}
