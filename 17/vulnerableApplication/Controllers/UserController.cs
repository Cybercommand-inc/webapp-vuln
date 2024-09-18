using Microsoft.AspNetCore.Mvc;

namespace VulnerableApp.Controllers
{
    public class UserController : Controller
    {
        [HttpGet("/emails")]
        public IActionResult ShowEmail()
        {
            // Exposing email addresses
            return Content("User Email: john.doe@example.com", "text/html");
        }
    }
}
