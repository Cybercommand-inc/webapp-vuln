using Microsoft.AspNetCore.Mvc;

namespace VulnerableApp.Controllers
{
    public class ConfigController : Controller
    {
        [HttpGet("/db-connection")]
        public IActionResult ExposeConnectionString()
        {
            // Intentionally disclosing the connection string
            string connectionString = "Server=myServer;Database=myDB;User Id=myUser;Password=myPassword;";
            return Content($"Connection String: {connectionString}", "text/plain");
        }
    }
}
